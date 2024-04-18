from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ResultsSetPagination(PageNumberPagination):
    page_size_query_param = "count_per_page"

    def get_paginated_response(self, data):
        try:
            current_page = int(self.request.query_params.get("page", 1))
        except (ValueError, TypeError):
            current_page = 1

        return Response(
            OrderedDict(
                [
                    ("count", self.page.paginator.count),
                    ("total_pages", self.page.paginator.num_pages),
                    ("current_page", current_page),
                    ("results", data),
                ]
            )
        )
