import pandas as pd
import numpy as np
import COVID

Cuyahoga_population = COVID.get_county_pop('Cuyahoga')

Cuyahoga_df = COVID.get_county_COVID_df('Cuyahoga')

Cuyahoga_deaths = COVID.count_dead(Cuyahoga_df)

print(Cuyahoga_deaths)