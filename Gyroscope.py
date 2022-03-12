def get_gyro_data():
    import time
    import time, threading
    import csv
    import sys
    
    def foo():
        print(time.ctime())
        threading.Timer(0.1,foo).start()
            
    #import the ADXL345 module.
    from mpu6050 import mpu6050
    mpu = mpu6050(0x68)
    print('Printing X,Y,Z axis values, press Ctrl-C to quit...')

    try:
        log_file = open('Gyroscope_data.csv','a')
        print("data stored in file name 'Gyroscope_data.csv'")
        log_file.write("data from new session is written from here:\n")
    except:
        print("there was an error in creating/reading from file.")
        sys.exit("Error in file handling")            
    for n in range(100):
        #read the X,Y,Z axis acceleration values and print them
        gyro_data = mpu.get_gyro_data()
        print(time.ctime())
        print("Gyro X : "+str(gyro_data['x']))
        print("Gyro Y : "+str(gyro_data['y']))
        print("Gyro Z : "+str(gyro_data['z']))
        print()
        print("-------------------------------")
        
        log_file = open('Gyroscope_data.csv','a')
        log_file.write( str(time.ctime()) + ',' + str(gyro_data['x']) + ',' + str(gyro_data['y']) + ',' + str(gyro_data['z'])+ '\n')
        log_file.close()
        time.sleep(0.1)
# get_gyro_data()