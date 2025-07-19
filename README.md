# Mogakso_LLM

정규표현식과 문자열 처리 실습 프로젝트

## 학습 목표

학부생 3,4학년 수준의 파이썬 프로그래밍 실습을 통해 다음을 학습합니다:

- [x] 정규표현식: 패턴 찾기 (전화번호, 이메일)
- [x] 문자열 처리: split, replace 등 기본기

## 파일 구조

```
Mogakso_LLM/
├── README.md                           # 프로젝트 설명
├── regex_and_string_practice.py        # 기본 실습 (정규표현식 + 문자열 처리)
├── regex_exercises.py                  # 추가 연습 문제
└── notebooks/
    ├── README.md                       # 노트북 설명
    └── pandas_matplotlib_practice.py   # pandas/matplotlib 실습
```

## 실행 방법

### 1. 기본 실습 실행
```bash
python regex_and_string_practice.py
```

### 2. 추가 연습 문제 실행
```bash
python regex_exercises.py
```

## 학습 내용

### 1. 정규표현식 (Regular Expression)

#### 전화번호 패턴
- 한국 휴대폰: `010-XXXX-XXXX`, `010.XXXX.XXXX`, `010 XXXX XXXX`
- 한국 지역번호: `02-XXX-XXXX`, `02.XXX.XXXX`, `02 XXX XXXX`
- 통합 패턴: `(?:010|02)[-.\s]?\d{3,4}[-.\s]?\d{4}`

#### 이메일 패턴
- 기본 형식: `username@domain.com`
- 패턴: `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b`

### 2. 문자열 처리

#### 기본 메서드
- `split()`: 문자열 분할
- `join()`: 리스트를 문자열로 결합
- `strip()`, `lstrip()`, `rstrip()`: 공백 제거
- `replace()`: 문자열 치환
- `upper()`, `lower()`, `title()`: 대소문자 변환

#### 실전 활용
- CSV 데이터 파싱
- 로그 파일 분석
- 텍스트 정제 및 변환

## 실습 예제

### 1. 전화번호 유효성 검사
```python
korean_phone_pattern = r'^(?:010|02)[-.\s]?\d{3,4}[-.\s]?\d{4}$'
is_valid = bool(re.match(korean_phone_pattern, phone_number))
```

### 2. 이메일 추출
```python
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, text)
```

### 3. CSV 데이터 처리
```python
lines = csv_data.split('\n')
headers = lines[0].split(',')
for line in lines[1:]:
    values = line.split(',')
    data = dict(zip(headers, values))
```

## 추가 학습 자료

- [정규표현식 테스트 도구](https://regex101.com/)
- [Python re 모듈 공식 문서](https://docs.python.org/3/library/re.html)
- [Python 문자열 메서드](https://docs.python.org/3/library/stdtypes.html#string-methods)

## 연습 문제

1. **전화번호 유효성 검사**: 다양한 형식의 전화번호 검증
2. **이메일 유효성 검사**: 이메일 주소 형식 검증
3. **텍스트 파싱**: 구조화된 텍스트에서 정보 추출
4. **CSV 처리**: CSV 데이터를 딕셔너리로 변환
5. **로그 분석**: 웹 서버 로그에서 정보 추출
6. **실전 예제**: 실제 프로젝트에서 활용할 수 있는 패턴들

## 학습 효과

이 실습을 통해 다음과 같은 능력을 기를 수 있습니다:

- 텍스트 데이터 처리 능력 향상
- 정규표현식을 활용한 패턴 매칭
- 실제 프로젝트에서 활용 가능한 문자열 처리 기법
- 데이터 정제 및 변환 기술 습득

## 문의

프로젝트에 대한 질문이나 개선 사항이 있으시면 언제든 연락주세요! 