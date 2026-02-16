import multiprocessing
import time

def taskx():
    time.sleep(2)
    print("Done")

if __name__ == '__main__':

    mpx = multiprocessing.Process(target=taskx)
    mp2 = multiprocessing.Process(target=taskx)

    mpx.start()
    mp2.start()
    mp2.join()
    mp2.join()
