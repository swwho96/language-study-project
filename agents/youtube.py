from youtube_transcript_api import YouTubeTranscriptApi
import re
from agents.state import State
import spacy

nlp = spacy.load("en_core_web_sm")

yta = YouTubeTranscriptApi()

def extract_youtube_id(url:str) -> str | None:
    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else None


def text_to_sentence(text: str):
    normalized = re.sub(r'\s+', ' ', text.strip())
    
    doc = nlp(normalized)
    sentences = [sent.text.strip() for sent in doc.sents]
    return '\n'.join(sentences)


def get_transcript(state: State)->State:
    video_id = extract_youtube_id(state["url"])
    if video_id is not None:
        transcript = yta.fetch(video_id)
        result_text = ""
        for line in transcript:
            result_text += " "+line.text
        
        result_text = text_to_sentence(result_text)
        print("transcript를 가져왔습니다.")    

        return {"result": "콘텐츠의 script를 가져왔습니다.", "origin_text": result_text}
    return {"origin_text": ""}