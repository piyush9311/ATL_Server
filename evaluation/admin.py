from django.contrib import admin
from django import forms
from evaluation.models import Test1, Question, Option, Lesson, Test2, PictureDescriptionPair
from evaluation.models import NumberList, Test3, Test4, AudioDescriptionPair
from evaluation.models import Test5, ImageQuestion, ImageOption, Test6, PictureTextInput
from evaluation.models import Test9, TextPair

# Test 1 --------------------------------------------------------------


class OptionsInline(admin.TabularInline):
    model = Option
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        OptionsInline,
    ]


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Test1)
class Test1Admin(admin.ModelAdmin):
    inlines = [
        QuestionInline
    ]


# Test 2 --------------------------------------------------------------

class PicturePairInline(admin.TabularInline):
    model = PictureDescriptionPair
    extra = 1


@admin.register(Test2)
class Test2Admin(admin.ModelAdmin):
    inlines = [
        PicturePairInline,
    ]

# Test 3 --------------------------------------------------------------


class NumberListInline(admin.TabularInline):
    model = NumberList
    extra = 1
    verbose_name_plural = "Numbers List (space separated, max. 5 recommended)"


@admin.register(Test3)
class Test3Admin(admin.ModelAdmin):
    inlines = [
        NumberListInline,
    ]


# Test 4 --------------------------------------------------------------

class AudioPairInline(admin.TabularInline):
    model = AudioDescriptionPair
    extra = 1


@admin.register(Test4)
class Test4Admin(admin.ModelAdmin):
    inlines = [
        AudioPairInline,
    ]


# Test 5 --------------------------------------------------------------

class ImageOptionsInline(admin.TabularInline):
    model = ImageOption
    extra = 1


@admin.register(ImageQuestion)
class ImageQuestionAdmin(admin.ModelAdmin):
    inlines = [
        ImageOptionsInline,
    ]


class ImageQuestionInline(admin.TabularInline):
    model = ImageQuestion
    extra = 1


@admin.register(Test5)
class Test5Admin(admin.ModelAdmin):
    inlines = [
        ImageQuestionInline
    ]


# Test 2 --------------------------------------------------------------

class PictureTextInputPair(admin.TabularInline):
    model = PictureTextInput
    extra = 1


@admin.register(Test6)
class Test6Admin(admin.ModelAdmin):
    inlines = [
        PictureTextInputPair,
    ]


# Test 9 --------------------------------------------------------------

class TextPairInline(admin.TabularInline):
    model = TextPair
    extra = 1

@admin.register(Test9)
class Test9Admin(admin.ModelAdmin):
    inlines = [
        TextPairInline,
    ]

# Inlines --------------------------------------------------------------

class Test9Inline(admin.TabularInline):
    verbose_name_plural = "Text Pairs Maching Tests"
    verbose_name = "Text Pair Matching Test"
    model = Test9
    extra = 1

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['name', 'heading', ]
        else:
            return []


class Test6Inline(admin.TabularInline):
    verbose_name_plural = "Picture Text Input Pairs"
    verbose_name = "Picture  Text Input"
    model = Test6
    extra = 1

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['name', 'heading', ]
        else:
            return []


class Test5Inline(admin.TabularInline):
    verbose_name_plural = "Multiple Choices Tests with Image"
    verbose_name = "Multiple Choices Test with Image"
    model = Test5
    extra = 1

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['name', 'heading', ]
        else:
            return []


class Test4Inline(admin.TabularInline):
    verbose_name_plural = "Audio Description Pairs"
    verbose_name = "Audio Description Match"
    model = Test4
    extra = 1

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['name', 'heading', ]
        else:
            return []


class Test3Inline(admin.TabularInline):
    verbose_name_plural = "Number Sorting Puzzles"
    verbose_name = "Number Sorting Puzzle"
    model = Test3
    extra = 1

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['name', 'heading', ]
        else:
            return []


class Test2Inline(admin.TabularInline):
    verbose_name_plural = "Picture Description Pairs"
    verbose_name = "Picture Description Match"
    model = Test2
    extra = 1

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['name', 'heading', ]
        else:
            return []


class Test1Inline(admin.TabularInline):
    verbose_name_plural = "Multiple Choices Tests"
    verbose_name = "Multiple Choices Test"
    model = Test1
    extra = 1

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ['name', 'heading']
        else:
            return []


class LessonForm(forms.ModelForm):
    study_text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Lesson
        fields = ['title', 'intro_text', 'study_text', 'type']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    form = LessonForm
    inlines = [
        Test1Inline,
        Test2Inline,
        Test3Inline,
        Test4Inline,
        Test5Inline,
        Test6Inline,
        Test9Inline,
    ]
