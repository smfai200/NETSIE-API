from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from Bridger.usecases import *
from rest_framework.decorators import action

class UserProfile_ViewSet(ViewSet):

    def create(self, request):
        request.data._mutable = True
        request.data.update({"FK_User": request.user.id,"IsActive":True})
        response_data = UserProfile_UseCases().Update_Profile(data=request.data,pk=request.user.id)
        return Response(response_data)

    def destroy(self, request, pk=None):
        response_data = UserProfile_UseCases().Delete_Profile(data=request.data, pk=pk)
        return Response(response_data)

    def list(self, request, pk=None):
        response_data = UserProfile_UseCases().Get_Profile(id_=request.user.id)
        return Response(response_data)

    @action(detail=False, methods=['get'])
    def New_Favourite(self, request):
        request.data._mutable = True
        request.data.update({"FK_User": request.user.id, "IsActive": True})
        try:
            title_ = request.GET["title"]
        except:
            return Response(status=500)

        response_data = UserProfile_UseCases().New_Favourite(data_=request.data)
        return Response(response_data)
