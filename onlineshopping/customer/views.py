from django.shortcuts import render
from.models import*
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class CreateItems(APIView):
    def post(self,request):
        name=request.data.get('name')
        description=request.data.get('description')
        price=request.data.get('price')
        
        items=Items(name=name,description=description,price=price)
        items.save()
        resp={
            'resultcode':'1',
            'result':'inserted data successfully',
        }
        return Response(resp)
        

    

#http://127.0.0.1:8000/product/create_product/
#http://127.0.0.1:8000/customer/Create_Product/
#http://127.0.0.1:8000/customer/create_product/

 #'resultcode':'1','result':'inserted successfully'