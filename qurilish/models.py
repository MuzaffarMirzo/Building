from django.db import models

class Hudud(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Qurilish_tashkiloti(models.Model):
    name=models.CharField(max_length=150)
    description = models.TextField()
    qachon_tashkil_topgan=models.DateField()
    hudud=models.ForeignKey(Hudud,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Qurilish_binosi(models.Model):
    qurilish_tashkiloti=models.ForeignKey(Qurilish_tashkiloti,on_delete=models.CASCADE)
    hudud=models.ForeignKey(Hudud,on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    maydoni=models.PositiveIntegerField()
    qavat=models.PositiveIntegerField()
    porkovka=models.BooleanField(default=False)
    bolalar_maydonchasi=models.BooleanField(default=False)
    lift=models.BooleanField(default=False)

    def __str__(self):
        return self.name