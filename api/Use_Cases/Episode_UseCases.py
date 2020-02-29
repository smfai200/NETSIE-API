from Bridger.models import Episode
from Bridger.serializers import EpisodeSerializer

class Episode_UseCases():
    def __init__(self):
        pass

    def Get_All(self):
        AllEpisodes = Episode.objects.sort_ascending()
        Serializer = EpisodeSerializer(AllEpisodes, many=True)
        return Serializer.data

    def Get_ByEpisodeID(self,id_):
        Episode_ = Episode.objects.sort_ascending().filter(Episode_Episode=id_)
        if (len(Episode_) > 1):
            Serializer = EpisodeSerializer(Episode_, many=True)
        else:
            Serializer = EpisodeSerializer(Episode_[0])
        return Serializer.data

    def Get_BySeasonID(self,id_):
        Episode_ = Episode.objects.sort_ascending().filter(Episode_Season=id_)
        if (len(Episode_) > 1):
            Serializer = EpisodeSerializer(Episode_, many=True)
        else:
            Serializer = EpisodeSerializer(Episode_[0])
            return [Serializer.data]
        return Serializer.data

    def Get_ByID(self,id_):
        Episode_ = Episode.objects.sort_ascending().filter(id=id_)[0]
        Serializer = EpisodeSerializer(Episode_)
        return Serializer.data

    def Get_ByCreateDate(self,date_):
        Episode_ = Episode.objects.all_active().filter(CreateDate=date_)
        if(len(Episode_) > 1):
            Serializer = EpisodeSerializer(Episode_, many=True)
        else:
            Serializer = EpisodeSerializer(Episode_[0])
        return Serializer.data

    def Get_ByUpdateDate(self,date_):
        Episode_ = Episode.objects.all_active().filter(UpdateDate=date_)
        if(len(Episode_) > 1):
            Serializer = EpisodeSerializer(Episode_, many=True)
        else:
            Serializer = EpisodeSerializer(Episode_[0])
        return Serializer.data

    def Search_ByTitle(self,title_):
        Episode_ = Episode.objects.all_active().filter(Episode_Title__icontains=title_)
        if (len(Episode_) > 1):
            Serializer = EpisodeSerializer(Episode_, many=True)
        else:
            Serializer = EpisodeSerializer(Episode_[0])
        return Serializer.data

    def Create_Episode(self, data_):
        serializer = EpisodeSerializer(data=data_)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors

    def Update_Episode(self, data, pk):
        try:
            item = Episode.objects.get(pk=pk)
            if (not "Episode_Season" in data):
                return {"Error": "Invalid Season Reference"}
            elif (not item.Episode_Season.id == int(data["Episode_Season"])):
                return {"Error": "aYou are not Authorized to Edit the Episode"}
            elif (item.Episode_Season.Fk_Story.FK_User.id == data["FK_User"]):
                return {"Error": "bYou are not Authorized to Edit the Episode"}
            else:
                pass
        except Episode.DoesNotExist:
            return {"Error": "Record Does not Exists"}

        serializer = EpisodeSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data

        return serializer.errors

    def Delete_Episode(self, data, pk):
        try:
            item = Episode.objects.get(pk=pk)
        except Episode.DoesNotExist:
            return {"Error": "Record Does not Exists"}
        item.delete()
        return {"Success": "Deleted Successfully!"}


