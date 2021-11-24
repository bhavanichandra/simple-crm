from rest_framework import routers

from .views import UserViewSet, RoleViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'roles', RoleViewSet, basename='roles')

urlpatterns = router.urls
