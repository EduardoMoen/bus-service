from station.views import BusViewSet
from rest_framework.routers import DefaultRouter

app_name = "station"
router = DefaultRouter()

router.register("buses", BusViewSet)

urlpatterns = router.urls
