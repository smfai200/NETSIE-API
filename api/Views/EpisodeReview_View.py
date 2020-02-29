from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from Bridger.models import *
from Bridger.serializers import *


class EpisodeReviewViewSet(ViewSet):

    def list(self, request):
        queryset = EpisodeReview.objects.all()
        serializer = EpisodeReviewSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = EpisodeReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = EpisodeReview.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = EpisodeReviewSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = EpisodeReview.objects.get(pk=pk)
        except EpisodeReview.DoesNotExist:
            return Response(status=404)
        serializer = EpisodeReviewSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = EpisodeReview.objects.get(pk=pk)
        except EpisodeReview.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)