import streamlit as st
from urllib.parse import quote
import random

# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="MBTI 코디 이미지 추천기",
    page_icon="👗",
    layout="wide"
)

# =========================================================
# CSS
# =========================================================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff7fb 0%, #f4fbff 100%);
    }

    .main-title {
        text-align: center;
        font-size: 44px;
        font-weight: 900;
        color: #ff6f91;
        margin-top: 18px;
        margin-bottom: 6px;
    }

    .sub-title {
        text-align: center;
        font-size: 18px;
        color: #666;
        margin-bottom: 32px;
    }

    .cute-box {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 24px;
        border-radius: 24px;
        box-shadow: 0 8px 24px rgba(255, 150, 180, 0.18);
        border: 1px solid #ffe1ec;
        margin-bottom: 24px;
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

    .card-title {
        font-size: 25px;
        font-weight: 850;
        color: #ff6f91;
        margin-bottom: 10px;
    }

    .outfit-name {
        font-size: 22px;
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
        font-size: 15px;
        line-height: 1.7;
    }

    .notice {
        color: #777;
        font-size: 14px;
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
        "mood": "단정하고 믿음직한 클래식 무드",
        "tags": ["깔끔함", "클래식", "실용적"],
        "male": {
            "title": "차분한 클래식 댄디룩",
            "items": ["네이비 싱글 블레이저", "화이트 셔츠", "베이지 치노 팬츠", "브라운 로퍼", "가죽 시계"],
            "keywords": "navy single blazer, white shirt, beige chino pants, brown loafers, leather watch, classic clean menswear",
            "tip": "네이비, 화이트, 베이지처럼 안정적인 색을 쓰면 신뢰감 있는 분위기가 잘 살아나요."
        },
        "female": {
            "title": "깔끔한 오피스 캐주얼룩",
            "items": ["아이보리 블라우스", "네이비 니트 가디건", "베이지 H라인 스커트", "브라운 플랫슈즈", "심플 토트백"],
            "keywords": "ivory blouse, navy knit cardigan, beige pencil skirt, brown flat shoes, simple tote bag, clean office casual outfit",
            "tip": "과한 장식보다 핏과 소재가 깔끔한 옷을 고르면 차분한 매력이 잘 보여요."
        }
    },
    "ISFJ": {
        "emoji": "🧸",
        "mood": "따뜻하고 부드러운 포근 무드",
        "tags": ["포근함", "러블리", "차분함"],
        "male": {
            "title": "부드러운 니트 캐주얼룩",
            "items": ["크림색 라운드 니트", "연청 데님 팬츠", "베이지 코트", "화이트 스니커즈", "캔버스 에코백"],
            "keywords": "cream round knit sweater, light blue jeans, beige coat, white sneakers, canvas eco bag, soft warm casual mens outfit",
            "tip": "따뜻한 색감과 부드러운 소재를 쓰면 다정한 이미지가 더 잘 살아나요."
        },
        "female": {
            "title": "포근한 데이트 캐주얼룩",
            "items": ["파스텔 핑크 니트", "아이보리 플리츠 스커트", "숏 무스탕 재킷", "메리제인 슈즈", "미니 크로스백"],
            "keywords": "pastel pink knit sweater, ivory pleated skirt, short shearling jacket, mary jane shoes, mini crossbody bag, cute cozy outfit",
            "tip": "파스텔톤과 폭신한 소재를 조합하면 사랑스럽고 편안한 느낌이 나요."
        }
    },
    "INFJ": {
        "emoji": "🌙",
        "mood": "신비롭고 감성적인 무드",
        "tags": ["감성적", "몽환적", "우아함"],
        "male": {
            "title": "감성적인 미니멀 모노톤룩",
            "items": ["차콜 터틀넥", "블랙 와이드 슬랙스", "롱 코트", "첼시 부츠", "실버 목걸이"],
            "keywords": "charcoal turtleneck, black wide slacks, long coat, chelsea boots, silver necklace, minimal monochrome mens outfit",
            "tip": "어두운 톤에 작은 실버 포인트를 더하면 분위기 있는 스타일이 완성돼요."
        },
        "female": {
            "title": "몽환적인 시크 페미닌룩",
            "items": ["블랙 블라우스", "롱 플레어 스커트", "그레이 롱 코트", "앵클부츠", "진주 귀걸이"],
            "keywords": "black blouse, long flare skirt, gray long coat, ankle boots, pearl earrings, dreamy chic feminine outfit",
            "tip": "블랙, 그레이, 딥퍼플 계열을 활용하면 신비로운 분위기가 살아나요."
        }
    },
    "INTJ": {
        "emoji": "🖤",
        "mood": "지적이고 세련된 시크 무드",
        "tags": ["시크함", "미니멀", "도시적"],
        "male": {
            "title": "블랙 미니멀 시티룩",
            "items": ["블랙 셔츠", "그레이 슬랙스", "블랙 싱글 코트", "더비 슈즈", "메탈 프레임 안경"],
            "keywords": "black shirt, gray slacks, black single coat, derby shoes, metal frame glasses, sleek minimal city mens outfit",
            "tip": "컬러를 절제하고 실루엣을 깔끔하게 잡으면 지적인 느낌이 강해져요."
        },
        "female": {
            "title": "세련된 모던 시크룩",
            "items": ["블랙 터틀넥", "화이트 와이드 팬츠", "블랙 재킷", "스틸레토 슈즈", "미니멀 숄더백"],
            "keywords": "black turtleneck, white wide pants, black blazer, stiletto shoes, minimal shoulder bag, modern chic womens outfit",
            "tip": "블랙 앤 화이트 조합은 선명하고 세련된 이미지를 잘 보여줘요."
        }
    },
    "ISTP": {
        "emoji": "🛹",
        "mood": "쿨하고 자유로운 스트릿 무드",
        "tags": ["쿨함", "실용적", "스트릿"],
        "male": {
            "title": "편한데 멋있는 스트릿룩",
            "items": ["오버핏 후드티", "카고 팬츠", "블랙 항공점퍼", "하이탑 스니커즈", "볼캡"],
            "keywords": "oversized hoodie, cargo pants, black bomber jacket, high top sneakers, baseball cap, cool streetwear mens outfit",
            "tip": "활동성 좋은 아이템을 중심으로 고르면 쿨한 분위기가 살아나요."
        },
        "female": {
            "title": "힙한 캐주얼 스트릿룩",
            "items": ["크롭 맨투맨", "와이드 카고 팬츠", "레더 재킷", "청키 스니커즈", "미니 백팩"],
            "keywords": "cropped sweatshirt, wide cargo pants, leather jacket, chunky sneakers, mini backpack, hip casual streetwear womens outfit",
            "tip": "편안한 핏에 레더나 카고 소재를 섞으면 자유로운 느낌이 나요."
        }
    },
    "ISFP": {
        "emoji": "🎨",
        "mood": "감각적이고 자연스러운 아트 무드",
        "tags": ["감각적", "내추럴", "개성"],
        "male": {
            "title": "내추럴 아티스트룩",
            "items": ["린넨 셔츠", "와이드 데님 팬츠", "카키 야상 재킷", "캔버스 스니커즈", "비니"],
            "keywords": "linen shirt, wide denim pants, khaki field jacket, canvas sneakers, beanie, natural artist casual mens outfit",
            "tip": "자연스러운 소재와 편안한 핏을 선택하면 감각적인 분위기가 나요."
        },
        "female": {
            "title": "빈티지 감성 아트룩",
            "items": ["플라워 패턴 블라우스", "롱 데님 스커트", "니트 베스트", "스웨이드 로퍼", "라탄백"],
            "keywords": "floral blouse, long denim skirt, knit vest, suede loafers, rattan bag, vintage artistic womens outfit",
            "tip": "패턴 하나를 포인트로 두면 예술적인 감성이 돋보여요."
        }
    },
    "INFP": {
        "emoji": "☁️",
        "mood": "몽글몽글 감성적인 로맨틱 무드",
        "tags": ["감성", "로맨틱", "빈티지"],
        "male": {
            "title": "부드러운 빈티지 감성룩",
            "items": ["오트밀 니트", "브라운 코듀로이 팬츠", "체크 셔츠", "스웨이드 로퍼", "캔버스백"],
            "keywords": "oatmeal knit sweater, brown corduroy pants, check shirt, suede loafers, canvas bag, soft vintage mens outfit",
            "tip": "따뜻한 브라운 계열을 활용하면 부드러운 감성이 잘 드러나요."
        },
        "female": {
            "title": "동화 같은 로맨틱룩",
            "items": ["레이스 블라우스", "크림색 롱 스커트", "베이지 니트 가디건", "메리제인 슈즈", "리본 헤어핀"],
            "keywords": "lace blouse, cream long skirt, beige knit cardigan, mary jane shoes, ribbon hairpin, romantic vintage womens outfit",
            "tip": "레이스, 리본, 니트처럼 섬세한 디테일을 활용하면 좋아요."
        }
    },
    "INTP": {
        "emoji": "💻",
        "mood": "편안하고 지적인 너드 시크 무드",
        "tags": ["편안함", "너드미", "미니멀"],
        "male": {
            "title": "너드미 있는 편안한 캐주얼룩",
            "items": ["그래픽 티셔츠", "체크 셔츠", "블랙 와이드 팬츠", "컨버스 스니커즈", "동그란 안경"],
            "keywords": "graphic t shirt, check shirt, black wide pants, converse sneakers, round glasses, nerdy casual mens outfit",
            "tip": "꾸민 듯 안 꾸민 듯한 편안함이 잘 어울려요."
        },
        "female": {
            "title": "편안한 북카페 감성룩",
            "items": ["루즈핏 니트", "와이드 데님", "체크 재킷", "스니커즈", "큰 에코백"],
            "keywords": "loose knit sweater, wide denim jeans, check jacket, sneakers, large eco bag, cozy book cafe womens outfit",
            "tip": "여유로운 실루엣과 체크 패턴을 활용하면 지적인 분위기가 나요."
        }
    },
    "ESTP": {
        "emoji": "⚡",
        "mood": "에너지 넘치는 스포티 무드",
        "tags": ["활동적", "화려함", "스포티"],
        "male": {
            "title": "눈에 띄는 스포티 스트릿룩",
            "items": ["컬러 포인트 바람막이", "조거 팬츠", "화이트 티셔츠", "러닝화", "스포츠 시계"],
            "keywords": "color block windbreaker, jogger pants, white t shirt, running shoes, sports watch, energetic sporty mens outfit",
            "tip": "강한 컬러 포인트를 하나 넣으면 활동적인 매력이 잘 보여요."
        },
        "female": {
            "title": "상큼한 애슬레저룩",
            "items": ["크롭 집업", "하이웨스트 조거 팬츠", "볼드한 스니커즈", "캡 모자", "미니 크로스백"],
            "keywords": "cropped zip up jacket, high waist jogger pants, bold sneakers, cap, mini crossbody bag, sporty athleisure womens outfit",
            "tip": "스포티한 아이템에 밝은 색을 더하면 활발한 느낌이 살아나요."
        }
    },
    "ESFP": {
        "emoji": "🎉",
        "mood": "화사하고 사랑스러운 파티 무드",
        "tags": ["화려함", "러블리", "트렌디"],
        "male": {
            "title": "트렌디한 컬러 포인트룩",
            "items": ["비비드 컬러 니트", "블랙 데님 팬츠", "화이트 스니커즈", "데님 재킷", "실버 액세서리"],
            "keywords": "vivid color knit sweater, black denim pants, white sneakers, denim jacket, silver accessories, trendy colorful mens outfit",
            "tip": "밝은 색 포인트를 활용하면 밝은 매력이 돋보여요."
        },
        "female": {
            "title": "러블리 트렌디 데이트룩",
            "items": ["퍼프소매 블라우스", "미니 스커트", "컬러 가디건", "롱부츠", "하트 귀걸이"],
            "keywords": "puff sleeve blouse, mini skirt, colorful cardigan, long boots, heart earrings, lovely trendy womens outfit",
            "tip": "귀여운 디테일과 트렌디한 아이템을 함께 쓰면 좋아요."
        }
    },
    "ENFP": {
        "emoji": "🌈",
        "mood": "톡톡 튀는 자유로운 컬러풀 무드",
        "tags": ["자유로움", "컬러풀", "개성"],
        "male": {
            "title": "개성 가득 컬러 믹스룩",
            "items": ["컬러풀 스트라이프 니트", "연청 와이드 데님", "스니커즈", "비니", "패턴 양말"],
            "keywords": "colorful striped knit sweater, light blue wide denim jeans, sneakers, beanie, patterned socks, playful colorful mens outfit",
            "tip": "색과 패턴을 너무 두려워하지 말고 즐겁게 섞어보세요."
        },
        "female": {
            "title": "상큼한 키치 캐주얼룩",
            "items": ["그래픽 티셔츠", "컬러 플리츠 스커트", "오버핏 가디건", "플랫폼 스니커즈", "키링 미니백"],
            "keywords": "graphic t shirt, colorful pleated skirt, oversized cardigan, platform sneakers, keychain mini bag, cute kitsch womens outfit",
            "tip": "귀여운 소품을 더하면 발랄한 분위기가 잘 살아나요."
        }
    },
    "ENTP": {
        "emoji": "🧩",
        "mood": "재치 있고 힙한 믹스매치 무드",
        "tags": ["힙함", "실험적", "유니크"],
        "male": {
            "title": "센스 있는 믹스매치룩",
            "items": ["프린팅 셔츠", "와이드 슬랙스", "레더 재킷", "독특한 스니커즈", "체인 팔찌"],
            "keywords": "printed shirt, wide slacks, leather jacket, unique sneakers, chain bracelet, stylish mix match mens outfit",
            "tip": "평범한 조합보다 의외의 아이템을 섞으면 유니크한 매력이 나요."
        },
        "female": {
            "title": "유니크한 하이틴 시크룩",
            "items": ["크롭 셔츠", "체크 미니 스커트", "오버핏 재킷", "워커 부츠", "볼드 선글라스"],
            "keywords": "cropped shirt, check mini skirt, oversized jacket, combat boots, bold sunglasses, unique high teen chic womens outfit",
            "tip": "강한 아이템을 하나 정하고 나머지를 균형 있게 맞추면 좋아요."
        }
    },
    "ESTJ": {
        "emoji": "👔",
        "mood": "당당하고 정돈된 리더 무드",
        "tags": ["단정함", "포멀", "당당함"],
        "male": {
            "title": "깔끔한 비즈니스 캐주얼룩",
            "items": ["화이트 셔츠", "그레이 블레이저", "네이비 슬랙스", "블랙 로퍼", "브리프 케이스"],
            "keywords": "white shirt, gray blazer, navy slacks, black loafers, briefcase, clean business casual mens outfit",
            "tip": "정돈된 핏과 차분한 색을 선택하면 리더십 있는 분위기가 나요."
        },
        "female": {
            "title": "당당한 포멀 페미닌룩",
            "items": ["새틴 블라우스", "블랙 테일러드 재킷", "슬랙스", "포인티드 토 슈즈", "스퀘어 숄더백"],
            "keywords": "satin blouse, black tailored jacket, slacks, pointed toe shoes, square shoulder bag, formal feminine business outfit",
            "tip": "각 잡힌 재킷과 깔끔한 가방이 당당한 이미지를 잘 표현해요."
        }
    },
    "ESFJ": {
        "emoji": "🌷",
        "mood": "밝고 호감 가는 단정 러블리 무드",
        "tags": ["호감형", "단정함", "러블리"],
        "male": {
            "title": "호감형 캠퍼스룩",
            "items": ["스트라이프 셔츠", "니트 베스트", "크림 치노 팬츠", "화이트 스니커즈", "깔끔한 백팩"],
            "keywords": "striped shirt, knit vest, cream chino pants, white sneakers, neat backpack, friendly campus mens outfit",
            "tip": "밝고 단정한 조합이 친근한 매력을 살려줘요."
        },
        "female": {
            "title": "화사한 러블리 캐주얼룩",
            "items": ["파스텔 블라우스", "A라인 스커트", "트위드 재킷", "플랫슈즈", "미니 숄더백"],
            "keywords": "pastel blouse, a line skirt, tweed jacket, flat shoes, mini shoulder bag, lovely neat casual womens outfit",
            "tip": "화사한 색과 단정한 실루엣을 조합하면 호감도가 올라가요."
        }
    },
    "ENFJ": {
        "emoji": "✨",
        "mood": "따뜻하고 세련된 주인공 무드",
        "tags": ["세련됨", "따뜻함", "우아함"],
        "male": {
            "title": "따뜻한 세미 포멀룩",
            "items": ["베이지 니트", "브라운 블레이저", "아이보리 슬랙스", "로퍼", "가죽 벨트"],
            "keywords": "beige knit sweater, brown blazer, ivory slacks, loafers, leather belt, warm semi formal mens outfit",
            "tip": "부드러운 색감에 포멀한 아이템을 더하면 신뢰감과 따뜻함이 함께 보여요."
        },
        "female": {
            "title": "우아한 주인공룩",
            "items": ["랩 원피스", "롱 코트", "앵클부츠", "진주 목걸이", "토트백"],
            "keywords": "wrap dress, long coat, ankle boots, pearl necklace, tote bag, elegant main character womens outfit",
            "tip": "우아한 실루엣과 따뜻한 색을 사용하면 매력이 돋보여요."
        }
    },
    "ENTJ": {
        "emoji": "🦁",
        "mood": "카리스마 있고 고급스러운 파워 무드",
        "tags": ["카리스마", "럭셔리", "시크"],
        "male": {
            "title": "카리스마 있는 파워 수트룩",
            "items": ["블랙 터틀넥", "차콜 수트 셋업", "블랙 더비 슈즈", "고급 시계", "레더 브리프백"],
            "keywords": "black turtleneck, charcoal suit set, black derby shoes, luxury watch, leather brief bag, charismatic power suit mens outfit",
            "tip": "강한 실루엣과 어두운 색을 사용하면 카리스마가 살아나요."
        },
        "female": {
            "title": "시크한 파워 드레싱룩",
            "items": ["화이트 셔츠", "블랙 와이드 슬랙스", "오버핏 테일러드 재킷", "스틸레토 힐", "골드 이어링"],
            "keywords": "white shirt, black wide slacks, oversized tailored jacket, stiletto heels, gold earrings, chic power dressing womens outfit",
            "tip": "클래식한 아이템에 골드 포인트를 더하면 고급스러운 느낌이 나요."
        }
    }
}

