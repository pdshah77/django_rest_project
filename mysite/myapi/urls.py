# myapi/urls.py

from django.conf.urls import url,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.HeroViewSet)

addrouter = routers.DefaultRouter()
addrouter.register('',views.AddressViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url('heroes', include(router.urls)),
	url('address',include(addrouter.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]