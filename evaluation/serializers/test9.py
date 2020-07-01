from rest_framework import serializers
from evaluation.models import Test9, TextPair


class TextPairSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextPair
        fields = ['first', 'second', ]


class Test9Serializer(serializers.ModelSerializer):
    questions = TextPairSerializer(many=True)

    class Meta:
        model = Test9
        fields = ['name', 'heading', 'questions',  'subject']
