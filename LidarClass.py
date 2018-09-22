from rplidar import RPLidar
from threading import Thread

class Lidar_Class:
    def __init__(self):
        self.lidar = RPLidar('/dev/ttyUSB0')
        self.flag=1
        while(self.flag!=0):
            try:
                self.ssc = self.lidar.iter_scans(max_buf_meas=1000, min_len=5)
                self.flag=0
                break
            except:
                print("Restarting")
                continue
        self.stopped = False
        self.state=[]

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return
            try:
                self.state = next(self.ssc)
            except:
                self.ssc = self.lidar.iter_scans(max_buf_meas=1000, min_len=5)
                print("lidar still in configuration mode...")
                continue

    def read(self):
        # return the frame most recently read
        return self.state

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True
