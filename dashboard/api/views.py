from django.shortcuts import render
from rest_framework.response import  Response
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView

from landing.models import Bb
from .serializers import BbSerializer, BbDetailSerializer

@api_view(['GET'])
def bbs(request):
    if request.method == 'GET':
        bbs = Bb.objects.filter(is_active=True)[:10]
        serializer = BbSerializer(bbs, many=True)
        return Response(serializer.data)

class BbDetailView(RetrieveAPIView):
    queryset = Bb.objects.filter(is_active=True)
    serializer_class = BbDetailSerializer