# https://pypi.org/project/pyttsx3/
# https://github.com/KBNLresearch/iromlab/issues/100


# importing the pyttsx library 
import pyttsx3 
  
# initialisation 
engine = pyttsx3.init() 
  
# testing 
engine.say("Hi i am Rahul.I love programing in Python.")
engine.runAndWait() 


"""
# import the pyttsx module inside program
import pyttsx3

# initializing the module
engine = pyttsx3.init()

# .say() function is used to speak the text you have written 
# inside the function
text=str(input("Enter TEXT to be spoken: "))
engine.say(text)

# this is used to process and run the program commands
engine.runAndWait()

"""
# Changing voices
"""
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
"""

# Changing speech rate
""""
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+50)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
"""

# Changing volume
"""
engine = pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.25)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
"""

#Saving voice to a file
"""
import pyttsx3
engine = pyttsx3.init()
engine.save_to_file('Hello World' , 'test.mp3')
engine.runAndWait()
"""