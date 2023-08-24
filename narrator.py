import pyttsx3
import time 

engine = pyttsx3.init()

def start_countdown(seconds : int) -> None:
    for second in (seconds, 0, -1):
        engine.say(f"{second} seconds untill start.")
        engine.runAndWait()
        time.sleep(1)
    engine.say("Exam started.")
    engine.runAndWait()
    start_test(chapters=8,time_for_each_chapter=20,breaks=False, text_chapter=True)

def start_text_chapter(time : int) -> None:
    first_period = time * (5/6) * 60
    second_period = time * (1/5) * 60
    engine.say("Chapter Started.")
    engine.runAndWait()
    time.sleep(first_period)
    engine.say(f"{int(second_period)} minutes left!")
    engine.runAndWait()
    time.sleep(second_period)
    engine.say("Time ended, please move to the next chapter!")
    engine.runAndWait()

def start_test(chapters : int, time_for_each_chapter : int, breaks : bool, text_chapter : bool) -> None:
    if text_chapter:
        start_text_chapter()
    first_period = time_for_each_chapter * (3/4) * 60
    second_period = time_for_each_chapter * (1/4) * 60
    for period in range(chapters):
        engine.say(f"Chapter {period + 1} Started.")
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
    while type(countdown:=input("Enter time for countdown: ")) != int:
        try: 
            countdown = int(countdown)
            break
        except ValueError:
            print("", end="")
    print(countdown)

    start_countdown(countdown)
