from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 3  # Net size 10
    page_query_param = 'p'  # to change page name to p
    page_size_query_param = 'size'  # To change page number
    max_page_size = 4
