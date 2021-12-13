from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, viewsets, generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from student_management.students.models import Students, Grade
from .serializers import StudentsSerializer, GradeSerializer
from .throttling import StudentDetailThrottling
from .pagination import StudentListPagination, StudentListOffsetPagination, GradeCursorPagination


class StudentGradeModelViewSet(viewsets.ModelViewSet):
	queryset = Grade.objects.all()
	serializer_class = GradeSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]
	# throttle_classes = [AnonRateThrottle, UserRateThrottle]
	pagination_class = GradeCursorPagination
	filter_backends = [filters.SearchFilter]
	search_fields = ['^name']


class StudentListGV(generics.ListCreateAPIView):
	'''test'''
	queryset = Students.objects.all()
	serializer_class = StudentsSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]
	
	# throttle_classes = [ScopedRateThrottle]
	# throttle_scope = 'student-list'
	
	filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
	filter_fields = ['grade__name', 'age']
	search_fields = ['name','grade__name']
	ordering_fields = ['age', 'name']

	# pagination_class = StudentListPagination
	pagination_class = StudentListOffsetPagination


	def perform_create(self, serializer):
		grade = serializer.validated_data.get('grade')
		grade.total_student_count += 1
		grade.save()
		serializer.save(grade=grade)


	# # Filter with queryset
	# def get_queryset(self):
	# 	qs = super().get_queryset()
	# 	grade = self.request.query_params.get('grade', None)
	# 	if grade:
	# 		qs = qs.filter(grade__name__iexact=grade)
	# 	return qs

class StudentDetailGV(generics.RetrieveUpdateDestroyAPIView):
	queryset = Students.objects.all()
	serializer_class = StudentsSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]
	# throttle_classes = [StudentDetailThrottling]
