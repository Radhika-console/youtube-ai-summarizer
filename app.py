import whisper
from langchain.llms import OpenAI

def transcribe_and_summarize(audio_file):
    # 1. Transcribe Audio using Whisper
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    full_text = result['text']
    
    # 2. Summarize the transcript
    # In a real app, you would pass 'full_text' to an LLM here
    print("Transcription Complete. Generating Summary...")
    return full_text[:500] + "..."

if __name__ == "__main__":
    print("YouTube AI Summarizer Ready.")
