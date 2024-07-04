from rest_framework import Serializer
from .models import Hudud,Qurilish_tashkiloti,Qurilish_binosi

class HududSerializer(Serializer):
    class Meta:
        model = Hudud
        fields = '__all__'

class Qurilish_tashkilotiSerializer(Serializer):
    class Meta:
        model = Qurilish_tashkiloti
        fields = '__all__'

class Qurilish_binosiSerializer(Serializer):
    class Meta:
        model = Qurilish_binosi
        fields = '__all__'

        