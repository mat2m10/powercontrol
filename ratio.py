import pandas as pd
import numpy as np
def find_power_vals(pwr):
    df_ratios_power = pd.read_pickle("./data/df_ratio_vs_power.pkl")
    concated = pd.DataFrame()
    for col in list(df_ratios_power.columns)[0:1]:
        concated['power'] = df_ratios_power[col]
        concated['maf'] = np.ones(len(df_ratios_power[col])) * float(col)
        concated['ratio'] = df_ratios_power.index
    for col in list(df_ratios_power.columns)[1:]:
        temp = pd.DataFrame()
        temp['power'] = df_ratios_power[col]
        temp['maf'] = np.ones(len(df_ratios_power[col])) * float(col)
        temp['ratio'] = df_ratios_power.index
        concated = pd.concat([concated, temp])
        rslt_df = concated[pwr-2 < concated['power']]
        rslt_df = rslt_df[rslt_df['power'] < pwr+2]
        
    mafs = np.array(rslt_df['maf'])
    ratios = np.array(rslt_df['ratio'])
    a = (ratios.min()-ratios.max())/(mafs.max())**2
    b = -2*a*mafs.max()
    c = ratios.min()
    return [a, b, c]