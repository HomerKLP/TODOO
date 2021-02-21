from rest_framework.routers import DefaultRouter

from .views import CategoryView, CardView

router = DefaultRouter()
router.register(
    prefix='categories', viewset=CategoryView, basename='categories',
)
router.register(
    prefix='cards', viewset=CardView, basename='cards',
)

urlpatterns = router.urls
