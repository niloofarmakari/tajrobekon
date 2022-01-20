import json

from django.conf import settings
from django.db import connection
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from graphene_django.views import GraphQLView


class CustomGraphQLView(GraphQLView):
    """
    A customized GraphQL view which:
    - Prints GraphQL query and SQL queries in development environment
    - Passes "ensure_ascii=False" to json.dumps (to reduce response size)
    """

    def json_encode(self, request, d, pretty=False):
        return json.dumps(d, separators=(",", ":"), ensure_ascii=False)

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, request, *args, **kwargs):
        initial_query_count = 0
        if settings.DEBUG:
            initial_query_count = len(connection.queries)
        result = super().dispatch(request, *args, **kwargs)
        if settings.DEBUG:
            query_count = len(connection.queries) - initial_query_count
            print("\n", "-" * 40, f"-> {query_count=}")
            for q in connection.queries[-query_count:]:
                print(">", q["time"], "sec\n", q["sql"], "\n", "-" * 40, "\n")
        return result
