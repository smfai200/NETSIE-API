from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', schema_view),
    url(r'^api/', include('Bridger.urls')),
    url(r'^api/socialauth/', include('rest_social_auth.urls_token')),
    path('api-token-auth/', obtain_jwt_token, name='create-token'),
    re_path('api/(?P<version>(v1|v2))/', include('authentication.urls')),
]
