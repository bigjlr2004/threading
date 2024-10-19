#!/usr/bin/python3

import threading
import time
exitFlag = 0

class EpicThread(threading.Thread):
    def __init__(self, threadID, name, counter):
         threading.Thread.__init__(self)
         self.threadID = threadID
         self.name = name
         self.counter = counter
    def run(self):
         print("Starting " + self.name) 
         TimeFunc(self.name, self.counter, 3)    
         print("Exiting " + self.name)

def TimeFunc(thread, delay, counter):
   
   while counter:
      if exitFlag:
            thread.exit()
      time.sleep(delay)
      print("%s: %s" %(thread, time.ctime(time.time())))
      counter -=1

thread1 = EpicThread(1, "Thread Number 1A", 1)
thread2 = EpicThread(1, "Thread Number 2B", 2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print("Exit the Main Thread")