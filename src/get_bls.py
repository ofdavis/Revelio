# %% --------------------------------imports------------------------------------------------

import os
import numpy as np 
import pandas as pd 
import markdown 
import statsmodels.api as sm
import requests
from bs4 import BeautifulSoup as bs
from fredapi import Fred
from dotenv import load_dotenv
load_dotenv()
key = os.getenv('FRED_API_KEY') # 
fred = Fred(api_key=key)

# %% --------------------------------state dict------------------------------------------------
def get_ur(start,end):
    state_dict = {
        "AK": "Alaska",
        "AL": "Alabama",
        "AR": "Arkansas",
        "AZ": "Arizona",
        "CA": "California",
        "CO": "Colorado",
        "CT": "Connecticut",
        "DE": "Delaware",
        "FL": "Florida",
        "GA": "Georgia",
        "HI": "Hawaii",
        "IA": "Iowa",
        "ID": "Idaho",
        "IL": "Illinois",
        "IN": "Indiana",
        "KS": "Kansas",
        "KY": "Kentucky",
        "LA": "Louisiana",
        "MA": "Massachusetts",
        "MD": "Maryland",
        "ME": "Maine",
        "MI": "Michigan",
        "MN": "Minnesota",
        "MO": "Missouri",
        "MS": "Mississippi",
        "MT": "Montana",
        "NC": "North Carolina",
        "ND": "North Dakota",
        "NE": "Nebraska",
        "NH": "New Hampshire",
        "NJ": "New Jersey",
        "NM": "New Mexico",
        "NV": "Nevada",
        "NY": "New York",
        "OH": "Ohio",
        "OK": "Oklahoma",
        "OR": "Oregon",
        "PA": "Pennsylvania",
        "RI": "Rhode Island",
        "SC": "South Carolina",
        "SD": "South Dakota",
        "TN": "Tennessee",
        "TX": "Texas",
        "UT": "Utah",
        "VA": "Virginia",
        "VT": "Vermont",
        "WA": "Washington",
        "WI": "Wisconsin",
        "WV": "West Virginia",
        "WY": "Wyoming",
        "DC": "District of Columbia",
    }

    # %% ----- import from fred ----- 
    ur = pd.DataFrame()
    for st, state in state_dict.items():
        tmp = fred.get_series(f'{st}UR', observation_start=start, observation_end=end).reset_index()
        tmp['state'] = state
        tmp['post_mo'] = tmp['index'].dt.to_period('M')
        tmp.rename(columns={0:'ur'}, inplace=True)
        ur = pd.concat([ur, tmp[['ur', 'state', 'post_mo']]], ignore_index=True)

    # %%
    return ur 
