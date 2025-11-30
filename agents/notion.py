import requests
import dotenv
import os
from agents.state import State

dotenv.load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("DATABASE_ID")
PAGE_ENDPOINT = os.getenv("PAGE_ENDPOINT")
POST_ENDPOINT = os.getenv("POST_ENDPOINT")

headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def post_page_and_get_id(title_text, date_str):
    """데이터베이스에 새로운 페이지를 추가하는 함수"""
    page_endpoint = PAGE_ENDPOINT
    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "제목": {"title": [{"text": {"content": title_text}}]},
            "날짜": {"date": {"start": date_str}}
        }
    }
    res = requests.post(url=page_endpoint, headers=headers, json=payload)
    data = res.json()
    return data.get('id')

def transcript_chunk(origin:str, translated: str):
    """노션 API를 위한 텍스트 chunk 함수"""
    chunks = []
    tmp_len_cnt = 0
    tmp_text = ""
    for o, t in zip(origin.split("\n"), translated.split("\n")):
        if tmp_len_cnt + len(o) + len(t) >= 2000:
            chunks.append(tmp_text)
            tmp_len_cnt = 0
            tmp_text = ""
        tmp_len_cnt += len(o) + len(t)
        tmp_text += o + "\n" + t + "\n\n"
    if tmp_text != "": chunks.append(tmp_text)
    return chunks

def make_block(content: str):
    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": content,
                        "link": None                        
                    }
                }
            ]
        }
    }

def make_page_contents(state: State)->State:
    """만들어진 컨텐츠를 페이지에 삽입하는 함수"""
    page_id = post_page_and_get_id(state["title_text"], state["date_str"])
    chunks = transcript_chunk(state["origin_text"], state["translated_text"])
    post_endpoint = POST_ENDPOINT.format(page_id=page_id)
    payload = {
        "children": [
            {
                "object": "block",
                "type": "embed",
                "embed": {
                    "url": state["url"]
                }
            },
            ] + [make_block(chunk) for chunk in chunks]
        }

    requests.patch(url=post_endpoint, headers=headers, json=payload)
    print("notion에 페이지를 생성했습니다.")
    return {"result": "notion에 새로운 페이지를 생성했습니다."}