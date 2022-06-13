from django.db import models
from django.utils. timezone import now
from django.contrib.auth.models import User


class Mofast(models.Model):
    date = models.DateField(default=now)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    scheduled = models.IntegerField()
    cancelled = models.IntegerField()
    pending = models.IntegerField()
    percentage = models.FloatField(default=0)

    def __str__(self):
        return str(self.owner)

    class Meta:
        verbose_name_plural = 'Mofast'


class Trade2w(models.Model):
    date = models.DateField(default=now)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    scheduled = models.IntegerField()
    cancelled = models.IntegerField()
    pending = models.IntegerField()
    percentage = models.FloatField(default=0)

    def __str__(self):
        return str(self.owner)
    class Meta:
        verbose_name_plural = '2W Trade'


class Eglobal(models.Model):
    date = models.DateField(default=now)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    scheduled = models.IntegerField()
    cancelled = models.IntegerField()
    pending = models.IntegerField()
    percentage = models.FloatField(default=0)

    def __str__(self):
        return str(self.owner)

    class Meta:
        verbose_name_plural = 'Eglobal'


class Unateus(models.Model):
    date = models.DateField(default=now)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    scheduled = models.IntegerField()
    cancelled = models.IntegerField()
    pending = models.IntegerField()
    percentage = models.FloatField(default=0)

    def __str__(self):
        return str(self.owner)

    class Meta:
        verbose_name_plural = 'Unateus'


class Halisi(models.Model):
    date = models.DateField(default=now)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    scheduled = models.IntegerField()
    cancelled = models.IntegerField()
    pending = models.IntegerField()
    percentage = models.FloatField(default=0)

    def __str__(self):
        return str(self.owner)

    class Meta:
        verbose_name_plural = 'Halisi'


class Mainstream(models.Model):
    date = models.DateField(default=now)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    scheduled = models.IntegerField()
    cancelled = models.IntegerField()
    pending = models.IntegerField()
    percentage = models.FloatField(default=0)

    def __str__(self):
        return str(self.owner)

    class Meta:
        verbose_name_plural = 'Mainstream'


class Clinton(models.Model):
    date = models.DateField(default=now)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    scheduled = models.IntegerField()
    cancelled = models.IntegerField()
    pending = models.IntegerField()
    percentage = models.FloatField(default=0)

    def __str__(self):
        return str(self.owner)

    class Meta:
        verbose_name_plural = 'Clinton Stores'


class WarehouseKe(models.Model):
    date = models.DateField(default=now)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    scheduled = models.IntegerField()
    cancelled = models.IntegerField()
    pending = models.IntegerField()
    percentage = models.FloatField(default=0)

    def __str__(self):
        return str(self.owner)

    class Meta:
        verbose_name_plural = 'Ke-Warehouse'


class Adlat(models.Model):
    date = models.DateField(default=now)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    scheduled = models.IntegerField()
    cancelled = models.IntegerField()
    pending = models.IntegerField()
    percentage = models.FloatField(default=0)

    def __str__(self):
        return str(self.owner)

    class Meta:
        verbose_name_plural = 'Adlat'


class BNE(models.Model):
    date = models.DateField(default=now)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    scheduled = models.IntegerField()
    cancelled = models.IntegerField()
    pending = models.IntegerField()
    percentage = models.FloatField(default=0)

    def __str__(self):
        return str(self.owner)

    class Meta:
        verbose_name_plural = '2BNE'


class Vital(models.Model):
    date = models.DateField(default=now)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    total = models.IntegerField()
    scheduled = models.IntegerField()
    cancelled = models.IntegerField()
    pending = models.IntegerField()
    percentage = models.FloatField(default=0)

    def __str__(self):
        return str(self.owner)

    class Meta:
        verbose_name_plural = 'Vital'


'''class Agent(models.Model):
    owner = models.CharField( Mofast, Trade2w, Eglobal, Unateus, Halisi, Mainstream, Clinton, WarehouseKe, Adlat, BNE,
                              Vital, on_delete=models.CASCADE)
    date = models.CharField(Mofast, Trade2w, Eglobal, Unateus, Halisi, Mainstream, Clinton, WarehouseKe, Adlat, BNE,
                            Vital, on_delete=models.CASCADE)
    percentage = models.FloatField(Mofast, Trade2w, Eglobal, Unateus, Halisi, Mainstream, Clinton, WarehouseKe, Adlat,
                                   BNE, Vital)
   
    @property
    def name(self):
        return self.owner.name

    @property
    def date_called(self):
        return self.date

    @property
    def perfomance(self):
        return self.percentage
'''






