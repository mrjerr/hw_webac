from random import randint
from urllib.parse import urlparse

from django.conf import settings
from django.conf.urls import url
from django.shortcuts import redirect, render
from django.utils.baseconv import base56

from .models import Url


ALLOWED_SCHEMES = {'http', 'https', 'ftp'}


def index(request):
    pass


def redirect_view(request, key):
    pass
