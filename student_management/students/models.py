from django.db import models


class Grade(models.Model):
	name = models.CharField(max_length=20)
	total_student_count = models.IntegerField(default=0)


class Students(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='students')

	def __str__(self):
		return self.name