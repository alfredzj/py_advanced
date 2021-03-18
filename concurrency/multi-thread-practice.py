import threading
import time

from queue import Queue

# daemon = True, please run it using a script
def main():
    def foo():
        for i in range(3):
            print('i={},foo thread daemon is {}'.format(i, threading.current_thread().isDaemon()))
            time.sleep(1)

    t = threading.Thread(target=foo,daemon=True)
    t.start()

    print("Main thread daemon is {}".format(threading.current_thread().isDaemon()))
    print("Main Thread Exit.")

if __name__ == '__main__':
    main()