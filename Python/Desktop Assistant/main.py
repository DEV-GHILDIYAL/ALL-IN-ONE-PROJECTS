import win32com.client

speaker = win32com.client.Dispatch("SAPI.SPVoice")

while 1:
    print("Hey")
    s = input()
    speaker.Speak(s)