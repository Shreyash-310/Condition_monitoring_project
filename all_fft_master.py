def all_in_one():
    import numpy as np
    import pandas as pd
    from scipy.fftpack import fft
    import matplotlib.pyplot as plt
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
        #here the computation of fft begins:
        #set this to your desired value
    sampling_frequency = 700 #in hertz
    sampling_time = 1.0/sampling_frequency

        #following is to calculate the fft and then to scale it acrossthe calculated frequency domain
    fft_array_x = fft(x)
    n = len(x)
    axis_for_fft_x = np.linspace(0.0, 1.0/sampling_time, n//2)[1:]
    amplitude_x = (2.0/n*np.abs(fft_array_x[0:n//2]))[1:]

    fft_array_y = fft(y)
    n = len(y)
    axis_for_fft_y = np.linspace(0.0, 1.0/sampling_time, n//2)[1:]
    amplitude_y = (2.0/n*np.abs(fft_array_y[0:n//2]))[1:]

    fft_array_z = fft(z)
    n = len(z)
    axis_for_fft_z = np.linspace(0.0, 1.0/sampling_time, n//2)[1:]
    amplitude_z = (2.0/n*np.abs(fft_array_z[0:n//2]))[1:]

    #from here onwards, all the statements are for plotting the generated data
    plt.subplot(2, 2, 1)
    plt.plot(axis_for_fft_x, amplitude_x, 'r', label="x fft")
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude - X Direction')
    plt.legend()
    plt.grid()
    
    plt.subplot(2, 2, 2)
    plt.plot(axis_for_fft_y, amplitude_y, 'g', label="y fft")
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude - Y Direction')
    plt.legend()
    plt.grid()
    
    plt.subplot(2, 2, 3)
    plt.plot(axis_for_fft_z, amplitude_z, 'b', label="z fft")
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude - Z Direction')
    plt.legend()
    plt.grid()
    
    plt.savefig('fft_figure.png')
    plt.show()
    
    n = len(amplitude_x)
    FX, AX, FY, AY, FZ, AZ = [], [], [], [], [], []
    
    for i in range(n):
        fx = axis_for_fft_x[i]
        FX.append(fx)
        ax = amplitude_x[i]
        AX.append(ax)
        fy = axis_for_fft_y[i]
        FY.append(fy)
        ay = amplitude_y[i]
        AY.append(ay)
        fz = axis_for_fft_z[i]
        FZ.append(fz)
        az = amplitude_z[i]
        AZ.append(az)
        
    df = pd.DataFrame()
    df['FX'] = FX
    df['AX'] = AX
    df['FY'] = FY
    df['AY'] = AY
    df['FZ'] = FZ
    df['AZ'] = AZ
    
    df.to_csv('Analyzed_data.csv')
# all_in_one()
