from django.shortcuts import render
from rest_framework import viewsets
from .models import School, Class, Student
from .serializers import SchoolSerializer, ClassSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

@api_view(['GET'])
def get_schools(request):
    print(123123)
    address = request.request.query_params.get('address')
    limit = request.GET.get('limit',2) # default limit to 2 if not provided
    schools = School.objects.all()
    print(limit, 'this is address')
    print(address, 'this is address')
    if address:
        schools = schools.filter(address=address)

    if limit:
        schools = schools[:int(limit)]

    serializer = SchoolSerializer(schools, many=True)
    return Response(serializer.data) 
'''
@api_view(['GET'])
def get_schools(request):
    # Get the 'limit' parameter from the query string (defaults to 5 if not provided)
    limit = request.GET.get('limit', 5)
    
    # Ensure the 'limit' is a valid integer (fall back to 5 if not)
    try:
        limit = int(limit)
    except ValueError:
        limit = 5  # Default to 5 if limit is not an integer

    # Retrieve all schools from the database
    schools = School.objects.all()

    # Limit the number of schools returned based on the 'limit' parameter
    schools = schools[:limit]

    # Serialize the data using the SchoolSerializer
    serializer = SchoolSerializer(schools, many=True)

    # Return the serialized data as a response
    return Response(serializer.data)
'''
