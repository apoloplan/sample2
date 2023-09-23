from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http.response import JsonResponse
# Create your views here.
def index(request):
    data =[
      {
        'id': 1,
        'title': 'sample_image_1',
        'url': 'image/sample_1',
      },
      {
        'id': 2,
        'title': 'sample_image_2',
        'url': 'image/sample_2',
      },
      {
        'id': 3,
        'title': 'sample_image_3',
        'url': 'image/sample_3',
      },
      {
        'id': 4,
        'title': 'sample_image_4',
        'url': 'image/sample_4',
      },
      {
        'id': 5,
        'title': 'sample_image_5',
        'url': 'image/sample_5',
      },
    ]

    return JsonResponse({'data': data})
