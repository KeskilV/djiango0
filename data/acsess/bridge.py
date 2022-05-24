import pandas as pd
import sys
#import numpy as np


def helper_models(x):
    mytypes = ['float', 'int', 'str']
    mydict = {'float': 'FloatField',
              'int': 'IntegerField',
              'str': 'CharField'}
    for mt in mytypes:
        if x.__contains__(mt):
            return mydict[mt]

if len(sys.argv) == 2:
    filecsv = sys.argv[1]
else:
    filecsv = 'for_site0.csv'
df = pd.read_csv(filecsv, sep=';', encoding='cp1251')
print('ok', len(df))
df['col_gia'] = None
df['cla_gia'] = None
df['cut_gia'] = None
df['res'] = None
names = list(df.columns)
types = [type(df.iloc[0,i]) for i in range(len(names))]
new_names = ['id_1', 'kod_t', 'part', 'kod_r', 'nsert', 'dsert', 'ogr', 'shape', 'DiametrMin', 'DiametrMax',
 'sizes', 'obshmass', 'carat', 'psc', 'col_r', 'cla_r', 'po_r', 'flour', 'comment', 'TotalDepth',
 'diametr', 'PavilDepth', 'PavilAngle', 'CrownHeight', 'CrownAngle', 'TableSize', 'Girdle_max',
 'Girdle_min', 'CuletSize', 'print', 'diamdev', 'Weight', 'kod', 'mras', 'col_gia', 'cla_gia', 'cut_gia', 'res']
d = dict()
for i,x in enumerate(names):
    d[x] = new_names[i]
'''
for i, n in enumerate(names):
    print("    {} = models.{}('{}'{})".format(
        new_names[i], helper_models(str(types[i])), n,
        ', max_length=' if  helper_models(str(types[i])) == 'CharField' else ''))
'''
df.rename(columns=d, inplace=True)
flcols=[]
for i,n in enumerate(names):
    if helper_models(str(types[i])) == 'FloatField':
        flcols.append(new_names[i])
flcols.remove('flour')
flcols.remove('diamdev')
for c in flcols:
    df[c]=round(df[c],3)
df['slug'] = df.kod_t.astype('str')+'-'+df.carat.astype('str')+'c'+df.kod_r+df.nsert
df.to_csv(filecsv.split('.')[0]+'slug_conv.csv', encoding='cp1251')
print ('saved: ', filecsv.split('.')[0]+'slag_conv.csv')
#df.columns

'''
cla = models.CharField('Чистота', max_length=3)
cut = models.CharField('Параметр огранки', max_length=1)
carat = models.FloatField('Карат')
pcs = models.IntegerField('Штук')
'''