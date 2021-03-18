import multiprocessing
import time
import sys


def daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    sys.stdout.flush()
    # time.sleep(2)
    # with sleep(2), the output should be no exiting daemon process
    # why: all of the non-daemon processes (including the main program) 
    # exit before the daemon process wakes up from its two second sleep.
    # The daemon process is terminated automatically before the main program exits, 
    # which avoids leaving orphaned processes running. 
    # try to comment out the sleep(2) then you will see deamon process
    print('Exiting :', p.name, p.pid)
    sys.stdout.flush()


def non_daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)
    sys.stdout.flush()
    print('Exiting :', p.name, p.pid)
    sys.stdout.flush()


if __name__ == '__main__':
    d = multiprocessing.Process(
        name='daemon',
        target=daemon,
    )
    d.daemon = True

    n = multiprocessing.Process(
        name='non-daemon',
        target=non_daemon,
    )
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()