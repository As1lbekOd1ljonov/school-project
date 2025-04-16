from rest_framework import serializers

from .models import Teacher, Class, Student


class ClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"