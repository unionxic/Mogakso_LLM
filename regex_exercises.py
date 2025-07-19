#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
정규표현식과 문자열 처리 연습 문제
학부생 3,4학년 수준 - 추가 연습
"""

import re

def exercise_1_phone_validation():
    """연습 1: 전화번호 유효성 검사"""
    print("=" * 50)
    print("연습 1: 전화번호 유효성 검사")
    print("=" * 50)
    
    phone_numbers = [
        "010-1234-5678",
        "010.9876.5432", 
        "010 5555 1234",
        "02-123-4567",
        "02.123.4567",
        "02 123 4567",
        "123-456-7890",  # 잘못된 형식
        "010-123-456",   # 잘못된 형식
        "abc-def-ghij",  # 잘못된 형식
    ]
    
    # 한국 전화번호 패턴
    korean_phone_pattern = r'^(?:010|02)[-.\s]?\d{3,4}[-.\s]?\d{4}$'
    
    print("전화번호 유효성 검사 결과:")
    for phone in phone_numbers:
        is_valid = bool(re.match(korean_phone_pattern, phone))
        status = "유효" if is_valid else "무효"
        print(f"{phone:15} -> {status}")

def exercise_2_email_validation():
    """연습 2: 이메일 유효성 검사"""
    print("\n" + "=" * 50)
    print("연습 2: 이메일 유효성 검사")
    print("=" * 50)
    
    emails = [
        "user@example.com",
        "test.email@gmail.com",
        "user_name@company.co.kr",
        "student@university.ac.kr",
        "invalid.email@",
        "@invalid.com",
        "no.at.sign",
        "user@domain",
        "user@.com",
        "user@domain..com",
    ]
    
    # 이메일 패턴
    email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
    
    print("이메일 유효성 검사 결과:")
    for email in emails:
        is_valid = bool(re.match(email_pattern, email))
        status = "유효" if is_valid else "무효"
        print(f"{email:25} -> {status}")

def exercise_3_text_processing():
    """연습 3: 텍스트 처리"""
    print("\n" + "=" * 50)
    print("연습 3: 텍스트 처리")
    print("=" * 50)
    
    text = """
    제목: 파이썬 프로그래밍 기초
    작성자: 김철수 (kim@university.ac.kr)
    날짜: 2024-01-15
    조회수: 1,234
    
    내용:
    파이썬은 배우기 쉬운 프로그래밍 언어입니다.
    정규표현식(regex)을 사용하면 텍스트 처리가 훨씬 쉬워집니다.
    
    연락처: 010-1234-5678
    """
    
    print("원본 텍스트:")
    print(text)
    
    # 1. 제목 추출
    title_match = re.search(r'제목:\s*(.+)', text)
    if title_match:
        print(f"\n제목: {title_match.group(1).strip()}")
    
    # 2. 작성자 정보 추출
    author_match = re.search(r'작성자:\s*(.+?)\s*\(([^)]+)\)', text)
    if author_match:
        print(f"작성자: {author_match.group(1).strip()}")
        print(f"이메일: {author_match.group(2)}")
    
    # 3. 날짜 추출
    date_match = re.search(r'날짜:\s*(\d{4}-\d{2}-\d{2})', text)
    if date_match:
        print(f"날짜: {date_match.group(1)}")
    
    # 4. 조회수 추출
    views_match = re.search(r'조회수:\s*([0-9,]+)', text)
    if views_match:
        views = views_match.group(1).replace(',', '')
        print(f"조회수: {views}")
    
    # 5. 전화번호 추출
    phone_match = re.search(r'연락처:\s*([0-9\-]+)', text)
    if phone_match:
        print(f"연락처: {phone_match.group(1)}")

def exercise_4_string_manipulation():
    """연습 4: 문자열 조작"""
    print("\n" + "=" * 50)
    print("연습 4: 문자열 조작")
    print("=" * 50)
    
    # CSV 데이터 처리
    csv_data = "이름,나이,전공,학점\n김철수,20,컴퓨터공학,3.8\n이영희,21,전자공학,3.9\n박민수,19,기계공학,3.5"
    
    print("원본 CSV 데이터:")
    print(csv_data)
    
    # 1. CSV를 리스트로 변환
    lines = csv_data.split('\n')
    headers = lines[0].split(',')
    
    print(f"\n헤더: {headers}")
    
    # 2. 데이터 행 처리
    students = []
    for line in lines[1:]:
        if line.strip():
            values = line.split(',')
            student = dict(zip(headers, values))
            students.append(student)
    
    print("\n학생 정보:")
    for student in students:
        print(f"  {student}")
    
    # 3. 학점이 3.8 이상인 학생 필터링
    high_gpa_students = [s for s in students if float(s['학점']) >= 3.8]
    print(f"\n고학점 학생 (3.8 이상):")
    for student in high_gpa_students:
        print(f"  {student['이름']}: {student['학점']}")

def exercise_5_advanced_regex():
    """연습 5: 고급 정규표현식"""
    print("\n" + "=" * 50)
    print("연습 5: 고급 정규표현식")
    print("=" * 50)
    
    # 로그 파일 분석
    log_entries = [
        "2024-01-15 10:30:15 [INFO] User login successful: user123",
        "2024-01-15 10:35:22 [ERROR] Database connection failed: timeout",
        "2024-01-15 10:40:18 [WARN] High memory usage: 85%",
        "2024-01-15 10:45:33 [INFO] User logout: user456",
        "2024-01-15 10:50:45 [ERROR] File not found: /path/to/file.txt",
    ]
    
    print("로그 엔트리:")
    for entry in log_entries:
        print(f"  {entry}")
    
    # 1. 로그 레벨별 분류
    print("\n로그 레벨별 분류:")
    log_pattern = r'\[(INFO|ERROR|WARN)\]'
    
    for entry in log_entries:
        level_match = re.search(log_pattern, entry)
        if level_match:
            level = level_match.group(1)
            print(f"  {level}: {entry}")
    
    # 2. 사용자 ID 추출
    print("\n사용자 ID 추출:")
    user_pattern = r'user\d+'
    
    for entry in log_entries:
        users = re.findall(user_pattern, entry)
        if users:
            print(f"  {entry} -> 사용자: {users}")
    
    # 3. 시간대별 로그 분석
    print("\n시간대별 분석:")
    time_pattern = r'(\d{2}):(\d{2}):(\d{2})'
    
    for entry in log_entries:
        time_match = re.search(time_pattern, entry)
        if time_match:
            hour = time_match.group(1)
            minute = time_match.group(2)
            print(f"  {hour}시 {minute}분: {entry}")

def exercise_6_practical_example():
    """연습 6: 실전 예제 - 웹 로그 분석"""
    print("\n" + "=" * 50)
    print("연습 6: 실전 예제 - 웹 로그 분석")
    print("=" * 50)
    
    # 웹 서버 로그 데이터
    web_logs = [
        '192.168.1.100 - - [15/Jan/2024:10:30:15 +0900] "GET /index.html HTTP/1.1" 200 1234',
        '192.168.1.101 - - [15/Jan/2024:10:30:20 +0900] "POST /login HTTP/1.1" 302 567',
        '192.168.1.102 - - [15/Jan/2024:10:30:25 +0900] "GET /images/logo.png HTTP/1.1" 404 123',
        '192.168.1.100 - - [15/Jan/2024:10:30:30 +0900] "GET /api/users HTTP/1.1" 200 890',
        '192.168.1.103 - - [15/Jan/2024:10:30:35 +0900] "GET /admin HTTP/1.1" 403 234',
    ]
    
    print("웹 로그 데이터:")
    for log in web_logs:
        print(f"  {log}")
    
    # 1. IP 주소 추출
    print("\nIP 주소 추출:")
    ip_pattern = r'(\d+\.\d+\.\d+\.\d+)'
    ips = []
    for log in web_logs:
        ip_match = re.search(ip_pattern, log)
        if ip_match:
            ips.append(ip_match.group(1))
    print(f"  고유 IP 주소: {list(set(ips))}")
    
    # 2. HTTP 상태 코드 분석
    print("\nHTTP 상태 코드 분석:")
    status_pattern = r'"\w+\s[^"]+\sHTTP/[^"]+"\s(\d+)'
    
    status_counts = {}
    for log in web_logs:
        status_match = re.search(status_pattern, log)
        if status_match:
            status = status_match.group(1)
            status_counts[status] = status_counts.get(status, 0) + 1
    
    for status, count in status_counts.items():
        print(f"  {status}: {count}회")
    
    # 3. 요청 URL 추출
    print("\n요청 URL 추출:")
    url_pattern = r'"\w+\s([^"]+)\sHTTP/[^"]+"'
    
    for log in web_logs:
        url_match = re.search(url_pattern, log)
        if url_match:
            url = url_match.group(1)
            print(f"  {url}")

def main():
    """메인 함수 - 모든 연습 실행"""
    print("정규표현식과 문자열 처리 연습")
    print("학부생 3,4학년 수준")
    
    exercise_1_phone_validation()
    exercise_2_email_validation()
    exercise_3_text_processing()
    exercise_4_string_manipulation()
    exercise_5_advanced_regex()
    exercise_6_practical_example()
    
    print("\n" + "=" * 50)
    print("연습 완료")
    print("=" * 50)
    print("\n학습 참고 자료:")
    print("1. 정규표현식 테스트 도구: regex101.com")
    print("2. 다양한 텍스트 데이터로 패턴 연습하기")
    print("3. 실제 프로젝트에서 로그 분석, 데이터 정제 등에 활용하기")

if __name__ == "__main__":
    main() 