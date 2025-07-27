# Mogakso_LLM

파란학기 LLM 관련 실습을 통한 준비
## 주차별 실습 내용

### 1주차: Pandas & Matplotlib 데이터 분석
- **파일**: `notebooks/pandas_matplotlib_practice.py`
- **내용**: 
  - Pandas DataFrame 조작
  - 데이터 필터링 및 그룹화
  - Matplotlib 시각화 (막대그래프, 파이차트, 히스토그램, 산점도)
  - 신조어 사용 패턴 분석

### 2주차: 정규표현식과 문자열 처리
- **파일**: 
  - `regex_and_string_practice.py` (기본 실습)
  - `regex_exercises.py` (추가 연습)
- **내용**:
  - 정규표현식 패턴 찾기 (전화번호, 이메일)
  - 문자열 처리 기본기 (split, replace, strip 등)
  - CSV 데이터 파싱
  - 로그 파일 분석
  - 웹 서버 로그 처리

### 3주차: AI 모델 실습
- **파일**: 
  - `week3_ai_models_practice.py` (이론 및 예시)
  - `week3_ai_models_hands_on.py` (실제 API 사용)
- **내용**:
  - Hugging Face: 이미 만들어진 모델 써보기
  - OpenAI API: ChatGPT API로 챗봇 만들기
  - 번역 모델: 한영 번역기 체험
  - 감정 분석, 텍스트 요약, 대화형 챗봇

## 파일 구조

```
Mogakso_LLM/
├── README.md                           # 프로젝트 설명
├── regex_and_string_practice.py        # 2주차 기본 실습
├── regex_exercises.py                  # 2주차 추가 연습
├── week3_ai_models_practice.py         # 3주차 이론 및 예시
├── week3_ai_models_hands_on.py         # 3주차 실제 API 사용
└── notebooks/
    ├── README.md                       # 1주차 설명
    └── pandas_matplotlib_practice.py   # 1주차 실습
```

## 실행 방법

### 1주차 실습
```bash
cd notebooks
python pandas_matplotlib_practice.py
```

### 2주차 실습
```bash
# 기본 실습
python regex_and_string_practice.py

# 추가 연습
python regex_exercises.py
```

### 3주차 실습
```bash
# 이론 및 예시
python week3_ai_models_practice.py

# 실제 API 사용 (API 키 필요)
python week3_ai_models_hands_on.py
```

## 학습 내용

### 1주차: 데이터 분석 기초
- Pandas DataFrame 생성 및 조작
- 데이터 필터링: `df[df['컬럼'] >= 값]`
- 그룹화: `df.groupby('컬럼')['컬럼'].mean()`
- Matplotlib 시각화 기법
- 신조어 데이터 분석 실습

### 2주차: 텍스트 처리 기초

#### 정규표현식 (Regular Expression)
- 전화번호 패턴: `(?:010|02)[-.\s]?\d{3,4}[-.\s]?\d{4}`
- 이메일 패턴: `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b`
- 패턴 매칭: `re.findall()`, `re.search()`, `re.match()`

#### 문자열 처리
- `split()`: 문자열 분할
- `join()`: 리스트를 문자열로 결합
- `strip()`, `lstrip()`, `rstrip()`: 공백 제거
- `replace()`: 문자열 치환
- `upper()`, `lower()`, `title()`: 대소문자 변환

#### 실전 활용
- CSV 데이터 파싱
- 로그 파일 분석
- 웹 서버 로그 처리
- 텍스트 정보 추출

### 3주차: AI 모델 활용

#### Hugging Face 모델
- 감정 분석: 텍스트의 감정 상태 분류
- 텍스트 분류: 스팸 탐지, 주제 분류
- 텍스트 생성: GPT, BERT 모델 활용
- 번역: 다국어 번역 모델
- 이미지 분류: Vision Transformer

#### OpenAI API
- ChatGPT 챗봇: 대화형 AI 어시스턴트
- 텍스트 요약: 긴 문서를 간단히 요약
- 번역: 다국어 번역 서비스
- 코드 생성: 프로그래밍 코드 작성
- 창의적 글쓰기: 스토리, 시 등 생성

#### 실전 활용
- 고객 서비스 챗봇
- 문서 자동 요약 시스템
- 다국어 지원 서비스
- 감정 분석 기반 리뷰 시스템

## 실습 예제

### 1주차: 신조어 데이터 분석
```python
# 데이터 필터링
popular_words = df[df['사용빈도'] >= 200]

# 그룹화
category_avg = df.groupby('카테고리')['사용빈도'].mean()

# 시각화
plt.bar(df['신조어'], df['사용빈도'])
```

### 2주차: 정규표현식 활용
```python
# 전화번호 유효성 검사
korean_phone_pattern = r'^(?:010|02)[-.\s]?\d{3,4}[-.\s]?\d{4}$'
is_valid = bool(re.match(korean_phone_pattern, phone_number))

# 이메일 추출
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, text)

# CSV 데이터 처리
lines = csv_data.split('\n')
headers = lines[0].split(',')
for line in lines[1:]:
    values = line.split(',')
    data = dict(zip(headers, values))
```

### 3주차: AI 모델 활용
```python
# OpenAI 챗봇
import openai
openai.api_key = "your-api-key"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "안녕하세요!"}]
)

# Hugging Face 감정 분석
import requests
API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = {"Authorization": "Bearer YOUR_API_KEY"}

response = requests.post(API_URL, headers=headers, json={"inputs": "I love this!"})
```

## 추가 학습 자료

- [정규표현식 테스트 도구](https://regex101.com/)
- [Python re 모듈 공식 문서](https://docs.python.org/3/library/re.html)
- [Python 문자열 메서드](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Pandas 공식 문서](https://pandas.pydata.org/docs/)
- [Matplotlib 공식 문서](https://matplotlib.org/)
- [OpenAI API 문서](https://platform.openai.com/docs/)
- [Hugging Face API 문서](https://huggingface.co/docs/api-inference)
- [Transformers 라이브러리](https://huggingface.co/docs/transformers/)

