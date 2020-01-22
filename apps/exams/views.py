from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Examination
from .serializers import ExamSerializer
from django.http import Http404


class ExamsListView(APIView):
    """
    List all exams.
    """
    def get(self, request, format=None):
        snippets = Examination.objects.all()
        serializer = ExamSerializer(snippets, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)