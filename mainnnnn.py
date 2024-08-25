import threading
import time
from queue import Queue


def f(n):
    time.sleep(n)


class Worker(threading.Thread):
    def __init__(self, queue):
        super(Worker, self).__init__()
        self.q = queue
        self.daemon = True
        self.start()

    def run(self):
        while 1:
            f, args, kwargs = self.q.get()
            try:
                f(*args, **kwargs)
            except Exception as e:
                print(e)
            self.q.task_done()


class ThreadPool(object):
    def __init__(self, thread_num=10):
        self.q = Queue(thread_num)
        for i in range(thread_num):
            Worker(self.q)

    def add_task(self, f, *args, **kwargs):
        self.q.put((f, args, kwargs))

    def wait_complete(self):
        self.q.join()


if __name__ == '__main__':
    start = time.time()
    pool = ThreadPool(5)
    for i in range(10):
        pool.add_task(f, 3)
    pool.wait_complete()
    end = time.time() 