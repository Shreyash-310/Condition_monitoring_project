def sorting():
    import pandas as pd
    df = pd.read_csv('Analyzed_data.csv')
    
    data_x = df[['FX', 'AX']].copy()
    data_x = data_x.sort_values('AX', ascending=False).head()
    data_y = df[['FY', 'AY']].copy()
    data_y = data_y.sort_values('AY', ascending=False).head()
    data_z = df[['FZ', 'AZ']].copy()
    data_z = data_z.sort_values('AZ', ascending=False).head()
    
    data_x.reset_index(inplace=True)
    data_x.drop('index', axis=1, inplace=True)
    data_y.reset_index(inplace=True)
    data_y.drop('index', axis=1, inplace=True)
    data_z.reset_index(inplace=True)
    data_z.drop('index', axis=1, inplace=True)
    
    data_final = pd.concat([data_x, data_y, data_z], axis=1)
    print(data_final)
    data_final.to_csv('sorted.csv')

# sorting()