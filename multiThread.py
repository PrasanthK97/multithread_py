import threading
import time 

start = time.perf_counter()

def do_something():
    print("sleeping 1 second...")
    time.sleep(1)
    print('Done Sleeping...')



t1 = threading.Thread(target= do_something)
t2 = threading.Thread(target= do_something)

t1.start()
t2.start()
t1.join()
t2.join()

finish = time.perf_counter()

print(finish, start)
# n = 0
# while(True):
#     n += 1
#     time.sleep(1)
#     print(1)

