from rest_framework import serializers
from evaluation.models import Test6, PictureTextInput


class PictureTextInputSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField('get_image')

    class Meta:
        model = PictureTextInput
        fields = ['picture', 'correct_text', ]

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.picture:
            url = obj.picture.url
            return request.build_absolute_uri(url)
        else:
            return None


class Test6Serializer(serializers.ModelSerializer):
    pictures = PictureTextInputSerializer(many=True)

    class Meta:
        model = Test6
        fields = ['name', 'heading', 'pictures',  'subject']
