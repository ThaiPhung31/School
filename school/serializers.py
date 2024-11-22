from rest_framework import serializers
from .models import School, Class, Student

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all(), source='school.name')
    class Meta:
        model = Class
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    student_class = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(), source='student_class.name')
    class Meta:
        model = Student
        fields = '__all__'
