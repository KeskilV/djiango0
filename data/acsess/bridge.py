# new bridge
import pandas as pd
import sys


# import numpy as np

def test_col(df, key):
    '''
    key=0 enter after acsess q
    key=1 output for SQLite and MySQL
    '''
    if key == 0:
        test_columns = ['id', 'id_11', 'kod_t', 'part', 'kod_r', 'nsert', 'dsert', 'ogr',
                        'shape', 'DiametrMin', 'DiametrMax', 'sizes', 'obshmass', 'carat',
                        'pcs', 'col_r', 'cla_r', 'po_r', 'flour', 'comment', 'TotalDepth',
                        'diametr', 'PavilDepth', 'PavilAngle', 'CrownHeight', 'CrownAngle',
                        'TableSize', 'Girdle_max', 'Girdle_min', 'CuletSize', 'print',
                        'diamdev', 'Weight', 'kod', 'mras', 'col_gia', 'cla_gia', 'cut_gia',
                        'res', 'slug']
    else:
        test_columns = ['id', 'id_1', 'kod_t', 'part', 'kod_r', 'nsert', 'dsert', 'ogr',
                        'shape', 'DiametrMin', 'DiametrMax', 'sizes', 'obshmass', 'carat',
                        'pcs', 'col_r', 'cla_r', 'po_r', 'flour', 'comment', 'TotalDepth',
                        'diametr', 'PavilDepth', 'PavilAngle', 'CrownHeight', 'CrownAngle',
                        'TableSize', 'Girdle_max', 'Girdle_min', 'CuletSize', 'print',
                        'diamdev', 'Weight', 'kod', 'mras', 'col_gia', 'cla_gia', 'cut_gia',
                        'res', 'slug']
    return all(df.columns == test_columns)


def corr_floats(df):
    '''
    formatting floats
    '''
    flcols = ['DiametrMin',
              'DiametrMax',
              'sizes',
              'obshmass',
              'carat',
              'TotalDepth',
              'diametr',
              'PavilDepth',
              'PavilAngle',
              'CrownHeight',
              'CrownAngle',
              'TableSize',
              'Girdle_max',
              'Girdle_min',
              'CuletSize',
              'Weight',
              'kod',
              'mras']
    for c in flcols:
        df[c] = round(df[c], 3)
    return df


def load_df(file_in=False):
    if len(sys.argv) == 2:
        file_in = sys.argv[1]
    else:
        if not file_in:
            file_in = input('file for bridge: ')
    if file_in.split('.')[-1] == 'csv':
        df = pd.read_csv(file_in, sep=';', encoding='cp1251')
    else:
        df = pd.read_excel(file_in)
    print('ok ', len(df))
    return df, file_in


def save_res(df, file_in):
    file_out = file_in.split('.')[0] + '_conv8.csv'
    df.to_csv(file_out, encoding='cp1251', index=False)
    print('saved: ', resfilename)


def main():
    df, file_in = load_df()
    print('test columns in ', test_col(df, 0))
    df = corr_floats(df)
    # df['slug'] = df.kod_t.astype('str')+'-'+df.kod_r+df.nsert #df.carat.astype('str')+'c'+
    df.rename(columns={"id_11": "id_1"}, inplace=True)
    print('test columns out ', test_col(df, 1))
    save_res(df, file_in)


main()