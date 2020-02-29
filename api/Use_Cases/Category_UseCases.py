from Bridger.models import Category,Story
from Bridger.serializers import CategorySerializer,StorySerializer


class Category_UseCases():
    def __init__(self):
        pass

    def Get_All(self):
        AllVideos = Category.objects.sort_ascending()
        Serializer = CategorySerializer(AllVideos, many=True)
        return Serializer.data

    def get_StoryByCategoryId(self,id_):
        AllVideos = Story.objects.sort_ascending().filter(Story_Category=id_)
        if(len(AllVideos)<=15):
            pass
        else:
            AllVideos = AllVideos[:15]
        Serializer = StorySerializer(AllVideos, many=True)
        return Serializer.data

    def Get_BySeasonID(self,id_):
        Video_ = Category.objects.sort_ascending().filter(Episode_Season=id_)
        if (len(Video_) > 1):
            Serializer = CategorySerializer(Video_, many=True)
        else:
            Serializer = CategorySerializer(Video_[0])
        return Serializer.data

    def Get_ByID(self,id_):
        Video_ = Category.objects.sort_ascending().filter(id=id_)[0]
        Serializer = CategorySerializer(Video_)
        return Serializer.data

    def Get_ByCreateDate(self,date_):
        Video_ = Category.objects.all_active().filter(CreateDate=date_)
        if(len(Video_) > 1):
            Serializer = CategorySerializer(Video_, many=True)
        else:
            Serializer = CategorySerializer(Video_[0])
        return Serializer.data

    def Get_ByUpdateDate(self,date_):
        Video_ = Category.objects.all_active().filter(UpdateDate=date_)
        if(len(Video_) > 1):
            Serializer = CategorySerializer(Video_, many=True)
        else:
            Serializer = CategorySerializer(Video_[0])
        return Serializer.data


    def Search_ByTitle(self,title_):
        Video_ = Category.objects.all_active().filter(Story_Title__icontains=title_)
        if (len(Video_) > 1):
            Serializer = CategorySerializer(Video_, many=True)
        else:
            Serializer = CategorySerializer(Video_[0])
        return Serializer.data

    def Update_Video(self,data,pk):
        try:
            item = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return {"Error":"Record Does not Exists"}
        serializer = CategorySerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data

        return serializer.errors

    def Delete_Video(self,data,pk):
        try:
            item = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return {"Error":"Record Does not Exists"}
        item.delete()
        return 204

