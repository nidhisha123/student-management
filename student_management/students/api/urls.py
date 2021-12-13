from . import views as student
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('grade', student.StudentGradeModelViewSet, basename='grade')

urlpatterns = [
	path('', include(router.urls)),
	path('student/', student.StudentListGV.as_view(), name='students_list'),
	path('student/<int:pk>/', student.StudentDetailGV.as_view(), name='student_detail'),
]