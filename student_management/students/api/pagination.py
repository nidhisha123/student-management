from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class StudentListPagination(PageNumberPagination):
	page_size = 2
	page_query_param = 'record'
	page_size_query_param = 'size'
	max_page_size = 4
	last_page_strings = 'end'


class StudentListOffsetPagination(LimitOffsetPagination):
	default_limit = 2
	limit_query_param = 'per_page'
	offset_query_param = 'start'
	max_limit = 4

class GradeCursorPagination(CursorPagination):
	page_size = 2
	ordering = 'name'
