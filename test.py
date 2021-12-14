import multiprocessing as mp
import time, keyboard, sys, random, os
from pynput.keyboard import Key, Controller as KBController
from pynput.mouse import Button, Controller as MController

key = Key.f17


def kill(run, processes):
    print('kill')
    run.value = False
    for p in processes:
        p.terminate()
    os._exit(1)

def pauseOrResume(run, processes):
    print('pause')
    if (run.value):
        # Currently running, kill it
        for p in processes:
            p.terminate()
        del processes[:]
    run.value = not run.value


# def worker(run):
#     kb = KBController()
#     m = MController()
#     while True:
#         if run.value:
#             process = mp.Process(target=do_work, args=(kb, m,))
#             process.start()
#             process.join()

def do_work():
    kb = KBController()
    m = MController()
    while True:
        longDelay = random.uniform(30, 60)
        numMouseActivities = random.randrange(10, 20)
        numKeyboardActivities = random.randrange(10, 30)
        print(f'doing {numMouseActivities} mouse actions')
        for i in range(numMouseActivities):
            delayBetweenActivity = random.uniform(1, 2)
            scrollDirection = random.randint(0, 1)
            time.sleep(delayBetweenActivity)
            print('mouse activity')
            m.scroll(0, -1 if scrollDirection else 1)
        print(f'doing {numKeyboardActivities} keyboard actions')
        for i in range(numKeyboardActivities):
            delayBetweenPress = random.uniform(0.1, 0.5)
            time.sleep(delayBetweenPress)
            print('keyboard activity')
            kb.press(key)
            kb.release(key)
        print(f'sleeping for {longDelay} seconds')
        time.sleep(longDelay)
        
        
    
def listener(args):
    print('listener')

if __name__ == '__main__':
    mp.set_start_method('spawn')

    run = mp.Value('i', 1)
    processes = []

    keyboard.add_hotkey('ctrl+shift+f4', lambda: kill(run, processes))
    keyboard.add_hotkey('ctrl+shift+f5', lambda: pauseOrResume(run, processes))

    while True:
        print('while loop')
        if run.value:
            worker = mp.Process(target=do_work)
            processes.append(worker)
            for p in processes:
                p.start()
            for p in processes:
                p.join()
        time.sleep(1)
    