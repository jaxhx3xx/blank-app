import streamlit as st
import random

# --- 앱 기본 설정 ---
st.set_page_config(page_title="초성게임+", page_icon="✨")

# --- 초성 퀴즈 데이터 ---
CHOSUNG_LIST = [
    "ㄱㄴ", "ㄴㄷ", "ㄷㄹ", "ㄹㅁ", "ㅁㅂ", "ㅂㅅ", "ㅅㅇ", "ㅇㅈ",
    "ㅈㅊ", "ㅊㅋ", "ㅋㅌ", "ㅌㅍ", "ㅍㅎ", "ㄱㅅ", "ㄴㅈ", "ㄷㅂ",
    "ㄹㄱ", "ㅁㅅ", "ㅂㅇ", "ㅅㅈ", "ㅇㅊ", "ㅈㅋ", "ㅊㅌ", "ㅋㅍ", "ㅌㅎ"
]

# --- 디자인 개선을 위한 CSS ---
st.markdown("""
<style>
    /* 전체적인 폰트 및 배경 설정 */
    .stApp {
        background: linear-gradient(to right top, #FFAEF1, #FFBED3, #FDDEBE, #FFF58C, #F1FA7E);
        color: 009665;
    }
    /* 제목 스타일 */
    h1 {
        color: #FF5F5F; /* 금색 계열 */
        text-shadow: 2px 2px 4px #000000;
    }
    /* 헤더(제시어) 스타일 */
    h2 {
        background-color: rgba(0, 0, 0, 0.3);
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #FFD700;
    }
    /* 버튼 스타일 */
    .stButton>button {
        border: 2px solid #FFFFFF;
        border-radius: 20px;
        color: #FFFFFF;
        background-color: transparent;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        border-color: #FFD700;
        color: #FFD700;
        background-color: rgba(255, 255, 255, 0.1);
    }
    /* Primary 버튼(종료하기) 스타일 */
    .stButton>button[kind="primary"] {
        background-color: #C70039;
        border: none;
    }
    .stButton>button[kind="primary"]:hover {
        background-color: #900C3F;
    }
    /* 정보 메시지(입력한 단어) 스타일 */
    .stAlert {
        background-color: rgba(0, 0, 0, 0.2);
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)


# --- 세션 상태 초기화 ---
if 'current_quiz' not in st.session_state:
    st.session_state.current_quiz = random.choice(CHOSUNG_LIST)
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""


# --- 함수 정의 ---
def start_new_game():
    """새로운 게임을 시작하는 함수"""
    previous_quiz = st.session_state.current_quiz
    new_quiz_list = [q for q in CHOSUNG_LIST if q != previous_quiz]
    st.session_state.current_quiz = random.choice(new_quiz_list)
    st.session_state.submitted = False
    st.session_state.user_input = "" # 입력 필드 초기화를 위해 추가

def end_game():
    """게임 종료 처리를 하는 함수"""
    st.success("게임을 종료합니다. 다음에 또 만나요! 👋")
    st.balloons()
    st.stop()


# --- UI 및 게임 로직 ---
st.title("✨ 초성게임 PLUS ✨")
st.divider()

# 제출 전 화면
if not st.session_state.submitted:
    st.header(f"제시어: `{st.session_state.current_quiz}`")
    st.write("위 초성에 맞는 단어를 입력하고 '제출하기' 버튼을 누르세요!")

    with st.form(key="answer_form"):
        user_input = st.text_input(
            "정답 입력:",
            placeholder="예시) 강남, 과일",
            key="input_field"
        )
        submit_button = st.form_submit_button(label="제출하기 🧐")

    if submit_button:
        if not user_input.strip():
            st.warning("단어를 입력해주세요!")
        else:
            st.session_state.user_input = user_input # 입력값 저장
            st.session_state.submitted = True
            st.rerun()

# 제출 후 화면
if st.session_state.submitted:
    st.header(f"제시어: `{st.session_state.current_quiz}`")
    st.info(f"입력한 단어: **{st.session_state.user_input}**")
    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("새로운 문제 풀기 🎲", use_container_width=True):
            start_new_game()
            st.rerun()
    with col2:
        if st.button("게임 종료하기 🛑", type="primary", use_container_width=True):
            end_game()
