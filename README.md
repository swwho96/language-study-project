# 외국어 공부 Agent

언어 공부를 위해 시청한 유튜브 영상의 링크를 입력하면  
번역본이 포함된 새로운 노션 페이지를 생성해주는 agent 입니다.  
듣고, 원문을 보고, 해석본을 보면서 자연스럽게 언어를 익혀보세요.

## 설치

```bash
pip install -r requirements.txt
```

## 환경설정

```ini
# LLM API 키
OPENAI_API_KEY = "OpenAI API 키"
OPENAI_MODEL_NAME = "사용할 모델 이름 (예: gpt-5-mini)"

# Notion 키
NOTION_API_KEY = "Notion API 키"

# Notion 데이터베이스 설정
DATABASE_ID = "Notion 데이터베이스 링크 (공유링크 확인)"
PAGE_ENDPOINT = "https://api.notion.com/v1/pages"
POST_ENDPOINT = "https://api.notion.com/v1/blocks/{page_id}/children"
```

### Notion 데이터베이스 ID  
```https://www.notion.com/abcd123efgh4567890?v=xxxx``` 에서  
-> ```abcd123efgh4567890``` 이 부분이 데이터베이스 ID 입니다. 

## 사용하기
1. OpenAI API Key 생성
2. 노션 API KEY 생성
3. 노션 데이터베이스 생성 -> 공유 링크 복사
4. ```.env``` 파일 생성 및 입력
5. 명령어 실행  
    ```bash
    python main --url "https://www.youtube.com/watch?v=영상ID" --title "페이지 제목"
    ```

## 실행결과
- 제목: 입력한 제목  
- 본문: 영상 임베딩 / 원문 텍스트와 번역 텍스트