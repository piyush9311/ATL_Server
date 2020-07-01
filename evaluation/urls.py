from django.urls import path
from .views import LessonsGetView, LessonDetailView, AssessmentDetailView

urlpatterns = [
    path('lessons', LessonsGetView.as_view(), name='lessons_get_view'),
    path('lesson/<int:id>', LessonDetailView.as_view(), name='lesson_detail_view'),
    path('assessment', AssessmentDetailView.as_view(), name='Assessment_detail_view'),
]
