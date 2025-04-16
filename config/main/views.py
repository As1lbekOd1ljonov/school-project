from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Class, Teacher, Student
from .serializers import ClassSerializers,TeacherSerializers, StudentSerializers


# Create your views here.


class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializers


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers