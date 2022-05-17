from django.db import models

class Diamonds4c(models.Model):

    ogr = models.CharField('Огранка', max_length=20)
    col = models.CharField('Цвет', max_length=3)
    cla = models.CharField('Чистота', max_length=3)
    cut = models.CharField('Параметр огранки', max_length=1)
    carat = models.FloatField('Карат')
    pcs = models.IntegerField('Штук')

    def __str__(self):
        return str(self.pcs)+self.ogr+"-"+self.col+'/'+self.cla+\
               ' ' + self.cut+'-'+str(self.carat)
    class Meta:
        verbose_name = 'Сертифицированный бриллиант'
        verbose_name_plural = 'Сертифицированные бриллианты'


class SertDiamonds(models.Model):
    num = models.CharField('Номер сертификата', max_length=14)
    CP_front = models.ImageField('ФотоКПспереди')
    ogr = models.CharField('Огранка', max_length=20)
    col = models.CharField('Цвет', max_length=3)
    cla = models.CharField('Чистота', max_length=3)
    cut = models.CharField('Параметр огранки', max_length=1)
    carat = models.FloatField('Карат')
    pcs = models.IntegerField('Штук')

    def __str__(self):
        return num + str(self.pcs) + self.ogr + "-" + self.col + '/' + self.cla + \
               ' ' + self.cut + '-' + str(self.carat)

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'



