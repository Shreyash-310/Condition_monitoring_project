def gyro_peaks():
    import pandas as pd
    import csv
    t = []
    x = []
    y = []
    z = []

    with open('Gyroscope_data.csv') as csvfile:     #in above line, change data.csv to any file name stored in the same folder
        header = csv.reader(csvfile, delimiter=',')
        flag=0
            
        for row in header:
            if flag==0:   #this flag case is to ignore the first line csv file because it is a title
                flag=1
            else:
                #print(row)
                try:
                    t.append(row[0])
                    x.append(float(row[1]))
                    y.append(float(row[2]))
                    z.append(float(row[3]))
                        # there the values of acceleration are stored in various arrays of x.y and z
                except:
                        #this is to ignore a few cases where the file is reporting blank values
                    pass
    df = pd.DataFrame()
    df['Time'] = t
    df['GX'] = x
    df['GY'] = y
    df['GZ'] = z
    print(df.head())
    
    data_x = df[['Time','GX']].copy()
    data_x = data_x.sort_values('GX', ascending=False).head()
    data_y = df[['Time','GY']].copy()
    data_y = data_y.sort_values('GY', ascending=False).head()
    data_z = df[['Time','GZ']].copy()
    data_z = data_z.sort_values('GZ', ascending=False).head()
    
    data_x.reset_index(inplace=True)
    data_x.drop('index', axis=1, inplace=True)
    data_y.reset_index(inplace=True)
    data_y.drop('index', axis=1, inplace=True)
    data_z.reset_index(inplace=True)
    data_z.drop('index', axis=1, inplace=True)
    
    data_final = pd.concat([data_x, data_y, data_z], axis=1)
    print(data_final)
    data_final.to_csv('gyro_peaks.csv')

# gyro_peaks()