from django.http import JsonResponse


def project(request):
    if request.method == 'POST':
        return JsonResponse({'data': True})
    elif request.method == 'GET':
        return JsonResponse({'data': True})
    elif request.method == 'PUT':
        return JsonResponse({'data': True})
    elif request.method == 'DELETE':
        return JsonResponse({'data': True})
    

def sprint(request):
    if request.method == 'POST':
        return JsonResponse({'data': True})
    elif request.method == 'GET':
        return JsonResponse({'data': True})
    elif request.method == 'PUT':
        return JsonResponse({'data': True})
    elif request.method == 'DELETE':
        return JsonResponse({'data': True})
    

def iteration(request):
    if request.method == 'POST':
        return JsonResponse({'data': True})
    elif request.method == 'GET':
        return JsonResponse({'data': True})
    elif request.method == 'PUT':
        return JsonResponse({'data': True})
    elif request.method == 'DELETE':
        return JsonResponse({'data': True})
    

def log(request):
    if request.method == 'POST':
        return JsonResponse({'data': True})
    elif request.method == 'GET':
        return JsonResponse({'data': True})
    elif request.method == 'PUT':
        return JsonResponse({'data': True})
    elif request.method == 'DELETE':
        return JsonResponse({'data': True})
    
    