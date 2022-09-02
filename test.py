from gtts import gTTS

f = gTTS(text="안녕하세요", lang='ko', slow=True)
f.save('파일이름.mp3')