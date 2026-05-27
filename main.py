import streamlit as st
from urllib.parse import quote

# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="MBTI 코디 추천기",
    page_icon="👗",
    layout="centered"
)

# =========================================================
# CSS 스타일
# =========================================================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff7fb 0%, #f4fbff 100%);
    }

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 900;
        color: #ff6f91;
        margin-top: 20px;
        margin-bottom: 8px;
    }

    .sub-title {
        text-align: center;
        font-size: 17px;
        color: #666;
        margin-bottom: 30px;
        line-height: 1.6;
    }

    .cute-box {
        background-color: rgba(255, 255, 255, 0.92);
        padding: 24px;
        border-radius: 24px;
        box-shadow: 0 8px 24px rgba(255, 150, 180, 0.18);
        border: 1px solid #ffe1ec;
        margin-bottom: 24px;
    }

    .personality-line {
        background-color: #fff0f6;
        color: #555;
        padding: 13px 16px;
        border-radius: 16px;
        border: 1px solid #ffd6e5;
        font-size: 15.5px;
        line-height: 1.6;
        margin-top: 14px;
    }

    .mbti-badge {
        display: inline-block;
        background: linear-gradient(135deg, #ff8fab, #ffc2d1);
        color: white;
        padding: 8px 18px;
        border-radius: 999px;
        font-size: 22px;
        font-weight: 900;
        margin-bottom: 10px;
    }

    .mood-text {
        color: #555;
        font-size: 18px;
        line-height: 1.7;
    }

    .tag {
        display: inline-block;
        background-color: #fff0f6;
        color: #ff5c8a;
        padding: 7px 13px;
        border-radius: 999px;
        font-size: 14px;
        margin-right: 6px;
        margin-top: 8px;
        border: 1px solid #ffd6e5;
    }

    .card {
        background-color: white;
        padding: 24px;
        border-radius: 24px;
        box-shadow: 0 8px 22px rgba(0, 0, 0, 0.07);
        border: 1px solid #ffe1ec;
        margin-bottom: 22px;
    }

    .card-title {
        font-size: 25px;
        font-weight: 850;
        color: #ff6f91;
        margin-bottom: 12px;
    }

    .outfit-name {
        font-size: 21px;
        font-weight: 800;
        color: #333;
        margin-bottom: 12px;
    }

    .item-list {
        font-size: 16px;
        line-height: 1.9;
        color: #444;
    }

    .tip-box {
        background-color: #fff7fb;
        padding: 15px;
        border-radius: 16px;
        border-left: 5px solid #ff9eb5;
        color: #555;
        margin-top: 14px;
        margin-bottom: 16px;
        font-size: 15px;
        line-height: 1.7;
    }

    .footer {
        text-align: center;
        color: #999;
        font-size: 14px;
        margin-top: 45px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# MBTI별 코디 데이터
# =========================================================
outfits = {
    "ISTJ": {
        "emoji": "📚",
        "personality": "책임감이 강하고 계획적이며, 안정적이고 실용적인 선택을 좋아하는 타입이에요.",
        "mood": "단정하고 믿음직한 클래식 무드",
        "tags": ["깔끔함", "클래식", "실용적"],
        "male": {
            "title": "차분한 클래식 댄디룩",
            "items": ["네이비 싱글 블레이저", "화이트 셔츠", "베이지 치노 팬츠", "브라운 로퍼", "가죽 시계"],
            "tip": "네이비, 화이트, 베이지처럼 안정적인 색을 쓰면 신뢰감 있는 분위기가 잘 살아나요.",
            "query": "남자 네이비 블레이저 화이트 셔츠 베이지 치노팬츠 댄디룩 코디"
        },
        "female": {
            "title": "깔끔한 오피스 캐주얼룩",
            "items": ["아이보리 블라우스", "네이비 니트 가디건", "베이지 H라인 스커트", "브라운 플랫슈즈", "심플 토트백"],
            "tip": "과한 장식보다 핏과 소재가 깔끔한 옷을 고르면 차분한 매력이 잘 보여요.",
            "query": "여자 아이보리 블라우스 네이비 가디건 베이지 스커트 오피스 캐주얼 코디"
        }
    },
    "ISFJ": {
        "emoji": "🧸",
        "personality": "다정하고 배려심이 깊으며, 주변 사람을 편안하게 해주는 따뜻한 타입이에요.",
        "mood": "따뜻하고 부드러운 포근 무드",
        "tags": ["포근함", "러블리", "차분함"],
        "male": {
            "title": "부드러운 니트 캐주얼룩",
            "items": ["크림색 라운드 니트", "연청 데님 팬츠", "베이지 코트", "화이트 스니커즈", "캔버스 에코백"],
            "tip": "따뜻한 색감과 부드러운 소재를 쓰면 다정한 이미지가 더 잘 살아나요.",
            "query": "남자 크림 니트 연청 데님 베이지 코트 캐주얼 코디"
        },
        "female": {
            "title": "포근한 데이트 캐주얼룩",
            "items": ["파스텔 핑크 니트", "아이보리 플리츠 스커트", "숏 무스탕 재킷", "메리제인 슈즈", "미니 크로스백"],
            "tip": "파스텔톤과 폭신한 소재를 조합하면 사랑스럽고 편안한 느낌이 나요.",
            "query": "여자 파스텔 핑크 니트 아이보리 플리츠 스커트 데이트룩 코디"
        }
    },
    "INFJ": {
        "emoji": "🌙",
        "personality": "깊이 있는 생각과 섬세한 감성을 가진, 조용하지만 신념이 뚜렷한 타입이에요.",
        "mood": "신비롭고 감성적인 무드",
        "tags": ["감성적", "몽환적", "우아함"],
        "male": {
            "title": "감성적인 미니멀 모노톤룩",
            "items": ["차콜 터틀넥", "블랙 와이드 슬랙스", "롱 코트", "첼시 부츠", "실버 목걸이"],
            "tip": "어두운 톤에 작은 실버 포인트를 더하면 분위기 있는 스타일이 완성돼요.",
            "query": "남자 차콜 터틀넥 블랙 슬랙스 롱코트 미니멀 코디"
        },
        "female": {
            "title": "몽환적인 시크 페미닌룩",
            "items": ["블랙 블라우스", "롱 플레어 스커트", "그레이 롱 코트", "앵클부츠", "진주 귀걸이"],
            "tip": "블랙, 그레이, 딥퍼플 계열을 활용하면 신비로운 분위기가 살아나요.",
            "query": "여자 블랙 블라우스 롱 플레어 스커트 그레이 코트 시크 코디"
        }
    },
    "INTJ": {
        "emoji": "🖤",
        "personality": "분석적이고 독립적이며, 목표를 향해 체계적으로 움직이는 전략가 타입이에요.",
        "mood": "지적이고 세련된 시크 무드",
        "tags": ["시크함", "미니멀", "도시적"],
        "male": {
            "title": "블랙 미니멀 시티룩",
            "items": ["블랙 셔츠", "그레이 슬랙스", "블랙 싱글 코트", "더비 슈즈", "메탈 프레임 안경"],
            "tip": "컬러를 절제하고 실루엣을 깔끔하게 잡으면 지적인 느낌이 강해져요.",
            "query": "남자 블랙 셔츠 그레이 슬랙스 블랙 코트 미니멀룩 코디"
        },
        "female": {
            "title": "세련된 모던 시크룩",
            "items": ["블랙 터틀넥", "화이트 와이드 팬츠", "블랙 재킷", "스틸레토 슈즈", "미니멀 숄더백"],
            "tip": "블랙 앤 화이트 조합은 선명하고 세련된 이미지를 잘 보여줘요.",
            "query": "여자 블랙 터틀넥 화이트 와이드 팬츠 블랙 재킷 시크룩 코디"
        }
    },
    "ISTP": {
        "emoji": "🛹",
        "personality": "쿨하고 현실적이며, 직접 경험하면서 문제를 해결하는 자유로운 타입이에요.",
        "mood": "쿨하고 자유로운 스트릿 무드",
        "tags": ["쿨함", "실용적", "스트릿"],
        "male": {
            "title": "편한데 멋있는 스트릿룩",
            "items": ["오버핏 후드티", "카고 팬츠", "블랙 항공점퍼", "하이탑 스니커즈", "볼캡"],
            "tip": "활동성 좋은 아이템을 중심으로 고르면 쿨한 분위기가 살아나요.",
            "query": "남자 오버핏 후드티 카고팬츠 블랙 항공점퍼 스트릿룩 코디"
        },
        "female": {
            "title": "힙한 캐주얼 스트릿룩",
            "items": ["크롭 맨투맨", "와이드 카고 팬츠", "레더 재킷", "청키 스니커즈", "미니 백팩"],
            "tip": "편안한 핏에 레더나 카고 소재를 섞으면 자유로운 느낌이 나요.",
            "query": "여자 크롭 맨투맨 와이드 카고팬츠 레더 자켓 스트릿룩 코디"
        }
    },
    "ISFP": {
        "emoji": "🎨",
        "personality": "감각적이고 유연하며, 자신만의 취향과 분위기를 자연스럽게 표현하는 타입이에요.",
        "mood": "감각적이고 자연스러운 아트 무드",
        "tags": ["감각적", "내추럴", "개성"],
        "male": {
            "title": "내추럴 아티스트룩",
            "items": ["린넨 셔츠", "와이드 데님 팬츠", "카키 야상 재킷", "캔버스 스니커즈", "비니"],
            "tip": "자연스러운 소재와 편안한 핏을 선택하면 감각적인 분위기가 나요.",
            "query": "남자 린넨 셔츠 와이드 데님 카키 야상 아티스트룩 코디"
        },
        "female": {
            "title": "빈티지 감성 아트룩",
            "items": ["플라워 패턴 블라우스", "롱 데님 스커트", "니트 베스트", "스웨이드 로퍼", "라탄백"],
            "tip": "패턴 하나를 포인트로 두면 예술적인 감성이 돋보여요.",
            "query": "여자 플라워 블라우스 롱 데님 스커트 니트 베스트 빈티지 코디"
        }
    },
    "INFP": {
        "emoji": "☁️",
        "personality": "상상력이 풍부하고 감성적이며, 자신만의 가치와 이야기를 중요하게 여기는 타입이에요.",
        "mood": "몽글몽글 감성적인 로맨틱 무드",
        "tags": ["감성", "로맨틱", "빈티지"],
        "male": {
            "title": "부드러운 빈티지 감성룩",
            "items": ["오트밀 니트", "브라운 코듀로이 팬츠", "체크 셔츠", "스웨이드 로퍼", "캔버스백"],
            "tip": "따뜻한 브라운 계열을 활용하면 부드러운 감성이 잘 드러나요.",
            "query": "남자 오트밀 니트 브라운 코듀로이 팬츠 체크 셔츠 빈티지 코디"
        },
        "female": {
            "title": "동화 같은 로맨틱룩",
            "items": ["레이스 블라우스", "크림색 롱 스커트", "베이지 니트 가디건", "메리제인 슈즈", "리본 헤어핀"],
            "tip": "레이스, 리본, 니트처럼 섬세한 디테일을 활용하면 좋아요.",
            "query": "여자 레이스 블라우스 크림 롱스커트 베이지 가디건 로맨틱룩 코디"
        }
    },
    "INTP": {
        "emoji": "💻",
        "personality": "호기심이 많고 논리적이며, 자신만의 방식으로 깊게 탐구하는 타입이에요.",
        "mood": "편안하고 지적인 너드 시크 무드",
        "tags": ["편안함", "너드미", "미니멀"],
        "male": {
            "title": "너드미 있는 편안한 캐주얼룩",
            "items": ["그래픽 티셔츠", "체크 셔츠", "블랙 와이드 팬츠", "컨버스 스니커즈", "동그란 안경"],
            "tip": "꾸민 듯 안 꾸민 듯한 편안함이 잘 어울려요.",
            "query": "남자 그래픽 티셔츠 체크 셔츠 블랙 와이드 팬츠 너드룩 코디"
        },
        "female": {
            "title": "편안한 북카페 감성룩",
            "items": ["루즈핏 니트", "와이드 데님", "체크 재킷", "스니커즈", "큰 에코백"],
            "tip": "여유로운 실루엣과 체크 패턴을 활용하면 지적인 분위기가 나요.",
            "query": "여자 루즈핏 니트 와이드 데님 체크 자켓 북카페룩 코디"
        }
    },
    "ESTP": {
        "emoji": "⚡",
        "personality": "활동적이고 에너지가 넘치며, 순간을 즐기고 도전하는 것을 좋아하는 타입이에요.",
        "mood": "에너지 넘치는 스포티 무드",
        "tags": ["활동적", "화려함", "스포티"],
        "male": {
            "title": "눈에 띄는 스포티 스트릿룩",
            "items": ["컬러 포인트 바람막이", "조거 팬츠", "화이트 티셔츠", "러닝화", "스포츠 시계"],
            "tip": "강한 컬러 포인트를 하나 넣으면 활동적인 매력이 잘 보여요.",
            "query": "남자 컬러 바람막이 조거팬츠 화이트 티셔츠 스포티 스트릿 코디"
        },
        "female": {
            "title": "상큼한 애슬레저룩",
            "items": ["크롭 집업", "하이웨스트 조거 팬츠", "볼드한 스니커즈", "캡 모자", "미니 크로스백"],
            "tip": "스포티한 아이템에 밝은 색을 더하면 활발한 느낌이 살아나요.",
            "query": "여자 크롭 집업 하이웨스트 조거팬츠 애슬레저룩 코디"
        }
    },
    "ESFP": {
        "emoji": "🎉",
        "personality": "밝고 사교적이며, 분위기를 즐겁게 만들고 트렌디한 감각이 뛰어난 타입이에요.",
        "mood": "화사하고 사랑스러운 파티 무드",
        "tags": ["화려함", "러블리", "트렌디"],
        "male": {
            "title": "트렌디한 컬러 포인트룩",
            "items": ["비비드 컬러 니트", "블랙 데님 팬츠", "화이트 스니커즈", "데님 재킷", "실버 액세서리"],
            "tip": "밝은 색 포인트를 활용하면 밝은 매력이 돋보여요.",
            "query": "남자 비비드 컬러 니트 블랙 데님 데님 자켓 트렌디 코디"
        },
        "female": {
            "title": "러블리 트렌디 데이트룩",
            "items": ["퍼프소매 블라우스", "미니 스커트", "컬러 가디건", "롱부츠", "하트 귀걸이"],
            "tip": "귀여운 디테일과 트렌디한 아이템을 함께 쓰면 좋아요.",
            "query": "여자 퍼프소매 블라우스 미니 스커트 컬러 가디건 롱부츠 코디"
        }
    },
    "ENFP": {
        "emoji": "🌈",
        "personality": "상상력과 에너지가 풍부하며, 새로운 가능성과 개성 있는 표현을 좋아하는 타입이에요.",
        "mood": "톡톡 튀는 자유로운 컬러풀 무드",
        "tags": ["자유로움", "컬러풀", "개성"],
        "male": {
            "title": "개성 가득 컬러 믹스룩",
            "items": ["컬러풀 스트라이프 니트", "연청 와이드 데님", "스니커즈", "비니", "패턴 양말"],
            "tip": "색과 패턴을 너무 두려워하지 말고 즐겁게 섞어보세요.",
            "query": "남자 컬러풀 스트라이프 니트 연청 와이드 데님 개성 코디"
        },
        "female": {
            "title": "상큼한 키치 캐주얼룩",
            "items": ["그래픽 티셔츠", "컬러 플리츠 스커트", "오버핏 가디건", "플랫폼 스니커즈", "키링 미니백"],
            "tip": "귀여운 소품을 더하면 발랄한 분위기가 잘 살아나요.",
            "query": "여자 그래픽 티셔츠 컬러 플리츠 스커트 오버핏 가디건 키치룩 코디"
        }
    },
    "ENTP": {
        "emoji": "🧩",
        "personality": "재치 있고 아이디어가 많으며, 새로운 시도와 독특한 조합을 즐기는 타입이에요.",
        "mood": "재치 있고 힙한 믹스매치 무드",
        "tags": ["힙함", "실험적", "유니크"],
        "male": {
            "title": "센스 있는 믹스매치룩",
            "items": ["프린팅 셔츠", "와이드 슬랙스", "레더 재킷", "독특한 스니커즈", "체인 팔찌"],
            "tip": "평범한 조합보다 의외의 아이템을 섞으면 유니크한 매력이 나요.",
            "query": "남자 프린팅 셔츠 와이드 슬랙스 레더 자켓 믹스매치 코디"
        },
        "female": {
            "title": "유니크한 하이틴 시크룩",
            "items": ["크롭 셔츠", "체크 미니 스커트", "오버핏 재킷", "워커 부츠", "볼드 선글라스"],
            "tip": "강한 아이템을 하나 정하고 나머지를 균형 있게 맞추면 좋아요.",
            "query": "여자 크롭 셔츠 체크 미니 스커트 오버핏 재킷 워커 하이틴룩 코디"
        }
    },
    "ESTJ": {
        "emoji": "👔",
        "personality": "현실적이고 추진력이 있으며, 목표를 정하면 빠르고 체계적으로 실행하는 타입이에요.",
        "mood": "당당하고 정돈된 리더 무드",
        "tags": ["단정함", "포멀", "당당함"],
        "male": {
            "title": "깔끔한 비즈니스 캐주얼룩",
            "items": ["화이트 셔츠", "그레이 블레이저", "네이비 슬랙스", "블랙 로퍼", "브리프 케이스"],
            "tip": "정돈된 핏과 차분한 색을 선택하면 리더십 있는 분위기가 나요.",
            "query": "남자 화이트 셔츠 그레이 블레이저 네이비 슬랙스 비즈니스 캐주얼 코디"
        },
        "female": {
            "title": "당당한 포멀 페미닌룩",
            "items": ["새틴 블라우스", "블랙 테일러드 재킷", "슬랙스", "포인티드 토 슈즈", "스퀘어 숄더백"],
            "tip": "각 잡힌 재킷과 깔끔한 가방이 당당한 이미지를 잘 표현해요.",
            "query": "여자 새틴 블라우스 블랙 테일러드 재킷 슬랙스 포멀룩 코디"
        }
    },
    "ESFJ": {
        "emoji": "🌷",
        "personality": "친화력이 좋고 배려심이 많으며, 주변 분위기를 따뜻하게 만드는 타입이에요.",
        "mood": "밝고 호감 가는 단정 러블리 무드",
        "tags": ["호감형", "단정함", "러블리"],
        "male": {
            "title": "호감형 캠퍼스룩",
            "items": ["스트라이프 셔츠", "니트 베스트", "크림 치노 팬츠", "화이트 스니커즈", "깔끔한 백팩"],
            "tip": "밝고 단정한 조합이 친근한 매력을 살려줘요.",
            "query": "남자 스트라이프 셔츠 니트 베스트 크림 치노팬츠 캠퍼스룩 코디"
        },
        "female": {
            "title": "화사한 러블리 캐주얼룩",
            "items": ["파스텔 블라우스", "A라인 스커트", "트위드 재킷", "플랫슈즈", "미니 숄더백"],
            "tip": "화사한 색과 단정한 실루엣을 조합하면 호감도가 올라가요.",
            "query": "여자 파스텔 블라우스 A라인 스커트 트위드 재킷 러블리 코디"
        }
    },
    "ENFJ": {
        "emoji": "✨",
        "personality": "따뜻한 리더십과 공감 능력이 뛰어나며, 사람들에게 좋은 영향을 주는 타입이에요.",
        "mood": "따뜻하고 세련된 주인공 무드",
        "tags": ["세련됨", "따뜻함", "우아함"],
        "male": {
            "title": "따뜻한 세미 포멀룩",
            "items": ["베이지 니트", "브라운 블레이저", "아이보리 슬랙스", "로퍼", "가죽 벨트"],
            "tip": "부드러운 색감에 포멀한 아이템을 더하면 신뢰감과 따뜻함이 함께 보여요.",
            "query": "남자 베이지 니트 브라운 블레이저 아이보리 슬랙스 세미 포멀 코디"
        },
        "female": {
            "title": "우아한 주인공룩",
            "items": ["랩 원피스", "롱 코트", "앵클부츠", "진주 목걸이", "토트백"],
            "tip": "우아한 실루엣과 따뜻한 색을 사용하면 매력이 돋보여요.",
            "query": "여자 랩 원피스 롱 코트 앵클부츠 우아한 코디"
        }
    },
    "ENTJ": {
        "emoji": "🦁",
        "personality": "목표 지향적이고 카리스마가 있으며, 큰 그림을 보고 과감하게 이끄는 타입이에요.",
        "mood": "카리스마 있고 고급스러운 파워 무드",
        "tags": ["카리스마", "럭셔리", "시크"],
        "male": {
            "title": "카리스마 있는 파워 수트룩",
            "items": ["블랙 터틀넥", "차콜 수트 셋업", "블랙 더비 슈즈", "고급 시계", "레더 브리프백"],
            "tip": "강한 실루엣과 어두운 색을 사용하면 카리스마가 살아나요.",
            "query": "남자 블랙 터틀넥 차콜 수트 셋업 파워 수트룩 코디"
        },
        "female": {
            "title": "시크한 파워 드레싱룩",
            "items": ["화이트 셔츠", "블랙 와이드 슬랙스", "오버핏 테일러드 재킷", "스틸레토 힐", "골드 이어링"],
            "tip": "클래식한 아이템에 골드 포인트를 더하면 고급스러운 느낌이 나요.",
            "query": "여자 화이트 셔츠 블랙 와이드 슬랙스 테일러드 재킷 파워 드레싱 코디"
        }
    }
}

# =========================================================
# 함수
# =========================================================
def make_pinterest_url(query):
    return f"https://www.pinterest.com/search/pins/?q={quote(query)}"


def render_outfit_card(gender_label, outfit_data):
    pinterest_url = make_pinterest_url(outfit_data["query"])

    items_html = ""
    for item in outfit_data["items"]:
        items_html += f"• {item}<br>"

    st.markdown(
        f"""
        <div class="card">
            <div class="card-title">{gender_label} 코디 추천</div>
            <div class="outfit-name">✨ {outfit_data["title"]}</div>
            <div class="item-list">
                {items_html}
            </div>
            <div class="tip-box">
                <b>💡 스타일 팁</b><br>
                {outfit_data["tip"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "Pinterest에서 코디 찾아보기 🔎",
        pinterest_url,
        use_container_width=True
    )


# =========================================================
# 화면 제목
# =========================================================
st.markdown('<div class="main-title">MBTI 코디 추천기 👗👕</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="sub-title">
    MBTI를 선택하면 어울리는 남자 코디와 여자 코디를 추천해줄게요.<br>
    마음에 드는 스타일은 Pinterest 링크로 더 찾아볼 수 있어요 ✨
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# MBTI 선택 영역
# =========================================================
st.markdown('<div class="cute-box">', unsafe_allow_html=True)

mbti_list = list(outfits.keys())

selected_mbti = st.selectbox(
    "MBTI를 선택해 주세요 💌",
    mbti_list,
    index=0
)

selected_data = outfits[selected_mbti]

# 선택창 밑 MBTI 성격 설명 1줄
st.markdown(
    f"""
    <div class="personality-line">
        {selected_data["emoji"]} <b>{selected_mbti}</b>는 {selected_data["personality"]}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# 선택 결과
# =========================================================
st.markdown('<div class="cute-box">', unsafe_allow_html=True)

st.markdown(
    f"""
    <span class="mbti-badge">{selected_mbti} {selected_data["emoji"]}</span>
    <div class="mood-text">
        <b>{selected_data["mood"]}</b>
    </div>
    """,
    unsafe_allow_html=True
)

tag_html = ""
for tag in selected_data["tags"]:
    tag_html += f'<span class="tag">#{tag}</span>'

st.markdown(tag_html, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# 코디 추천 카드
# =========================================================
render_outfit_card("🧑 남자", selected_data["male"])
render_outfit_card("👩 여자", selected_data["female"])

# =========================================================
# 안내
# =========================================================
with st.expander("Pinterest 링크 안내 📌"):
    st.write(
        """
        이 앱은 Pinterest 이미지를 직접 가져오지 않고,  
        선택한 코디 키워드로 Pinterest 검색 결과 페이지를 열어주는 방식입니다.  
        그래서 저작권 문제를 줄이면서 다양한 실제 코디 예시를 찾아볼 수 있어요.
        """
    )

st.markdown(
    """
    <div class="footer">
        Made with Streamlit 💗 | MBTI 코디 추천은 재미용이에요 🌈
    </div>
    """,
    unsafe_allow_html=True
)
