# Multimodal YouTube AI Summarizer 🎥🎙️

A productivity tool that converts long-form video content into digestible, timestamped summaries. Perfect for students and researchers looking to extract value from lectures and podcasts quickly.

## 🚀 Key Features
- **Speech-to-Text:** Leverages OpenAI's **Whisper** model for high-accuracy transcription.
- **Automated Chaptering:** Uses GPT-4 to identify logical breaks in the conversation and create timestamped chapters.
- **Key Takeaways:** Generates a "TL;DR" (Too Long; Didn't Read) summary for the entire video.

## 🛠️ Tech Stack
- **Transcription:** OpenAI Whisper
- **Summarization:** LangChain / OpenAI GPT-4
- **Audio Extraction:** Pytube / FFmpeg

## 🔧 Technical Challenge Overcome
Handling audio file sizes and long-form transcripts was a hurdle for standard LLM context windows. I implemented a **Map-Reduce summarization chain** in LangChain, allowing the system to summarize hours of footage without losing the core narrative.
