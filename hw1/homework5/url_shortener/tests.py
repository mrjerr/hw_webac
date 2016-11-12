from django.test import TestCase

from .models import Url

class UrlShortenerTestView(TestCase):
    def test_index_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_post(self):
        response = self.client.post('/', {'url': 'http://example.com/'})
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/', {'url': 'mailto:admin@google.com'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'http')
        self.assertContains(response, 'https')
        self.assertContains(response, 'ftp')

    def test_redirect_invalid_key(self):
        response = self.client.get('/randomnonsense')
        self.assertRedirects(response, '/')

    def test_create_duplicate_url(self):
        url = 'http://www.example.com'
        response = self.client.post('/', {'url': url})
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/', {'url': url})
        self.assertEqual(response.status_code, 200)
        num_rec = Url.objects.filter(source=url).count()
        self.assertEqual(num_rec, 1)
        
    def test_redirect_count(self):
        url = 'http://www.example.com'
        obj = Url.objects.create(source=url, key='asdf')
        self.assertEqual(obj.redirect_count, 0)
        for i in range(1, 9):
            response = self.client.get('/asdf')
            count = Url.objects.get(key='asdf').redirect_count
            self.assertRedirects(response, url, fetch_redirect_response=False)
            self.assertEqual(count, i)

