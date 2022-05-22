from django.db import models
from django.urls import reverse


class SertDiamonds1(models.Model):
    id_1 = models.IntegerField('id_1')
    kod_t = models.IntegerField('код_т')
    part = models.IntegerField('партия')
    kod_r = models.CharField('код_случ', max_length=6)
    nsert = models.CharField('номер_паспорта', max_length=10)
    dsert = models.CharField('дата_паспорта', max_length=10)
    ogr = models.CharField('огранка', max_length=25)
    shape = models.CharField('shape', max_length=25)
    DiametrMin = models.FloatField('DiametrMin')
    DiametrMax = models.FloatField('DiametrMax')
    sizes = models.FloatField('Размеры')
    obshmass = models.FloatField('ОБЩМАССА')
    carat = models.FloatField('масса')
    pcs = models.IntegerField('штук')
    col_r = models.CharField('цвет', max_length=4)
    cla_r = models.CharField('чистота', max_length=4)
    po_r = models.CharField('геом_парам', max_length=2)
    flour = models.CharField('флуор',  max_length=10)
    comment = models.CharField('комент', max_length=50)
    TotalDepth = models.FloatField('TotalDepth')
    diametr = models.FloatField('diametr')
    PavilDepth = models.FloatField('PavilDepth')
    PavilAngle = models.FloatField('PavilAngle')
    CrownHeight = models.FloatField('CrownHeight')
    CrownAngle = models.FloatField('CrownAngle')
    TableSize = models.FloatField('TableSize')
    Girdle_max = models.FloatField('Girdle_max')
    Girdle_min = models.FloatField('Girdle_min')
    CuletSize = models.FloatField('CuletSize')
    print = models.IntegerField('принт')
    diamdev = models.FloatField('diamdev')
    Weight = models.FloatField('Weight')
    kod = models.FloatField('kod')
    mras = models.FloatField('mras')
    col_gia = models.CharField('col_gia', max_length=20)
    cla_gia = models.CharField('cla_gia', max_length=10)
    cut_gia = models.CharField('cut_gia', max_length=10)
    res = models.CharField('res', max_length=10)

    def __str__(self):
        return self.nsert+'  '+str(self.pcs) + '  ' + self.ogr + "  " + self.col_r + '/' + self.cla_r + \
               ' ' + self.po_r + '  ' + str(round(self.carat, 2))

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

    def get_absolut_url(self):
        return reverse('sertpar', kwargs={'id_1':self.pk})

