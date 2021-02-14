from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class PersonPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'p'
    page_size_query_param = 'records'
    max_page_size = 5
    # last_page_strings = 'end'

class PersonLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 5
    limit_query_param = 'mylimit'


class PersonCursorPagination(CursorPagination):
    page_size = 2
    ordering = 'phone'
    