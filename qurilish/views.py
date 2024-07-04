
from .models import Hudud,Qurilish_tashkiloti,Qurilish_binosi

from .serializers import HududSerializer,Qurilish_tashkilotiSerializer,Qurilish_binosiSerializer
from .permissions import CastomPermission
from rest_framework.viewsets import ModelViewSet

class HududView(ModelViewSet):
    queryset = Hudud.objects.all()
    serializer_class = HududSerializer
    permission_classes = [CastomPermission]

class Qurilish_tashkilotiView(ModelViewSet):
    queryset = Qurilish_tashkiloti.objects.all()
    serializer_class = Qurilish_tashkilotiSerializer
    permission_classes = [CastomPermission]

class Qurilish_binosiView(ModelViewSet):
    queryset = Qurilish_binosi.objects.all()
    serializer_class = Qurilish_binosiSerializer
    permission_classes = [CastomPermission]
