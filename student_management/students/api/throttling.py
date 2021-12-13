from rest_framework.throttling import UserRateThrottle


class StudentDetailThrottling(UserRateThrottle):
	scope = 'student-detail'