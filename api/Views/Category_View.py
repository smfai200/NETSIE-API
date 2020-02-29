from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from Bridger.usecases import *
from rest_framework.decorators import action
from Bridger.models import *
from Bridger.serializers import *


class CategoryViewSet(ViewSet):

    def list(self, request):
        queryset = Category_UseCases().Get_All()
        return Response(queryset)

    @action(detail=False, methods=['get'])
    def get_StoryByCategoryId(self, request):
        try:
            id_ = request.GET["id"]
        except:
            return Response(status=500)
        response_data = Category_UseCases().get_StoryByCategoryId(id_)
        return Response(response_data)