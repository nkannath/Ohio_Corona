# library for COVID Data

import pandas as pd
import numpy as np

county_pop_data =  "ohio_county_populations.csv"

gov_data = "COVIDSummaryData.csv"

counties_df = pd.read_csv(county_pop_data)
gov_df = pd.read_csv(gov_data)

def get_county_pop(county):
    # returns population as integer
    county_str = county + " County"
    df = counties_df.set_index('County')
    county_series = df.loc[county_str]
    population = county_series['Population']
    return population


def get_county_COVID_df(county):
    # returns df of a given county
    county_indices = gov_df.index[gov_df['County'] == county].tolist()
    county_df = gov_df.iloc[county_indices]
    return county_df
    

def count_dead(df):
    # counts the number of dead
    deaths = df['Death Count'].sum()
    deaths = int(deaths)
    return deaths