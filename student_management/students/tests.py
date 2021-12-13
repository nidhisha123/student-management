from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from student_management.students.models import Grade, Students
from student_management.users.tests.factories import UserFactory


class GradeTestCase(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(refresh.access_token))
        self.grade = Grade.objects.create(name="Test Grade 2")

    def test_grade_list(self):
        url = reverse("grade-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_grade_create(self):
        url = reverse("grade-list")
        data = {
            "name" : "Test Grade",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_grade_individual(self):
        url = reverse("grade-detail", kwargs={"pk":self.grade.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_grade_update(self):
        url = reverse("grade-detail", kwargs={"pk":self.grade.id})
        data = {
            "name" : "Test Grade 1",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_grade_delete(self):
        url = reverse("grade-detail", kwargs={"pk":self.grade.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class StudentTestCase(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(refresh.access_token))
        self.grade = Grade.objects.create(name="Test Grade")
        self.student = Students.objects.create(name="Test Student 1", age=3, grade = self.grade)

    def test_student_list(self):
        url = reverse("students_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_list_search(self):
        url = reverse("students_list")+"?search=test"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("count"), 1)

    def test_student_create(self):
        url = reverse("students_list")
        data = {
            "name" : "Test Student",
            "age" : 5,
            "grade" : self.grade.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_student_individual(self):
        url = reverse("student_detail", kwargs={"pk":self.student.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_update(self):
        url = reverse("student_detail", kwargs={"pk":self.student.id})
        data = {
            "name" : "Test student",
            "age" : 3,
            "grade" : self.grade.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_delete(self):
        url = reverse("student_detail", kwargs={"pk":self.student.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
