from time import time 

# 파이썬에서 함수도 객체다.
# loggings로 이름 변경.
def log_time(func):
    # 함수 실행 시간을 로그로 남김
    def wrapper(*args, **kwargs):
        print("wrapper")
        start = time()
        val = func(*args, **kwargs)
        end = time()

        duration = end - start 
        #print(f"{func.__name__}'s parameter *args - {*args}, **kwargs - {**kwargs}")
        print(f"{func.__name__} time {duration} seconds to run")

        return val 
    return wrapper
