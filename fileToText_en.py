# coding: utf-8

import speech_recognition as sr

def wav2txt_en(wavfilepath):
    r = sr.Recognizer()
    sudio = ""
    with sr.AudioFile(wavfilepath) as src:
        sudio = r.record(src)
        return(r.recognize_sphinx(sudio))

def wav2txt_zh(wavfilepath):
    r = sr.Recognizer()
    sudio = ""
    with sr.AudioFile(wavfilepath) as src:
        sudio = r.record(src)
        return(r.recognize_sphinx(sudio, language = "zh-CN"))


