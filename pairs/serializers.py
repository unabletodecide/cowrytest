from rest_framework import serializers
from .models import KVPairTable

class KVPairSerializer(serializers.Serializer):

    result_set = serializers.DictField(child=serializers.CharField(), allow_empty=False, read_only=True)

