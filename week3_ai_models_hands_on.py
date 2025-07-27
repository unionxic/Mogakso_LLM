#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3주차: AI 모델 실습 - 실제 API 사용
실제 API 키를 사용하여 AI 모델을 체험해보세요.
"""

import os
import requests
import json
from typing import Dict, List, Optional

# API 키 설정 (환경변수에서 가져오기)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

def check_api_keys():
    """API 키 확인"""
    print("API 키 확인:")
    print(f"OpenAI API 키: {'설정됨' if OPENAI_API_KEY else '설정되지 않음'}")
    print(f"Hugging Face API 키: {'설정됨' if HUGGINGFACE_API_KEY else '설정되지 않음'}")
    print()

def huggingface_sentiment_analysis():
    """Hugging Face 감정 분석"""
    print("=" * 50)
    print("Hugging Face 감정 분석")
    print("=" * 50)
    
    if not HUGGINGFACE_API_KEY:
        print("Hugging Face API 키가 설정되지 않았습니다.")
        print("환경변수 HUGGINGFACE_API_KEY를 설정해주세요.")
        return
    
    API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    
    # 테스트 텍스트들
    test_texts = [
        "I love this movie!",
        "This product is terrible.",
        "The weather is okay today.",
        "I'm so excited about this new project!",
        "This is the worst experience ever."
    ]
    
    print("감정 분석 결과:")
    for text in test_texts:
        try:
            output = query({"inputs": text})
            if isinstance(output, list) and len(output) > 0:
                result = output[0]
                label = result.get('label', 'UNKNOWN')
                score = result.get('score', 0)
                print(f"'{text}' -> {label} (신뢰도: {score:.3f})")
            else:
                print(f"'{text}' -> 분석 실패")
        except Exception as e:
            print(f"'{text}' -> 오류: {e}")

def openai_chatbot_demo():
    """OpenAI 챗봇 데모"""
    print("\n" + "=" * 50)
    print("OpenAI 챗봇 데모")
    print("=" * 50)
    
    if not OPENAI_API_KEY:
        print("OpenAI API 키가 설정되지 않았습니다.")
        print("환경변수 OPENAI_API_KEY를 설정해주세요.")
        return
    
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
            self.conversation_history.append({
                "role": role,
                "content": content
            })
        
        def get_response(self, user_message: str) -> str:
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
            self.conversation_history = []
    
    chatbot = SimpleChatbot(OPENAI_API_KEY)
    
    # 대화 예시
    test_conversations = [
        "안녕하세요!",
        "파이썬에 대해 간단히 설명해주세요.",
        "인공지능의 미래에 대해 어떻게 생각하시나요?",
        "감사합니다!"
    ]
    
    print("챗봇과의 대화:")
    for message in test_conversations:
        print(f"\n사용자: {message}")
        response = chatbot.get_response(message)
        print(f"챗봇: {response}")

def translation_demo():
    """번역 데모"""
    print("\n" + "=" * 50)
    print("번역 데모")
    print("=" * 50)
    
    if not OPENAI_API_KEY:
        print("OpenAI API 키가 설정되지 않았습니다.")
        return
    
    def translate_with_openai(text: str, target_lang: str = "English") -> str:
        api_url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        
        prompt = f"다음 텍스트를 {target_lang}로 번역해주세요: {text}"
        
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 100,
            "temperature": 0.3
        }
        
        try:
            response = requests.post(api_url, headers=headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            return result["choices"][0]["message"]["content"]
        except Exception as e:
            return f"번역 오류: {e}"
    
    # 번역 테스트
    korean_texts = [
        "안녕하세요",
        "파이썬 프로그래밍을 배우고 있습니다",
        "인공지능과 머신러닝에 관심이 있습니다",
        "감사합니다"
    ]
    
    print("한국어 -> 영어 번역:")
    for text in korean_texts:
        translation = translate_with_openai(text, "English")
        print(f"'{text}' -> '{translation}'")
    
    english_texts = [
        "Hello",
        "I am learning Python programming",
        "I am interested in AI and machine learning",
        "Thank you"
    ]
    
    print("\n영어 -> 한국어 번역:")
    for text in english_texts:
        translation = translate_with_openai(text, "Korean")
        print(f"'{text}' -> '{translation}'")

def text_summarization_demo():
    """텍스트 요약 데모"""
    print("\n" + "=" * 50)
    print("텍스트 요약 데모")
    print("=" * 50)
    
    if not OPENAI_API_KEY:
        print("OpenAI API 키가 설정되지 않았습니다.")
        return
    
    def summarize_text(text: str) -> str:
        api_url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        
        prompt = f"다음 텍스트를 간단히 요약해주세요:\n\n{text}"
        
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 100,
            "temperature": 0.3
        }
        
        try:
            response = requests.post(api_url, headers=headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            return result["choices"][0]["message"]["content"]
        except Exception as e:
            return f"요약 오류: {e}"
    
    # 요약할 텍스트
    long_text = """
    인공지능(AI)은 컴퓨터가 인간의 지능을 모방하여 학습하고, 추론하고, 문제를 해결할 수 있도록 하는 기술입니다. 
    머신러닝은 AI의 한 분야로, 데이터로부터 패턴을 학습하여 예측이나 분류를 수행합니다. 
    딥러닝은 머신러닝의 하위 분야로, 인공신경망을 사용하여 복잡한 패턴을 학습합니다. 
    최근에는 자연어 처리, 컴퓨터 비전, 음성 인식 등 다양한 분야에서 AI가 활용되고 있습니다. 
    AI는 의료, 금융, 교육, 교통 등 거의 모든 산업 분야에서 혁신을 가져오고 있습니다.
    """
    
    print("원본 텍스트:")
    print(long_text)
    
    print("\n요약 결과:")
    summary = summarize_text(long_text)
    print(summary)

def interactive_chat():
    """대화형 챗봇"""
    print("\n" + "=" * 50)
    print("대화형 챗봇")
    print("=" * 50)
    
    if not OPENAI_API_KEY:
        print("OpenAI API 키가 설정되지 않았습니다.")
        return
    
    class InteractiveChatbot:
        def __init__(self, api_key: str):
            self.api_key = api_key
            self.api_url = "https://api.openai.com/v1/chat/completions"
            self.headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            self.conversation_history = []
        
        def chat(self, user_message: str) -> str:
            self.conversation_history.append({
                "role": "user",
                "content": user_message
            })
            
            payload = {
                "model": "gpt-3.5-turbo",
                "messages": self.conversation_history,
                "max_tokens": 200,
                "temperature": 0.7
            }
            
            try:
                response = requests.post(self.api_url, headers=self.headers, json=payload)
                response.raise_for_status()
                
                result = response.json()
                assistant_message = result["choices"][0]["message"]["content"]
                self.conversation_history.append({
                    "role": "assistant",
                    "content": assistant_message
                })
                
                return assistant_message
            except Exception as e:
                return f"오류: {e}"
        
        def reset(self):
            self.conversation_history = []
    
    chatbot = InteractiveChatbot(OPENAI_API_KEY)
    
    print("챗봇과 대화를 시작합니다. 'quit'를 입력하면 종료됩니다.")
    print("'reset'을 입력하면 대화 기록이 초기화됩니다.")
    
    while True:
        user_input = input("\n사용자: ").strip()
        
        if user_input.lower() == 'quit':
            print("대화를 종료합니다.")
            break
        elif user_input.lower() == 'reset':
            chatbot.reset()
            print("대화 기록이 초기화되었습니다.")
            continue
        elif not user_input:
            continue
        
        response = chatbot.chat(user_input)
        print(f"챗봇: {response}")

def main():
    """메인 함수"""
    print("3주차: AI 모델 실습 - 실제 API 사용")
    print("학부생 3,4학년 수준")
    
    check_api_keys()
    
    # API 키가 설정된 경우에만 실행
    if HUGGINGFACE_API_KEY:
        huggingface_sentiment_analysis()
    
    if OPENAI_API_KEY:
        openai_chatbot_demo()
        translation_demo()
        text_summarization_demo()
        
        # 대화형 챗봇 (선택사항)
        try_interactive = input("\n대화형 챗봇을 시도하시겠습니까? (y/n): ").strip().lower()
        if try_interactive == 'y':
            interactive_chat()
    else:
        print("\nOpenAI API 키가 설정되지 않아 일부 기능을 사용할 수 없습니다.")
        print("환경변수 OPENAI_API_KEY를 설정해주세요.")
    
    print("\n" + "=" * 50)
    print("실습 완료")
    print("=" * 50)

if __name__ == "__main__":
    main() 