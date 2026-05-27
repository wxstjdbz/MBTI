import streamlit as st
from urllib.parse import quote

# =============================
# 기본 페이지 설정
# =============================
st.set_page_config(
    page_title="MBTI 코디 추천기",
    page_icon="🧸",
    layout="wide"
)

# =============================
# CSS 스타일
# =============================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff7fb 0%, #f6fbff 100%);
    }

    .main-title {
        text-align: center;
        font-size: 44px;
        font-weight: 900;
        color: #ff6f91;
        margin-top: 20px;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        font-size: 18px;
        color: #666;
        margin-bottom: 30px;
    }

    .cute-box {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 24px;
        border-radius: 24px;
        box-shadow: 0 8px 24px rgba(255, 150, 180, 0.18);
        border: 1px solid #ffe1ec;
        margin-bottom: 25px;
    }

    .mbti-badge {
        display: inline-block;
        background: linear-gradient(135deg, #ff9eb5, #ffc3d5);
        color: white;
        padding: 8px 18px;
        border-radius: 999px;
        font-size: 20px;
        font-weight: 800;
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
        margin-top: 6px;
        border: 1px solid #ffd6e5;
    }

    .section-title {
        font-size: 26px;
        font-weight: 850;
        color: #ff6f91;
        margin-top: 5px;
        margin-bottom: 12px;
    }

    .card-title {
        font-size: 23px;
        font-weight: 800;
        color: #333;
        margin-bottom: 10px;
    }

    .item-list {
        font-size: 16px;
        line-height: 1.9;
        color: #444;
    }

    .tip-box {
        background-color: #fff7fb;
        padding: 14px;
        border-radius: 16px;
        border-left: 5px solid #ff9eb5;
        color: #555;
        margin-top: 12px;
        font-size: 15px;
        line-height: 1.7;
    }

    .small-note {
        color: #888;
        font-size: 13px;
        line-height: 1.6;
    }

    .footer {
        text-align: center;
        color: #999;
        font-size: 14px;
        margin-top: 50px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =============================
# MBTI별 코디 데이터
# =============================
outfits = {
    "ISTJ": {
        "emoji": "📚",
        "mood": "단정하고 믿음직한 클래식 무드",
        "tags": ["깔끔함", "클래식", "실용적"],
        "male": {
            "title": "차분한 클래식 댄디룩",
            "items": ["네이비 싱글 블레이저", "화이트 셔츠", "베이지 치노 팬츠", "브라운 로퍼", "가죽 시계"],
            "tip": "색은 네이비, 화이트, 베이지처럼 안정적인 조합을 쓰면 신뢰감 있는 분위기가 살아나요.",
            "image_tags": "menswear,classic,outfit",
            "pinterest_query": "남자 클래식 댄디룩 네이비 블레이저 코디"
        },
        "female": {
            "title": "깔끔한 오피스 캐주얼룩",
            "items": ["아이보리 블라우스", "네이비 가디건", "베이지 H라인 스커트", "브라운 플랫슈즈", "심플 토트백"],
            "tip": "과한 장식보다 핏과 소재가 깔끔한 옷을 고르면 ISTJ의 차분함이 잘 표현돼요.",
            "image_tags": "women,classic,fashion",
            "pinterest_query": "여자 오피스 캐주얼 아이보리 블라우스 베이지 스커트 코디"
        }
    },
    "ISFJ": {
        "emoji": "🧸",
        "mood": "따뜻하고 부드러운 포근 무드",
        "tags": ["포근함", "러블리", "차분함"],
        "male": {
            "title": "부드러운 니트 캐주얼룩",
            "items": ["크림색 라운드 니트", "연청 데님 팬츠", "베이지 코트", "화이트 스니커즈", "캔버스 에코백"],
            "tip": "따뜻한 색감과 부드러운 소재를 쓰면 다정한 이미지가 더 잘 살아나요.",
            "image_tags": "men,knit,casual",
            "pinterest_query": "남자 크림 니트 연청 데님 베이지 코트 코디"
        },
        "female": {
            "title": "포근한 데이트 캐주얼룩",
            "items": ["파스텔 핑크 니트", "아이보리 플리츠 스커트", "숏 무스탕", "메리제인 슈즈", "미니 크로스백"],
            "tip": "파스텔톤과 폭신한 소재를 조합하면 사랑스럽고 안정적인 분위기가 나요.",
            "image_tags": "women,knit,cute,outfit",
            "pinterest_query": "여자 파스텔 니트 플리츠 스커트 데이트룩 코디"
        }
    },
    "INFJ": {
        "emoji": "🌙",
        "mood": "신비롭고 감성적인 무드",
        "tags": ["감성적", "몽환적", "우아함"],
        "male": {
            "title": "감성적인 미니멀 모노톤룩",
            "items": ["차콜 터틀넥", "블랙 와이드 슬랙스", "롱 코트", "첼시 부츠", "실버 목걸이"],
            "tip": "어두운 톤에 작은 실버 포인트를 더하면 분위기 있는 스타일이 완성돼요.",
            "image_tags": "men,minimal,black,outfit",
            "pinterest_query": "남자 차콜 터틀넥 블랙 슬랙스 롱코트 코디"
        },
        "female": {
            "title": "몽환적인 시크 페미닌룩",
            "items": ["블랙 시스루 블라우스", "롱 플레어 스커트", "그레이 롱 코트", "앵클부츠", "진주 귀걸이"],
            "tip": "블랙, 그레이, 딥퍼플 계열을 활용하면 INFJ 특유의 신비로운 분위기가 살아나요.",
            "image_tags": "women,black,elegant,fashion",
            "pinterest_query": "여자 블랙 블라우스 롱스커트 그레이 코트 코디"
        }
    },
    "INTJ": {
        "emoji": "🖤",
        "mood": "지적이고 세련된 시크 무드",
        "tags": ["시크함", "미니멀", "도시적"],
        "male": {
            "title": "블랙 미니멀 시티룩",
            "items": ["블랙 셔츠", "그레이 슬랙스", "블랙 싱글 코트", "더비 슈즈", "메탈 프레임 안경"],
            "tip": "컬러를 절제하고 실루엣을 깔끔하게 잡으면 지적인 느낌이 강해져요.",
            "image_tags": "men,black,minimal,fashion",
            "pinterest_query": "남자 블랙 셔츠 그레이 슬랙스 미니멀 코디"
        },
        "female": {
            "title": "세련된 모던 시크룩",
            "items": ["블랙 터틀넥", "화이트 와이드 팬츠", "블랙 재킷", "스틸레토 슈즈", "미니멀 숄더백"],
            "tip": "블랙 앤 화이트 조합은 INTJ의 선명하고 세련된 이미지를 잘 보여줘요.",
            "image_tags": "women,minimal,black,white,outfit",
            "pinterest_query": "여자 블랙 터틀넥 화이트 와이드팬츠 시크룩"
        }
    },
    "ISTP": {
        "emoji": "🛹",
        "mood": "쿨하고 자유로운 스트릿 무드",
        "tags": ["쿨함", "실용적", "스트릿"],
        "male": {
            "title": "편한데 멋있는 스트릿룩",
            "items": ["오버핏 후드티", "카고 팬츠", "블랙 항공점퍼", "하이탑 스니커즈", "볼캡"],
            "tip": "활동성 좋은 아이템을 중심으로 고르면 ISTP다운 쿨함이 살아나요.",
            "image_tags": "men,streetwear,hoodie",
            "pinterest_query": "남자 오버핏 후드티 카고팬츠 스트릿룩 코디"
        },
        "female": {
            "title": "힙한 캐주얼 스트릿룩",
            "items": ["크롭 맨투맨", "와이드 카고 팬츠", "레더 재킷", "청키 스니커즈", "미니 백팩"],
            "tip": "편안한 핏에 레더나 카고 소재를 섞으면 멋있고 자유로운 느낌이 나요.",
            "image_tags": "women,streetwear,cargo,outfit",
            "pinterest_query": "여자 크롭 맨투맨 카고팬츠 레더자켓 스트릿룩"
        }
    },
    "ISFP": {
        "emoji": "🎨",
        "mood": "감각적이고 자연스러운 아트 무드",
        "tags": ["감각적", "내추럴", "개성"],
        "male": {
            "title": "내추럴 아티스트룩",
            "items": ["린넨 셔츠", "와이드 데님 팬츠", "카키 야상 재킷", "캔버스 스니커즈", "비니"],
            "tip": "자연스러운 소재와 편안한 핏을 선택하면 감각적인 분위기가 나요.",
            "image_tags": "men,linen,casual,fashion",
            "pinterest_query": "남자 린넨 셔츠 와이드 데님 아티스트룩 코디"
        },
        "female": {
            "title": "빈티지 감성 아트룩",
            "items": ["플라워 패턴 블라우스", "롱 데님 스커트", "니트 베스트", "스웨이드 로퍼", "라탄백"],
            "tip": "패턴 하나를 포인트로 두면 ISFP다운 예술적인 감성이 돋보여요.",
            "image_tags": "women,vintage,boho,outfit",
            "pinterest_query": "여자 빈티지 플라워 블라우스 롱 데님 스커트 코디"
        }
    },
    "INFP": {
        "emoji": "☁️",
        "mood": "몽글몽글 감성적인 로맨틱 무드",
        "tags": ["감성", "로맨틱", "빈티지"],
        "male": {
            "title": "부드러운 빈티지 감성룩",
            "items": ["오트밀 니트", "브라운 코듀로이 팬츠", "체크 셔츠", "스웨이드 로퍼", "캔버스백"],
            "tip": "따뜻한 브라운 계열을 활용하면 INFP의 부드러운 감성이 잘 드러나요.",
            "image_tags": "men,vintage,knit,outfit",
            "pinterest_query": "남자 오트밀 니트 브라운 코듀로이 빈티지 코디"
        },
        "female": {
            "title": "동화 같은 로맨틱룩",
            "items": ["레이스 블라우스", "크림색 롱 스커트", "베이지 니트 가디건", "메리제인 슈즈", "리본 헤어핀"],
            "tip": "레이스, 리본, 니트처럼 섬세한 디테일을 활용하면 로맨틱한 느낌이 강해져요.",
            "image_tags": "women,romantic,vintage,fashion",
            "pinterest_query": "여자 레이스 블라우스 크림 롱스커트 로맨틱룩"
        }
    },
    "INTP": {
        "emoji": "💻",
        "mood": "편안하고 지적인 너드 시크 무드",
        "tags": ["편안함", "너드미", "미니멀"],
        "male": {
            "title": "너드미 있는 편안한 캐주얼룩",
            "items": ["그래픽 티셔츠", "체크 셔츠", "블랙 와이드 팬츠", "컨버스 스니커즈", "동그란 안경"],
            "tip": "꾸민 듯 안 꾸민 듯한 편안함이 INTP와 잘 어울려요.",
            "image_tags": "men,casual,geek,outfit",
            "pinterest_query": "남자 체크셔츠 와이드팬츠 너드룩 캐주얼 코디"
        },
        "female": {
            "title": "편안한 북카페 감성룩",
            "items": ["루즈핏 니트", "와이드 데님", "체크 재킷", "스니커즈", "큰 에코백"],
            "tip": "여유로운 실루엣과 체크 패턴을 활용하면 지적인 분위기가 나요.",
            "image_tags": "women,casual,book,cafe,outfit",
            "pinterest_query": "여자 루즈핏 니트 와이드 데님 체크자켓 코디"
        }
    },
    "ESTP": {
        "emoji": "⚡",
        "mood": "에너지 넘치는 스포티 무드",
        "tags": ["활동적", "화려함", "스포티"],
        "male": {
            "title": "눈에 띄는 스포티 스트릿룩",
            "items": ["컬러 포인트 바람막이", "조거 팬츠", "화이트 티셔츠", "러닝화", "스포츠 시계"],
            "tip": "강한 컬러 포인트를 하나 넣으면 ESTP의 에너지가 잘 보여요.",
            "image_tags": "men,sporty,streetwear,outfit",
            "pinterest_query": "남자 바람막이 조거팬츠 스포티 스트릿룩 코디"
        },
        "female": {
            "title": "상큼한 애슬레저룩",
            "items": ["크롭 집업", "하이웨스트 조거 팬츠", "볼드한 스니커즈", "캡 모자", "미니 크로스백"],
            "tip": "스포티한 아이템에 밝은 색을 더하면 활발한 느낌이 살아나요.",
            "image_tags": "women,athleisure,sporty,outfit",
            "pinterest_query": "여자 크롭 집업 조거팬츠 애슬레저룩 코디"
        }
    },
    "ESFP": {
        "emoji": "🎉",
        "mood": "화사하고 사랑스러운 파티 무드",
        "tags": ["화려함", "러블리", "트렌디"],
        "male": {
            "title": "트렌디한 컬러 포인트룩",
            "items": ["비비드 컬러 니트", "블랙 데님 팬츠", "화이트 스니커즈", "데님 재킷", "실버 액세서리"],
            "tip": "밝은 색 포인트를 활용하면 ESFP의 밝은 매력이 돋보여요.",
            "image_tags": "men,colorful,street,fashion",
            "pinterest_query": "남자 컬러 니트 블랙 데님 트렌디 코디"
        },
        "female": {
            "title": "러블리 트렌디 데이트룩",
            "items": ["퍼프소매 블라우스", "미니 스커트", "컬러 가디건", "롱부츠", "하트 귀걸이"],
            "tip": "귀여운 디테일과 트렌디한 아이템을 함께 쓰면 좋아요.",
            "image_tags": "women,colorful,cute,fashion",
            "pinterest_query": "여자 퍼프 블라우스 미니스커트 컬러 가디건 코디"
        }
    },
    "ENFP": {
        "emoji": "🌈",
        "mood": "톡톡 튀는 자유로운 컬러풀 무드",
        "tags": ["자유로움", "컬러풀", "개성"],
        "male": {
            "title": "개성 가득 컬러 믹스룩",
            "items": ["컬러풀 스트라이프 니트", "연청 와이드 데님", "스니커즈", "비니", "패턴 양말"],
            "tip": "색과 패턴을 너무 두려워하지 말고 즐겁게 섞어보세요.",
            "image_tags": "men,colorful,casual,outfit",
            "pinterest_query": "남자 컬러풀 스트라이프 니트 와이드 데님 코디"
        },
        "female": {
            "title": "상큼한 키치 캐주얼룩",
            "items": ["그래픽 티셔츠", "컬러 플리츠 스커트", "오버핏 가디건", "플랫폼 스니커즈", "키링 미니백"],
            "tip": "귀여운 소품을 더하면 ENFP다운 발랄함이 잘 살아나요.",
            "image_tags": "women,kitsch,colorful,outfit",
            "pinterest_query": "여자 키치룩 그래픽 티셔츠 컬러 스커트 코디"
        }
    },
    "ENTP": {
        "emoji": "🧩",
        "mood": "재치 있고 힙한 믹스매치 무드",
        "tags": ["힙함", "실험적", "유니크"],
        "male": {
            "title": "센스 있는 믹스매치룩",
            "items": ["프린팅 셔츠", "와이드 슬랙스", "레더 재킷", "독특한 스니커즈", "체인 팔찌"],
            "tip": "평범한 조합보다 의외의 아이템을 섞으면 ENTP다운 매력이 나요.",
            "image_tags": "men,unique,streetwear,outfit",
            "pinterest_query": "남자 프린팅 셔츠 와이드 슬랙스 레더자켓 코디"
        },
        "female": {
            "title": "유니크한 하이틴 시크룩",
            "items": ["크롭 셔츠", "체크 미니 스커트", "오버핏 재킷", "워커 부츠", "볼드 선글라스"],
            "tip": "강한 아이템을 하나 정하고 나머지를 균형 있게 맞추면 좋아요.",
            "image_tags": "women,unique,street,fashion",
            "pinterest_query": "여자 크롭 셔츠 체크 스커트 워커 하이틴룩"
        }
    },
    "ESTJ": {
        "emoji": "👔",
        "mood": "당당하고 정돈된 리더 무드",
        "tags": ["단정함", "포멀", "당당함"],
        "male": {
            "title": "깔끔한 비즈니스 캐주얼룩",
            "items": ["화이트 셔츠", "그레이 블레이저", "네이비 슬랙스", "블랙 로퍼", "브리프 케이스"],
            "tip": "정돈된 핏과 차분한 색을 선택하면 리더십 있는 분위기가 나요.",
            "image_tags": "men,business,casual,outfit",
            "pinterest_query": "남자 비즈니스 캐주얼 그레이 블레이저 네이비 슬랙스"
        },
        "female": {
            "title": "당당한 포멀 페미닌룩",
            "items": ["새틴 블라우스", "블랙 테일러드 재킷", "슬랙스", "포인티드 토 슈즈", "스퀘어 숄더백"],
            "tip": "각 잡힌 재킷과 깔끔한 가방이 ESTJ의 당당함을 잘 표현해요.",
            "image_tags": "women,business,elegant,outfit",
            "pinterest_query": "여자 테일러드 자켓 슬랙스 포멀룩 코디"
        }
    },
    "ESFJ": {
        "emoji": "🌷",
        "mood": "밝고 호감 가는 단정 러블리 무드",
        "tags": ["호감형", "단정함", "러블리"],
        "male": {
            "title": "호감형 캠퍼스룩",
            "items": ["스트라이프 셔츠", "니트 베스트", "크림 치노 팬츠", "화이트 스니커즈", "깔끔한 백팩"],
            "tip": "밝고 단정한 조합이 ESFJ의 친근한 매력을 살려줘요.",
            "image_tags": "men,campus,casual,outfit",
            "pinterest_query": "남자 스트라이프 셔츠 니트베스트 캠퍼스룩 코디"
        },
        "female": {
            "title": "화사한 러블리 캐주얼룩",
            "items": ["파스텔 블라우스", "A라인 스커트", "트위드 재킷", "플랫슈즈", "미니 숄더백"],
            "tip": "화사한 색과 단정한 실루엣을 조합하면 호감도가 올라가요.",
            "image_tags": "women,lovely,casual,outfit",
            "pinterest_query": "여자 파스텔 블라우스 A라인 스커트 트위드 자켓 코디"
        }
    },
    "ENFJ": {
        "emoji": "✨",
        "mood": "따뜻하고 세련된 주인공 무드",
        "tags": ["세련됨", "따뜻함", "우아함"],
        "male": {
            "title": "따뜻한 세미 포멀룩",
            "items": ["베이지 니트", "브라운 블레이저", "아이보리 슬랙스", "로퍼", "가죽 벨트"],
            "tip": "부드러운 색감에 포멀한 아이템을 더하면 신뢰감과 따뜻함이 함께 보여요.",
            "image_tags": "men,elegant,casual,outfit",
            "pinterest_query": "남자 베이지 니트 브라운 블레이저 세미 포멀 코디"
        },
        "female": {
            "title": "우아한 주인공룩",
            "items": ["랩 원피스", "롱 코트", "앵클부츠", "진주 목걸이", "토트백"],
            "tip": "우아한 실루엣과 따뜻한 색을 사용하면 ENFJ의 매력이 돋보여요.",
            "image_tags": "women,elegant,dress,outfit",
            "pinterest_query": "여자 랩원피스 롱코트 우아한 코디"
        }
    },
    "ENTJ": {
        "emoji": "🦁",
        "mood": "카리스마 있고 고급스러운 파워 무드",
        "tags": ["카리스마", "럭셔리", "시크"],
        "male": {
            "title": "카리스마 있는 파워 수트룩",
            "items": ["블랙 터틀넥", "차콜 수트 셋업", "블랙 더비 슈즈", "고급 시계", "레더 브리프백"],
            "tip": "강한 실루엣과 어두운 색을 사용하면 ENTJ다운 카리스마가 살아나요.",
            "image_tags": "men,suit,black,fashion",
            "pinterest_query": "남자 블랙 터틀넥 차콜 수트 코디"
        },
        "female": {
            "title": "시크한 파워 드레싱룩",
            "items": ["화이트 셔츠", "블랙 와이드 슬랙스", "오버핏 테일러드 재킷", "스틸레토 힐", "골드 이어링"],
            "tip": "클래식한 아이템에 골드 포인트를 더하면 고급스러운 느낌이 나요.",
            "image_tags": "women,power,suit,fashion",
            "pinterest_query": "여자 화이트 셔츠 블랙 슬랙스 테일러드 자켓 파워 드레싱"
        }
    }
}

# =============================
# 함수
# =============================
def get_loremflickr_image(tags, lock_number):
    """
    무료 이미지 서비스인 LoremFlickr에서 태그 기반 이미지를 가져오는 URL을 생성합니다.
    lock 값을 주면 새로고침해도 같은 이미지가 유지됩니다.
    """
    safe_tags = tags.replace(" ", ",")
    return f"https://loremflickr.com/900/1100/{safe_tags}?lock={lock_number}"


def get_pinterest_url(query):
    """
    Pinterest 검색 결과 페이지 URL을 생성합니다.
    """
    return f"https://www.pinterest.com/search/pins/?q={quote(query)}"


def render_outfit_card(gender_label, gender_emoji, outfit_data, image_lock):
    """
    코디 카드 출력 함수
    """
    image_url = get_loremflickr_image(outfit_data["image_tags"], image_lock)
    pinterest_url = get_pinterest_url(outfit_data["pinterest_query"])

    with st.container(border=True):
        st.markdown(f'<div class="section-title">{gender_emoji} {gender_label} 코디 추천</div>', unsafe_allow_html=True)

        img_col, text_col = st.columns([1, 1.15], gap="large")

        with img_col:
            st.image(
                image_url,
                use_container_width=True,
                caption="추천 분위기 참고 이미지 📸"
            )
            st.markdown(
                '<div class="small-note">이미지는 무료 이미지 소스에서 태그 기반으로 불러온 참고용 사진이에요.</div>',
                unsafe_allow_html=True
            )

        with text_col:
            st.markdown(f'<div class="card-title">{outfit_data["title"]}</div>', unsafe_allow_html=True)

            item_html = ""
            for item in outfit_data["items"]:
                item_html += f"• {item}<br>"

            st.markdown(
                f"""
                <div class="item-list">
                    {item_html}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="tip-box">
                    <b>💡 스타일 팁</b><br>
                    {outfit_data["tip"]}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")
            st.link_button(
                "Pinterest에서 비슷한 코디 더 보기 🔎",
                pinterest_url,
                use_container_width=True
            )

# =============================
# 화면 제목
# =============================
st.markdown('<div class="main-title">MBTI 코디 추천기 🧸✨</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">MBTI를 고르면 어울리는 남자 코디와 여자 코디를 사진 느낌과 함께 추천해줄게요 👕👗</div>',
    unsafe_allow_html=True
)

# =============================
# 안내 문구
# =============================
with st.expander("꼭 읽어보기: 이미지 사용 안내 📌"):
    st.write(
        """
        Pinterest 이미지를 웹앱에서 자동으로 가져와 직접 보여주는 것은 저작권이나 서비스 약관 문제가 생길 수 있어요.  
        그래서 이 앱은 앱 내부에는 무료 이미지 소스 기반의 참고 이미지를 보여주고,  
        더 많은 실제 코디는 Pinterest 검색 버튼을 통해 직접 확인할 수 있게 만들었습니다.
        """
    )

# =============================
# MBTI 선택 영역
# =============================
st.markdown('<div class="cute-box">', unsafe_allow_html=True)

mbti_list = list(outfits.keys())

selected_mbti = st.selectbox(
    "당신의 MBTI를 선택해 주세요 💌",
    mbti_list,
    index=0
)

st.markdown('</div>', unsafe_allow_html=True)

# =============================
# 선택 결과
# =============================
selected_data = outfits[selected_mbti]

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

# =============================
# 코디 카드 출력
# =============================
mbti_index = mbti_list.index(selected_mbti)
male_lock = 1000 + mbti_index
female_lock = 2000 + mbti_index

col1, col2 = st.columns(2, gap="large")

with col1:
    render_outfit_card(
        gender_label="남자",
        gender_emoji="🧑",
        outfit_data=selected_data["male"],
        image_lock=male_lock
    )

with col2:
    render_outfit_card(
        gender_label="여자",
        gender_emoji="👩",
        outfit_data=selected_data["female"],
        image_lock=female_lock
    )

# =============================
# 추가 활용 팁
# =============================
st.write("")
st.write("")

with st.expander("이 앱을 더 발전시키는 아이디어 보기 🌱"):
    st.write("1. 계절 선택 기능 추가하기: 봄, 여름, 가을, 겨울")
    st.write("2. 상황 선택 기능 추가하기: 학교, 데이트, 여행, 발표")
    st.write("3. 색상 팔레트 추천 기능 추가하기")
    st.write("4. 사용자가 직접 이미지 URL을 넣어서 저장하는 기능 추가하기")
    st.write("5. 실제 쇼핑몰 링크 대신 학습용 예시 링크를 연결해 보기")

st.markdown(
    """
    <div class="footer">
        Made with Streamlit 💗 | MBTI 코디 추천은 재미용이에요 🌈
    </div>
    """,
    unsafe_allow_html=True
)
