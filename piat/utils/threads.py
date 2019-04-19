import threading


class ThreadsManager:

    def __init__(self):
        self.proc_pool = []

    def add(self, target, args):
        self.proc_pool.append(threading.Thread(target=target, args=args))

    def start(self):
        for proc in self.proc_pool:
            proc.start()

    def join(self):
        for proc in self.proc_pool:
            proc.join()