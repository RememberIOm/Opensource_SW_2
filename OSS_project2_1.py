import pandas as pd


def top_10_players(data_df):
    years_pick = range(2015, 2019)
    data_years = [data_df[data_df['year'] == year] for year in years_pick]

    columns_pick = ['H', 'avg', 'HR', 'OBP']
    data_sort = []
    for data_years_i in data_years:
        data_sort += [[data_years_i.sort_values(by=column, ascending=False) for column in columns_pick]]

    data_top10 = []
    for data_sort_i in data_sort:
        data_top10 += [[data_sort_i_i['batter_name'].head(10) for data_sort_i_i in data_sort_i]]

    return data_top10


data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

top_10_players_list = top_10_players(data_df)
years_pick = range(2015, 2019)
columns_pick = ['H', 'avg', 'HR', 'OBP']

for i in range(len(years_pick)):
    print("%d년" % (years_pick[0] + i), end='\n')
    for j in range(len(columns_pick)):
        print("%s:\t" % columns_pick[j], end='')
        print(*top_10_players_list[i][j], sep=' ', end='\n')