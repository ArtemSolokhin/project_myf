from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'user', views.UserViewSet)
router.register(r'culture', views.CultureViewSet)
router.register(r'field', views.FieldViewSet)
router.register(r'dates-cults', views.DatesCultsViewSet)


urlpatterns = [
    path('api/v1/', include((router.urls, "api"), namespace='api')),
    path('api/v1/user/', views.UserViewSet.as_view({'get': 'list'}), name='user'),
    path('api/v1/field/', views.FieldViewSet.as_view({'get': 'list'}), name='field'),
    path('api/v1/culture/', views.CultureViewSet.as_view({'get': 'list'}), name='culture'),
    path('api/v1/dates-cults/', views.DatesCultsViewSet.as_view({'get': 'list'}), name='culture'),
]