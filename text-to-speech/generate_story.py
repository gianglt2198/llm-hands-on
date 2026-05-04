
from models import llm

from gtts import gTTS
import io
from pydub import AudioSegment
from pydub.playback import play


def generate_story(topic):
    prompt = f"""Write an engaging and educational story about {topic} for beginners.
            Use simple and clear language to explain basic concepts. 
            Include interesting facts and keep it friendly and encouraging. 
            The story should be around 200-300 words and end with a brief summary of what we learned. 
            Make it perfect for someone just starting to learn about this topic.
            Especially, using vietnamese"""

    res = llm.invoke(prompt)
    return res.content

topic = "the life cycle of a human"
story = generate_story(topic)

tts = gTTS(story, lang='vi')

audio_bytes = io.BytesIO()
tts.write_to_fp(audio_bytes)
audio_bytes.seek(0)

audio = AudioSegment.from_file(audio_bytes, format="mp3") # specify format if needed
play(audio)

tts.save("generated_story.mp3")
