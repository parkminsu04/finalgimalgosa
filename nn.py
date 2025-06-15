import streamlit as st
import streamlit.components.v1 as components
import json
import pandas as pd
import base64
import os

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="박민수의 프로필 발표",
    page_icon="👨‍💻",
    layout="wide"
)

# --- 스타일(CSS) 통합 관리 ---
# 커서 스타일은 각 슬라이드에 직접 주입하므로, 여기서는 기본 스타일만 유지합니다.
st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    <style>
        html, body, [class*="st-"] { font-family: 'Noto Sans KR', sans-serif !important; }
        .stButton>button { border: 1px solid #e0e0e0; border-radius: 0.5rem; transition: all 0.2s; }
        .stButton>button:hover { border-color: #667eea; color: #667eea; }
    </style>
""", unsafe_allow_html=True)


# --- 데이터 관리를 위한 Session State ---
if 'job_values' not in st.session_state:
    st.session_state.job_values = {'경제적 보상': 5.0, '성취': 4.7, '직업안정': 4.6, '자기개발': 4.2, '일과 삶의 균형': 4.0, '자율성': 3.8, '변화지향': 3.2, '사회적 인정': 2.7, '사회적 공헌': 2.2}
if 'competency_values' not in st.session_state:
    st.session_state.competency_values = {'논리력': 95, '창의성': 90, '목표지향성': 85, '책임감': 80, '협업능력': 60, '감정적 안정성': 55}
if 'job_chart_type' not in st.session_state: st.session_state.job_chart_type = '레이더 차트'
if 'competency_chart_type' not in st.session_state: st.session_state.competency_chart_type = '레이더 차트'


# --- 이미지 파일을 Base64로 인코딩하는 함수 ---
def get_image_as_base64(path):
    if not os.path.exists(path):
        return None
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# --- 이미지 경로 및 Base64 인코딩 ---
image_path = "박민수 사진.jpg"
base64_image = get_image_as_base64(image_path)

if base64_image:
    image_html_tag = f'<img src="data:image/jpeg;base64,{base64_image}" alt="박민수 프로필 사진" style="width:100%; height:100%; object-fit:cover; border-radius:10px;">'
else:
    image_html_tag = '<i class="fas fa-user"></i>'

# --- 모든 슬라이드에 공통으로 주입할 커서 스타일 정의 ---
# !important 를 사용하여 다른 모든 스타일을 덮어쓰고 최우선으로 적용시킵니다.
CUSTOM_CURSOR_STYLE = """
<style>
    html, body, button, a, div, span, h1, h2, i, p, [class*="st-"], [style*="cursor"] {
        cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><circle cx="16" cy="16" r="12" fill="rgba(255, 0, 0, 0.7)" stroke="white" stroke-width="2"/></svg>') 16 16, auto !important;
    }
</style>
"""

# --- HTML 콘텐츠 정의 ---

# 1번 슬라이드 (홈)
home_slide_html = f"""
<!DOCTYPE html><html lang="ko"><head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>박민수의 프로필 발표</title>
    {CUSTOM_CURSOR_STYLE}
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    <style>
        body {{ margin: 0; padding: 0; font-family: 'Noto Sans KR', sans-serif; }}
        .slide-container {{ width: 100%; height: 100vh; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); position: relative; display: flex; align-items: center; justify-content: center; padding: 2rem; box-sizing: border-box; overflow: hidden; }}
        .floating-shapes {{ position: absolute; width: 100%; height: 100%; top: 0; left: 0; pointer-events: none; }}
        .shape {{ position: absolute; border-radius: 50%; background: rgba(255, 255, 255, 0.08); animation: float 8s ease-in-out infinite; }}
        .shape:nth-child(1) {{ width: 120px; height: 120px; top: 10%; left: 8%; animation-delay: 0s; }}
        .shape:nth-child(2) {{ width: 180px; height: 180px; top: 20%; right: 12%; animation-delay: 3s; }}
        .shape:nth-child(3) {{ width: 100px; height: 100px; bottom: 15%; left: 15%; animation-delay: 6s; }}
        .shape:nth-child(4) {{ width: 140px; height: 140px; bottom: 25%; right: 20%; animation-delay: 4s; }}
        @keyframes float {{ 0%, 100% {{ transform: translateY(0px) rotate(0deg); }} 50% {{ transform: translateY(-30px) rotate(180deg); }} }}
        .main-content {{
            background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(15px); border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 30px;
            padding: 4rem 3rem; text-align: center; box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
            transform: perspective(1000px) translateY(30px); opacity: 0; animation: slideUp 1s ease-out forwards;
            max-width: 800px; width: 100%; position: relative; z-index: 10;
            transform-style: preserve-3d;
        }}
        @keyframes slideUp {{ to {{ transform: perspective(1000px) translateY(0); opacity: 1; }} }}
        .main-title {{
            font-weight: 900; font-size: 5rem; background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
            margin-bottom: 2rem; line-height: 1.1; min-height: 7rem;
        }}
        .typed-cursor {{ font-size: 5rem; color: #764ba2; animation: blink 0.7s infinite; }}
        @keyframes blink {{ 50% {{ opacity: 0; }} }}
        .welcome-icon {{
            font-size: 8rem; background: linear-gradient(135deg, #ff9a9e, #fecfef); -webkit-background-clip: text;
            -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 2rem; opacity: 0;
            animation: bounceIn 1s ease-out 0.8s forwards; transform: translateZ(50px);
        }}
        @keyframes bounceIn {{ 0% {{ transform: scale(0); opacity: 0; }} 50% {{ transform: scale(1.1); opacity: 1; }} 100% {{ transform: scale(1); opacity: 1; }} }}
        .meme-gif-container {{ position: absolute; bottom: 20px; right: 20px; width: 200px; height: auto; z-index: 1000; border-radius: 15px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }}
    </style>
</head><body>
    <div class="slide-container">
        <div class="floating-shapes"> <div class="shape"></div><div class="shape"></div><div class="shape"></div><div class="shape"></div> </div>
        <div class="main-content" data-tilt data-tilt-max="10" data-tilt-speed="400" data-tilt-perspective="1000" data-tilt-glare="true" data-tilt-max-glare="0.5">
            <div class="welcome-icon"><i class="fas fa-user-graduate"></i></div>
            <h1 class="main-title"><span id="typed-title"></span></h1>
        </div>
        <div class="meme-gif-container"> <img src="https://media.tenor.com/M0b6-2420w0AAAAM/toothless-dancing-toothless.gif" alt="Toothless Dancing GIF"> </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>
    <script src="https://cdn.jsdelivr.net/npm/vanilla-tilt@1.7.2/dist/vanilla-tilt.min.js"></script>
    <script>
        VanillaTilt.init(document.querySelector(".main-content"));
        document.addEventListener('DOMContentLoaded', function() {{
            var options = {{
                strings: ['프로필 발표'],
                typeSpeed: 120,
                backSpeed: 50,
                startDelay: 900,
                showCursor: true,
                cursorChar: '_',
                loop: false
            }};
            var typed = new Typed('#typed-title', options);
        }});
    </script>
</body></html>
"""

# 2번 슬라이드 (기본 소개) - .format()을 사용하기 때문에 f-string이 아님
intro_slide_html_template = """
<!DOCTYPE html><html lang="ko"><head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>박민수 - 기본 소개</title>
    {cursor_style}
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    <style>
        body {{ margin: 0; padding: 0; font-family: 'Noto Sans KR', sans-serif; }}
        .slide-container {{ width: 100%; height: 100vh; display: flex; align-items: center; justify-content: center; position: relative; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; box-sizing: border-box; }}
        .main-title {{ color: #e9e7f5; font-weight: 700; font-size: 3.5rem; text-align: center; margin-bottom: 2rem; animation: titlePulse 5s ease-in-out infinite; text-shadow: 2px 2px 8px rgba(30, 27, 46, 0.5); }}
        .content-card {{ background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(15px); border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 20px; transform: translateY(30px); opacity: 0; animation: slideUp 0.8s ease-out forwards; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1); padding: 1.5rem; height: 100%; display: flex; flex-direction: column; justify-content: center;}}
        @keyframes slideUp {{ to {{ transform: translateY(0); opacity: 1; }} }}
        .profile-section {{ display: grid; grid-template-columns: 1.5fr 1fr; gap: 2rem; margin-bottom: 2rem; align-items: stretch;}}
        .bottom-section {{ display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }}
        .info-item, .education-item, .cert-badge, .hobby-badge {{ }}
        .info-item {{ display: flex; align-items: center; margin-bottom: 0.75rem; padding: 0.5rem 0.75rem; border-radius: 10px; transition: all 0.3s ease; background: rgba(102, 126, 234, 0.05); }}
        .info-item:last-child {{ margin-bottom: 0; }}
        .education-item:last-child {{ margin-bottom: 0; }}
        .info-icon {{ background: linear-gradient(135deg, #84fab0, #8fd3f4); color: #374151; width: 35px; height: 35px; border-radius: 8px; display: flex; align-items: center; justify-content: center; margin-right: 1rem; font-size: 0.9rem; flex-shrink: 0; }}
        .info-label {{ font-weight: 600; color: #6b7280; min-width: 80px; margin-right: 1rem; }}
        .info-value {{ color: #374151; font-weight: 500; }}
        .cert-badge {{ background: linear-gradient(135deg, #ff9a9e, #fecfef); color: #444; padding: 0.75rem 1.5rem; border-radius: 25px; font-weight: 600; margin: 0.5rem; display: inline-flex; align-items: center; box-shadow: 0 4px 15px rgba(255, 154, 158, 0.3); }}
        .hobby-badge {{ background: linear-gradient(135deg, #a8edea, #fed6e3); color: #374151; padding: 0.75rem 1.25rem; border-radius: 20px; font-weight: 600; margin: 0.5rem; display: inline-flex; align-items: center; box-shadow: 0 3px 12px rgba(168, 237, 234, 0.3); }}
        .education-item {{ background: rgba(132, 250, 176, 0.1); padding: 1rem; border-radius: 12px; border-left: 4px solid #84fab0; margin-bottom: 1rem; }}
        .school-name {{ font-weight: 700; color: #374151; margin-bottom: 0.25rem; }}
        .school-status {{ font-size: 0.9rem; color: #6b7280; }}
        .section-title {{ color: #4a5568; font-weight: 700; font-size: 1.25rem; margin-bottom: 1rem; display: flex; align-items: center; }}
        .icon-container {{ background: linear-gradient(135deg, #667eea, #764ba2); color: white; width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 0.75rem; }}
        @keyframes pop-in {{ 0% {{ transform: scale(0.95); }} 50% {{ transform: scale(1.05); }} 100% {{ transform: scale(1); }} }}
        .animate-pop {{ animation: pop-in 0.3s ease-out; }}
        .modal-overlay {{ display: none; position: fixed; z-index: 1001; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.85); align-items: center; justify-content: center; }}
        .modal-content {{ margin: auto; display: block; max-width: 80%; max-height: 80vh; animation: zoom 0.4s; }}
        @keyframes zoom {{ from {{ transform: scale(0.1); }} to {{ transform: scale(1); }} }}
        .modal-close-button {{ position: absolute; top: 20px; right: 35px; color: #f1f1f1; font-size: 40px; font-weight: bold; transition: 0.3s; }}
        .modal-close-button:hover {{ color: #bbb; }}
    </style>
</head><body>
    <div class="slide-container">
        <div class="relative z-10" style="width:100%; max-width: 1200px;">
            <h1 class="main-title" style="margin-bottom: 1rem;">기본 소개</h1>
            <div class="profile-section">
                <div class="content-card">
                    <h2 class="section-title"><div id="profile-pic-trigger" class="icon-container" style="padding:0;">{image_placeholder}</div>기본 정보</h2>
                    <div>
                        <div class="info-item anim-target"><div class="info-icon"><i class="fas fa-signature"></i></div><div class="info-label">이름</div><div class="info-value">박민수</div></div>
                        <div class="info-item anim-target"><div class="info-icon"><i class="fas fa-id-card"></i></div><div class="info-label">학번</div><div class="info-value">23683013</div></div>
                        <div class="info-item anim-target"><div class="info-icon"><i class="fas fa-map-marker-alt"></i></div><div class="info-label">출생지</div><div class="info-value">충청남도 공주시</div></div>
                    </div>
                </div>
                <div class="content-card">
                    <h2 class="section-title"><div class="icon-container"><i class="fas fa-graduation-cap"></i></div>학력</h2>
                    <div>
                        <div class="education-item anim-target"><div class="school-name">공주영명고등학교</div><div class="school-status">졸업</div></div>
                        <div class="education-item anim-target"><div class="school-name">건양대학교(논산)</div><div class="school-status">재학 중</div></div>
                    </div>
                </div>
            </div>
            <div class="bottom-section">
                <div class="content-card">
                    <h2 class="section-title"><div class="icon-container"><i class="fas fa-certificate"></i></div>자격증</h2>
                    <div class="text-center">
                        <div class="cert-badge anim-target"><i class="fas fa-award mr-2"></i>한국사능력검정시험 1급</div>
                        <div class="cert-badge anim-target"><i class="fas fa-fire mr-2"></i>위험물기능사</div>
                    </div>
                </div>
                <div class="content-card">
                    <h2 class="section-title"><div class="icon-container"><i class="fas fa-gamepad"></i></div>취미 & 여가생활</h2>
                    <div class="text-center">
                        <div class="hobby-badge anim-target"><i class="fas fa-film mr-2"></i>영화 감상</div>
                        <div class="hobby-badge anim-target"><i class="fas fa-palette mr-2"></i>그림 그리기</div>
                        <div class="hobby-badge anim-target"><i class="fas fa-mountain mr-2"></i>클라이밍</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div id="image-modal" class="modal-overlay">
      <span id="modal-close" class="modal-close-button">&times;</span>
      <img class="modal-content" id="modal-image">
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const targets = document.querySelectorAll('.anim-target');
            targets.forEach(target => {{
                target.addEventListener('click', (e) => {{
                    if (e.currentTarget.classList.contains('animate-pop')) {{
                        e.currentTarget.classList.remove('animate-pop');
                    }}
                    void e.currentTarget.offsetWidth;
                    e.currentTarget.classList.add('animate-pop');
                }});
            }});
            const modal = document.getElementById('image-modal');
            const trigger = document.getElementById('profile-pic-trigger');
            const modalImg = document.getElementById('modal-image');
            const closeBtn = document.getElementById('modal-close');
            if (trigger) {{
                const thumbnailImg = trigger.querySelector('img');
                if (thumbnailImg) {{
                    trigger.onclick = function() {{
                        if(modal && modalImg) {{
                            modal.style.display = "flex";
                            modalImg.src = thumbnailImg.src;
                        }}
                    }}
                }}
            }}
            if (closeBtn) {{
                closeBtn.onclick = function() {{
                    if(modal) modal.style.display = "none";
                }}
            }}
            if (modal) {{
                modal.addEventListener('click', function(event) {{
                   if (event.target == modal) {{
                       modal.style.display = "none";
                   }}
                }});
            }}
        }});
    </script>
</body></html>
"""
# .format() 함수에 값을 채워넣습니다.
intro_slide_html = intro_slide_html_template.format(
    cursor_style=CUSTOM_CURSOR_STYLE, 
    image_placeholder=image_html_tag
)


# 3번 슬라이드 (MBTI)
mbti_slide_body_html = f"""
<!DOCTYPE html><html lang="ko"><head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>박민수 - MBTI</title>
    {CUSTOM_CURSOR_STYLE}
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    <style>
        body {{ margin: 0; padding: 0; font-family: 'Noto Sans KR', sans-serif; }}
        .slide-container {{ width: 100%; height: 100vh; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); position: relative; padding: 2rem; box-sizing: border-box; display: flex; align-items: center; justify-content: center; }}
        .main-title {{ font-weight: 700; font-size: 4.5rem; text-align: center; margin-bottom: 1.5rem; color: white; text-shadow: 2px 2px 8px rgba(30, 27, 46, 0.5); }}
        .content-card {{ background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(15px); border-radius: 20px; display: flex; flex-direction: column; padding: 1.5rem; animation: slideUp 0.8s ease-out forwards; opacity: 0; transform: translateY(30px); }}
        @keyframes slideUp {{ to {{ transform: translateY(0); opacity: 1; }} }}
        .keyword-badge {{ background: linear-gradient(135deg, #ff9a9e, #fecfef); color: #444; padding: 0.75rem 1.5rem; border-radius: 25px; font-weight: 600; margin: 0.5rem; display: inline-flex; align-items: center; box-shadow: 0 4px 15px rgba(255, 154, 158, 0.3); }}
        .mbti-component {{ background: linear-gradient(135deg, #a8edea, #fed6e3); padding: 1rem; border-radius: 15px; text-align: center; box-shadow: 0 4px 15px rgba(168, 237, 234, 0.3); height:100%; transition: transform 0.2s ease-in-out; }}
        .mbti-component:hover {{ transform: translateY(-5px); }}
        .mbti-letter {{ font-size: 2.5rem; font-weight: 900; color: #4a5568; margin-bottom: 0.5rem; }}
        .comparison-table {{ background: rgba(255, 255, 255, 0.9); border-radius: 15px; overflow: hidden; height: 100%; }}
        .table-header {{ background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 1rem; font-weight: 700; text-align: center; }}
        .table-content {{ padding: 1.5rem; }}
        .strength-item, .development-item {{ display: flex; align-items: center; margin-bottom: 0.75rem; padding: 0.5rem; border-radius: 8px; }}
        .field-badge {{ background: linear-gradient(135deg, #84fab0, #8fd3f4); color: #444; padding: 0.75rem 1.25rem; border-radius: 20px; font-weight: 600; margin: 0.25rem; display: inline-block; box-shadow: 0 3px 12px rgba(132, 250, 176, 0.3); }}
        .section-title {{ color: #4a5568; font-weight: 700; font-size: 1.25rem; margin-bottom: 1rem; display: flex; align-items: center; }}
        .icon-container {{ background: linear-gradient(135deg, #667eea, #764ba2); color: white; width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 0.75rem; }}
        @keyframes wiggle {{ 0%, 100% {{ transform: rotate(-2deg); }} 50% {{ transform: rotate(2deg); }} }}
        .animate-wiggle {{ animation: wiggle 0.3s ease-in-out; }}
        .mbti-modal-overlay {{ display: none; position: fixed; z-index: 1001; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.6); align-items: center; justify-content: center; opacity: 0; transition: opacity 0.3s ease-in-out; }}
        .mbti-modal-overlay.show {{ display: flex; opacity: 1; }}
        .mbti-modal-content {{ background: white; padding: 2rem 2.5rem; border-radius: 20px; max-width: 500px; width: 90%; text-align: left; position: relative; box-shadow: 0 5px 20px rgba(0,0,0,0.2); transform: scale(0.9); transition: transform 0.3s ease-in-out; }}
        .mbti-modal-overlay.show .mbti-modal-content {{ transform: scale(1); }}
        .mbti-modal-close-button {{ position: absolute; top: 10px; right: 20px; color: #aaa; font-size: 30px; font-weight: bold; transition: color 0.2s; }}
        .mbti-modal-close-button:hover {{ color: #333; }}
        #mbti-modal-title {{ font-size: 1.75rem; font-weight: 700; color: #4a5568; margin-bottom: 1rem; }}
        #mbti-modal-description {{ font-size: 1rem; line-height: 1.7; color: #6b7280; }}
    </style>
</head><body>
    <div class="slide-container">
        <div class="relative z-10" style="width:100%; max-width: 1200px;">
            <h1 class="main-title">INTJ</h1>
            <div class="content-card p-6 mb-6">
                <h2 class="section-title"><div class="icon-container"><i class="fas fa-star"></i></div>핵심 키워드</h2>
                <div class="text-center">
                    <div class="keyword-badge anim-target"><i class="fas fa-lightbulb mr-2"></i>논리적</div><div class="keyword-badge anim-target"><i class="fas fa-chart-line mr-2"></i>전략적</div><div class="keyword-badge anim-target"><i class="fas fa-brain mr-2"></i>분석적</div><div class="keyword-badge anim-target"><i class="fas fa-bullseye mr-2"></i>목표지향적</div><div class="keyword-badge anim-target"><i class="fas fa-tools mr-2"></i>독창적</div>
                </div>
            </div>
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <div class="content-card p-6">
                    <h2 class="section-title"><div class="icon-container"><i class="fas fa-puzzle-piece"></i></div>구성요소</h2>
                    <div class="grid grid-cols-2 gap-3">
                        <div class="mbti-component" data-title="I : 내향형 (Introversion)" data-desc="에너지의 방향이 내면 세계를 향합니다. 주로 혼자 있는 시간을 통해 에너지를 얻으며, 소수의 사람들과 깊이 있는 관계를 맺는 것을 선호합니다.">
                            <div class="mbti-letter">I</div><div class="text-sm font-semibold">내향형</div>
                        </div>
                        <div class="mbti-component" data-title="N : 직관형 (iNtuition)" data-desc="오감보다 영감이나 육감을 통해 정보를 받아들입니다. 현재보다 미래의 가능성을 보고, 나무보다는 숲을 보는 경향이 있습니다.">
                            <div class="mbti-letter">N</div><div class="text-sm font-semibold">직관형</div>
                        </div>
                        <div class="mbti-component" data-title="T : 사고형 (Thinking)" data-desc="객관적인 사실과 논리를 바탕으로 결정을 내립니다. 원칙과 공정성을 중시하며, 감정보다는 이성적인 판단을 우선시합니다.">
                            <div class="mbti-letter">T</div><div class="text-sm font-semibold">사고형</div>
                        </div>
                        <div class="mbti-component" data-title="J : 판단형 (Judging)" data-desc="체계적이고 계획적인 생활을 선호합니다. 목표를 설정하고 달성하는 것을 중요하게 여기며, 빠르고 명확한 결론에 도달하고자 합니다.">
                            <div class="mbti-letter">J</div><div class="text-sm font-semibold">판단형</div>
                        </div>
                    </div>
                </div>
                <div class="content-card p-0">
                    <div class="comparison-table">
                        <div class="table-header"><i class="fas fa-balance-scale mr-2"></i>강점 & 발전영역</div>
                        <div class="table-content">
                            <div class="mb-4"><h4 class="font-bold text-green-600 mb-2"><i class="fas fa-thumbs-up mr-1"></i>주요 강점</h4><div class="strength-item"><i class="fas fa-check-circle text-green-500 mr-2"></i><span class="text-sm">높은 독립성</span></div><div class="strength-item"><i class="fas fa-check-circle text-green-500 mr-2"></i><span class="text-sm">분석적 사고</span></div><div class="strength-item"><i class="fas fa-check-circle text-green-500 mr-2"></i><span class="text-sm">문제 해결 능력</span></div></div>
                            <div><h4 class="font-bold text-orange-600 mb-2"><i class="fas fa-arrow-up mr-1"></i>발전 영역</h4><div class="development-item"><i class="fas fa-exclamation-triangle text-orange-500 mr-2"></i><span class="text-sm">감정 표현</span></div><div class="development-item"><i class="fas fa-exclamation-triangle text-orange-500 mr-2"></i><span class="text-sm">사회적 교류</span></div></div>
                        </div>
                    </div>
                </div>
                <div class="content-card p-6">
                    <h2 class="section-title"><div class="icon-container"><i class="fas fa-code"></i></div>적합한 개발 분야</h2>
                    <div class="text-center flex-grow flex flex-col justify-center">
                        <div class="field-badge">데이터 과학/AI</div><div class="field-badge">시스템 설계</div><div class="field-badge">백엔드 개발</div><div class="field-badge">알고리즘 최적화</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div id="mbti-modal" class="mbti-modal-overlay">
      <div class="mbti-modal-content">
        <span id="mbti-modal-close" class="mbti-modal-close-button">&times;</span>
        <h3 id="mbti-modal-title"></h3>
        <p id="mbti-modal-description"></p>
      </div>
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const wiggleTargets = document.querySelectorAll('.anim-target');
            wiggleTargets.forEach(target => {{
                target.addEventListener('click', (e) => {{
                    if (e.currentTarget.classList.contains('animate-wiggle')) {{
                        e.currentTarget.classList.remove('animate-wiggle');
                    }}
                    void e.currentTarget.offsetWidth;
                    e.currentTarget.classList.add('animate-wiggle');
                }});
            }});

            const mbtiComponents = document.querySelectorAll('.mbti-component');
            const mbtiModal = document.getElementById('mbti-modal');
            const mbtiModalTitle = document.getElementById('mbti-modal-title');
            const mbtiModalDesc = document.getElementById('mbti-modal-description');
            const mbtiModalClose = document.getElementById('mbti-modal-close');

            mbtiComponents.forEach(component => {{
                component.addEventListener('click', function(e) {{
                    e.stopPropagation();
                    const title = this.getAttribute('data-title');
                    const desc = this.getAttribute('data-desc');
                    
                    if (title && desc && mbtiModal) {{
                        mbtiModalTitle.innerText = title;
                        mbtiModalDesc.innerText = desc;
                        mbtiModal.style.display = 'flex';
                        setTimeout(() => {{
                            mbtiModal.classList.add('show');
                        }}, 10);
                    }}
                }});
            }});

            function closeMbtiModal() {{
                if (mbtiModal) {{
                    mbtiModal.classList.remove('show');
                    setTimeout(() => {{
                        mbtiModal.style.display = 'none';
                    }}, 300);
                }}
            }}

            if(mbtiModalClose) mbtiModalClose.addEventListener('click', closeMbtiModal);
            if(mbtiModal) mbtiModal.addEventListener('click', function(event) {{
                if (event.target === mbtiModal) {{
                    closeMbtiModal();
                }}
            }});
        }});
    </script>
</body></html>
"""

# 4번 슬라이드 (직업가치관)
job_values_html_template = f"""
<!DOCTYPE html><html lang="ko"><head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>직업가치관 검사</title>
    {CUSTOM_CURSOR_STYLE}
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{ margin: 0; padding: 0; font-family: 'Noto Sans KR', sans-serif; }}
        .slide-container {{ width: 100%; height: 100vh; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); position: relative; padding: 2rem; box-sizing: border-box; display: flex; align-items: center; justify-content: center; }}
        .main-title {{ color: #e9e7f5; font-weight: 700; font-size: 3rem; text-align: center; margin-bottom: 1.5rem; }}
        .content-card {{ background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(15px); border-radius: 20px; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1); animation: slideUp 0.8s ease-out forwards; opacity: 0; transform: translateY(30px); }}
        @keyframes slideUp {{ to {{ transform: translateY(0); opacity: 1; }} }}
        .main-grid {{ display: grid; grid-template-columns: 1.2fr 1fr; gap: 1.5rem; }}
        .chart-container {{ height: 350px; position: relative; padding: 1rem;}}
        .value-item {{ display: flex; align-items: center; justify-content: space-between; padding: 0.75rem; margin-bottom: 0.5rem; border-radius: 10px; font-size: 0.9rem; }}
        .top-value {{ background: linear-gradient(135deg, #10b981, #059669); color: white; }}
        .bottom-value {{ background: linear-gradient(135deg, #f59e0b, #d97706); color: white; }}
        .score-badge {{ background: rgba(255, 255, 255, 0.3); padding: 0.25rem 0.75rem; border-radius: 15px; font-weight: 700; font-size: 0.85rem; }}
        .job-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem; }}
        .job-badge {{ background: linear-gradient(135deg, #84fab0, #8fd3f4); color: #374151; padding: 0.5rem 0.75rem; border-radius: 15px; font-weight: 600; font-size: 0.8rem; text-align: center; box-shadow: 0 3px 12px rgba(132, 250, 176, 0.3); }}
        .insight-text {{ color: #4a5568; font-size: 1rem; line-height: 1.8; text-align:center; }}
        .highlight {{ background: linear-gradient(135deg, #ff9a9e, #fecfef); color: #444; padding: 0.25rem 0.5rem; border-radius: 8px; font-weight: 600; }}
        .section-title {{ color: #4a5568; font-weight: 700; font-size: 1.25rem; margin-bottom: 1rem; display: flex; align-items: center; }}
        .icon-container {{ background: linear-gradient(135deg, #667eea, #764ba2); color: white; width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 0.75rem; }}
    </style>
</head><body>
    <div class="slide-container">
        <div class="relative z-10" style="width:100%; max-width: 1200px;">
            <h1 class="main-title">직업가치관 검사 결과</h1>
            <div class="main-grid">
                <div class="content-card p-6"><h2 class="section-title"><div class="icon-container"><i class="fas fa-chart-pie"></i></div>가치관 분석 차트</h2><div class="chart-container">__CHART_AREA__</div></div>
                <div class="space-y-4">
                    <div class="content-card p-4"><h2 class="section-title"><div class="icon-container"><i class="fas fa-trophy"></i></div>상위 가치관</h2>__TOP_VALUES_HTML__</div>
                    <div class="content-card p-4"><h2 class="section-title"><div class="icon-container"><i class="fas fa-arrow-down"></i></div>하위 가치관</h2>__BOTTOM_VALUES_HTML__</div>
                </div>
            </div>
            <div class="content-card p-6 mt-6">
                <h2 class="section-title justify-center"><div class="icon-container"><i class="fas fa-briefcase"></i></div>추천 직업 분야</h2>
                <div class="job-grid mb-4">
                    <div class="job-badge"><i class="fas fa-shield-alt mr-1"></i>산업안전원</div><div class="job-badge"><i class="fas fa-flask mr-1"></i>자연과학연구원</div><div class="job-badge"><i class="fas fa-balance-scale mr-1"></i>법무사</div><div class="job-badge"><i class="fas fa-user-tie mr-1"></i>정부행정관리자</div><div class="job-badge"><i class="fas fa-microscope mr-1"></i>환경시험원</div><div class="job-badge"><i class="fas fa-map mr-1"></i>GIS전문가</div>
                </div>
                <div class="insight-text mt-4">
                    <p>
                        <span class="highlight">__INSIGHT_TEXT__</span>
                    </p>
                </div>
            </div>
        </div>
    </div>
</body></html>
"""

# 5번 슬라이드 (직무역량)
competency_html_template = f"""
<!DOCTYPE html><html lang="ko"><head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>직무역량 분석</title>
    {CUSTOM_CURSOR_STYLE}
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{ margin: 0; padding: 0; font-family: 'Noto Sans KR', sans-serif; }}
        .slide-container {{ width: 100%; height: 100vh; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); position: relative; padding: 2rem; box-sizing: border-box; display: flex; align-items: center; justify-content: center; }}
        .main-title {{ color: #e9e7f5; font-weight: 700; font-size: 3rem; text-align: center; margin-bottom: 1.5rem; }}
        .content-card {{ background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(15px); border-radius: 20px; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1); animation: slideUp 0.8s ease-out forwards; opacity: 0; transform: translateY(30px); }}
        @keyframes slideUp {{ to {{ transform: translateY(0); opacity: 1; }} }}
        .main-grid {{ display: grid; grid-template-columns: 1.2fr 1fr; gap: 1.5rem; }}
        .chart-container {{ height: 300px; position: relative; padding: 1rem;}}
        .competency-item {{ display: flex; align-items: center; margin-bottom: 0.75rem; padding: 0.75rem; border-radius: 10px; font-size: 0.9rem; color: white;}}
        .strength-item {{ background: linear-gradient(135deg, #10b981, #059669); }}
        .development-item {{ background: linear-gradient(135deg, #f59e0b, #d97706); }}
        .score-badge {{ background: rgba(255, 255, 255, 0.3); padding: 0.25rem 0.75rem; border-radius: 15px; font-weight: 700; font-size: 0.85rem; margin-left: auto; }}
        .insight-text {{ color: #4a5568; font-size: 1rem; line-height: 1.8; text-align:center;}}
        .highlight {{ background: linear-gradient(135deg, #ff9a9e, #fecfef); color: #444; padding: 0.25rem 0.5rem; border-radius: 8px; font-weight: 600; }}
        .competency-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 1rem; }}
        .competency-badge {{ background: linear-gradient(135deg, #84fab0, #8fd3f4); color: #374151; padding: 0.5rem 1rem; border-radius: 15px; font-weight: 600; font-size: 0.85rem; text-align: center; box-shadow: 0 3px 12px rgba(132, 250, 176, 0.3); }}
        .section-title {{ color: #4a5568; font-weight: 700; font-size: 1.25rem; margin-bottom: 1rem; display: flex; align-items: center; }}
        .icon-container {{ background: linear-gradient(135deg, #667eea, #764ba2); color: white; width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 0.75rem; }}
    </style>
</head><body>
    <div class="slide-container">
        <div class="relative z-10" style="width:100%; max-width: 1200px;">
            <h1 class="main-title">직무역량 분석</h1>
            <div class="main-grid">
                <div class="content-card p-6"><h2 class="section-title"><div class="icon-container"><i class="fas fa-chart-pie"></i></div>역량 분포 차트</h2><div class="chart-container">__CHART_AREA__</div></div>
                <div class="space-y-4">
                    <div class="content-card p-4"><h2 class="section-title"><div class="icon-container"><i class="fas fa-star"></i></div>핵심 강점</h2>__STRENGTHS_HTML__</div>
                    <div class="content-card p-4"><h2 class="section-title"><div class="icon-container"><i class="fas fa-arrow-up"></i></div>보완 영역</h2>__DEVELOPMENT_AREAS_HTML__</div>
                </div>
            </div>
            <div class="content-card p-6 mt-6">
                <h2 class="section-title justify-center"><div class="icon-container"><i class="fas fa-chart-line"></i></div>종합 분석 및 발전 방향</h2>
                <div class="competency-grid mb-4">
                    <div class="competency-badge"><i class="fas fa-cogs mr-2"></i>복잡한 문제 해결</div><div class="competency-badge"><i class="fas fa-project-diagram mr-2"></i>시스템적 사고</div><div class="competency-badge"><i class="fas fa-handshake mr-2"></i>소통 역량 개발</div><div class="competency-badge"><i class="fas fa-balance-scale mr-2"></i>감정 관리 기술</div>
                </div>
                <div class="insight-text mt-4">
                    <p>
                        <span class="highlight">__INSIGHT_TEXT__</span>
                    </p>
                </div>
            </div>
        </div>
    </div>
</body></html>
"""

# 6번 슬라이드 (지향점 및 목표)
vision_goal_slide_html = f"""
<!DOCTYPE html><html lang="ko"><head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>향후 계획 및 목표</title>
    {CUSTOM_CURSOR_STYLE}
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    <style>
        body {{ margin: 0; padding: 0; font-family: 'Noto Sans KR', sans-serif; }}
        .slide-container {{ width: 100%; height: 100vh; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); position: relative; padding: 2rem; box-sizing: border-box; display: flex; align-items: center; justify-content: center; }}
        .main-title {{ color: #e9e7f5; font-weight: 700; text-shadow: 2px 2px 8px rgba(30, 27, 46, 0.5); }}
        .content-card {{ background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(15px); border-radius: 20px; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1); animation: slideUp 0.8s ease-out forwards; opacity: 0; transform: translateY(30px); height: 100%; display: flex; flex-direction: column; }}
        @keyframes slideUp {{ to {{ transform: translateY(0); opacity: 1; }} }}
        .section-title {{ color: #4a5568; font-weight: 700; font-size: 1.5rem; margin-bottom: 1.5rem; display: flex; align-items: center; border-bottom: 2px solid #e0e0e0; padding-bottom: 0.75rem; }}
        .icon-container {{ background: linear-gradient(135deg, #667eea, #764ba2); color: white; min-width: 45px; height: 45px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-right: 1rem; font-size: 1.2rem; }}
        .cert-card {{ transition: transform 0.2s ease, box-shadow 0.2s ease; }}
        .cert-card:hover {{ transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }}
        .step {{ perspective: 1000px; padding-bottom: 1.5rem; }}
        .step-flipper {{ position: relative; width: 100%; height: 100%; transition: transform 0.6s; transform-style: preserve-3d; }}
        .step.flipped .step-flipper {{ transform: rotateY(180deg); }}
        .step-front, .step-back {{ position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; display: flex; flex-direction: column; justify-content: center; padding: 1.5rem; border-radius: 15px; }}
        .step-front {{ background: #f7f8fc; border: 1px solid #e2e8f0; }}
        .step-back {{ background: linear-gradient(135deg, #667eea, #764ba2); color: white; transform: rotateY(180deg); }}
        .step-title {{ font-weight: 700; font-size: 1.1rem; color: #4a5568; margin-bottom: 0.25rem; }}
        .step-content {{ font-size: 0.95rem; color: #6b7280; line-height: 1.6; }}
        .step-back .step-title {{ color: white; }}
        .step-back .step-content {{ color: #e9e7f5; font-size: 0.9rem; }}
        .step-back ul {{ list-style-type: '✔  '; padding-left: 1.2rem; }}
        .info-modal-overlay {{ display: none; position: fixed; z-index: 1001; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.6); align-items: center; justify-content: center; opacity: 0; transition: opacity 0.3s ease-in-out; }}
        .info-modal-overlay.show {{ display: flex; opacity: 1; }}
        .info-modal-content {{ background: white; padding: 2rem 2.5rem; border-radius: 20px; max-width: 500px; width: 90%; text-align: left; position: relative; box-shadow: 0 5px 20px rgba(0,0,0,0.2); transform: scale(0.9); transition: transform 0.3s ease-in-out; }}
        .info-modal-overlay.show .info-modal-content {{ transform: scale(1); }}
        .info-modal-close-button {{ position: absolute; top: 10px; right: 20px; color: #aaa; font-size: 30px; font-weight: bold; transition: color 0.2s; }}
        #info-modal-title {{ font-size: 1.75rem; font-weight: 700; color: #4a5568; margin-bottom: 1rem; }}
        #info-modal-description {{ font-size: 1rem; line-height: 1.7; color: #6b7280; }}
    </style>
</head><body>
    <div class="slide-container">
        <div class="relative z-10" style="width:100%; max-width: 1200px;">
            <h1 class="main-title text-center" style="font-size: 3.5rem; margin-bottom: 2rem;">향후 계획 및 목표</h1>
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                <div class="content-card p-8 justify-center">
                    <h2 class="section-title"><div class="icon-container"><i class="fas fa-gem"></i></div>핵심 자격증</h2>
                    <div class="space-y-4 pt-4">
                        <div class="cert-card p-4 bg-purple-50 rounded-lg text-lg font-semibold text-purple-800 shadow-sm" data-title="소방설비기사 (기계/전기)" data-desc="소방 시스템의 설계, 시공, 감리 등 실무의 핵심 자격증입니다. 소방 안전 전문가로 성장하기 위한 가장 중요한 첫걸음입니다.">
                            <i class="fas fa-fire-extinguisher mr-3"></i>소방설비기사 (기계/전기)
                        </div>
                        <div class="cert-card p-4 bg-yellow-50 rounded-lg text-lg font-semibold text-yellow-800 shadow-sm" data-title="산업안전기사" data-desc="소방 안전을 넘어, 건설 및 제조 현장의 전반적인 안전 관리 역량을 증명합니다. 종합적인 안전 컨설턴트가 되기 위한 필수 역량입니다.">
                            <i class="fas fa-hard-hat mr-3"></i>산업안전기사
                        </div>
                        <div class="cert-card p-4 bg-blue-50 rounded-lg text-lg font-semibold text-blue-800 shadow-sm" data-title="컴퓨터활용능력 1급" data-desc="모든 기술 분야의 기본 소양입니다. 각종 보고서 작성, 데이터 관리, 행정 처리 등 효율적인 업무 수행 능력을 뒷받침하여 전문성을 더욱 빛나게 합니다.">
                            <i class="fas fa-laptop-code mr-3"></i>컴퓨터활용능력 1급
                        </div>
                    </div>
                </div>
                <div class="content-card p-8 justify-center">
                    <h2 class="section-title"><div class="icon-container"><i class="fas fa-road"></i></div>성장의 3단계 로드맵</h2>
                    <div class="relative pt-4 space-y-4">
                        <div class="step" style="height: 110px;">
                            <div class="step-flipper">
                                <div class="step-front">
                                    <div class="step-title">Foundation: 실무 역량 기반 구축</div>
                                    <p class="step-content">소방 안전 분야 진출 후, 현장 경험을 통해 전문가의 기반을 다집니다.</p>
                                </div>
                                <div class="step-back">
                                    <div class="step-title">주요 실행 계획</div>
                                    <ul class="step-content"><li>소방 설비 점검 및 유지보수</li><li>기본 도면 해석 능력 배양</li><li>관련 법규 및 기술 기준 숙지</li></ul>
                                </div>
                            </div>
                        </div>
                        <div class="step" style="height: 110px;">
                            <div class="step-flipper">
                                <div class="step-front">
                                    <div class="step-title">Growth: 전문성 심화 및 확장</div>
                                    <p class="step-content">실무 경험 기반으로 역량을 고도화하고, 소방기술사로 전문성을 검증받습니다.</p>
                                </div>
                                <div class="step-back">
                                    <div class="step-title">주요 실행 계획</div>
                                    <ul class="step-content"><li>복합 건축물 시스템 분석</li><li>성능위주설계(PBD) 학습</li><li>기술사 스터디 그룹 참여</li></ul>
                                </div>
                            </div>
                        </div>
                         <div class="step" style="height: 110px;">
                            <div class="step-flipper">
                                <div class="step-front">
                                    <div class="step-title">Pinnacle: 기술 솔루션 전문가</div>
                                    <p class="step-content">이론과 실무를 통합하여, 복잡한 문제에 대한 최적의 해결책을 제시합니다.</p>
                                </div>
                                <div class="step-back">
                                    <div class="step-title">주요 실행 계획</div>
                                    <ul class="step-content"><li>고난도 시스템 컨설팅 수행</li><li>기술 논문 발표 및 세미나 참여</li><li>후배 양성을 위한 멘토링</li></ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div id="info-modal" class="info-modal-overlay">
      <div class="info-modal-content">
        <span id="info-modal-close" class="info-modal-close-button">&times;</span>
        <h3 id="info-modal-title"></h3>
        <p id="info-modal-description"></p>
      </div>
    </div>
    <script>
    document.addEventListener('DOMContentLoaded', function() {{
        const certCards = document.querySelectorAll('.cert-card');
        const infoModal = document.getElementById('info-modal');
        const infoModalTitle = document.getElementById('info-modal-title');
        const infoModalDesc = document.getElementById('info-modal-description');
        const infoModalClose = document.getElementById('info-modal-close');
        certCards.forEach(card => {{
            card.addEventListener('click', function() {{
                const title = this.getAttribute('data-title');
                const desc = this.getAttribute('data-desc');
                if (title && desc && infoModal) {{
                    infoModalTitle.innerText = title;
                    infoModalDesc.innerText = desc;
                    infoModal.classList.add('show');
                }}
            }});
        }});
        function closeInfoModal() {{
            if (infoModal) {{
                infoModal.classList.remove('show');
            }}
        }}
        if(infoModalClose) infoModalClose.addEventListener('click', closeInfoModal);
        if(infoModal) infoModal.addEventListener('click', function(event) {{
            if (event.target === infoModal) {{
                closeInfoModal();
            }}
        }});
        const steps = document.querySelectorAll('.step');
        steps.forEach(step => {{
            step.addEventListener('click', function() {{
                this.classList.toggle('flipped');
            }});
        }});
    }});
    </script>
</body></html>
"""


# --- 사이드바 및 페이지 렌더링 로직 ---

st.sidebar.title("📑 발표 목차")
page_options = ["🏠 홈", "1. 기본 소개", "2. 성격유형(MBTI)", "3. 직업가치관 검사", "4. 직무역량 분석", "5. 향후 계획 및 목표"]
selected_page = st.sidebar.radio("이동할 페이지를 선택하세요:", page_options)


if selected_page == "🏠 홈":
    components.html(home_slide_html, height=1050, scrolling=False)
elif selected_page == "1. 기본 소개":
    if not base64_image:
        st.warning(f"'{image_path}' 파일을 찾을 수 없습니다. 스크립트와 같은 폴더에 있는지 확인해주세요.")
    components.html(intro_slide_html, height=1050, scrolling=False)
elif selected_page == "2. 성격유형(MBTI)":
    components.html(mbti_slide_body_html, height=1050, scrolling=False)
elif selected_page == "3. 직업가치관 검사":
    with st.expander("📊 직업가치관 데이터 편집"):
        cols = st.columns(3)
        for i, (label, value) in enumerate(st.session_state.job_values.items()):
            with cols[i % 3]:
                st.session_state.job_values[label] = st.slider(label, 0.0, 5.0, value, 0.1, key=f"job_{label}")

    st.write("---")
    cols = st.columns(3)
    if cols[0].button("📊 레이더 차트", key="job_radar", use_container_width=True): st.session_state.job_chart_type = '레이더 차트'
    if cols[1].button("📊 막대 차트", key="job_bar", use_container_width=True): st.session_state.job_chart_type = '막대 차트'
    if cols[2].button("📝 데이터 표", key="job_table", use_container_width=True): st.session_state.job_chart_type = '데이터 표'
    
    values = st.session_state.job_values
    labels = list(values.keys())
    data_points = list(values.values())
    df = pd.DataFrame(list(values.items()), columns=['가치관', '점수'])
    top_3 = df.nlargest(3, '점수')
    bottom_3 = df.nsmallest(3, '점수').sort_values(by='점수', ascending=False)
    
    top_html = "".join([f'<div class="top-value value-item"><span><i class="fas fa-medal mr-2"></i>{row["가치관"]}</span><span class="score-badge">{row["점수"]:.1f}</span></div>' for _, row in top_3.iterrows()])
    bottom_html = "".join([f'<div class="bottom-value value-item"><span><i class="fas fa-hand-holding-heart mr-2"></i>{row["가치관"]}</span><span class="score-badge">{row["점수"]:.1f}</span></div>' for _, row in bottom_3.iterrows()])
    insight = f'{top_3.iloc[0]["가치관"]}, {top_3.iloc[1]["가치관"]} 등을 중시하며, 안정적인 환경을 선호합니다.'

    chart_area_html = ""
    chart_type = st.session_state.job_chart_type
    
    if chart_type == '레이더 차트':
        chart_script = """
            <canvas id="valueChart"></canvas>
            <script>
                if (window.myJobChart) { window.myJobChart.destroy(); }
                window.myJobChart = new Chart(document.getElementById('valueChart'), {
                    type: 'radar',
                    data: { labels: %s, datasets: [{ data: %s, backgroundColor: 'rgba(102, 126, 234, 0.2)', borderColor: 'rgba(102, 126, 234, 1)', borderWidth: 3, pointRadius: 5 }] },
                    options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { r: { beginAtZero: true, max: 5, pointLabels: { font: { size: 12 } } } } }
                });
            </script>
        """ % (json.dumps(labels), data_points)
        chart_area_html = chart_script
        
    elif chart_type == '막대 차트':
        chart_script = """
            <canvas id="valueChart"></canvas>
            <script>
                if (window.myJobChart) { window.myJobChart.destroy(); }
                window.myJobChart = new Chart(document.getElementById('valueChart'), {
                    type: 'bar',
                    data: { labels: %s, datasets: [{ data: %s, backgroundColor: 'rgba(102, 126, 234, 0.6)' }] },
                    options: { responsive: true, maintainAspectRatio: false, indexAxis: 'y', plugins: { legend: { display: false } }, scales: { x: { beginAtZero: true, max: 5 } } }
                });
            </script>
        """ % (json.dumps(labels), data_points)
        chart_area_html = chart_script

    elif chart_type == '데이터 표':
        table_html = '<div style="overflow-y:auto;height:350px;"><table class="w-full text-left"><thead><tr class="border-b"><th class="p-2">가치관</th><th class="p-2 text-right font-bold">점수</th></tr></thead><tbody>'
        table_html += "".join([f'<tr class="border-b"><td class="p-2">{k}</td><td class="p-2 text-right font-bold">{v:.1f}</td></tr>' for k, v in sorted(values.items(), key=lambda item: item[1], reverse=True)])
        table_html += '</tbody></table></div>'
        chart_area_html = table_html

    final_html = job_values_html_template.replace('__CHART_AREA__', chart_area_html).replace('__TOP_VALUES_HTML__', top_html).replace('__BOTTOM_VALUES_HTML__', bottom_html).replace('__INSIGHT_TEXT__', insight)
    components.html(final_html, height=1050, scrolling=False)

elif selected_page == "4. 직무역량 분석":
    with st.expander("📊 직무역량 데이터 편집"):
        cols = st.columns(2)
        all_items = list(st.session_state.competency_values.items())
        mid_index = (len(all_items) + 1) // 2
        with cols[0]:
            for label, value in all_items[:mid_index]:
                 st.session_state.competency_values[label] = st.slider(label, 0, 100, value, 1, key=f"comp_{label}")
        with cols[1]:
            for label, value in all_items[mid_index:]:
                st.session_state.competency_values[label] = st.slider(label, 0, 100, value, 1, key=f"comp_{label}")

    st.write("---")
    cols = st.columns(3)
    if cols[0].button("📊 레이더 차트", key="comp_radar", use_container_width=True): st.session_state.competency_chart_type = '레이더 차트'
    if cols[1].button("📊 막대 차트", key="comp_bar", use_container_width=True): st.session_state.competency_chart_type = '막대 차트'
    if cols[2].button("📝 데이터 표", key="comp_table", use_container_width=True): st.session_state.competency_chart_type = '데이터 표'

    values = st.session_state.competency_values
    labels = list(values.keys())
    data_points = list(values.values())
    df = pd.DataFrame(list(values.items()), columns=['역량', '점수'])
    strengths = df[df['점수'] >= 80]
    dev_areas = df[df['점수'] < 80].sort_values(by='점수', ascending=False)

    strengths_html = "".join([f'<div class="strength-item competency-item"><span><i class="fas fa-brain mr-2"></i>{row["역량"]}</span><span class="score-badge">{row["점수"]}</span></div>' for _, row in strengths.iterrows()])
    dev_areas_html = "".join([f'<div class="development-item competency-item"><span><i class="fas fa-users mr-2"></i>{row["역량"]}</span><span class="score-badge">{row["점수"]}</span></div>' for _, row in dev_areas.iterrows()])
    
    insight = "핵심 강점과 보완점을 파악하여 지속적으로 성장하는 개발자가 되겠습니다."
    if not strengths.empty and len(strengths) > 1 and not dev_areas.empty:
        insight = f'{strengths.iloc[0]["역량"]}, {strengths.iloc[1]["역량"]} 역량이 뛰어나며, {dev_areas.iloc[0]["역량"]} 역량을 보완하면 좋습니다.'
    elif not strengths.empty:
        insight = f'{strengths.iloc[0]["역량"]} 역량이 뛰어납니다.'
    
    chart_area_html = ""
    chart_type = st.session_state.competency_chart_type
    
    if chart_type == '레이더 차트':
        chart_script = """
            <canvas id="competencyChart"></canvas>
            <script>
                if (window.myCompChart) window.myCompChart.destroy();
                window.myCompChart = new Chart(document.getElementById('competencyChart'), {
                    type: 'radar', data: { labels: %s, datasets: [{ data: %s, backgroundColor:'rgba(255,154,158,0.2)', borderColor:'rgba(255,154,158,1)', borderWidth:3 }] },
                    options: { responsive: true, maintainAspectRatio: false, plugins: { legend:{display:false} }, scales: { r: { beginAtZero:true, max:100, pointLabels:{font:{size:12}} } } }
                });
            </script>
        """ % (json.dumps(labels), data_points)
        chart_area_html = chart_script
        
    elif chart_type == '막대 차트':
        chart_script = """
            <canvas id="competencyChart"></canvas>
            <script>
                if (window.myCompChart) window.myCompChart.destroy();
                window.myCompChart = new Chart(document.getElementById('competencyChart'), {
                    type: 'bar', data: { labels: %s, datasets: [{ data: %s, backgroundColor:'rgba(255,154,158,0.6)' }] },
                    options: { responsive: true, maintainAspectRatio: false, plugins: { legend:{display:false} }, scales: { y: { beginAtZero:true, max:100 } } }
                });
            </script>
        """ % (json.dumps(labels), data_points)
        chart_area_html = chart_script

    elif chart_type == '데이터 표':
        table_html = '<div style="overflow-y:auto;height:300px;"><table class="w-full text-left"><thead><tr class="border-b"><th class="p-2">역량</th><th class="p-2 text-right font-bold">점수</th></tr></thead><tbody>'
        table_html += "".join([f'<tr class="border-b"><td class="p-2">{k}</td><td class="p-2 text-right font-bold">{v}</td></tr>' for k, v in sorted(values.items(), key=lambda item: item[1], reverse=True)])
        table_html += '</tbody></table></div>'
        chart_area_html = table_html

    final_html = competency_html_template.replace('__CHART_AREA__', chart_area_html).replace('__STRENGTHS_HTML__', strengths_html).replace('__DEVELOPMENT_AREAS_HTML__', dev_areas_html).replace('__INSIGHT_TEXT__', insight)
    components.html(final_html, height=1050, scrolling=False)

elif selected_page == "5. 향후 계획 및 목표":
    components.html(vision_goal_slide_html, height=1050, scrolling=False)