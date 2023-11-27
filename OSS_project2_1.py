import pandas as pd


def top_10_players(data_df):
    YEARS_PICK = range(2015, 2019)
    data_years = [data_df[data_df['year'] == year] for year in YEARS_PICK]

    COLUMNS_PICK = ['H', 'avg', 'HR', 'OBP']
    data_sort = []
    for data_years_i in data_years:
        data_sort += [[data_years_i.sort_values(by=column, ascending=False) for column in COLUMNS_PICK]]

    data_top10 = []
    for data_sort_i in data_sort:
        data_top10 += [[data_sort_i_i['batter_name'].head(10) for data_sort_i_i in data_sort_i]]

    return data_top10

def top_players_cp(data_df):
    YEARS_PICK = 2018
    data_years = data_df[data_df['year'] == YEARS_PICK]

    CPS_PICK = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']
    data_cps = [data_years[data_years['cp'] == cp] for cp in CPS_PICK]

    COLUMNS_PICK = 'war'
    data_sort = [data_cps_i.sort_values(by=COLUMNS_PICK, ascending=False) for data_cps_i in data_cps]

    data_top = [data_sort_i['batter_name'].head(1) for data_sort_i in data_sort]

    return data_top

def cal_corr(data_df):
    COLUMNS_PICK_1 = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']
    COLUMNS_PICK_2 = 'salary'

    data_corr = [data_df[column].corr(data_df[COLUMNS_PICK_2]) for column in COLUMNS_PICK_1]

    return data_corr


data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

# Q1
top_10_players_list = top_10_players(data_df)
YEARS_PICK = range(2015, 2019)
COLUMNS_PICK = ['H', 'avg', 'HR', 'OBP']

for i in range(len(YEARS_PICK)):
    print("%d년" % (YEARS_PICK[0] + i), end='\n')
    for j in range(len(COLUMNS_PICK)):
        print("%s:\t" % COLUMNS_PICK[j], end='')
        print(*top_10_players_list[i][j], sep=' ', end='\n')

print()

# Q2
top_players_cp_list = top_players_cp(data_df)
CPS_PICK = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']

for i in range(len(CPS_PICK)):
    print("%s:\t%s" % (CPS_PICK[i], top_players_cp_list[i].values[0]))

print()

# Q3
data_corr_list = cal_corr(data_df)
COLUMNS_PICK_1 = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']

for column in range(len(COLUMNS_PICK_1)):
    print("%s:\t%f" % (COLUMNS_PICK_1[column], data_corr_list[column]))

print("가장 상관관계가 높은 변수는 %s이다." % COLUMNS_PICK_1[data_corr_list.index(max(data_corr_list))])