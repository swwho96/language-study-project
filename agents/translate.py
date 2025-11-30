from openai import OpenAI
import dotenv
import os
from agents.state import State

dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")

client = OpenAI(api_key=OPENAI_API_KEY)

def translate_transcript(state: State)->State:
    prompts = """
당신은 언어 전문가입니다. 주어진 문장들을 문장별로 자연스러운 한국어로 번역하세요. 
아래 [예시]의 답변과 같이, 번역한 문장만을 반환하고 원문은 반환하지 않습니다.

[예시]
입력 : I love you.
답변 : 나는 당신을 사랑해

입력 : I am a boy. \nI want to go to school.
답변 : 나는 소년이다. \n나는 학교에 가고 싶다.
    """
    if state["origin_text"] != "":
        res = client.responses.create(
            model=MODEL_NAME,
            input = [
                {
                    "role":"assistant",
                    "content":prompts
                },
                {
                    "role":"user",
                    "content":state["origin_text"]
                }
            ]
        )
        print("script 번역을 생성했습니다.")

        return {"result": "script의 번역을 생성했습니다.", "translated_text": res.output_text}
    else:
        print("번역에 실패했습니다.")
        return {"result": "script의 번역을 생성했습니다.", "translated_text": ""}