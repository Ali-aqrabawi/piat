import threading


class ThreadsManager:
    """ object that manage the callback threads """

    def __init__(self):
        self.proc_pool = []

    def add(self, target, args):
        """ add callabck func to the manager """
        self.proc_pool.append(threading.Thread(target=target, args=args))

    def start(self):
        """ start all added callbacks"""
        for proc in self.proc_pool:
            proc.start()

    def join(self):
        """ join callbacks gt"""
        for proc in self.proc_pool:
            proc.join()