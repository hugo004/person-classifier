from django.db.models import fields
from rest_framework import serializers
from .models import Seiyu

class SeiyuSerializer(serializers.ModelSerializer):
  class Meta:
    model = Seiyu
    fields = ('name', 'image')
    