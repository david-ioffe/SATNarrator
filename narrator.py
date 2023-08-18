import pyttsx3
import time 

engine = pyttsx3.init()

def start_test(chapters=8, time_for_each_chapter=20, breaks=False):
    first_period = time_for_each_chapter * (3/4) * 60
    second_period = time_for_each_chapter * (1/4) * 60
    for period in range(chapters):
        engine.say(f"Chapter {period + 1} Started")
        engine.runAndWait()
        time.sleep(first_period)
        engine.say(f"{int(second_period)} minutes left!")
        engine.runAndWait()
        time.sleep(second_period)
        if period == chapters - 1:
            engine.say("Test ended, please put down your pencils!")
            engine.runAndWait()
            break
        engine.say("Time ended, please move to the next chapter!")
        engine.runAndWait()

if __name__ == "__main__":
    start_test(chapters=8,time_for_each_chapter=20,breaks=False)
