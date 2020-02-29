from Bridger.models import Story
from Bridger.serializers import StorySerializer,StorySeasonSerializer


class Story_UseCases():
    def __init__(self):
        pass

    def Get_All(self):
        AllStorys = Story.objects.sort_ascending()
        Serializer = StorySerializer(AllStorys, many=True)
        return Serializer.data

    def Get_All_WithSeasons(self):
        AllStorys = Story.objects.sort_ascending()
        Serializer = StorySeasonSerializer(AllStorys, many=True)
        return Serializer.data

    def GetSpecific_WithSeasons(self,id_):
        AllStorys = Story.objects.sort_ascending().filter(id=id_)
        if (len(AllStorys) < 1):
            return {"Error":"Story does not exists"}
        else:
            Serializer = StorySeasonSerializer(AllStorys, many=True)
        return Serializer.data

    def Get_LatestFifteen(self):
        AllStorys = Story.objects.sort_ascending()
        if(len(AllStorys)<=15):
            pass
        else:
            AllStorys = AllStorys[:15]
        Serializer = StorySerializer(AllStorys, many=True)
        return Serializer.data

    def Get_StoriesOfUser(self,id_):
        Story_ = Story.objects.sort_ascending().filter(FK_User=id_)
        if (len(Story_) > 1):
            Serializer = StorySerializer(Story_, many=True)
        else:
            Serializer = StorySerializer(Story_[0])
        return Serializer.data

    def Get_StoriesOfUserWithSeasons(self,id_):
        Story_ = Story.objects.sort_ascending().filter(FK_User=id_)
        if (len(Story_) > 1):
            Serializer = StorySeasonSerializer(Story_, many=True)
        else:
            Serializer = StorySeasonSerializer(Story_[0])
        return Serializer.data

    def Get_ByID(self,id_):
        Story_ = Story.objects.sort_ascending().filter(id=id_)[0]
        Serializer = StorySerializer(Story_)
        return Serializer.data

    def Get_ByCreateDate(self,date_):
        Story_ = Story.objects.all_active().filter(CreateDate=date_)
        if(len(Story_) > 1):
            Serializer = StorySerializer(Story_, many=True)
        else:
            Serializer = StorySerializer(Story_[0])
        return Serializer.data

    def Get_ByUpdateDate(self,date_):
        Story_ = Story.objects.all_active().filter(UpdateDate=date_)
        if(len(Story_) > 1):
            Serializer = StorySerializer(Story_, many=True)
        else:
            Serializer = StorySerializer(Story_[0])
        return Serializer.data


    def Search_ByTitle(self,title_):
        Story_ = Story.objects.all_active().filter(Story_Title__icontains=title_)
        if (len(Story_) > 1):
            Serializer = StorySerializer(Story_, many=True)
        else:
            Serializer = StorySerializer(Story_[0])
        return Serializer.data

    def Create_Story(self,data_):

        serializer = StorySerializer(data=data_)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors

    def Update_Story(self,data,pk):
        try:
            item = Story.objects.get(pk=pk)
            if(item.FK_User.id == data["FK_User"]):
                pass
            else:
                return {"Error": "You are not Authorized to Edit the Story"}
        except Story.DoesNotExist:
            return {"Error":"Record Does not Exists"}
        serializer = StorySerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data

        return serializer.errors

    def Delete_Story(self,data,pk):
        try:
            item = Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            return {"Error":"Record Does not Exists"}
        item.delete()
        return {"Success":"Deleted Successfully!"}



