from rest_framework import routers

from .views import UserViewSet, RoleViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('roles', RoleViewSet)

urlpatterns = router.urls
