import pyttsx3 

# personal function
import variable_storage as var_s 

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    var_s.context.append(text)
    var_s.context_utt_label.append('sys')