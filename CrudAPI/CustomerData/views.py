from django.http import JsonResponse
import json 
from django.views.decorators.csrf import csrf_exempt
from .Models import *

@csrf_exempt
def addCustomer(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Create a new BusinessEntity
        new_business_entity = BusinessEntity.objects.create()
        
        # Prepare person data
        person_person_data = {
            "BusinessEntityID": new_business_entity,  # This should be the BusinessEntity instance
            "PersonType": data.get('PersonType'),
            "NameStyle": data.get('NameStyle'),
            "FirstName": data.get('FirstName'),
            "LastName": data.get('LastName'),
            "EmailPromotion": data.get('EmailPromotion'),  
        }
        
        new_person = Person.objects.create(**person_person_data)
        
        person_email_address_data = {
            "BusinessEntityID": new_business_entity,  # Use the new business entity instance
            "EmailAddress": data.get('EmailAddress'),
        }
        new_email_address = EmailAddress.objects.create(**person_email_address_data)
        
        state_province_name = data.get('StateProvinceName')
        state_province_id = StateProvince.objects.filter(Name=state_province_name).first().StateProvinceID
        
        person_address_data = {
            "AddressLine1": data.get('AddressLine1'),
            "City": data.get('City'),
            "StateProvinceID": state_province_id,
            "PostalCode": data.get('PostalCode'),
        }
        
        try:
            # Add a log before creating the person
            print("Attempting to create new person...")
            
            new_address = Address.objects.create(**person_address_data)
            

            address_type = data.get('AddressType')
            address_type_instance = AddressType.objects.get(Name=address_type)
            
            person_business_entity_address_data = {
                "BusinessEntityID": new_person,
                "AddressID": new_address,
                "AddressTypeID": address_type_instance,
            }
            
            new_business_entity_address = BusinessEntityAddress.objects.create(**person_business_entity_address_data)
            return JsonResponse({'message': 'Successfully created customer demographics'}, status=201)
        except Exception as e:
            print("Error occurred while creating new person:", str(e))
            return JsonResponse({'message': str(e)}, status=500)
            
@csrf_exempt
def getAllCustomer(request):
    if request.method == 'GET':
        response = []
        count = 0
        try:
            # Get last 500 business entities, ordered by ID in descending order
            business_entities = BusinessEntityAddress.objects.all().order_by('-BusinessEntityID')[:500]
            for business_entity in business_entities:
                person = Person.objects.filter(BusinessEntityID=business_entity.BusinessEntityID.BusinessEntityID).first()
                if not person:
                    continue
                
                email_address = EmailAddress.objects.filter(BusinessEntityID=business_entity.BusinessEntityID.BusinessEntityID).first()
                if not email_address:
                    continue
                address_id = business_entity.AddressID.AddressID
                address_type_id = business_entity.AddressTypeID.AddressTypeID
                address = Address.objects.get(AddressID=address_id)
                address_type = AddressType.objects.get(AddressTypeID=address_type_id)
                data = {
                    "BusinessEntityID": person.BusinessEntityID.BusinessEntityID,
                    "PersonType": person.PersonType,
                    "NameStyle": person.NameStyle,
                    "FirstName": person.FirstName,
                    "LastName": person.LastName,
                    "EmailPromotion": person.EmailPromotion,
                    "AddressLine1": address.AddressLine1,
                    "City": address.City,
                    "StateProvinceName": StateProvince.objects.get(StateProvinceID=address.StateProvinceID).Name,
                    "CountryRegionName": CountryRegion.objects.get(CountryRegionCode=StateProvince.objects.get(StateProvinceID=address.StateProvinceID).CountryRegionCode).Name,
                    "PostalCode": address.PostalCode,
                    "EmailAddress": email_address.EmailAddress,
                    "AddressType": address_type.Name,   
                }
                
                response.append(data)
            
            return JsonResponse(response, safe=False)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
        
@csrf_exempt
def deleteCustomer(request, BusinessEntityID):
    if request.method == 'DELETE':
        try:
            business_entity = BusinessEntity.objects.get(BusinessEntityID=BusinessEntityID)
            address = BusinessEntityAddress.objects.filter(BusinessEntityID=BusinessEntityID).first().AddressID
            business_entity.delete()
            address.delete()
            return JsonResponse({'message': 'Successfully deleted customer'}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405) 
        
@csrf_exempt
def updateCustomer(request, BusinessEntityID):
    if request.method == 'PATCH':
        try:
            data = json.loads(request.body)
            
            person_person_data = {
            "BusinessEntityID": BusinessEntityID,  
            "PersonType": data.get('PersonType'),
            "NameStyle": data.get('NameStyle'),
            "FirstName": data.get('FirstName'),
            "LastName": data.get('LastName'),
            "EmailPromotion": data.get('EmailPromotion'),  
            }
            
            updated_person = Person.objects.filter(BusinessEntityID=BusinessEntityID).update(**person_person_data)
            
            person_email_address_data = {
                "BusinessEntityID": BusinessEntityID,  # Use the new business entity instance
                "EmailAddress": data.get('EmailAddress'),
            }
            updated_email_address = EmailAddress.objects.filter(BusinessEntityID=BusinessEntityID).update(**person_email_address_data)
            
            state_province_name = data.get('StateProvinceName')
            state_province_id = StateProvince.objects.filter(Name=state_province_name).first().StateProvinceID
            
            person_address_data = {
                "AddressLine1": data.get('AddressLine1'),
                "City": data.get('City'),
                "StateProvinceID": state_province_id,
                "PostalCode": data.get('PostalCode'),
            }
            
            updated_address = Address.objects.filter(AddressID=BusinessEntityAddress.objects.filter(BusinessEntityID=BusinessEntityID).first().AddressID.AddressID).update(**person_address_data)
            
            return JsonResponse({'message': 'Successfully updated customer'}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
            
            
            
            