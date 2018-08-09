import threading


class MyThread(threading.thread):

    def __init__(self, nPings):
        self.nPings = nPings

    def run(self):
        for i in range(self.nPings):
            self.ping()

    def ping(self):
        print('yeet')


def start(nThreads, nPings):
    threadList = []
    for i in range(nThreads):
        threadList.push(MyThread(nThreads, nPings))
    for i in range(threadList):
        threadList[i].run()

if __name__ == '__main__':
    nThreads = 10
    nPings = 10
    start(nThreads, nPings)