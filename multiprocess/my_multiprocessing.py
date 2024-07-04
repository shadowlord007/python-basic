# my_multiprocessing.py
import multiprocessing as mp
import math
import time

result_list_one = []
result_list_two = [] 
result_list_three = [] 


def calculation_one(numbers):
    for number in  numbers:
        result_list_one.append(math.sqrt(number ** 3))

def calculation_two(numbers):
    for number in  numbers:
        result_list_two.append(math.sqrt(number ** 4))

def calculation_three(numbers):
    for number in  numbers:
        result_list_three.append(math.sqrt(number ** 5))


if __name__ == '__main__':

    numbers = list(range(1000000))
    p1 = mp.Process(target=calculation_one, args=(numbers,))
    p2 = mp.Process(target=calculation_two, args=(numbers,))
    p3 = mp.Process(target=calculation_three, args=(numbers,))


    start=time.time()
    p1.start()
    p2.start()
    p3.start()
    end=time.time()

    print(end-start)