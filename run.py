import subprocess
from concurrent.futures import ThreadPoolExecutor

def startJarvis():
    print("Process 1 is running.")
    from main import start
    start()

def listenHotword():
    print("Process 2 is running.")
    from engine.features import hotword
    hotword()

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        future1 = executor.submit(startJarvis)
        subprocess.call([r'device.bat'])
        future2 = executor.submit(listenHotword)
        
        # Wait for the tasks to complete
        future1.result()
        future2.result()

    print("system stop")
