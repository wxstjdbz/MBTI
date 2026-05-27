import streamlit as st

# -----------------------------
# 페이지 기본 설정
# -----------------------------
st.set_page_config(
    page_title="MBTI 코디 추천",
    page_icon="👗",
    layout="centered"
)

# -----------------------------
# CSS 스타일
# -----------------------------
st.markdown(
    """
    <style>
    .main {
        background-color: #fffafc;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #ff6f91;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #777;
        margin-bottom: 30px;
    }

    .mbti-box {
        background: linear-gradient(135deg, #fff0f5, #f0f8ff);
        padding: 25px;
        border-radius: 25px;
        box-shadow: 0 8px 20px rgba(255, 182, 193, 0.25);
        margin-bottom: 25px;
        text-align: center;
    }

    .card {
        background-color: white;
        padding: 25px;
        border-radius: 22px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        margin-top: 20px;
        border: 2px solid #ffe4ec;
    }

    .card-title {
        font-size: 24px;
        font-weight: 700;
        color: #ff6f91;
        margin-bottom: 15px;
    }

    .item {
        font-size: 17px;
        line-height: 1.8;
        color: #444;
    }

    .tag {
        display: inline-block;
        background-color: #ffe4ec;
        color: #ff4f7b;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 14px;
        margin: 4px;
    }

    .footer {
        text-align: center;
        color: #999;
        font-size: 14px;
        margin-top: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# MBTI별 코디 데이터
# -----------------------------
outfits = {
    "ISTJ": {
        "mood": "단정하고 믿음직한 클래식 무드 📚",
        "tags": ["깔끔함", "클래식", "실용적"],
        "male": {
            "title": "차분한 클래식 댄디룩",
            "items": [
                "네이비 싱글 블레이저",
                "화이트 셔츠",
                "슬림한 베이지 치노 팬츠",
                "브라운 로퍼",
                "가죽 시계"
            ],
            "tip": "전체적으로 단정한 색 조합을 쓰면 ISTJ의 신뢰감 있는 분위기가 잘 살아나요."
        },
        "female": {
            "title": "깔끔한 오피스 캐주얼룩",
            "items": [
                "아이보리 블라우스",
                "네이비 니트 가디건",
                "H라인 베이지 스커트",
                "브라운 플랫슈즈",
                "심플한 토트백"
            ],
            "tip": "과한 장식보다 핏과 소재가 깔끔한 옷을 고르면 좋아요."
        }
    },
    "ISFJ": {
        "mood": "따뜻하고 부드러운 포근 무드 🧸",
        "tags": ["포근함", "러블리", "차분함"],
        "male": {
            "title": "부드러운 니트 캐주얼룩",
            "items": [
                "크림색 라운드 니트",
                "연청 데님 팬츠",
                "베이지 코트",
                "화이트 스니커즈",
                "캔버스 에코백"
            ],
            "tip": "따뜻한 색감을 활용하면 다정한 이미지가 더 잘 표현돼요."
        },
        "female": {
            "title": "포근한 데이트 캐주얼룩",
            "items": [
                "파스텔 핑크 니트",
                "아이보리 플리츠 스커트",
                "숏 무스탕 재킷",
                "메리제인 슈즈",
                "작은 크로스백"
            ],
            "tip": "파스텔톤과 부드러운 소재를 조합하면 사랑스러운 분위기가 나요."
        }
    },
    "INFJ": {
        "mood": "신비롭고 감성적인 무드 🌙",
        "tags": ["감성적", "몽환적", "우아함"],
        "male": {
            "title": "감성적인 미니멀 모노톤룩",
            "items": [
                "차콜 터틀넥",
                "블랙 와이드 슬랙스",
                "롱 코트",
                "첼시 부츠",
                "실버 목걸이"
            ],
            "tip": "어두운 톤에 포인트 액세서리를 더하면 분위기 있는 스타일이 완성돼요."
        },
        "female": {
            "title": "몽환적인 시크 페미닌룩",
            "items": [
                "블랙 시스루 블라우스",
                "롱 플레어 스커트",
                "그레이 롱 코트",
                "앵클부츠",
                "진주 귀걸이"
            ],
            "tip": "블랙, 그레이, 딥퍼플 같은 색을 활용하면 INFJ 특유의 신비로움이 살아나요."
        }
    },
    "INTJ": {
        "mood": "지적이고 세련된 시크 무드 🖤",
        "tags": ["시크함", "미니멀", "도시적"],
        "male": {
            "title": "블랙 미니멀 시티룩",
            "items": [
                "블랙 셔츠",
                "그레이 슬랙스",
                "블랙 싱글 코트",
                "더비 슈즈",
                "메탈 프레임 안경"
            ],
            "tip": "컬러를 절제하고 실루엣을 깔끔하게 잡으면 지적인 느낌이 강해져요."
        },
        "female": {
            "title": "세련된 모던 시크룩",
            "items": [
                "블랙 터틀넥",
                "화이트 와이드 팬츠",
                "블랙 재킷",
                "스틸레토 힐",
                "미니멀 숄더백"
            ],
            "tip": "대비가 강한 블랙 앤 화이트 조합이 INTJ의 선명한 이미지를 잘 보여줘요."
        }
    },
    "ISTP": {
        "mood": "쿨하고 자유로운 스트릿 무드 🛹",
        "tags": ["쿨함", "실용적", "스트릿"],
        "male": {
            "title": "편한데 멋있는 스트릿룩",
            "items": [
                "오버핏 후드티",
                "카고 팬츠",
                "블랙 항공점퍼",
                "하이탑 스니커즈",
                "볼캡"
            ],
            "tip": "활동성 좋은 아이템을 중심으로 고르면 ISTP다운 쿨함이 살아나요."
        },
        "female": {
            "title": "힙한 캐주얼 스트릿룩",
            "items": [
                "크롭 맨투맨",
                "와이드 카고 팬츠",
                "레더 재킷",
                "청키 스니커즈",
                "미니 백팩"
            ],
            "tip": "편안한 핏에 강한 소재를 섞으면 멋있고 자유로운 느낌이 나요."
        }
    },
    "ISFP": {
        "mood": "감각적이고 자연스러운 아트 무드 🎨",
        "tags": ["감각적", "내추럴", "개성"],
        "male": {
            "title": "내추럴 아티스트룩",
            "items": [
                "린넨 셔츠",
                "와이드 데님 팬츠",
                "카키 야상 재킷",
                "캔버스 스니커즈",
                "비니"
            ],
            "tip": "자연스러운 소재와 편안한 핏을 선택하면 감각적인 분위기가 나요."
        },
        "female": {
            "title": "빈티지 감성 아트룩",
            "items": [
                "플라워 패턴 블라우스",
                "롱 데님 스커트",
                "니트 베스트",
                "스웨이드 로퍼",
                "라탄백"
            ],
            "tip": "패턴 하나를 포인트로 두면 ISFP다운 예술적인 감성이 돋보여요."
        }
    },
    "INFP": {
        "mood": "몽글몽글 감성적인 로맨틱 무드 ☁️",
        "tags": ["감성", "로맨틱", "빈티지"],
        "male": {
            "title": "부드러운 빈티지 감성룩",
            "items": [
                "오트밀 니트",
                "브라운 코듀로이 팬츠",
                "체크 셔츠",
                "스웨이드 로퍼",
                "캔버스백"
            ],
            "tip": "따뜻한 브라운 계열을 활용하면 INFP의 부드러운 감성이 잘 드러나요."
        },
        "female": {
            "title": "동화 같은 로맨틱룩",
            "items": [
                "레이스 블라우스",
                "크림색 롱 스커트",
                "베이지 니트 가디건",
                "메리제인 슈즈",
                "리본 헤어핀"
            ],
            "tip": "레이스, 리본, 니트처럼 섬세한 디테일을 활용하면 좋아요."
        }
    },
    "INTP": {
        "mood": "편안하고 지적인 너드 시크 무드 💻",
        "tags": ["편안함", "너드미", "미니멀"],
        "male": {
            "title": "너드미 있는 편안한 캐주얼룩",
            "items": [
                "그래픽 티셔츠",
                "체크 셔츠",
                "블랙 와이드 팬츠",
                "컨버스 스니커즈",
                "동그란 안경"
            ],
            "tip": "꾸민 듯 안 꾸민 듯한 편안함이 INTP와 잘 어울려요."
        },
        "female": {
            "title": "편안한 북카페 감성룩",
            "items": [
                "루즈핏 니트",
                "와이드 데님",
                "체크 재킷",
                "스니커즈",
                "큰 에코백"
            ],
            "tip": "여유로운 실루엣과 체크 패턴을 활용하면 지적인 분위기가 나요."
        }
    },
    "ESTP": {
        "mood": "에너지 넘치는 스포티 무드 ⚡",
        "tags": ["활동적", "화려함", "스포티"],
        "male": {
            "title": "눈에 띄는 스포티 스트릿룩",
            "items": [
                "컬러 포인트 바람막이",
                "조거 팬츠",
                "화이트 티셔츠",
                "러닝화",
                "스포츠 시계"
            ],
            "tip": "강한 컬러 포인트를 하나 넣으면 ESTP의 에너지가 잘 보여요."
        },
        "female": {
            "title": "상큼한 애슬레저룩",
            "items": [
                "크롭 집업",
                "하이웨스트 조거 팬츠",
                "볼드한 스니커즈",
                "캡 모자",
                "미니 크로스백"
            ],
            "tip": "스포티한 아이템에 밝은 색을 더하면 활발한 느낌이 살아나요."
        }
    },
    "ESFP": {
        "mood": "화사하고 사랑스러운 파티 무드 🎉",
        "tags": ["화려함", "러블리", "트렌디"],
        "male": {
            "title": "트렌디한 컬러 포인트룩",
            "items": [
                "비비드 컬러 니트",
                "블랙 데님 팬츠",
                "화이트 스니커즈",
                "데님 재킷",
                "실버 액세서리"
            ],
            "tip": "밝은 색 포인트를 활용하면 ESFP의 밝은 매력이 돋보여요."
        },
        "female": {
            "title": "러블리 트렌디 데이트룩",
            "items": [
                "퍼프소매 블라우스",
                "미니 스커트",
                "컬러 가디건",
                "롱부츠",
                "하트 귀걸이"
            ],
            "tip": "귀여운 디테일과 트렌디한 아이템을 함께 쓰면 좋아요."
        }
    },
    "ENFP": {
        "mood": "톡톡 튀는 자유로운 컬러풀 무드 🌈",
        "tags": ["자유로움", "컬러풀", "개성"],
        "male": {
            "title": "개성 가득 컬러 믹스룩",
            "items": [
                "컬러풀 스트라이프 니트",
                "연청 와이드 데님",
                "스니커즈",
                "비니",
                "패턴 양말"
            ],
            "tip": "색과 패턴을 너무 두려워하지 말고 즐겁게 섞어보세요."
        },
        "female": {
            "title": "상큼한 키치 캐주얼룩",
            "items": [
                "그래픽 티셔츠",
                "컬러 플리츠 스커트",
                "오버핏 가디건",
                "플랫폼 스니커즈",
                "키링 달린 미니백"
            ],
            "tip": "귀여운 소품을 더하면 ENFP다운 발랄함이 잘 살아나요."
        }
    },
    "ENTP": {
        "mood": "재치 있고 힙한 믹스매치 무드 🧩",
        "tags": ["힙함", "실험적", "유니크"],
        "male": {
            "title": "센스 있는 믹스매치룩",
            "items": [
                "프린팅 셔츠",
                "와이드 슬랙스",
                "레더 재킷",
                "독특한 스니커즈",
                "체인 팔찌"
            ],
            "tip": "평범한 조합보다 의외의 아이템을 섞으면 ENTP다운 매력이 나요."
        },
        "female": {
            "title": "유니크한 하이틴 시크룩",
            "items": [
                "크롭 셔츠",
                "체크 미니 스커트",
                "오버핏 재킷",
                "워커 부츠",
                "볼드한 선글라스"
            ],
            "tip": "강한 아이템을 하나 정하고 나머지를 균형 있게 맞추면 좋아요."
        }
    },
    "ESTJ": {
        "mood": "당당하고 정돈된 리더 무드 👔",
        "tags": ["단정함", "포멀", "당당함"],
        "male": {
            "title": "깔끔한 비즈니스 캐주얼룩",
            "items": [
                "화이트 셔츠",
                "그레이 블레이저",
                "네이비 슬랙스",
                "블랙 로퍼",
                "브리프 케이스"
            ],
            "tip": "정돈된 핏과 차분한 색을 선택하면 리더십 있는 분위기가 나요."
        },
        "female": {
            "title": "당당한 포멀 페미닌룩",
            "items": [
                "새틴 블라우스",
                "블랙 테일러드 재킷",
                "슬랙스",
                "포인티드 토 슈즈",
                "스퀘어 숄더백"
            ],
            "tip": "각 잡힌 재킷과 깔끔한 가방이 ESTJ의 당당함을 잘 표현해요."
        }
    },
    "ESFJ": {
        "mood": "밝고 호감 가는 단정 러블리 무드 🌷",
        "tags": ["호감형", "단정함", "러블리"],
        "male": {
            "title": "호감형 캠퍼스룩",
            "items": [
                "스트라이프 셔츠",
                "니트 베스트",
                "크림 치노 팬츠",
                "화이트 스니커즈",
                "깔끔한 백팩"
            ],
            "tip": "밝고 단정한 조합이 ESFJ의 친근한 매력을 살려줘요."
        },
        "female": {
            "title": "화사한 러블리 캐주얼룩",
            "items": [
                "파스텔 블라우스",
                "A라인 스커트",
                "트위드 재킷",
                "플랫슈즈",
                "미니 숄더백"
            ],
            "tip": "화사한 색과 단정한 실루엣을 조합하면 호감도가 올라가요."
        }
    },
    "ENFJ": {
        "mood": "따뜻하고 세련된 주인공 무드 ✨",
        "tags": ["세련됨", "따뜻함", "우아함"],
        "male": {
            "title": "따뜻한 세미 포멀룩",
            "items": [
                "베이지 니트",
                "브라운 블레이저",
                "아이보리 슬랙스",
                "로퍼",
                "가죽 벨트"
            ],
            "tip": "부드러운 색감에 포멀한 아이템을 더하면 신뢰감과 따뜻함이 함께 보여요."
        },
        "female": {
            "title": "우아한 주인공룩",
            "items": [
                "랩 원피스",
                "롱 코트",
                "앵클부츠",
                "진주 목걸이",
                "토트백"
            ],
            "tip": "우아한 실루엣과 따뜻한 색을 사용하면 ENFJ의 매력이 돋보여요."
        }
    },
    "ENTJ": {
        "mood": "카리스마 있고 고급스러운 파워 무드 🦁",
        "tags": ["카리스마", "럭셔리", "시크"],
        "male": {
            "title": "카리스마 있는 파워 수트룩",
            "items": [
                "블랙 터틀넥",
                "차콜 수트 셋업",
                "블랙 더비 슈즈",
                "고급스러운 시계",
                "레더 브리프백"
            ],
            "tip": "강한 실루엣과 어두운 색을 사용하면 ENTJ다운 카리스마가 살아나요."
        },
        "female": {
            "title": "시크한 파워 드레싱룩",
            "items": [
                "화이트 셔츠",
                "블랙 와이드 슬랙스",
                "오버핏 테일러드 재킷",
                "스틸레토 힐",
                "골드 이어링"
            ],
            "tip": "클래식한 아이템에 골드 포인트를 더하면 고급스러운 느낌이 나요."
        }
    }
}

# -----------------------------
# 화면 제목
# -----------------------------
st.markdown('<div class="title">MBTI 코디 추천기 👗👕</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">MBTI를 선택하면 어울리는 남자 코디와 여자 코디를 추천해줄게요 ✨</div>',
    unsafe_allow_html=True
)

# -----------------------------
# MBTI 선택
# -----------------------------
mbti_list = list(outfits.keys())

st.markdown('<div class="mbti-box">', unsafe_allow_html=True)
selected_mbti = st.selectbox(
    "당신의 MBTI를 선택해 주세요 💌",
    mbti_list,
    index=0
)
st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# 결과 출력
# -----------------------------
data = outfits[selected_mbti]

st.markdown(f"## {selected_mbti} 추천 스타일 💖")
st.info(data["mood"])

tag_html = "".join([f'<span class="tag">#{tag}</span>' for tag in data["tags"]])
st.markdown(tag_html, unsafe_allow_html=True)

# 남자 코디 카드
male = data["male"]
male_items = "".join([f"👕 {item}<br>" for item in male["items"]])

st.markdown(
    f"""
    <div class="card">
        <div class="card-title">🧑 남자 코디 추천</div>
        <div class="item">
            <b>스타일:</b> {male["title"]}<br><br>
            {male_items}
            <br>
            <b>💡 스타일 팁:</b> {male["tip"]}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# 여자 코디 카드
female = data["female"]
female_items = "".join([f"👗 {item}<br>" for item in female["items"]])

st.markdown(
    f"""
    <div class="card">
        <div class="card-title">👩 여자 코디 추천</div>
        <div class="item">
            <b>스타일:</b> {female["title"]}<br><br>
            {female_items}
            <br>
            <b>💡 스타일 팁:</b> {female["tip"]}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# 추가 안내
# -----------------------------
st.markdown("---")

with st.expander("🌟 이 웹앱 활용 팁 보기"):
    st.write("MBTI는 재미로 참고하고, 실제 코디는 자신의 취향과 상황에 맞게 바꾸면 좋아요!")
    st.write("예를 들어 학교, 데이트, 여행, 발표 등 상황에 따라 신발이나 아우터만 바꿔도 분위기가 달라져요.")

st.markdown(
    """
    <div class="footer">
        Made with Streamlit 💗 | MBTI 코디 추천은 재미용이에요 🌈
    </div>
    """,
    unsafe_allow_html=True
)
