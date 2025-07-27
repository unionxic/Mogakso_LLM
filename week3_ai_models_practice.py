#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3주차: AI 모델 실습
- Hugging Face: 이미 만들어진 모델 써보기
- OpenAI API: ChatGPT API로 챗봇 만들기
- 번역 모델: 한영 번역기 체험
"""

import requests
import json
import os
from typing import Dict, List, Optional

def section_1_huggingface_models():
    """1. Hugging Face 모델 사용하기"""
    print("=" * 50)
    print("1. Hugging Face 모델 사용하기")
    print("=" * 50)
    
    print("Hugging Face는 다양한 사전 훈련된 모델을 제공합니다.")
    print("주요 모델 타입:")
    print("- 텍스트 분류 (감정 분석, 스팸 탐지)")
    print("- 텍스트 생성 (GPT, BERT)")
    print("- 번역 (다국어 번역)")
    print("- 이미지 분류 (Vision Transformer)")
    print("- 음성 인식 (Whisper)")
    
    print("\n사용 예시:")
    print("1. 감정 분석 모델")
    print("2. 텍스트 요약 모델")
    print("3. 이미지 분류 모델")
    
    # 실제 API 호출 예시 (API 키가 필요한 경우)
    print("\nHugging Face API 사용 예시:")
    print("""
    import requests
    
    API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    
    output = query({
        "inputs": "I love this movie!",
    })
    print(output)
    """)

def section_2_openai_chatbot():
    """2. OpenAI API로 챗봇 만들기"""
    print("\n" + "=" * 50)
    print("2. OpenAI API로 챗봇 만들기")
    print("=" * 50)
    
    print("OpenAI API를 사용하여 ChatGPT 기반 챗봇을 만들 수 있습니다.")
    
    # 간단한 챗봇 클래스
    class SimpleChatbot:
        def __init__(self, api_key: str):
            self.api_key = api_key
            self.api_url = "https://api.openai.com/v1/chat/completions"
            self.headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            self.conversation_history = []
        
        def add_message(self, role: str, content: str):
            """대화 기록에 메시지 추가"""
            self.conversation_history.append({
                "role": role,
                "content": content
            })
        
        def get_response(self, user_message: str) -> str:
            """사용자 메시지에 대한 응답 생성"""
            self.add_message("user", user_message)
            
            payload = {
                "model": "gpt-3.5-turbo",
                "messages": self.conversation_history,
                "max_tokens": 150,
                "temperature": 0.7
            }
            
            try:
                response = requests.post(self.api_url, headers=self.headers, json=payload)
                response.raise_for_status()
                
                result = response.json()
                assistant_message = result["choices"][0]["message"]["content"]
                self.add_message("assistant", assistant_message)
                
                return assistant_message
            except requests.exceptions.RequestException as e:
                return f"API 호출 오류: {e}"
            except KeyError as e:
                return f"응답 파싱 오류: {e}"
        
        def reset_conversation(self):
            """대화 기록 초기화"""
            self.conversation_history = []
    
    print("\n챗봇 클래스 예시:")
    print("""
    # API 키 설정 (실제 사용시 환경변수에서 가져오기)
    api_key = "your-openai-api-key"
    chatbot = SimpleChatbot(api_key)
    
    # 대화 예시
    response = chatbot.get_response("안녕하세요!")
    print(f"챗봇: {response}")
    
    response = chatbot.get_response("파이썬에 대해 설명해주세요.")
    print(f"챗봇: {response}")
    """)
    
    # 대화 시뮬레이션
    print("\n대화 시뮬레이션:")
    print("사용자: 안녕하세요!")
    print("챗봇: 안녕하세요! 무엇을 도와드릴까요?")
    print("사용자: 파이썬에 대해 설명해주세요.")
    print("챗봇: 파이썬은 배우기 쉽고 강력한 프로그래밍 언어입니다. 데이터 분석, 웹 개발, AI 등 다양한 분야에서 사용됩니다.")
    print("사용자: 감사합니다!")
    print("챗봇: 천만에요! 다른 질문이 있으시면 언제든 물어보세요.")

def section_3_translation_model():
    """3. 번역 모델 체험"""
    print("\n" + "=" * 50)
    print("3. 번역 모델 체험")
    print("=" * 50)
    
    print("다양한 번역 모델을 사용하여 한영 번역을 체험해보겠습니다.")
    
    # 번역 클래스
    class TranslationModel:
        def __init__(self, model_type: str = "huggingface"):
            self.model_type = model_type
            
        def translate_ko_to_en(self, text: str) -> str:
            """한국어를 영어로 번역"""
            if self.model_type == "huggingface":
                return self._translate_with_huggingface(text)
            elif self.model_type == "openai":
                return self._translate_with_openai(text)
            else:
                return self._translate_simple(text)
        
        def translate_en_to_ko(self, text: str) -> str:
            """영어를 한국어로 번역"""
            if self.model_type == "huggingface":
                return self._translate_with_huggingface(text, target_lang="ko")
            elif self.model_type == "openai":
                return self._translate_with_openai(text, target_lang="Korean")
            else:
                return self._translate_simple(text, reverse=True)
        
        def _translate_with_huggingface(self, text: str, target_lang: str = "en") -> str:
            """Hugging Face 번역 API 사용"""
            # 실제 구현시에는 Hugging Face API 호출
            return f"[Hugging Face 번역] {text} -> {target_lang}"
        
        def _translate_with_openai(self, text: str, target_lang: str = "English") -> str:
            """OpenAI 번역 API 사용"""
            # 실제 구현시에는 OpenAI API 호출
            return f"[OpenAI 번역] {text} -> {target_lang}"
        
        def _translate_simple(self, text: str, reverse: bool = False) -> str:
            """간단한 번역 시뮬레이션"""
            translations = {
                "안녕하세요": "Hello",
                "감사합니다": "Thank you",
                "파이썬": "Python",
                "인공지능": "Artificial Intelligence",
                "머신러닝": "Machine Learning",
                "딥러닝": "Deep Learning",
                "Hello": "안녕하세요",
                "Thank you": "감사합니다",
                "Python": "파이썬",
                "Artificial Intelligence": "인공지능",
                "Machine Learning": "머신러닝",
                "Deep Learning": "딥러닝"
            }
            
            return translations.get(text, f"[번역 불가] {text}")
    
    print("\n번역 모델 사용 예시:")
    translator = TranslationModel()
    
    # 한영 번역 예시
    korean_texts = [
        "안녕하세요",
        "파이썬 프로그래밍을 배우고 있습니다",
        "인공지능과 머신러닝에 관심이 있습니다",
        "감사합니다"
    ]
    
    print("\n한국어 -> 영어 번역:")
    for text in korean_texts:
        translation = translator.translate_ko_to_en(text)
        print(f"'{text}' -> '{translation}'")
    
    # 영한 번역 예시
    english_texts = [
        "Hello",
        "I am learning Python programming",
        "I am interested in AI and machine learning",
        "Thank you"
    ]
    
    print("\n영어 -> 한국어 번역:")
    for text in english_texts:
        translation = translator.translate_en_to_ko(text)
        print(f"'{text}' -> '{translation}'")

def section_4_practical_examples():
    """4. 실전 예제"""
    print("\n" + "=" * 50)
    print("4. 실전 예제")
    print("=" * 50)
    
    print("실제 프로젝트에서 활용할 수 있는 예제들:")
    
    # 1. 감정 분석 시스템
    print("\n1. 감정 분석 시스템")
    print("""
    def analyze_sentiment(text: str) -> Dict[str, float]:
        # Hugging Face 감정 분석 모델 사용
        API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
        headers = {"Authorization": "Bearer YOUR_API_KEY"}
        
        response = requests.post(API_URL, headers=headers, json={"inputs": text})
        return response.json()
    
    # 사용 예시
    sentiment = analyze_sentiment("I love this product!")
    print(sentiment)  # {'label': 'POSITIVE', 'score': 0.95}
    """)
    
    # 2. 문서 요약 시스템
    print("\n2. 문서 요약 시스템")
    print("""
    def summarize_text(text: str) -> str:
        # OpenAI API를 사용한 텍스트 요약
        prompt = f"다음 텍스트를 간단히 요약해주세요:\\n\\n{text}"
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        
        return response.choices[0].message.content
    """)
    
    # 3. 다국어 챗봇
    print("\n3. 다국어 챗봇")
    print("""
    class MultilingualChatbot:
        def __init__(self):
            self.translator = TranslationModel()
            self.chatbot = SimpleChatbot(api_key)
        
        def chat(self, message: str, language: str = "ko"):
            # 한국어가 아닌 경우 번역
            if language != "ko":
                message = self.translator.translate_to_ko(message)
            
            # 챗봇 응답
            response = self.chatbot.get_response(message)
            
            # 원래 언어로 번역
            if language != "ko":
                response = self.translator.translate_from_ko(response, language)
            
            return response
    """)

def section_5_setup_instructions():
    """5. 설정 가이드"""
    print("\n" + "=" * 50)
    print("5. 설정 가이드")
    print("=" * 50)
    
    print("API 키 설정 방법:")
    print("\n1. OpenAI API 키 설정")
    print("""
    # 환경변수 설정
    export OPENAI_API_KEY="your-api-key-here"
    
    # Python에서 사용
    import os
    api_key = os.getenv("OPENAI_API_KEY")
    """)
    
    print("\n2. Hugging Face API 키 설정")
    print("""
    # 환경변수 설정
    export HUGGINGFACE_API_KEY="your-api-key-here"
    
    # Python에서 사용
    import os
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    """)
    
    print("\n3. 필요한 라이브러리 설치")
    print("""
    pip install openai
    pip install transformers
    pip install torch
    pip install requests
    """)
    
    print("\n4. API 키 보안 주의사항")
    print("- API 키를 코드에 직접 입력하지 마세요")
    print("- 환경변수나 .env 파일을 사용하세요")
    print("- .gitignore에 API 키 파일을 추가하세요")
    print("- API 사용량과 비용을 모니터링하세요")

def main():
    """메인 함수"""
    print("3주차: AI 모델 실습")
    print("학부생 3,4학년 수준")
    
    section_1_huggingface_models()
    section_2_openai_chatbot()
    section_3_translation_model()
    section_4_practical_examples()
    section_5_setup_instructions()
    
    print("\n" + "=" * 50)
    print("실습 완료")
    print("=" * 50)
    print("\n다음 단계:")
    print("1. API 키를 발급받아 실제 모델을 사용해보세요")
    print("2. 다양한 프롬프트를 시도해보세요")
    print("3. 실제 프로젝트에 AI 모델을 통합해보세요")

if __name__ == "__main__":
    main() 