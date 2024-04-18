import speech_recognition as sr #import module

"""
print(sr.Microphone.list_microphone_names())
for name in sr.Microphone.list_microphone_names():
    print(index, ":", name)
    #print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    index = index + 1
"""    
#for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone#(device_index={0})`".format(index, name))

recognizer = sr.Recognizer() #create object (sr is module) (Recognizer is class) () is object (recognizer) [pass by object?]

def mic1():
    with sr.Microphone(device_index=1) as source :
        print ("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        
        audio = recognizer.listen(source)
        print("Recognizing.....")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text

if __name__ == "__main__":
    mic1()
