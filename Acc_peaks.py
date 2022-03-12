def acc_peaks():
    import pandas as pd
    import csv
    t = []
    x = []
    y = []
    z = []

    with open('Acceleration_data.csv') as csvfile:     #in above line, change data.csv to any file name stored in the same folder
        header = csv.reader(csvfile, delimiter=',')
        flag = 0
            
        for row in header:
            if flag == 0:   #this flag case is to ignore the first line csv file because it is a title
                flag = 1
            else:
                #print(row)
                try:
                    t.append(row[0])
                    x.append(int(row[1]))
                    y.append(int(row[2]))
                    z.append(int(row[3]))
                        # there the values of acceleration are stored in various arrays of x.y and z
                except:
                        #this is to ignore a few cases where the file is reporting blank values
                    pass
    df = pd.DataFrame()
    df['Time'] = t
    df['X'] = x
    df['Y'] = y
    df['Z'] = z
    print(df.head())
    
    data_x = df[['Time', 'X']].copy()
    data_x = data_x.sort_values('X', ascending=False).head()
    data_y = df[['Time', 'Y']].copy()
    data_y = data_y.sort_values('Y', ascending=False).head()
    data_z = df[['Time', 'Z']].copy()
    data_z = data_z.sort_values('Z', ascending=False).head()
    
    data_x.reset_index(inplace=True)
    data_x.drop('index', axis=1, inplace=True)
    data_y.reset_index(inplace=True)
    data_y.drop('index', axis=1, inplace=True)
    data_z.reset_index(inplace=True)
    data_z.drop('index', axis=1, inplace=True)
    
    data_final = pd.concat([data_x, data_y, data_z], axis=1)
    print(data_final)
    data_final.to_csv('acc_peaks.csv')

acc_peaks()
