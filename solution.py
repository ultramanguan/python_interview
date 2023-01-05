import pandas as pd
import sys
import os

def weather_result(file_name):
    file_path=os.path.join(os.getcwd(),file_name)

    # read in source file
    df=pd.read_csv(file_path)

    # manipulate timestamp to date
    df['Date']=pd.to_datetime(df['Measurement Timestamp']).dt.strftime('%m/%d/%Y')

    # sort timestamp for each station for first and last value
    df_sorted=df.sort_values(by=['Station Name','Measurement Timestamp'])

    # calculate daily aggregations
    df_result=df_sorted.groupby(['Station Name','Date'])['Air Temperature'].agg(['min','max','first','last']).reset_index()

    # rename columns
    rename_dict={'min':'Min Temp','max':'Max Temp','first':'First Temp','last':'Last Temp'}
    df_result.rename(columns=rename_dict,inplace=True)

    # export result
    df_result.to_csv('solution.csv',index=False)

if __name__ == "__main__":
    weather_result(sys.argv[1])