from django.http import JsonResponse
import json 
from django.views.decorators.csrf import csrf_exempt
from .models import *

@csrf_exempt
def adminRegister(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('Username')
        password = data.get('Password')
        
        Admin.objects.create(Username=username, Password=password)
        return JsonResponse({'message': 'Successfully created admin'}, status=201)
    
@csrf_exempt
def adminLogin(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('Username')
        password = data.get('Password')
        
        admin = Admin.objects.filter(Username=username, Password=password).first()
        if admin:
            return JsonResponse({'message': 'Successfully logged in'}, status=200)
        else:
            return JsonResponse({'message': 'Wrong username or password'}, status=401)
