from rest_framework import generics, mixins
from rest_framework.response import Response
from django.urls import re_path, path


class GenericGetAndListAPIView(generics.GenericAPIView, mixins.ListModelMixin):
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.detail_read_serializer(instance=instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if self.pagination_class:
            queryset = self.paginate_queryset(queryset)
            serializer = self.list_read_serializer(queryset, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.list_read_serializer(queryset, many=True)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        if self.lookup_url_kwarg in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
