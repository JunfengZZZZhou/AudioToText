# coding: utf-8

import speech_recognition as sr

def wav2txt(wavfilepath):
    r = sr.Recognizer()
    sudio = ""
    with sr.AudioFile(wavfilepath) as src:
        sudio = r.record(src)
        return(r.recognize_sphinx(sudio))

if __name__ == "__main__":
    wav2txt("of1_01 00_00_00-00_00_08.wav")

