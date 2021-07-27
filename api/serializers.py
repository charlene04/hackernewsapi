from rest_framework import serializers
from collections import OrderedDict
from . models import *


class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    #To remove null fields from response
    def to_representation(self, instance):
        result = super(itemSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])

#handle posted data
class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['by', 'title', 'type', 'time', 'text', 'url', 'custom']