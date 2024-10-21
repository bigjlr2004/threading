#!/usr/bin/python3
import queue
import threading
import time

exitFlag = 0

class EpicThread(threading.Thread):
    def __init__(self, passedThreadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = passedThreadID
        self.name = name
        self.q = q

    def run(self):
        print("Starting " + self.name)
        ProcessData(self.name, self.q) 
        print("Exiting " + self.name)  

def ProcessData(passedThread, q):
    while not exitFlag:
        queueLock.acquire()
        try:
            if not q.empty():
                data = q.get()
                print("%s processing %s" % (passedThread, data))
        finally:
            queueLock.release()
        time.sleep(0.1)  # Sleep to avoid busy waiting

threadList = ["Thread 1", "Thread 2", "Thread 3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue()
threads = []
threadID = 1

# Create and start threads
for tName in threadList:
    thread = EpicThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Fill the queue
queueLock.acquire()
try:
    for word in nameList:
        workQueue.put(word)
finally:
    queueLock.release()

# Wait for the queue to be empty and all threads to finish
while not workQueue.empty() or any(t.is_alive() for t in threads):
    time.sleep(1)

exitFlag = 1  # Set exit flag after queue is processed

# Wait for all threads to finish
for t in threads:
    t.join()

print("Exit the Main Thread")