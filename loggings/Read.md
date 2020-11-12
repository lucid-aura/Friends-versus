# 로깅을 위한 The Decorator Pattern
데코레이터 패턴은 함수 전 후에 뭔가를 할려고 할 때 유용하다. 함수 자체를 수정하지 않아도 된다. 
[3 Great Design Patterns for DataScientists 참고 ]('https://towardsdatascience.com/3-great-design-patterns-for-data-science-workflows-d3bf162d74e6')

아래와 같이 사용하면 된다. 
~~~python 
from logging import log_time

@log_time
def logging_test():
    print("Logging Test!!!")


if __name__ == "__main__":
    logging_test()
~~~


~~~sh
python logging_test.py
~~~