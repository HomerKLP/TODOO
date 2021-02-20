from rest_framework.routers import DefaultRouter

from .views import CategoryView

router = DefaultRouter()
router.register(
    prefix='categories', viewset=CategoryView, basename='categories',
)

urlpatterns = router.urls
