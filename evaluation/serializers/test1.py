from rest_framework import serializers
from evaluation.models import Option, Question, Test1


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['text', 'correct']


class QuestionSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ['image', 'text', 'options', 'youtube_video']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            url = obj.image.url
            return request.build_absolute_uri(url)
        else:
            return None


class Test1Serializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Test1
        fields = ['name', 'heading', 'questions', 'subject' ]
