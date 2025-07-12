
# AI 기초 실습 - Pandas & Matplotlib
# 작성자: 윤현식
# 날짜: 2024-12-07

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정 (Colab용)
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

print("✅ 라이브러리 로드 완료!")

# 샘플 신조어 데이터 생성
data = {
    '신조어': ['감다살', '킹받네', '갓생', '프불', '억텐', '밈', '레전드', '인싸'],
    '사용빈도': [150, 300, 200, 80, 120, 250, 180, 220],
    '세대': ['MZ', 'MZ', 'MZ', 'MZ', 'MZ', '전체', '전체', 'MZ'],
    '카테고리': ['감정', '감정', '라이프', '상태', '감정', '문화', '평가', '관계']
}

# DataFrame 생성
df = pd.DataFrame(data)

print("📋 데이터 기본 정보")
print(df.info())
print("\n📊 데이터 미리보기")
print(df.head())

# 기본 통계
print("\n📈 기본 통계")
print(df['사용빈도'].describe())

# 카테고리별 평균 사용빈도
category_avg = df.groupby('카테고리')['사용빈도'].mean()
print("\n카테고리별 평균 사용빈도:")
print(category_avg)

# 사용빈도가 200 이상인 신조어 필터링
popular_words = df[df['사용빈도'] >= 200]
print("\n인기 신조어 (사용빈도 200+):")
print(popular_words)

# 시각화
plt.figure(figsize=(12, 8))

# 1. 막대 그래프
plt.subplot(2, 2, 1)
plt.bar(df['신조어'], df['사용빈도'], color='skyblue')
plt.title('Slang Word Frequency')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

# 2. 파이 차트
plt.subplot(2, 2, 2)
category_counts = df['카테고리'].value_counts()
plt.pie(category_counts.values, labels=category_counts.index, autopct='%1.1f%%')
plt.title('Category Distribution')

# 3. 히스토그램
plt.subplot(2, 2, 3)
plt.hist(df['사용빈도'], bins=5, color='lightgreen', alpha=0.7)
plt.title('Frequency Distribution')
plt.xlabel('Frequency')
plt.ylabel('Count')

# 4. 산점도
plt.subplot(2, 2, 4)
word_length = [len(word) for word in df['신조어']]
plt.scatter(word_length, df['사용빈도'], color='red', alpha=0.6)
plt.title('Word Length vs Frequency')
plt.xlabel('Word Length')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

print("\n✅ 실습 완료!")
