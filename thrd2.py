import threading

xd = 0
lock = threading.Lock()
def inc():
    global xd

    for i in range(200000):
        with lock:
            xd += 1

th1 = threading.Thread(target=inc)
th2 = threading.Thread(target=inc)

th1.start()
th2.start()

th1.join()
th2.join()
print(xd)
