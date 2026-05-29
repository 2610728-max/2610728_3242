import streamlit as st

# 앱 제목 설정
st.title("🔢 재미있는 구구단 앱")
st.write("원하는 단을 선택하면 구구단이 동적으로 출력됩니다.")

# 사이드바에 슬라이더 추가 (2단부터 9단까지 선택 가능)
selected_dan = st.sidebar.slider("단을 선택하세요", min_value=2, max_value=9, value=2)

# 메인 화면에 선택한 단 표시
st.header(f"▶ {selected_dan}단 출력")

# 구구단 계산 및 출력
# 기존 코드의 중첩 반복문 대신, 선택된 단(i)에 대해서만 j가 반복되도록 변경했습니다.
for j in range(1, 10):
    result = selected_dan * j
    # 스트림닛의 text 기능을 사용해 화면에 출력
    st.text(f"{selected_dan} * {j} = {result}")

# 팁: 한 눈에 표로 보고 싶을 때를 위한 데이터 프레임 기능 (선택 사항)
if st.checkbox("전체 구구단 표 보기"):
    st.subheader("전체 구구단")
    # 2단부터 9단까지 격자 형태로 예쁘게 보여주기
    columns = st.columns(4) # 4개 열로 나누기
    for i in range(2, 10):
        col_idx = (i - 2) % 4
        with columns[col_idx]:
            st.markdown(f"**[{i}단]**")
            for j in range(1, 10):
                st.write(f"{i} * {j} = {i*j}")