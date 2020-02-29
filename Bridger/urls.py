from rest_framework.routers import SimpleRouter

from Bridger import views

router = SimpleRouter()

router.register(r'story', views.Story_ViewSet, 'Story'),
router.register(r'season', views.Season_ViewSet, 'Season'),
router.register(r'episode', views.Episode_ViewSet, 'Episodes')
router.register(r'category', views.CategoryViewSet, 'Category')
router.register(r'profile', views.UserProfile_ViewSet, 'Profile')
urlpatterns = router.urls
