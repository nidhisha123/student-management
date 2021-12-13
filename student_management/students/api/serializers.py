from rest_framework import serializers
from students.models import Students, Grade


class StudentsSerializer(serializers.ModelSerializer):
	standard = serializers.CharField(source='grade.name',read_only=True)

	class Meta:
		model = Students
		fields = '__all__'

	def validate_age(self,value):
		if value < 3 or value > 7:
			raise serializers.ValidationError('Student age must be between 3 and 7')
		return value


class GradeSerializer(serializers.ModelSerializer):
	students = StudentsSerializer(read_only=True, many=True)

	class Meta:
		model = Grade
		fields = '__all__'

	def validate_name(self,value):
		exist = Grade.objects.filter(name=value).exists()
		if exist:
			raise serializers.ValidationError('Grade already exists')
		return value