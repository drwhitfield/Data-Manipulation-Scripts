#!/usr/local/bin/python3

'''
This script transforms or cleans Excel files (provided by Business Units)
to help facilitate creating a scanning environment in Qualys.
'''

__author__    = 'Donald Whitfield'
__copyright__ = 'S-Box Security, LLC'
__email__     = 'donaldwhitfield@icloud.com'
__satus__     = 'Development Version'

import numpy as np
import pandas as pd

bus_unit = pd.read_excel('Exacq.xlsx')
bu_websites = pd.read_excel('Exacq.xlsx', sheet_name="website list")
bu_iplist = pd.read_excel('Exacq.xlsx', sheet_name="IP address")

pd.set_option("display.max_rows", None, "display.max_columns", None) 
pd.set_option('display.width', None, 'display.max_colwidth', None)

bu_websites_clean = bu_websites[['FQDNs', 'Environment']]
sorted_data = bu_websites_clean.sort_values('Environment', ascending=False)
summary = bu_websites_clean.value_counts('Environment')
print(sorted_data)
print('\n' * 2, summary, '\n' * 2)

def PrefixSeries(x):
    string = "https://"
    return string + x

bu_domains = bu_websites_clean['FQDNs']
bu_websites_clean['FQDNs'] = bu_websites_clean['FQDNs'].apply(PrefixSeries)
dataframe = bu_websites_clean
dataframe_sorted = bu_websites_clean.sort_values('Environment', ascending=False)
dataframe_no_indices = dataframe_sorted.to_string(index=False)
print(dataframe_no_indices)


import_df = bu_websites_clean['FQDNs'] + ", " + bu_websites['FQDNs']
final_df = import_df.to_string(index=False)
print('\n' * 2,final_df)
