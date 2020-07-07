import multiprocessing

def doubler(number):
    return number * 2

def t1():
    cores_quantity = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cores_quantity)
    results = pool.apply_async(doubler, (25,))
    print(11)
