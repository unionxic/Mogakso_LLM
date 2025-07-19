#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
정규표현식과 문자열 처리 실습
학부생 3,4학년 수준

1. 정규표현식: 패턴 찾기 (전화번호, 이메일)
2. 문자열 처리: split, replace 등 기본기
"""

import re
import string

def main():
    print("=" * 50)
    print("정규표현식과 문자열 처리 실습")
    print("=" * 50)
    
    # 1. 정규표현식 실습
    print("\n1. 정규표현식 패턴 찾기")
    print("-" * 30)
    
    # 샘플 텍스트
    sample_text = """
    연락처 정보:
    - 김철수: 010-1234-5678
    - 이영희: 010.9876.5432
    - 박민수: 010 5555 1234
    - 홍길동: 02-123-4567
    
    이메일 주소:
    - student1@university.ac.kr
    - test.email@gmail.com
    - user_name@company.co.kr
    - invalid.email@
    - @invalid.com
    """
    
    print("원본 텍스트:")
    print(sample_text)
    
    # 전화번호 패턴 찾기
    print("\n전화번호 패턴 찾기:")
    phone_patterns = [
        r'010-\d{4}-\d{4}',      # 010-XXXX-XXXX
        r'010\.\d{4}\.\d{4}',    # 010.XXXX.XXXX
        r'010\s\d{4}\s\d{4}',    # 010 XXXX XXXX
        r'02-\d{3}-\d{4}',       # 02-XXX-XXXX
    ]
    
    for pattern in phone_patterns:
        matches = re.findall(pattern, sample_text)
        if matches:
            print(f"패턴 '{pattern}': {matches}")
    
    # 통합 전화번호 패턴
    print("\n통합 전화번호 패턴:")
    unified_phone_pattern = r'(?:010|02)[-.\s]?\d{3,4}[-.\s]?\d{4}'
    phone_matches = re.findall(unified_phone_pattern, sample_text)
    print(f"찾은 전화번호: {phone_matches}")
    
    # 이메일 패턴 찾기
    print("\n이메일 패턴 찾기:")
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_matches = re.findall(email_pattern, sample_text)
    print(f"찾은 이메일: {email_matches}")
    
    # 2. 문자열 처리 실습
    print("\n\n2. 문자열 처리 기본기")
    print("-" * 30)
    
    # 샘플 문자열들
    text1 = "Python,Java,C++,JavaScript"
    text2 = "   공백이 있는 텍스트   "
    text3 = "대소문자 혼합 Text"
    text4 = "apple,banana,orange,grape"
    
    print(f"원본 문자열1: '{text1}'")
    print(f"원본 문자열2: '{text2}'")
    print(f"원본 문자열3: '{text3}'")
    print(f"원본 문자열4: '{text4}'")
    
    # split() 실습
    print("\nsplit() 실습:")
    print(f"text1.split(','): {text1.split(',')}")
    print(f"text4.split(','): {text4.split(',')}")
    
    # strip() 실습
    print("\nstrip() 실습:")
    print(f"text2.strip(): '{text2.strip()}'")
    print(f"text2.lstrip(): '{text2.lstrip()}'")
    print(f"text2.rstrip(): '{text2.rstrip()}'")
    
    # replace() 실습
    print("\nreplace() 실습:")
    print(f"text1.replace(',', ' | '): {text1.replace(',', ' | ')}")
    print(f"text3.replace('Text', '문자열'): {text3.replace('Text', '문자열')}")
    
    # upper(), lower() 실습
    print("\n대소문자 변환:")
    print(f"text3.upper(): {text3.upper()}")
    print(f"text3.lower(): {text3.lower()}")
    print(f"text3.title(): {text3.title()}")
    
    # join() 실습
    print("\njoin() 실습:")
    languages = ['Python', 'Java', 'C++', 'JavaScript']
    print(f"languages: {languages}")
    print(f"' | '.join(languages): {' | '.join(languages)}")
    print(f"'-'.join(languages): {'-'.join(languages)}")
    
    # 3. 실전 예제
    print("\n\n3. 실전 예제")
    print("-" * 30)
    
    # 로그 파일 파싱 예제
    log_data = """
    2024-01-15 10:30:15 INFO User login: user123@example.com
    2024-01-15 10:35:22 ERROR Database connection failed
    2024-01-15 10:40:18 INFO User logout: user456@test.com
    2024-01-15 10:45:33 WARN High memory usage detected
    """
    
    print("로그 데이터:")
    print(log_data)
    
    # 이메일 추출
    print("\n로그에서 이메일 추출:")
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    log_emails = re.findall(email_pattern, log_data)
    print(f"찾은 이메일: {log_emails}")
    
    # 로그 레벨별 분류
    print("\n로그 레벨별 분류:")
    log_lines = log_data.strip().split('\n')
    
    for line in log_lines:
        if line.strip():
            # 로그 레벨 추출
            level_match = re.search(r'(INFO|ERROR|WARN)', line)
            if level_match:
                level = level_match.group(1)
                print(f"{level}: {line.strip()}")
    
    # 4. 연습 문제
    print("\n\n4. 연습 문제")
    print("-" * 30)
    
    practice_text = """
    학생 정보:
    이름: 김철수, 전화: 010-1234-5678, 이메일: kim@university.ac.kr
    이름: 이영희, 전화: 010.9876.5432, 이메일: lee@company.co.kr
    이름: 박민수, 전화: 010 5555 1234, 이메일: park@gmail.com
    """
    
    print("연습용 텍스트:")
    print(practice_text)
    
    print("\n연습 문제:")
    print("1. 모든 학생의 이름을 추출하세요")
    print("2. 모든 전화번호를 추출하세요")
    print("3. 모든 이메일을 추출하세요")
    print("4. 각 학생의 정보를 딕셔너리로 정리하세요")
    
    # 해답
    print("\n결과:")
    
    # 이름 추출
    name_pattern = r'이름:\s*([가-힣]+)'
    names = re.findall(name_pattern, practice_text)
    print(f"1. 학생 이름: {names}")
    
    # 전화번호 추출
    phone_pattern = r'전화:\s*([0-9\-\s\.]+)'
    phones = re.findall(phone_pattern, practice_text)
    print(f"2. 전화번호: {phones}")
    
    # 이메일 추출
    email_pattern = r'이메일:\s*([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})'
    emails = re.findall(email_pattern, practice_text)
    print(f"3. 이메일: {emails}")
    
    # 딕셔너리로 정리
    students = []
    for i in range(len(names)):
        student = {
            'name': names[i],
            'phone': phones[i].strip(),
            'email': emails[i]
        }
        students.append(student)
    
    print(f"4. 학생 정보 딕셔너리:")
    for student in students:
        print(f"   {student}")

if __name__ == "__main__":
    main() 