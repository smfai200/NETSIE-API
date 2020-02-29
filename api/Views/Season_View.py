from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from Bridger.usecases import *
from rest_framework.decorators import action


class Season_ViewSet(ViewSet):

    def create(self, request):
        request.data._mutable = True
        request.data.update({"FK_User": request.user.id,"IsActive":True})
        response_data = Season_UseCases().Create_Season(data_=request.data)
        return Response(response_data)

    def update(self, request, pk=None):
        request.data._mutable = True
        request.data.update({"FK_User": request.user.id, "IsActive":True})
        response_data = Season_UseCases().Update_Season(data=request.data,pk=pk)
        return Response(response_data)

    def destroy(self, request, pk=None):
        response_data = Season_UseCases().Delete_Season(data=request.data, pk=pk)
        return Response(response_data)

    def list(self, request):
        response_data = Season_UseCases().Get_All()
        return Response(response_data)

    def retrieve(self, request, pk=None):
        response_data = Season_UseCases().Get_ByID(id_=pk)
        return Response(response_data)

    @action(detail=False, methods=['get'])
    def GetAll_WithEpisodes(self, request):
        response_data = Season_UseCases().Get_AllWithEpisodes()
        return Response(response_data)

    @action(detail=False, methods=['get'])
    def Get_SpecificWithEpisodes(self, request):
        try:
            id_ = request.GET["id"]
        except:
            return Response(status=500)
        response_data = Season_UseCases().Get_SpecificWithEpisodes(id_=id_)
        return Response(response_data)

    @action(detail=False, methods=['get'])
    def Get_ByStoryID(self, request):
        try:
            id_ = request.GET["id"]
        except:
            return Response(status=500)
        response_data = Season_UseCases().Get_ByStoryID(id_=id_)
        return Response(response_data)

    @action(detail=False, methods=['get'])
    def Search_ByTitle(self, request):
        try:
            title_ = request.GET["title"]
        except:
            return Response(status=500)

        response_data = Season_UseCases().Search_ByTitle(title_=title_)
        return Response(response_data)

    def get_permissions(self):
        permissions_bucket = ["update","create"]
        if self.action in permissions_bucket:
            return [IsAuthenticated()]
        else:
            return [AllowAny()]
            #return super(self, Season_ViewSet).get_permissions()