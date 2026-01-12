from rest_framework.viewsets import ModelViewSet

from station.models import Bus
from station.serializers import BusSerializer


class BusViewSet(ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer