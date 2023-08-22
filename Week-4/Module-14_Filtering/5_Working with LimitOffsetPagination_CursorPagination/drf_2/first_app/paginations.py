from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class ProductPagination(PageNumberPagination):
    page_size = 3  # Net size 10
    page_query_param = 'p'  # to change page name to p
    page_size_query_param = 'size'  # To change page number
    max_page_size = 4


class ProductLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'l'
    offset_query_param = 'start'
    max_limit = 3


class ProductCursorPagination(CursorPagination):
    page_size = 4
    ordering = 'price'
    cursor_query_param = 'Data'
