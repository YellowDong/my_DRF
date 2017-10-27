from . import views
from django.conf.urls import include, url
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'myapp', views.IpoInfoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

]