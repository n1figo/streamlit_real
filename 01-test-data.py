import streamlit as st
import pandas as pd
import numpy as np


st.title('주식 성공의 비결, TimingGenius와 함께 하세요!')

# Header 적용
st.header('1. TimingGenius 포트폴리오 수익률 (차트) :sparkles:')

# Header 적용
st.header('2. TimingGenius 오늘의 AI 점수 상위 20종목 :sparkles:')

# st.title('1. 오늘의 RL 랭킹')

# DataFrame 생성
dataframe = pd.DataFrame({
    'first column': ['삼성전자', '하이닉스', 3, 4],
    'second column': [10, 20, 30, 40],
    'AI점수 순위': [10, 20, 30, 40],
    '10년 예상 연복리수익률(%)': [10, 20, 30, 40],
    '지난 10년 연복리 자본총계 증가율(%)': [10, 20, 30, 40],
    '지난 10년 연복리 주가상승률(%)': [10, 20, 30, 40],
    '매수리스트 추가': [10, 20, 30, 40],
})

# DataFrame
# use_container_width 기능은 데이터프레임을 컨테이너 크기에 확장할 때 사용합니다. (True/False)
st.dataframe(dataframe, use_container_width=True)


# # 테이블(static)
# # DataFrame과는 다르게 interactive 한 UI 를 제공하지 않습니다.
# st.table(dataframe)


# # # 메트릭
# st.metric(label="온도", value="10°C", delta="1.2°C")
# st.metric(label="삼성전자", value="61,000 원", delta="-1,200 원")

# # 컬럼으로 영역을 나누어 표기한 경우
# col1, col2, col3 = st.columns(3)
# col1.metric(label="달러USD", value="1,228 원", delta="-12.00 원")
# col2.metric(label="일본JPY(100엔)", value="958.63 원", delta="-7.44 원")
# col3.metric(label="유럽연합EUR", value="1,335.82 원", delta="11.44 원")


# Header 적용
st.header('3. TimingGenius 매수리스트')

# DataFrame 생성
dataframe = pd.DataFrame({
    '종목명': ['포스코홀딩스', '롯데관광개발', 3, 4],
    '내재가치': [10, 20, 30, 40],
    '유지가능ROE': [10, 20, 30, 40],
    '시총': [10, 20, 30, 40],
    '시총/내재가치(%)': [10, 20, 30, 40],
    '10년 예상 연복리수익률(%)': [10, 20, 30, 40],
    '지난 10년 연복리 자본총계 증가율(%)': [10, 20, 30, 40],
    '지난 10년 연복리 주가상승률(%)': [10, 20, 30, 40],
    '내년 예상순이익': [10, 20, 30, 40],
    '내년 예상수익률(%)': [10, 20, 30, 40],
    '1차 매수가 (60%)': [10, 20, 30, 40],
    '2차 매수가 (50%)': [10, 20, 30, 40],
    '3차 매수가 (40%)': [10, 20, 30, 40],
})

# DataFrame
# use_container_width 기능은 데이터프레임을 컨테이너 크기에 확장할 때 사용합니다. (True/False)
st.dataframe(dataframe, use_container_width=True)



st.header('4. TimingGenius 매수리스트의 주가차트 및 AI예측차트(3개월 뒤)')


st.header('5. 회원가입시 인구통계정보 수취 화면 : 02-basic활용')