# =========================================================
# 함수
# =========================================================
def make_image_prompt(gender, outfit_title, keywords, mood, image_style):
    """
    코디 아이템을 바탕으로 이미지 생성용 영어 프롬프트를 만든다.
    """

    if image_style == "모델 착용샷":
        if gender == "male":
            model_text = "a stylish man fashion model wearing"
        else:
            model_text = "a stylish woman fashion model wearing"

        prompt = f"""
        high quality full body fashion lookbook photo,
        {model_text} a complete coordinated outfit:
        {keywords}.
        style mood: {mood}.
        clean cute Korean Pinterest style, soft pastel background,
        natural lighting, realistic clothing details,
        modest outfit, no text, no logo, no watermark,
        full outfit visible from head to shoes
        """

    else:
        prompt = f"""
        high quality flat lay fashion outfit collage,
        neatly arranged clothing items:
        {keywords}.
        style mood: {mood}.
        clean cute Korean Pinterest style, soft pastel background,
        realistic fabric texture, fashion magazine layout,
        no person, no text, no logo, no watermark
        """

    return " ".join(prompt.split())


def make_image_url(prompt, seed):
    """
    Pollinations AI 이미지 URL 생성.
    별도 API 키 없이 이미지 URL만으로 표시 가능.
    """
    encoded_prompt = quote(prompt)
    return (
        f"https://image.pollinations.ai/prompt/{encoded_prompt}"
        f"?width=768&height=1024&seed={seed}&nologo=true&enhance=true"
    )


