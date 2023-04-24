from rest_framework import routers
from app.api.viewsets import SensorViewSet, SensorRecordViewSet

router = routers.DefaultRouter()
router.register(r'sensor', SensorViewSet)
router.register(r'data', SensorRecordViewSet)

# Routes for service REST requests.
urlpatterns = router.urls
