from rest_framework.routers import DefaultRouter

from .views import ObtainTokenView

router = DefaultRouter()
router.register(
    prefix='tokens', viewset=ObtainTokenView, basename='tokens',
)

urlpatterns = router.urls
