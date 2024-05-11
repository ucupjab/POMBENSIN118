from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import PomBensin, Pembeli
from .serializers import PomBensinSerializer, PembeliSerializer


@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def PomBensin_list(request, format=None):

    if request.method == 'GET':
        PomBensin =PomBensin .objects.all()
        serializer = PomBensinSerializer(PomBensin, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PembeliSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
