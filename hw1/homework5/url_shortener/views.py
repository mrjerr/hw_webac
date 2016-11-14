from random import randint
from urllib.parse import urlparse

from django.conf import settings
from django.conf.urls import url
from django.shortcuts import redirect, render
from django.utils.baseconv import base56

from .models import Url


ALLOWED_SCHEMES = {'http', 'https', 'ftp'}


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == 'POST':
        u = request.POST.get('url', '')
        if urlparse(u).scheme not in ALLOWED_SCHEMES:
            msg = 'Введите коректный URL, Разрешенные схемы: {}'.format(
                ', '.join(ALLOWED_SCHEMES))
            return render(
                request, 'index.html', context={'message': msg})
        else:
            url_obj, created = Url.objects.get_or_create(source=u)
            if created:
                url_obj.key = base56.encode(randint(0, 0x7fffff))
                url_obj.save()
            short_url = 'http://localhost:8000/' + url_obj.key
            msg = 'Ваша короткая ссылка:'
            return render(
                request, 'index.html',
                context={'message': msg, 'url': short_url})


def redirect_view(request, key):
    url_obj = Url.objects.filter(key=key).first()
    if url_obj:
        return redirect(url_obj.source)
    return redirect('/')
