def get_acc_data():
    import time
    import time, threading
    import csv
    import sys
    
    def foo():
        print(time.ctime())
        threading.Timer(0.1,foo).start()
            
    #import the ADXL345 module.
    import Adafruit_ADXL345
    accel = Adafruit_ADXL345.ADXL345()
    print('Printing X,Y,Z axis values, press Ctrl-C to quit...')

    try:
        log_file = open('Acceleration_data.csv', 'a')
        print("data stored in file name 'Acceleration_data.csv'")
        log_file.write("data from new session is written from here:\n")
    except:
        print("there was an error in creating/reading from file.")
        sys.exit("Error in file handling")            
    for n in range(500):
        #read the X,Y,Z axis acceleration values and print them
        x, y, z = accel.read()
        print(time.ctime())
        print('X={0},Y={1},Z={2}'.format(x, y, z))
        log_file = open('Acceleration_data.csv','a')
        log_file.write(str(time.ctime()) + ',' + str(x) + ',' + str(y) + ',' + str(z) + '\n')
        log_file.close()
        #wait half a second and repeat.
        time.sleep(0.05) #change this parameter for a higher data rate
# get_acc_data()