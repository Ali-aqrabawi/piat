import time


def restart_on_failure(func):
    """ Decorator to restart function if it failed or an exc raised"""
    def wrapped(*args, **kwargs):
        while True:
            try:
                func(*args, **kwargs)

            except Exception as e:
                print(e)
            time.sleep(1)

    return wrapped
