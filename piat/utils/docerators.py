import time


def restart_on_failure(func):
    def wrapped(*args, **kwargs):
        while True:
            try:
                func(*args, **kwargs)

            except Exception as e:
                print(e)
            time.sleep(0.2)

    return wrapped
