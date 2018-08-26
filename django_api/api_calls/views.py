#from api_calls.models import Add_api,Provider#,service_area
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
### importing mongo models
from .models import service_provider,Provider
from django.core import serializers

import json

class provider(APIView):
    def get(self,request):
        
        name=request.GET.get('name')

        Email=request.GET.get('Email')

        phone_number=request.GET.get('phone_number')

        Language=request.GET.get('Language')

        Currency=request.GET.get('Currency')
        params = {}
        if name:
            params['name']=name
        if Email:    
            params['Email']= Email
        if phone_number:    
            params['phone_number']=phone_number    
        if Language:    
            params['Language']=Language
        if Currency:    
            params['Currency']=Currency 
        res=Provider.objects.filter(**params).order_by("id") 
        res=json.loads(serializers.serialize("json", res))
        if len(res)>0:
            data=[x['fields'] for x in res]
        
        return Response({"data":data})    
    def post(self,request):
        res=Provider.objects.create(**request.data)
        return Response({"message":"Data recorded successfully"})
    def delete(self,request):
        data=Provider.objects.get(**request.data)
        data.delete()
        return Response({"message":"Deleted successfully"})
    def put(self,request):
        filter_params=request.data['filter']
        new_params=request.data['new_value']
        service=Provider.objects.filter(**filter_params).update(**new_params)
        return Response({"message":"Data updated "})

class test_view(APIView):
    def get(self,request):
        user_name = request.GET.get('user_name')
        sa_name = request.GET.get('sa_name')
        cost = request.GET.get('cost')
        lat=request.GET.get('lat')
        long=request.GET.get('long')
        params = {}
        if user_name:
            params['user_name']=user_name
        if sa_name:    
            params['sa_name']= sa_name
        if cost:    
            params['cost']=cost    
        if lat:    
            params['lat']=lat
        if long:    
            params['long']=long            
        res=service_provider.objects.filter(**params).order_by("id")
        res=json.loads(serializers.serialize("json", res))
        if len(res)>0:
            data=[x['fields'] for x in res]
        return Response({"data":data})
        
    def post(self,request):
        res=service_provider.objects.create(user_name=request.data['user_name'],sa_name=request.data['sa_name'],cost=request.data['cost'],lat=request.data['lat'],long=request.data['long'])
        return Response({"message":"you called get test_view"})    
    def put(self,request):
        filter_params=request.data['filter']
        new_params=request.data['new_value']
        service=service_provider.objects.filter(**filter_params).update(**new_params)
        return Response({"message":"Data updated "})
    def delete(self,request):
        data=service_provider.objects.get(**request.data)
        data.delete()
        return Response({"message":"Deleted successfully"})