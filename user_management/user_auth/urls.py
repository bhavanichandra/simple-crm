from rest_framework import routers

from .views import LoginViewSet, RegisterView

router = routers.DefaultRouter()

router.register(r'login', LoginViewSet, 'login')
router.register(r'register', RegisterView, 'register')

urlpatterns = router.urls
