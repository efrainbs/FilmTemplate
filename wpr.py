import whisper

def tran(audio_file, nivel):
    model = whisper.load_model(nivel)
    result = model.transcribe(audio_file)

    name_text = audio_file.replace(".mp3", "")
    
    with open(f"{name_text}.txt", "w") as f:
        f.write(result["text"])

def(new)