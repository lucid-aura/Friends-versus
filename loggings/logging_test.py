from logging import log_time

@log_time
def logging_test():
    print("Logging Test!!!")


if __name__ == "__main__":
    logging_test()