from django.db import models


# Реализуйте модель со следующими полями:
# - source
#     исходная ссылка, уникальное поле
# - key
#     короткий ключ, уникальное поле
# - redirect_count
#     количество редиректов, положительное целое число,
#     по умолчанию = 0
#
# Реализуйте метод __str__, который будет возвращать строку
# вида <ключ>:<исходная ссылка>
#
class Url(models.Model):
    source = models.CharField(max_length=256, unique=True)
    key = models.CharField(max_length=6, unique=True)
    redirect_count = models.IntegerField(default=0)

    def __str__(self):
        return '<{key}>: <{url}>'.format(key=self.key, url=self.source)
