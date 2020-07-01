from rest_framework import serializers
from evaluation.models import Lesson
from .test1 import Test1Serializer
from .test2 import Test2Serializer
from .test3 import Test3Serializer
from .test4 import Test4Serializer
from .test5 import Test5Serializer
from .test6 import Test6Serializer
from .test9 import Test9Serializer

class LessonSerializer(serializers.ModelSerializer):
    test1 = Test1Serializer(many=True)
    test2 = Test2Serializer(many=True)
    test3 = Test3Serializer(many=True)
    test4 = Test4Serializer(many=True)
    test5 = Test5Serializer(many=True)
    test6 = Test6Serializer(many=True)
    test9 = Test9Serializer(many=True)
    class Meta:
        model = Lesson
        fields = [
            'title',
            'intro_text',
            'study_text',
            'test1',
            'test2',
            'test3',
            'test4',
            'test5',
            'test6',
            'test9',
        ]
