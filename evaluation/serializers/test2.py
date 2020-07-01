from rest_framework import serializers
from evaluation.models import Test2, PictureDescriptionPair


class PictureDescriptionPairSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField('get_image')

    class Meta:
        model = PictureDescriptionPair
        fields = ['picture', 'description', ]

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.picture:
            url = obj.picture.url
            return request.build_absolute_uri(url)
        else:
            return None


class Test2Serializer(serializers.ModelSerializer):
    pictures = PictureDescriptionPairSerializer(many=True)

    class Meta:
        model = Test2
        fields = ['name', 'heading', 'pictures', 'subject' ]
