from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def welcome_page(request):
    return render(request=request, template_name='welcome.html')


def category(request):
    return None


def category_items(request):
    return None


def item(request):
    return None


def item_detail(request):
    return None


def like(request):
    return None


def comment(request):
    return None

