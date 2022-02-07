import pandas as pd
from dataprocessing import final_process

if __name__ == '__main__':
    df = final_process()
    # print(df[df['lyrics'].str.contains("guitars")])
    # print(len(df))
    df.to_csv('metal_data_final.csv', index=False, encoding='utf-8')

