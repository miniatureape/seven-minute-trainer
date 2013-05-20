from time import time
import subprocess

modes = {
    'start': 3,
    'rest': 10,
    'work': 30,
}

excercises = ['jumping jacks', 'wall sit', 'push ups', 'abdominal crunch', 'step up onto chair', 'squat', 'tricep dips', 'plank', 'running in place', 'lunge', 'push ups with rotation', 'side plank']

mode = 'start'

def next_mode(mode):
    if mode is 'start':
        mode = 'work'
    elif mode is 'work':
        mode = 'rest';
    elif mode is 'rest':
        mode = 'work';
    return mode

def say(msg):
    cmd = "espeak -s 140 -v en '%s' --stdout|paplay" % msg
    talk = subprocess.Popen(cmd, stdin=subprocess.PIPE, shell=True)
    talk.wait()
    print msg

def start():
    global mode
    index = 0
    say("First excercise will be %s. Start when I say so" % excercises[index])
    running = True
    t = time()
    while running: 
        if time() - t > modes[mode]:
            t = time()
            mode = next_mode(mode)
            if mode is 'work':
                say("ok, start %s" % excercises[index])
                index += 1
            elif mode is 'rest':
                say("now rest. Next excercise will be %s" % excercises[index])
        if index > len(excercises) - 1:
            say("Good job. You are all done. See you tomorrow.")
            running = False

if __name__ == '__main__':
    start()
