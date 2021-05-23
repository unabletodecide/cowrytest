from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics #import CreateAPIView
from .models import KVPairTable
from .serializers import KVPairSerializer
import json
# Create your views here.

# @csrf_exempt
def home(request):
    return render(request, 'webpages/home.html')

class DictKVPair(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = KVPairSerializer
    http_method_names = ['get']
    queryset = KVPairTable.objects.all()
    def generate(self):
        newkv = KVPairTable()
        newkv.save()

    def get(self, request):
        mydict = {}
        self.generate()
        res_q_set = self.queryset.all().order_by('-time_stamp')
        for e in res_q_set:
            mydict[str(e.time_stamp)]=str(e.uuid_val)
        # serializer = KVPairSerializer(mydict, many=True)
        # return Response(serializer.data)
        return Response(mydict)