from threading import Thread

def printHello(i):
    print("Hello from Thread {}\n".format(i))

def createThread(n):
    for i in range(50,0,-1):
        thread = Thread(target=printHello, args = (i,))
        thread.start()
        thread.join()

if __name__ == "__main__":
    thread1 = Thread(target = createThread, args = (50,))
    thread1.start()
    thread1.join()