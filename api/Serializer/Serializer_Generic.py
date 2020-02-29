from rest_framework.serializers import ModelSerializer

from Bridger.models import Category, Story, Season, Episode, EpisodeReview,UserProfile,UserFavourite


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class StorySerializer(ModelSerializer):

    class Meta:
        model = Story
        fields = '__all__'


class SeasonSerializer(ModelSerializer):

    class Meta:
        model = Season
        fields = '__all__'


class StorySeasonSerializer(ModelSerializer):
    Seasons = SeasonSerializer(many=True)
    class Meta:
        model = Story
        fields = '__all__'

class EpisodeSerializer(ModelSerializer):

    class Meta:
        model = Episode
        fields = '__all__'


class SeasonEpisodeSerializer(ModelSerializer):
    Episodes = EpisodeSerializer(many=True)
    class Meta:
        model = Season
        fields = '__all__'

class EpisodeReviewSerializer(ModelSerializer):

    class Meta:
        model = EpisodeReview
        fields = '__all__'

class UserFavouriteSerializer(ModelSerializer):

    class Meta:
        model = UserFavourite
        fields = '__all__'

class UserProfileSerializer_Base(ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSerializer(ModelSerializer):
    Favourites = UserFavouriteSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


