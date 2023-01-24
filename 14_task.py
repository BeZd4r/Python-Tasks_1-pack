#Hey, i called you
import pyttsx3

my_dict = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', " ": " "}

num = " ".join([my_dict.get(word, "Unknown character") for word in list(input())])

engine = pyttsx3.init()
engine.setProperty("rate", 200)
engine.say(f"Hey, the caller is calling you. His number is")
engine.setProperty("rate", 110)
engine.say(num)
engine.runAndWait()
