import pandas as pd
from dataprocessing import final_process
from analysis import bands_songs_genre


if __name__ == '__main__':
    # df = final_process()
    # print(df[df['lyrics'].str.contains("guitars")])
    # print(len(df))
    # df.to_csv('metal_data_final.csv', index=False, encoding='utf-8')
    df = pd.read_csv('metal_data_final.csv', encoding='utf-8')
    df_bands = bands_songs_genre(df)
    df_all_bands = df_bands[['band']]
    df_all_bands.to_csv('band_list.csv', index=False, header=False, encoding='utf-8')
    df_black_bands = df_bands[df_bands['genre'] == 1]
    df_black_bands = df_black_bands[['band', 'songs']]
    df_black_bands.to_csv('blackmetal_list.csv', index=False, header=False, encoding='utf-8')
    df_death_bands = df_bands[df_bands['genre'] == 0]
    df_death_bands = df_death_bands[['band', 'songs']]
    df_death_bands.to_csv('deathmetal_list.csv', index=False, header=False, encoding='utf-8')

