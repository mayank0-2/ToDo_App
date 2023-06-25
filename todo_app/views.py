from django.shortcuts import render
from todo_app.models import todo_model
from rest_framework.views import APIView
from todo_app.serializer import todo_serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class todo_view(APIView) :
    
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    
    #This get method is defined to return the todo data in a sorted order
    
    def get(self, request, format=None) : 
        data = todo_model.objects.all().order_by('date')
        serial = todo_serializer(data, many = True)
        return Response(serial.data)
    
    #This get method is defined to receive the todo data and save it in the database
    
    def post(self, request, format=None) :
        serial = todo_serializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors) 
    
    # This put method is defined to update the todo data by receiving the id from the user and updating it into the database
    
    def put(self, request, id, format = None) :
        try:
            instance = todo_model.objects.get(id=id)
            serial = todo_serializer(instance, data = request.data, partial = True)
            if serial.is_valid():
                serial.save()
                return Response(serial.data)
            else :
                return Response(serial.errors)     
        except:
            return Response(status.HTTP_204_NO_CONTENT) 
    
    #This method is used to delete the data of todo from the database
    
    def delete(self, request, id, format = None) :
        
        instance = todo_model.objects.get(id=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    
