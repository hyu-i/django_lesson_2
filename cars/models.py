from django.db import models
from django.utils import timezone


class Insurance(models.Model):
    start_time = models.CharField('開始時期', max_length=100)
    end_time = models.CharField('終了時期', max_length=100)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return f'{self.start_time} ~ {self.end_time}'


class Area(models.Model):
    name = models.CharField('使用地域', max_length=10)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.name


class Car(models.Model):
    area = models.ForeignKey(
        Area, verbose_name='地域', on_delete=models.PROTECT
    )
    number = models.CharField('車番', max_length=30)
    chassis_number = models.CharField('車台番号', max_length=30)
    start_use = models.CharField('使用開始', max_length=40, blank=True)
    insurance_period = models.ForeignKey(
        Insurance, verbose_name='保険開始時期', related_name='insurance_1', on_delete=models.PROTECT
    )
    insurance_number = models.CharField('保険証番号', max_length=50)
    comment = models.TextField('コメント', max_length=255, blank=True)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return f'使用エリア：{self.area}, 車番：{self.number}'