def make_pinterest_url(query):
    """
    Pinterest 검색 링크 생성.
    앱 안에 이미지를 무단으로 가져오지 않고, 검색 결과로 이동하게 함.
    """
    return f"https://www.pinterest.com/search/pins/?q={quote(query)}"


def render_outfit_card(gender_label, gender_key, outfit_data, mbti, mood, image_style, seed):
    """
    남자/여자 코디 카드를 출력한다.
    """

    prompt = make_image_prompt(
        gender=gender_key,
        outfit_title=outfit_data["title"],
        keywords=outfit_data["keywords"],
        mood=mood,
        image_style=image_style
    )

    image_url = make_image_url(prompt, seed)

    pinterest_query = f"{mbti} {outfit_data['title']} {', '.join(outfit_data['items'])} 코디"
    pinterest_url = make_pinterest_url(pinterest_query)

    with st.container(border=True):
        st.markdown(
            f'<div class="card-title">{gender_label} 코디 이미지</div>',
            unsafe_allow_html=True
        )

        img_col, text_col = st.columns([1.05, 1], gap="large")

        with img_col:
            st.image(
                image_url,
                use_container_width=True,
                caption=f"{outfit_data['title']} 참고 코디 이미지"
            )

            st.link_button(
                "Pinterest에서 비슷한 코디 더 찾아보기 🔎",
                pinterest_url,
                use_container_width=True
            )

        with text_col:
            st.markdown(
                f'<div class="outfit-name">✨ {outfit_data["title"]}</div>',
                unsafe_allow_html=True
            )

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

            with st.expander("이미지 생성 프롬프트 보기"):
                st.write(prompt)


