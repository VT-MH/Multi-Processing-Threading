import multiprocessing
import threading
import time


def worker(num):
    """thread worker function"""
    print('Worker:', num)
    return

#
# if __name__ == '__main__':
#     # jobs = []
#     #
#     # start_time = time.time()
#     # for i in range(0, 100):
#     #     p = multiprocessing.Process(target=worker, args=(i,))
#     #     jobs.append(p)
#     #     p.start()
#     #
#     # print(time.time() - start_time)
#     #
#     # print('-' * 50)

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def multithreading(func, args, workers):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)


def multiprocessing(func, args, workers):
    with ProcessPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)


if __name__ == '__main__':
	# multithreading(worker, range(1000), 6)
	multiprocessing(worker, range(1000), 6)