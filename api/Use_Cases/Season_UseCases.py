from Bridger.models import Season
from Bridger.serializers import SeasonSerializer, SeasonEpisodeSerializer


class Season_UseCases():
    def __init__(self):
        pass

    def Get_All(self):
        AllSeasons = Season.objects.sort_ascending()
        Serializer = SeasonSerializer(AllSeasons, many=True)
        return Serializer.data

    def Get_AllWithEpisodes(self):
        AllSeasons = Season.objects.sort_ascending()
        Serializer = SeasonEpisodeSerializer(AllSeasons, many=True)
        return Serializer.data

    def Get_SpecificWithEpisodes(self,id_):
        AllSeasons = Season.objects.sort_ascending().filter(id=id_)
        Serializer = SeasonEpisodeSerializer(AllSeasons, many=True)
        return Serializer.data

    def Get_ByStoryID(self,id_):
        Season_ = Season.objects.sort_ascending().filter(Fk_Story=id_)
        print(Season_)
        if (len(Season_) > 1):
            Serializer = SeasonSerializer(Season_, many=True)
        else:
            Serializer = SeasonSerializer(Season_[0])
            return [Serializer.data]
        return Serializer.data

    def Get_ByID(self,id_):
        Season_ = Season.objects.sort_ascending().filter(id=id_)[0]
        Serializer = SeasonSerializer(Season_)
        return Serializer.data

    def Get_ByCreateDate(self,date_):
        Season_ = Season.objects.all_active().filter(CreateDate=date_)
        if(len(Season_) > 1):
            Serializer = SeasonSerializer(Season_, many=True)
        else:
            Serializer = SeasonSerializer(Season_[0])
        return Serializer.data

    def Get_ByUpdateDate(self,date_):
        Season_ = Season.objects.all_active().filter(UpdateDate=date_)
        if(len(Season_) > 1):
            Serializer = SeasonSerializer(Season_, many=True)
        else:
            Serializer = SeasonSerializer(Season_[0])
        return Serializer.data


    def Search_ByTitle(self,title_):
        Season_ = Season.objects.all_active().filter(Season_Title__icontains=title_)
        if (len(Season_) > 1):
            Serializer = SeasonSerializer(Season_, many=True)
        else:
            Serializer = SeasonSerializer(Season_[0])
        return Serializer.data
    
    def Create_Season(self,data_):
        serializer = SeasonSerializer(data=data_)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors

    def Update_Season(self,data,pk):
        try:
            item = Season.objects.get(pk=pk)
            if(not "Fk_Story" in data):
                return {"Error": "Invalid Story Reference"}
            elif (item.Fk_Story.id == data["Fk_Story"]):
                pass
            elif(item.Fk_Story.FK_User.id == data["FK_User"]):
                return {"Error": "You are not Authorized to Edit the Season"}
            else:
                pass
        except Season.DoesNotExist:
            return {"Error":"Record Does not Exists"}
        serializer = SeasonSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data

        return serializer.errors

    def Delete_Season(self,data,pk):
        try:
            item = Season.objects.get(pk=pk)
        except Season.DoesNotExist:
            return {"Error":"Record Does not Exists"}
        item.delete()
        return {"Success":"Deleted Successfully!"}

