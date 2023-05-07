from django.urls import path, include
from Profiles_API import views
from rest_framework.routers import DefaultRouter

# URL = http://127.0.0.1:8000/api/profile/
# For a specific user http://127.0.0.1:8000/api/profile/[id_name]

router = DefaultRouter()
# Since in views.py 'queryset' property is set so 'basename' parameter
# will be picked up from there automatically and we don't need to specify it
# in this case
router.register('profile', views.UserProfileViewset)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    # Registering Viewset to routers for DRF to take care of it automatically
    path('', include(router.urls))
]
