from time import sleep


def run(callbacks, port):
    while True:
        sleep(20)
        callbacks[0]('trap recived')
    pass
