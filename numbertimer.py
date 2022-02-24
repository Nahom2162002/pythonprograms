import time

def num_timer():
    for index in range(10):
        calc_time = time.perf_counter()
        print("It took ", calc_time, " seconds to find ", index)

def main():
    num_timer()

if __name__ == '__main__':
    main()