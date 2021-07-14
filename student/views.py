from django.shortcuts import render
from rest_framework.response import Response
from .models import Student, University
from .serializers import UniversitySerializer, StudentSerializer
from rest_framework import status
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


# Create your views here.

class UniversityViewSet(viewsets.ViewSet):

    def list(self, request):
        universities = University.objects.all()
        serializer = UniversitySerializer(universities, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UniversitySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrive(self, request, id=None):
        queryset = University.objects.all()
        university = get_object_or_404(queryset, id)
        serializer = UniversitySerializer(university)
        return Response(serializer.data)

    def update(self, request, id=None):
        university = University.objects.get(id=id)
        serializer = UniversitySerializer(university, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentViewSet(viewsets.ViewSet):

    def list(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrive(self, request, id=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def update(self, request, id=None):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
