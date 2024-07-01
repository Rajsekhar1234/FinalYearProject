import threading
import subprocess

def startJarvis():
    # Code for process 1
    print("Process 1 is running.")
    from main import start
    start()

def listenHotword():
    # Code for process 2
    print("Process 2 is running.")
    from engine.features import hotword
    hotword()

if __name__ == '__main__':
    thread1 = threading.Thread(target=startJarvis)
    thread2 = threading.Thread(target=listenHotword)
    
    thread1.start()
    subprocess.call([r'device.bat'])
    thread2.start()
    
    thread1.join()
    
    if thread2.is_alive():
        # There's no direct way to terminate a thread in Python,
        # you would need to use a flag or some other method to signal the thread to stop.
        print("Thread 2 is still running. Implement a stop mechanism if needed.")
        thread2.join()

    print("system stop")
