from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .ManagementRepository import ManagementRepository
from .Models import CustomerDemographics, CustomerGeography, FactTable

customer_demographics_repository = ManagementRepository(CustomerDemographics)
customer_geography_repository = ManagementRepository(CustomerGeography)
fact_table_repository = ManagementRepository(FactTable)

# Customer Demographics Views
def addCustomerDemographics(request):
    try:
        data = json.loads(request.body)
        response = customer_demographics_repository.add(data)
        return JsonResponse({
            'status': 'success',
            'data': response,
            'message': 'Successfully created customer demographics'
        }, status=201)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

def getAllCustomerDemographics(request):
    try:
        fact_table_entries = fact_table_repository.getAll().select_related('CustomerDemographicsID')
        
        customer_demographics_data = [
            {
                **model_to_dict(fact.CustomerDemographicsID)
            }
            for fact in fact_table_entries
        ]

        return JsonResponse({
            'status': 'success',
            'message': 'Successfully retrieved all customer demographics',
            'data': customer_demographics_data
        }, status=200)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

def removeCustomerDemographics(request):
    try:
        data = json.loads(request.body)
        response = customer_demographics_repository.remove(data['BusinessEntityID'])
        return JsonResponse({
            'status': 'success',
            'message': 'Successfully removed customer demographics',
            'data': response
        }, status=200)
    
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

# Customer Geography Views
def addCustomerGeography(request):
    try:
        data = json.loads(request.body)
        response = customer_demographics_repository.add(data)
        return JsonResponse({
            'status': 'success',
            'data': response,
            'message': 'Successfully created customer demographics'
        }, status=201)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

def getAllCustomerGeography(request):
    try:
        fact_table_entries = fact_table_repository.getAll().select_related('CustomerGeographyID')
        
        customer_geography_data = [
            {
                **model_to_dict(fact.CustomerGeographyID)
            }
            for fact in fact_table_entries
        ]
        
        return JsonResponse({
            'status': 'success',
            'message': 'Successfully retrieved all customer demographics',
            'data': customer_geography_data
        }, status=200)
    
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

def removeCustomerGeography(request):
    try:
        data = json.loads(request.body)
        response = customer_demographics_repository.remove(data['BusinessEntityID'])
        return JsonResponse({
            'status': 'success',
            'message': 'Successfully removed customer demographics',
            'data': response
        }, status=200)
    
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)
