from django.urls import include, path
from rest_framework import routers
from foodcart import views

router = routers.DefaultRouter()
router.register(r'api/menu', views.MenuViewSet),
router.register(r'api/cuisine', views.CuisineViewSet),
router.register(r'api/mealtype', views.MealTypeViewSet),
router.register(r'api/Address', views.AddressViewSet),
router.register(r'api/state', views.StateViewSet),

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]