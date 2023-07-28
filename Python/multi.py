import threading
import time

def print_hello():
    for i in range(10):
        if i==5:
            time.sleep(2)
        print("Hello")

def print_num(num):
    for i in range(num+1):
        print(i)

print("In main thread")
th1=threading.Thread(target=print_hello,args=())
th2=threading.Thread(target=print_num,args=(5,))
th1.start()
th2.start()
print("Again in main thread")
