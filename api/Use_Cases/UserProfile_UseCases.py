from Bridger.models import UserProfile
from Bridger.serializers import UserProfileSerializer,UserFavouriteSerializer,UserProfileSerializer_Base

class UserProfile_UseCases():
    def __init__(self):
        pass

    def New_Favourite(self,data_):
        serializer = UserFavouriteSerializer(data=data_)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors

    def Get_Profile(self, id_):
        #try:
        obj = UserProfile.objects.all_active().get(id=id_)
        serializer = UserProfileSerializer_Base(obj)
        return serializer.data
        #except:
         #   return {"Error":"User Does not Exists"}

    def Create_Profile(self, data_):
        serializer = UserProfileSerializer_Base(data=data_)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors

    def Update_Profile(self, data, pk):
        try:
            item = UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            return {"Error": "Record Does not Exists"}

        serializer = UserProfileSerializer_Base(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data

        return serializer.errors

    def Delete_Profile(self, data, pk):
        try:
            item = UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            return {"Error": "Record Does not Exists"}
        item.delete()
        return {"Success": "Deleted Successfully!"}


