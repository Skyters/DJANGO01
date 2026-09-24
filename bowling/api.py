from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, viewsets

from bowling.models import Booking
from bowling.serializers import BowlingSerializer

class BookingViewset(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,

    mixins.ListModelMixin, 
    GenericViewSet):
    queryset = Booking.objects.all()
    serializer_class = BowlingSerializer