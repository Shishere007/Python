from threading import Thread
from time import sleep


def print_num(number):
    for item in range(1,5) :
        print(f"{number} >>> {item}")
        sleep(1)





Thread(print_num(3)).start()
print ("step 1")
Thread(print_num(4)).start()
Thread(print_num(5)).start()