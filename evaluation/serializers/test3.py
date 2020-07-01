from rest_framework import serializers
from evaluation.models import Test3, NumberList


class NumberListSerializer(serializers.ModelSerializer):
    numbers = serializers.ListField(child=serializers.IntegerField(), source='get_numbers')

    class Meta:
        model = NumberList
        fields = ['numbers', ]


class Test3Serializer(serializers.ModelSerializer):
    number_lists = NumberListSerializer(many=True)

    class Meta:
        model = Test3
        fields = ['name', 'heading', 'number_lists', 'subject' ]
