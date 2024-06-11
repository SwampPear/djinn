from django.shortcuts import render
from django.http import JsonResponse


def log(request, *kwargs):
    print(kwargs)
    
    if request.method == 'POST':
        'item/<int:item_id>/'


    return JsonResponse({})