# =========================================================
# 세션 상태
# =========================================================
if "seed_offset" not in st.session_state:
    st.session_state.seed_offset = 0

# =========================================================
# 제목
# =========================================================
st.markdown('<div class="main-title">MBTI 코디 이미지 추천기 👗👕</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">MBTI를 선택하면 어울리는 남자 코디와 여자 코디를 이미지로 보여줄게요 ✨</div>',
    unsafe_allow_html=True
)

# =========================================================
# 안내
# =========================================================
with st.expander("이미지 사용 안내 📌"):
    st.markdown(
        """
        <div class="notice">
        Pinterest 이미지를 앱에서 자동으로 가져와 직접 보여주는 것은 저작권이나 서비스 약관 문제가 생길 수 있어요.<br>
        그래서 이 앱은 추천한 옷 아이템을 바탕으로 코디 이미지를 생성해서 보여주고,
        추가 탐색은 Pinterest 검색 버튼으로 연결하는 방식입니다.<br><br>
        이미지가 마음에 들지 않으면 <b>이미지 다시 만들기</b> 버튼을 눌러 다른 코디 이미지로 바꿀 수 있어요.
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# 선택 영역
# =========================================================
st.markdown('<div class="cute-box">', unsafe_allow_html=True)

select_col1, select_col2, select_col3 = st.columns([1.1, 1.1, 0.8], gap="large")

with select_col1:
    mbti_list = list(outfits.keys())
    selected_mbti = st.selectbox(
        "MBTI를 선택해 주세요 💌",
        mbti_list,
        index=0
    )

with select_col2:
    image_style = st.radio(
        "이미지 스타일을 선택해 주세요 🖼️",
        ["모델 착용샷", "옷만 플랫레이"],
        horizontal=True
    )

with select_col3:
    st.write("")
    st.write("")
    if st.button("이미지 다시 만들기 🎲", use_container_width=True):
        st.session_state.seed_offset = random.randint(1, 99999)

st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# 선택 결과 표시
# =========================================================
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

# =========================================================
# 코디 카드
# =========================================================
mbti_index = mbti_list.index(selected_mbti)

male_seed = 10000 + mbti_index * 10 + st.session_state.seed_offset
female_seed = 20000 + mbti_index * 10 + st.session_state.seed_offset

col1, col2 = st.columns(2, gap="large")

with col1:
    render_outfit_card(
        gender_label="🧑 남자",
        gender_key="male",
        outfit_data=selected_data["male"],
        mbti=selected_mbti,
        mood=selected_data["mood"],
        image_style=image_style,
        seed=male_seed
    )

with col2:
    render_outfit_card(
        gender_label="👩 여자",
        gender_key="female",
        outfit_data=selected_data["female"],
        mbti=selected_mbti,
        mood=selected_data["mood"],
        image_style=image_style,
        seed=female_seed
    )

# =========================================================
# 확장 아이디어
# =========================================================
st.write("")
with st.expander("프로젝트를 더 발전시키는 아이디어 🌱"):
    st.write("1. 계절 선택 추가하기: 봄, 여름, 가을, 겨울")
    st.write("2. 상황 선택 추가하기: 학교, 데이트, 여행, 발표")
    st.write("3. 색상 팔레트 추천 추가하기")
    st.write("4. 사용자가 직접 원하는 스타일 키워드를 입력하게 만들기")
    st.write("5. 마음에 드는 코디를 저장하는 기능 만들기")

st.markdown(
    """
    <div class="footer">
        Made with Streamlit 💗 | MBTI 코디 추천은 재미용이에요 🌈
    </div>
    """,
    unsafe_allow_html=True
)
