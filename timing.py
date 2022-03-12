import time
import schedule
from acceleration import get_acc_data
from Acc_peaks import acc_peaks
from Gyroscope import get_gyro_data
from Gyro_peaks import gyro_peaks
from all_fft_master import all_in_one
from sorting import sorting
from Upload import uploadFile
from Delete import delete

def time():
    schedule.every(1).minutes.do(job)
def job():
    delete()
    get_acc_data()
    acc_peaks()
    get_gyro_data()
    gyro_peaks()
    all_in_one()
    sorting()
    uploadFile('fft_figure.png', 'fft_figure.png', 'image/png')
    uploadFile('Acceleration_data.csv', 'Acceleration_data.csv', 'text/csv')
    uploadFile('Analyzed_data.csv', 'Analyzed_data.csv', 'text/csv')
    uploadFile('sorted.csv', 'sorted.csv', 'text/csv')
    uploadFile('peaks.csv', 'peaks.csv', 'text/csv')
    uploadFile('Gyroscope_data.csv', 'Gyroscope_data.csv', 'text/csv')
    uploadFile('gyro_peaks.csv', 'gyro_peaks.csv', 'text/csv')

schedule.every().day.at("12:37:30").do(time)
while True: 
    schedule.run_pending()