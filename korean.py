import streamlit as st
import base64
from pathlib import Path

# from gtts import gTTS
# from io import BytesIO


st.set_page_config(
    page_title="Ôn tập tiếng Hàn",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ── Enhanced Styling ──────────────────────────────────────────────
def apply_theme():
        st.markdown("""
        <style>
            table.custom-table {
                width: 100%;
                border-collapse: collapse;
            }
            table.custom-table th, table.custom-table td {
                padding: 8px;
                border-bottom: 1px solid #ddd;
                text-align: left;
            }
            table.custom-table th {
                background-color: #f2f2f2;
            }
            audio {
                width: 100px;
                height: 30px;
            }
            .positive {background-color: #d4edda; border-left: 5px solid #28a745;}
            .neutral {background-color: #fff3cd; border-left: 5px solid #ffc107;}
            .negative {background-color: #f8d7da; border-left: 5px solid #dc3545;}
            
        </style>
        """, unsafe_allow_html=True)

apply_theme()



#-- Header Section ──────────────────────────────────────────────
st.title("📖 Ôn tập tiếng Hàn")
st.markdown("Chào mừng bạn đến với trang ôn tập tiếng Hàn! \
            Dưới đây là tổng hợp một số từ vựng và ngữ pháp từ chương trình học")

def display_audio_only(audio_file_path):
    # Read and encode the audio file to base64
    with open(audio_file_path, "rb") as f:
        data = f.read()
        b64_audio = base64.b64encode(data).decode()
        
    # HTML5 audio element with hidden controls and autoplay
    audio_html = f"""
        <audio autoplay="true" hidden="true">
            <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs([
    "📜Bài 1",
    "📜Bài 2",
    "📜Bài 3"
])

with tab1:
    st.header("Bài 1: Giới thiệu")
    st.markdown('### Từ vựng')

    # --- Define data (data layer) ---
    rows = [
        {"Từ vựng": "바다", "Nghĩa": "Biển", "audio": "Files/Lesson1/bien.mp3"},
        {"Từ vựng": "오이", "Nghĩa": "Dưa leo", "audio": "Files/Lesson1/oi.mp3"},
        {"Từ vựng": "우유", "Nghĩa": "Sữa", "audio": "Files/Lesson1/uyu.mp3"},
        {"Từ vựng": "아이", "Nghĩa": "Trẻ em", "audio": "Files/Lesson1/ai.mp3"},
        {"Từ vựng": "여우", "Nghĩa": "Con cáo", "audio": "Files/Lesson1/yeou.mp3"},
        {"Từ vựng": "고기", "Nghĩa": "Thịt", "audio": "Files/Lesson1/gogi.mp3"},
        {"Từ vựng": "나무", "Nghĩa": "Cây cối", "audio": "Files/Lesson1/namu.mp3"},
        {"Từ vựng": "기구", "Nghĩa": "Dụng cụ", "audio": "Files/Lesson1/gigu.mp3"},
        {"Từ vựng": "소", "Nghĩa": "Con bò", "audio": "Files/Lesson1/so.mp3"},
        {"Từ vựng": "소고기", "Nghĩa": "Thịt bò", "audio": "Files/Lesson1/so_gogi.mp3"},
        {"Từ vựng": "버스", "Nghĩa": "Xe buýt", "audio": "Files/Lesson1/bose.mp3"},
        {"Từ vựng": "커피", "Nghĩa": "Cà phê", "audio": "Files/Lesson1/coffee.mp3"},
        {"Từ vựng": "스키", "Nghĩa": "Trượt tuyết", "audio": "Files/Lesson1/ski.mp3"},
        {"Từ vựng": "오토바이", "Nghĩa": "Xe máy", "audio": "Files/Lesson1/otobai.mp3"},
        {"Từ vựng": "아파트", "Nghĩa": "Chung cư", "audio": "Files/Lesson1/apart.mp3"},
        {"Từ vựng": "파", "Nghĩa": "Hành lá", "audio": "Files/Lesson1/par.mp3"},
        {"Từ vựng": "치마", "Nghĩa": "Váy", "audio": "Files/Lesson1/chim.mp3"},
        {"Từ vựng": "포도", "Nghĩa": "Nho", "audio": "Files/Lesson1/podo.mp3"},
        {"Từ vựng": "피자", "Nghĩa": "Pizza", "audio": "Files/Lesson1/pizza.mp3"},
        {"Từ vựng": "기차", "Nghĩa": "Tàu hỏa", "audio": "Files/Lesson1/gicha.mp3"},
        {"Từ vựng": "아저씨", "Nghĩa": "Chú, ông chú", "audio": "Files/Lesson1/ajusshi.mp3"},
        {"Từ vựng": "토끼", "Nghĩa": "Con thỏ", "audio": "Files/Lesson1/tori.mp3"},
        {"Từ vựng": "아빠", "Nghĩa": "Cha", "audio": "Files/Lesson1/appa.mp3"},
        {"Từ vựng": "오빠", "Nghĩa": "Anh trai", "audio": "Files/Lesson1/oppa.mp3"},
        {"Từ vựng": "떡", "Nghĩa": "Bánh gạo", "audio": "Files/Lesson1/duk.mp3"},
        {"Từ vựng": "빵", "Nghĩa": "Bánh mì", "audio": "Files/Lesson1/bang.mp3"},
        {"Từ vựng": "딸기", "Nghĩa": "Dâu tây", "audio": "Files/Lesson1/ddakgi.mp3"},
        {"Từ vựng": "배", "Nghĩa": "Tàu, quả lê", "audio": "Files/Lesson1/bae.mp3"},
        {"Từ vựng": "개", "Nghĩa": "Chó", "audio": "Files/Lesson1/gae.mp3"},
        {"Từ vựng": "얘기", "Nghĩa": "Trò chuyện", "audio": "Files/Lesson1/yegi.mp3"},
        {"Từ vựng": "세계", "Nghĩa": "Thế giới", "audio": "Files/Lesson1/segye.mp3"},
        {"Từ vựng": "게", "Nghĩa": "Cua", "audio": "Files/Lesson1/ge.mp3"},
        {"Từ vựng": "카메라", "Nghĩa": "Máy ảnh", "audio": "Files/Lesson1/camera.mp3"},
        {"Từ vựng": "사과", "Nghĩa": "Quả táo", "audio": "Files/Lesson1/sagoa.mp3"},
        {"Từ vựng": "휴지", "Nghĩa": "Khăn giấy", "audio": "Files/Lesson1/haeji.mp3"},
        {"Từ vựng": "모자", "Nghĩa": "Mũ", "audio": "Files/Lesson1/moja.mp3"},
        {"Từ vựng": "바지", "Nghĩa": "Quần", "audio": "Files/Lesson1/baji.mp3"},
        {"Từ vựng": "의자", "Nghĩa": "Cái ghế", "audio": "Files/Lesson1/uija.mp3"},
        {"Từ vựng": "한국", "Nghĩa": "Hàn Quốc", "audio": "Files/Lesson1/hanguk.mp3"},
        {"Từ vựng": "중국", "Nghĩa": "Trung Quốc", "audio": "Files/Lesson1/zhongguo.mp3"},
        {"Từ vựng": "베트남", "Nghĩa": "Việt Nam", "audio": "Files/Lesson1/betnam.mp3"},
        {"Từ vựng": "말레이시아", "Nghĩa": "Malaysia", "audio": "Files/Lesson1/maleysiya.mp3"},
        {"Từ vựng": "일본", "Nghĩa": "Nhật Bản", "audio": "Files/Lesson1/ilbon.mp3"},
        {"Từ vựng": "미국", "Nghĩa": "Mỹ", "audio": "Files/Lesson1/miguk.mp3"},
        {"Từ vựng": "태국", "Nghĩa": "Thái Lan", "audio": "Files/Lesson1/taeguk.mp3"},
        {"Từ vựng": "호주", "Nghĩa": "Úc", "audio": "Files/Lesson1/hoju.mp3"},
        {"Từ vựng": "몽고", "Nghĩa": "Mông Cổ", "audio": "Files/Lesson1/monggo.mp3"},
        {"Từ vựng": "인도네시아", "Nghĩa": "Indonesia", "audio": "Files/Lesson1/indo.mp3"},
        {"Từ vựng": "필리핀", "Nghĩa": "Philippines", "audio": "Files/Lesson1/filipin.mp3"},
        {"Từ vựng": "인도", "Nghĩa": "Ấn Độ", "audio": "Files/Lesson1/indu.mp3"},
        {"Từ vựng": "영국", "Nghĩa": "Anh", "audio": "Files/Lesson1/yeongguk.mp3"},
        {"Từ vựng": "독일", "Nghĩa": "Đức", "audio": "Files/Lesson1/dokil.mp3"},
        {"Từ vựng": "프랑스", "Nghĩa": "Pháp", "audio": "Files/Lesson1/france.mp3"},
        {"Từ vựng": "러시아", "Nghĩa": "Nga", "audio": "Files/Lesson1/nga.mp3"},
        {"Từ vựng": "학생", "Nghĩa": "Học sinh", "audio": "Files/Lesson1/hs.mp3"},
        {"Từ vựng": "회사원", "Nghĩa": "Nhân viên công ty", "audio": "Files/Lesson1/nvcty.mp3"},
        {"Từ vựng": "은행원", "Nghĩa": "Nhân viên ngân hàng", "audio": "Files/Lesson1/nvnh.mp3"},
        {"Từ vựng": "선생님", "Nghĩa": "Giáo viên", "audio": "Files/Lesson1/gv.mp3"},
        {"Từ vựng": "공무원", "Nghĩa": "Nhân viên công vụ", "audio": "Files/Lesson1/gongmowon.mp3"},
        {"Từ vựng": "관광가이드", "Nghĩa": "Hướng dẫn viên du lịch", "audio": "Files/Lesson1/hdvdl.mp3"},
        {"Từ vựng": "관광안내원", "Nghĩa": "Hướng dẫn viên du lịch", "audio": "Files/Lesson1/hdvdl2.mp3"},
        {"Từ vựng": "의사", "Nghĩa": "Bác sĩ", "audio": "Files/Lesson1/uisa.mp3"},
        {"Từ vựng": "주부", "Nghĩa": "Nội trợ", "audio": "Files/Lesson1/jubu.mp3"},
        {"Từ vựng": "약사", "Nghĩa": "Dược sĩ", "audio": "Files/Lesson1/aksa.mp3"},
        {"Từ vựng": "운전기사", "Nghĩa": "Lái xe", "audio": "Files/Lesson1/laixe.mp3"},
        {"Từ vựng": "안녕하세요?", "Nghĩa": "Xin chào", "audio": "Files/Lesson1/annyeonghaseyo.mp3"},
        {"Từ vựng": "안녕하십니까?", "Nghĩa": "Xin chào", "audio": "Files/Lesson1/khoehong.mp3"},
        {"Từ vựng": "안녕히 가세요", "Nghĩa": "Tạm biệt, đi về bình an", "audio": "Files/Lesson1/tambiet1.mp3"},
        {"Từ vựng": "안녕히 계세요", "Nghĩa": "Tạm biệt, ở lại bình an", "audio": "Files/Lesson1/tambiet2.mp3"},
        {"Từ vựng": "처음 뵙겠습니다", "Nghĩa": "Rất hân hạnh được gặp bạn", "audio": "Files/Lesson1/rathanhanh.mp3"},
        {"Từ vựng": "반갑습니다", "Nghĩa": "Rất vui được gặp bạn", "audio": "Files/Lesson1/ratvuigapban.mp3"}
    ]

    root = Path(__file__).resolve().parent

    def audio_to_data_uri(path: str) -> str:
        file_path = root / path
        with open(file_path, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return f"data:audio/mp3;base64,{encoded}"

    table_rows = ""
    for row in rows:
        audio_uri = audio_to_data_uri(row["audio"])
        table_rows += f"""
        <tr>
            <td><strong>{row['Từ vựng']}</strong></td>
            <td>{row['Nghĩa']}</td>
            <td class=\"audio-cell\"><button class=\"play-btn\" data-src=\"{audio_uri}\">▶</button></td>
        </tr>
        """

    table_html = f"""
    <div style=\"overflow-x:auto; width:100%;\">
        <style>
            table tr td {{
                padding: 12px;
                border: 1px solid #ddd;
                vertical-align: middle;
            }}
            table tr th {{
                padding: 12px;
                border: 1px solid #ddd;
                background: #f2f2f2;
                font-weight: bold;
            }}
            .audio-cell .play-btn {{
                font-size: 10px;
                padding: 8px 12px;
                border-radius: 6px;
                border: none;
                background: #007bff;
                color: white;
                cursor: pointer;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                min-width: 22px;
            }}
            .audio-cell .play-btn.playing {{
                background: #28a745;
            }}
            @media (max-width: 720px) {{
                table {{ min-width: 300px; }}
                .audio-cell .play-btn {{
                    font-size: 10px;
                    min-width: 22px;
                    padding: 8px 12px;
                }}
            }}
        </style>

        <table style=\"width:100%; border-collapse: collapse; min-width: 300px;\">
            <thead>
                <tr>
                    <th>Từ vựng</th>
                    <th>Nghĩa</th>
                    <th>Audio</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>

        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                const buttons = document.querySelectorAll('.play-btn');
                let currentAudio = null;
                let currentBtn = null;
                buttons.forEach(btn => {{
                    btn.addEventListener('click', function() {{
                        const src = btn.getAttribute('data-src');
                        if (currentAudio && !currentAudio.paused && currentAudio.src === src) {{
                            currentAudio.pause();
                            btn.classList.remove('playing');
                            return;
                        }}
                        if (currentAudio) {{
                            currentAudio.pause();
                            if (currentBtn) currentBtn.classList.remove('playing');
                        }}
                        const audio = new Audio(src);
                        currentAudio = audio;
                        currentBtn = btn;
                        btn.classList.add('playing');
                        audio.play().catch(() => {{ btn.classList.remove('playing'); }});
                        audio.addEventListener('ended', function() {{ btn.classList.remove('playing'); }});
                        audio.addEventListener('pause', function() {{ btn.classList.remove('playing'); }});
                    }});
                }});
            }});
        </script>
    </div>
    """

    st.iframe(table_html, height=len(rows) * 56)



    st.markdown('### Ngữ pháp')
    st.markdown(
        "- <span style='color: red; font-size: 18px; font-weight: bold;'>N (danh từ) + 입니다</span>"
        "<span style='color: #555; font-size: 16px;'>: là + N (danh từ)</span>.",
        # "<span style='font-family: Courier; background-color: #f0f2f6; padding: 2px 6px;'>: là cái gì</span>.", 
        unsafe_allow_html=True
    )
    st.markdown(
        "- <span style='color: red; font-size: 18px; font-weight: bold;'>N (danh từ) + 입니까?</span>"
        "<span style='color: #555; font-size: 16px;'>: là N (danh từ) phải không?</span>.",
        # "<span style='font-family: Courier; background-color: #f0f2f6; padding: 2px 6px;'>: là cái gì</span>.", 
        unsafe_allow_html=True
    )
    st.markdown(
        "- <span style='color: red; font-size: 18px; font-weight: bold;'> N (danh từ) + 은/는</span>"
        "<span style='color: #555; font-size: 16px;'>: danh từ có patchim + :red[은]; danh từ không có patchim + :green[는]</span>.",
        # "<span style='font-family: Courier; background-color: #f0f2f6; padding: 2px 6px;'>: là cái gì</span>.", 
        unsafe_allow_html=True
    )
    st.markdown('##### Ví dụ:')   
    st.markdown('''- **화입니다** - Tôi là Hoa''')  
    st.audio(root / "Files/Lesson1/hoa.mp3", format="audio/mp3")
    st.markdown('''- **저는 학생입니다** - Tôi là học sinh''')
    st.audio(root / "Files/Lesson1/lahs.mp3", format="audio/mp3")
    st.markdown('''- **저는 회사원입니다** - Tôi là nhân viên công ty''')
    st.audio(root / "Files/Lesson1/lanvcty.mp3", format="audio/mp3")
    st.markdown('''- **저는 은행원입니다** - Tôi là nhân viên ngân hàng''')
    st.audio(root / "Files/Lesson1/lanvnh.mp3", format="audio/mp3")
    st.markdown('''- **저는 선생님입니다** - Tôi là giáo viên''') 
    st.audio(root / "Files/Lesson1/lagv.mp3", format="audio/mp3")
    st.markdown('''- **저는 베트남 사람입니다** - Tôi là người Việt Nam''')
    st.audio(root / "Files/Lesson1/lanvn.mp3", format="audio/mp3")
    st.markdown('''- **저는 말레이시아 사람입니다** - Tôi là người Malaysia''')
    st.audio(root / "Files/Lesson1/lanml.mp3", format="audio/mp3")
    st.markdown('''- **저는 일본 사람입니다** - Tôi là người Nhật Bản''')
    st.audio(root / "Files/Lesson1/lannb.mp3", format="audio/mp3")
    st.divider()
    st.markdown('''- **의사입니까?** - Bạn là bác sĩ phải không?''')
    st.audio(root / "Files/Lesson1/bacsipk.mp3", format="audio/mp3")
    st.markdown('''- **주부입니까?** - Bạn là nội trợ phải không?''')
    st.audio(root / "Files/Lesson1/lantpk.mp3", format="audio/mp3")
    st.markdown('''- **공무원입니까?** - Bạn là nhân viên công vụ phải không?''')
    st.audio(root / "Files/Lesson1/lanvcvpk.mp3", format="audio/mp3")
    st.markdown('''- **관광가이드입니까?** - Bạn là hướng dẫn viên du lịch phải không?''')
    st.audio(root / "Files/Lesson1/hdvdlpk.mp3", format="audio/mp3")
    st.markdown('''- **한국 사람입니까?** - Bạn là người Hàn Quốc phải không?''')
    st.audio(root / "Files/Lesson1/lahqpk.mp3", format="audio/mp3")
    st.divider()
    st.markdown('''- **제 이름은 흐엉입니다** - Tên tôi là Hương''')
    st.audio(root / "Files/Lesson1/huong.mp3", format="audio/mp3")
    st.markdown('''- **선생님은 한국 사람입니까?** - Giáo viên là người Hàn Quốc phải không?''')
    st.audio(root / "Files/Lesson1/gvhq.mp3", format="audio/mp3")

    st.divider()
    st.markdown('''- **남 씨는 약사 입니까?** - Anh Nam là dược sĩ phải không?''')
    st.audio(root / "Files/Lesson1/nam1.mp3", format="audio/mp3")
    st.markdown('''- **네, 남 씨는 약사입니다** - Vâng, anh Nam là dược sĩ''')
    st.audio(root / "Files/Lesson1/nam2.mp3", format="audio/mp3")
    st.markdown('''- **아니요, 남 씨는 약사가 아닙니다** - Không, anh Nam không phải là dược sĩ''')
    st.audio(root / "Files/Lesson1/nam3.mp3", format="audio/mp3")
    st.divider()
    st.markdown('''- **박준영 씨, 이 사람은 풍 씨입니다** - Anh Park Jun Young, đây là chị Phụng''')
    st.audio(root / "Files/Lesson1/phung1.mp3", format="audio/mp3")
    st.markdown('''- **풍 씨, 이 사람은 박준영 씨입니다** - Chị Phụng, đây là anh Park Jun Young''')
    st.audio(root / "Files/Lesson1/phung2.mp3", format="audio/mp3")
    st.markdown('''- **안녕하세요? 박준영입니다** - Xin chào? Tôi là Park Jun Young''')
    st.audio(root / "Files/Lesson1/phung3.mp3", format="audio/mp3")
    st.markdown('''- **안녕하세요? 제 이름은 풍 입니다** - Xin chào? Tôi là Phụng''')
    st.audio(root / "Files/Lesson1/phung4.mp3", format="audio/mp3")
    st.markdown('''- **반갑습니다** - Rất vui được gặp bạn''')
    st.audio(root / "Files/Lesson1/phung5.mp3", format="audio/mp3")


with tab2:
    st.header("Bài 2: Trường học")
    st.markdown('### Từ vựng')

    # --- Define data (data layer) ---
    rows = [
        {"Từ vựng": "학교", "Nghĩa": "Trường học", "audio": "Files/Lesson2/school.mp3"},
        {"Từ vựng": "극장", "Nghĩa": "Rạp chiếu phim", "audio": "Files/Lesson2/theater.mp3"},
        {"Từ vựng": "백화점", "Nghĩa": "Trung tâm thương mại", "audio": "Files/Lesson2/supermarket.mp3"},
        {"Từ vựng": "도서관", "Nghĩa": "Thư viện", "audio": "Files/Lesson2/library.mp3"},
        {"Từ vựng": "우체국", "Nghĩa": "Bưu điện", "audio": "Files/Lesson2/post_office.mp3"},
        {"Từ vựng": "약국", "Nghĩa": "Nhà thuốc", "audio": "Files/Lesson2/pharmacy.mp3"},
        {"Từ vựng": "식당", "Nghĩa": "Nhà hàng", "audio": "Files/Lesson2/restaurant.mp3"},
        {"Từ vựng": "병원", "Nghĩa": "Bệnh viện", "audio": "Files/Lesson2/hospital.mp3"},
        {"Từ vựng": "가게", "Nghĩa": "Cửa hàng", "audio": "Files/Lesson2/gage.mp3"},
        {"Từ vựng": "호텔", "Nghĩa": "Khách sạn", "audio": "Files/Lesson2/hotel.mp3"},
        {"Từ vựng": "은행", "Nghĩa": "Ngân hàng", "audio": "Files/Lesson2/bank.mp3"},
        {"Từ vựng": "사무실", "Nghĩa": "Văn phòng", "audio": "Files/Lesson2/office.mp3"},
        {"Từ vựng": "강의실", "Nghĩa": "Giảng đường", "audio": "Files/Lesson2/lecture_hall.mp3"},
        {"Từ vựng": "교실", "Nghĩa": "Phòng học", "audio": "Files/Lesson2/classroom.mp3"},
        {"Từ vựng": "랩실(어학실)", "Nghĩa": "Phòng lab", "audio": "Files/Lesson2/lab.mp3"},
        {"Từ vựng": "강당", "Nghĩa": "Hội trường", "audio": "Files/Lesson2/auditorium.mp3"},
        {"Từ vựng": "동아리방", "Nghĩa": "Phòng câu lạc bộ", "audio": "Files/Lesson2/club.mp3"},
        {"Từ vựng": "학생 식당", "Nghĩa": "Nhà ăn học sinh", "audio": "Files/Lesson2/canteen.mp3"},
        {"Từ vựng": "화장실", "Nghĩa": "Phòng vệ sinh", "audio": "Files/Lesson2/restroom.mp3"},
        {"Từ vựng": "체육관", "Nghĩa": "Sân vận động", "audio": "Files/Lesson2/nhathethao.mp3"},
        {"Từ vựng": "세미나실", "Nghĩa": "Phòng seminar", "audio": "Files/Lesson2/seminar_room.mp3"},
        {"Từ vựng": "휴게실", "Nghĩa": "Phòng nghỉ", "audio": "Files/Lesson2/rest_room.mp3"},
        {"Từ vựng": "운동장", "Nghĩa": "Sân vận động", "audio": "Files/Lesson2/sanvdong.mp3"},
        {"Từ vựng": "서점", "Nghĩa": "Hiệu sách", "audio": "Files/Lesson2/bookstore.mp3"},
        {"Từ vựng": "책상", "Nghĩa": "Bàn học", "audio": "Files/Lesson2/desk.mp3"},
        {"Từ vựng": "창문", "Nghĩa": "Cửa sổ", "audio": "Files/Lesson2/window.mp3"},
        {"Từ vựng": "지도", "Nghĩa": "Bản đồ", "audio": "Files/Lesson2/map.mp3"},
        {"Từ vựng": "공책", "Nghĩa": "Vở", "audio": "Files/Lesson2/notebook.mp3"},
        {"Từ vựng": "칠판", "Nghĩa": "Bảng đen", "audio": "Files/Lesson2/chilpan.mp3"},
        {"Từ vựng": "가방", "Nghĩa": "Túi xách", "audio": "Files/Lesson2/gabang.mp3"},
        {"Từ vựng": "사전", "Nghĩa": "Từ điển", "audio": "Files/Lesson2/sajeon.mp3"},
        {"Từ vựng": "필통", "Nghĩa": "Hộp bút", "audio": "Files/Lesson2/pencil_case.mp3"},
        {"Từ vựng": "컴퓨터", "Nghĩa": "Máy tính", "audio": "Files/Lesson2/computer.mp3"},
        {"Từ vựng": "지우개", "Nghĩa": "Cục tẩy", "audio": "Files/Lesson2/eraser.mp3"},
        {"Từ vựng": "펜", "Nghĩa": "Bút", "audio": "Files/Lesson2/pen.mp3"},
        {"Từ vựng": "책", "Nghĩa": "Sách", "audio": "Files/Lesson2/book.mp3"},
        {"Từ vựng": "시계", "Nghĩa": "Đồng hồ", "audio": "Files/Lesson2/clock.mp3"},
        {"Từ vựng": "문", "Nghĩa": "Cửa", "audio": "Files/Lesson2/door.mp3"},

        {"Từ vựng": "라디오", "Nghĩa": "Đài phát thanh", "audio": "Files/Lesson2/radio.mp3"},
        {"Từ vựng": "많이", "Nghĩa": "Nhiều", "audio": "Files/Lesson2/many.mp3"},
        {"Từ vựng": "무엇", "Nghĩa": "Gì", "audio": "Files/Lesson2/mueot.mp3"},
        {"Từ vựng": "어디", "Nghĩa": "Đâu", "audio": "Files/Lesson2/eodi.mp3"},
        {"Từ vựng": "텔레비전", "Nghĩa": "Tivi", "audio": "Files/Lesson2/television.mp3"},
        {"Từ vựng": "휴대전화", "Nghĩa": "Điện thoại di động", "audio": "Files/Lesson2/mobile_phone.mp3"}
        
    ]

    root = Path(__file__).resolve().parent

    def audio_to_data_uri(path: str) -> str:
        file_path = root / path
        with open(file_path, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return f"data:audio/mp3;base64,{encoded}"

    table_rows = ""
    for row in rows:
        audio_uri = audio_to_data_uri(row["audio"])
        table_rows += f"""
        <tr>
            <td><strong>{row['Từ vựng']}</strong></td>
            <td>{row['Nghĩa']}</td>
            <td class=\"audio-cell\"><button class=\"play-btn\" data-src=\"{audio_uri}\">▶</button></td>
        </tr>
        """

    table_html = f"""
    <div style=\"overflow-x:auto; width:100%;\">
        <style>
            table tr td {{
                padding: 12px;
                border: 1px solid #ddd;
                vertical-align: middle;
            }}
            table tr th {{
                padding: 12px;
                border: 1px solid #ddd;
                background: #f2f2f2;
                font-weight: bold;
            }}
            .audio-cell .play-btn {{
                font-size: 10px;
                padding: 8px 12px;
                border-radius: 6px;
                border: none;
                background: #007bff;
                color: white;
                cursor: pointer;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                min-width: 22px;
            }}
            .audio-cell .play-btn.playing {{
                background: #28a745;
            }}
            @media (max-width: 720px) {{
                table {{ min-width: 300px; }}
                .audio-cell .play-btn {{
                    font-size: 10px;
                    min-width: 22px;
                    padding: 8px 12px;
                }}
            }}
        </style>

        <table style=\"width:100%; border-collapse: collapse; min-width: 300px;\">
            <thead>
                <tr>
                    <th>Từ vựng</th>
                    <th>Nghĩa</th>
                    <th>Audio</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>

        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                const buttons = document.querySelectorAll('.play-btn');
                let currentAudio = null;
                let currentBtn = null;
                buttons.forEach(btn => {{
                    btn.addEventListener('click', function() {{
                        const src = btn.getAttribute('data-src');
                        if (currentAudio && !currentAudio.paused && currentAudio.src === src) {{
                            currentAudio.pause();
                            btn.classList.remove('playing');
                            return;
                        }}
                        if (currentAudio) {{
                            currentAudio.pause();
                            if (currentBtn) currentBtn.classList.remove('playing');
                        }}
                        const audio = new Audio(src);
                        currentAudio = audio;
                        currentBtn = btn;
                        btn.classList.add('playing');
                        audio.play().catch(() => {{ btn.classList.remove('playing'); }});
                        audio.addEventListener('ended', function() {{ btn.classList.remove('playing'); }});
                        audio.addEventListener('pause', function() {{ btn.classList.remove('playing'); }});
                    }});
                }});
            }});
        </script>
    </div>
    """

    st.iframe(table_html, height=len(rows) * 56)



    st.markdown('### Ngữ pháp')
    st.markdown(
        "**1.** <span style=' font-size: 20px; font-weight: bold;'>:red[여기] / :red[거기] / :red[저기] + :blue[는] + N (nơi chốn) + :green[입니다]/:orange[입니까?]</span>"
        "<span style='color: #555; font-size: 16px;'>: Đây/Đó/Kia là + N (nơi chốn)</span>.",
        # "<span style='font-family: Courier; background-color: #f0f2f6; padding: 2px 6px;'>: là cái gì</span>.", 
        unsafe_allow_html=True
    )
    st.markdown('''**Ví dụ:** ''')
    st.markdown('''- **:red[여기]:blue[는] 학교:green[입니다]** - Đây là trường học''')
    st.audio(root / "Files/Lesson2/vidu1.mp3", format="audio/mp3")

    st.markdown('''- **:red[저기]:blue[는] 도서관:green[입니다]** - Kia là thư viện''')
    st.audio(root / "Files/Lesson2/vidu2.mp3", format="audio/mp3")

    st.markdown('''- **:red[거기]:blue[는] 병원:green[입니다]** - Đó là bệnh viện''')
    st.audio(root / "Files/Lesson2/vidu3.mp3", format="audio/mp3")

    st.markdown('''- **:red[여기]:blue[는] 강의실:orange[입니까?]** - Đây là giảng đường phải không?''')
    st.audio(root / "Files/Lesson2/vidu4.mp3", format="audio/mp3")

    st.markdown('''- **:red[저기]:blue[는] 사무실:orange[입니까?]** - Kia là văn phòng phải không?''')
    st.audio(root / "Files/Lesson2/vidu5.mp3", format="audio/mp3")

    st.markdown('''- **:red[거기]:blue[는] 화장실:orange[입니까?]** - Đó là phòng vệ sinh phải không?''')
    st.audio(root / "Files/Lesson2/vidu6.mp3", format="audio/mp3")
    st.divider()
    st.markdown(
        "**2.** <span style=' font-size: 20px; font-weight: bold;'>:red[이것] / :red[그것] / :red[저것] + :violet[은] + :N (đồ vật) + :green[입니다]/:orange[입니까?]</span>"
        "<span style='color: #555; font-size: 16px;'>: Cái này/Cái đó/Cái kia là + N (đồ vật)</span>.",
        # "<span style='font-family: Courier; background-color: #f0f2f6; padding: 2px 6px;'>: là cái gì</span>.", 
        unsafe_allow_html=True
    )
    st.markdown('''**Ví dụ:** ''')
    st.markdown('''- **:red[이것]:violet[은] 책:green[입니다]** - Cái này là sách''')
    st.audio(root / "Files/Lesson2/vidu7.mp3", format="audio/mp3")

    st.markdown('''- **:red[그것]:violet[은] 컴퓨터:green[입니다]** - Cái đó là máy tính''')
    st.audio(root / "Files/Lesson2/vidu8.mp3", format="audio/mp3")

    st.markdown('''- **:red[저것]:violet[은] 시계:green[입니다]** - Cái kia là đồng hồ''')
    st.audio(root / "Files/Lesson2/vidu9.mp3", format="audio/mp3")

    st.markdown('''- **:red[이것]:violet[은] 펜:orange[입니까?]** - Cái này là bút phải không?''')
    st.audio(root / "Files/Lesson2/vidu10.mp3", format="audio/mp3")

    st.markdown('''- **:red[그것]:violet[은] 지우개:orange[입니까?]** - Cái đó là cục tẩy phải không?''')
    st.audio(root / "Files/Lesson2/vidu11.mp3", format="audio/mp3")

    st.markdown('''- **:red[저것]:violet[은] 가방:orange[입니까?]** - Cái kia là túi xách phải không?''')
    st.audio(root / "Files/Lesson2/vidu12.mp3", format="audio/mp3")
    st.divider()


    st.markdown(
        "**3.**\n"
        "- <span style='font-size: 20px; font-weight: bold;'> N (danh từ) (có patchim) + :red[이] + :green[있습니다]/:orange[없습니다]</span>"
        "<span style='color: #555; font-size: 16px;'>: có N  / không có N </span>.\n"
        "- <span style='font-size: 20px; font-weight: bold;'> N (danh từ) (không patchim) + :red[가] + :green[있습니다]/:orange[없습니다]</span>"
        "<span style='color: #555; font-size: 16px;'>: có N  / không có N </span>.",
        # "<span style='font-family: Courier; background-color: #f0f2f6; padding: 2px 6px;'>: là cái gì</span>.", 
        unsafe_allow_html=True
    )
    st.markdown('''**Ví dụ:**''')   
    st.markdown('''- **책:red[이] 있습니다** - Có sách''')
    st.audio(root / "Files/Lesson2/vidu13.mp3", format="audio/mp3")
    st.markdown('''- **컴퓨터:red[가] 있습니다** - Có máy tính''')    
    st.audio(root / "Files/Lesson2/vidu14.mp3", format="audio/mp3")
    st.markdown('''- **시계:red[가] 있습니다** - Có đồng hồ''')
    st.audio(root / "Files/Lesson2/vidu15.mp3", format="audio/mp3") 
    st.markdown('''- **펜:red[이] 없습니다** - Không có bút''')
    st.audio(root / "Files/Lesson2/vidu16.mp3", format="audio/mp3")
    st.markdown('''- **지우개:red[가] 없습니다** - Không có cục tẩy''')
    st.audio(root / "Files/Lesson2/vidu17.mp3", format="   audio/mp3")
    st.markdown('''- **가방:red[이] 없습니다** - Không có túi xách''')
    st.audio(root / "Files/Lesson2/vidu18.mp3", format="audio/mp3")

    st.divider()

    st.markdown(
        "**4.** <span style=' font-size: 20px; font-weight: bold;'>:red[에] :green[있습니다]/:orange[있습니까?]</span>"
        "<span style='color: #555; font-size: 16px;'>: có ở ...</span>.",
        # "<span style='font-family: Courier; background-color: #f0f2f6; padding: 2px 6px;'>: là cái gì</span>.", 
        unsafe_allow_html=True
    )
    st.markdown('''**Ví dụ:**''')
    st.markdown('''- **학교:red[에] 있습니다** - Có ở trường học''')
    st.audio(root / "Files/Lesson2/vidu19.mp3", format="audio/mp3")
    st.markdown('''- **도서관:red[에] 있습니까?** - Có ở thư viện phải không?''')
    st.audio(root / "Files/Lesson2/vidu20.mp3", format="audio/mp3")
    st.markdown('''- **병원:red[에] 컴퓨터:green[가] 있습니까?** - Có máy tính ở bệnh viện không?''')
    st.audio(root / "Files/Lesson2/vidu21.mp3", format="audio/mp3")
    st.markdown('''- **아니요, 병원:red[에] 컴퓨터:green[가] 없습니다** - Không, không có máy tính ở bệnh viện''')
    st.audio(root / "Files/Lesson2/vidu22.mp3", format="audio/mp3")
    st.markdown('''- **네, 병원:red[에] 컴퓨터:green[가] 있습니다** - Vâng, có máy tính ở bệnh viện''')
    st.audio(root / "Files/Lesson2/vidu23.mp3", format="audio/mp3")

    st.divider()

    st.markdown(
        "**5.** <span style=' font-size: 20px; font-weight: bold;'>N (danh từ) + :red[이]/:green[가] + :blue[아]닙니다]</span>"
        "<span style='color: #555; font-size: 16px;'>: không phải là ...</span>.",
        # "<span style='font-family: Courier; background-color: #f0f2f6; padding: 2px 6px;'>: là cái gì</span>.", 
        unsafe_allow_html=True
    )
    st.markdown('''**Ví dụ:**''')
    st.markdown('''- **책상:red[이] 아닙니다** - Không phải là bàn học''')
    st.audio(root / "Files/Lesson2/vidu24.mp3", format="audio/mp3")
    st.markdown('''- **컴퓨터:red[가] 아닙니다** - Không phải là máy tính''')
    st.audio(root / "Files/Lesson2/vidu25.mp3", format="audio/mp3")
    st.markdown('''- **시계:red[가] 아닙니다** - Không phải là đồng hồ''')
    st.audio(root / "Files/Lesson2/vidu26.mp3", format="audio/mp3")
    st.markdown('''- **이것은 사전닙니까?** - Cái này là từ điển phải không?''')
    st.audio(root / "Files/Lesson2/vidu27.mp3", format="audio/mp3")
    st.markdown('''- **아니요, 이것은 사전이 아닙니다. 책입니다** - Không, cái này không phải là từ điển. Là sách''')
    st.audio(root / "Files/Lesson2/vidu28.mp3", format="audio/mp3")


    st.divider()
    st.markdown('''**Ví dụ hội thoại:**''')

    st.markdown('''- 여기는 어디입니까? - Đây là đâu vậy?''')
    st.audio(root / "Files/Lesson2/vidu29.mp3", format="audio/mp3")
    st.markdown('''- 여기는 백화점입니다 - Đây là trung tâm thương mại''')
    st.audio(root / "Files/Lesson2/vidu30.mp3", format="audio/mp3")
    st.markdown('''- 백화점에 무엇이 있습니까? - Ở trung tâm thương mại có gì vậy?''')
    st.audio(root / "Files/Lesson2/vidu31.mp3", format="audio/mp3")
    st.markdown('''- 백화점에 옷이 있습니다 - Ở trung tâm thương mại có quần áo''')
    st.audio(root / "Files/Lesson2/vidu32.mp3", format="audio/mp3")
    st.markdown('''- 백화점에 휴게실이 있습니까? - Ở trung tâm thương mại có phòng nghỉ không?''')
    st.audio(root / "Files/Lesson2/vidu33.mp3", format="audio/mp3")
    st.markdown('''- 아니요, 백화점에 휴게실이 없습니다 - Không, ở trung tâm thương mại không có phòng nghỉ''')
    st.audio(root / "Files/Lesson2/vidu34.mp3", format="audio/mp3")

    st.markdown('''**Ví dụ đoạn văn:**''')
    st.markdown('''- 여기는 학교입니다. 학교에 교실이 있습니다. 교실에 책상:red[과] 의자가 있습니다. 교실에 컴퓨터가 없습니다. 교실에 창문이 있습니다.\n
    Đây là trường học. Ở trường học có phòng học. Trong phòng học có bàn học :red[và] ghế. Trong phòng học không có máy tính. Trong phòng học có cửa sổ.''')
    st.audio(root / "Files/Lesson2/vidu35.mp3", format="audio/mp3")

    st.markdown(''' - 여기는 베트남 회사입니다. 여기에 사무실이 있습니다. 컴퓨터가 많이 있습니다. 책상이 있습니다. 식당이 없습니다.\n
    Đây là công ty Việt Nam. Ở đây có văn phòng. Có nhiều máy tính. Có bàn làm việc. Không có nhà ăn.''')
    st.audio(root / "Files/Lesson2/vidu36.mp3", format="audio/mp3")
    
with tab3:
    st.header("Bài 3: Sinh hoạt hàng ngày")
    st.markdown('### Từ vựng')

    # --- Define data (data layer) ---
    rows = [
        {"Từ vựng": "가다", "Nghĩa": "Đi", "audio": "Files/Lesson3/go.mp3"},
        {"Từ vựng": "갑니다", "Nghĩa": "Đi", "audio": "Files/Lesson3/go1.mp3"},

        {"Từ vựng": "오다", "Nghĩa": "Đến", "audio": "Files/Lesson3/arrive.mp3"},
        {"Từ vựng": "옵니다", "Nghĩa": "Đến", "audio": "Files/Lesson3/arrive1.mp3"},

        {"Từ vựng": "자다", "Nghĩa": "Ngủ", "audio": "Files/Lesson3/sleep.mp3"},
        {"Từ vựng": "잡니다", "Nghĩa": "Ngủ", "audio": "Files/Lesson3/sleep1.mp3"},

        {"Từ vựng": "먹다", "Nghĩa": "Ăn", "audio": "Files/Lesson3/eat.mp3"},
        {"Từ vựng": "먹습니다", "Nghĩa": "Ăn", "audio": "Files/Lesson3/eat1.mp3"},

        {"Từ vựng": "마시다", "Nghĩa": "Uống", "audio": "Files/Lesson3/drink.mp3"},
        {"Từ vựng": "마십니다", "Nghĩa": "Uống", "audio": "Files/Lesson3/drink1.mp3"},

        {"Từ vựng": "이야기하다", "Nghĩa": "Kể chuyện", "audio": "Files/Lesson3/tell_story.mp3"},
        {"Từ vựng": "이야기합니다", "Nghĩa": "Kể chuyện", "audio": "Files/Lesson3/tell_story1.mp3"},

        {"Từ vựng": "읽다", "Nghĩa": "Đọc", "audio": "Files/Lesson3/read.mp3"},
        {"Từ vựng": "읽습니다", "Nghĩa": "Đọc", "audio": "Files/Lesson3/read1.mp3"},

        {"Từ vựng": "듣다", "Nghĩa": "Nghe", "audio": "Files/Lesson3/listen.mp3"},
        {"Từ vựng": "듣습니다", "Nghĩa": "Nghe", "audio": "Files/Lesson3/listen1.mp3"},

        {"Từ vựng": "보다", "Nghĩa": "Xem", "audio": "Files/Lesson3/see.mp3"},
        {"Từ vựng": "봅니다", "Nghĩa": "Xem", "audio": "Files/Lesson3/see1.mp3"},

        {"Từ vựng": "일하다", "Nghĩa": "Làm việc", "audio": "Files/Lesson3/work.mp3"},
        {"Từ vựng": "일합니다", "Nghĩa": "Làm việc", "audio": "Files/Lesson3/work1.mp3"},

        {"Từ vựng": "공부하다", "Nghĩa": "Học", "audio": "Files/Lesson3/study.mp3"},
        {"Từ vựng": "공부합니다", "Nghĩa": "Học", "audio": "Files/Lesson3/study1.mp3"},

        {"Từ vựng": "운동하다", "Nghĩa": "Luyện tập thể dục", "audio": "Files/Lesson3/exercise.mp3"},
        {"Từ vựng": "운동합니다", "Nghĩa": "Luyện tập thể dục", "audio": "Files/Lesson3/exercise1.mp3"},

        {"Từ vựng": "쉬다", "Nghĩa": "Nghỉ ngơi", "audio": "Files/Lesson3/rest.mp3"},
        {"Từ vựng": "쉽니다", "Nghĩa": "Nghỉ ngơi", "audio": "Files/Lesson3/rest1.mp3"},

        {"Từ vựng": "만나다", "Nghĩa": "Gặp gỡ", "audio": "Files/Lesson3/meet.mp3"},
        {"Từ vựng": "만납니다", "Nghĩa": "Gặp gỡ", "audio": "Files/Lesson3/meet1.mp3"},

        {"Từ vựng": "사다", "Nghĩa": "Mua", "audio": "Files/Lesson3/buy.mp3"},
        {"Từ vựng": "삽니다", "Nghĩa": "Mua", "audio": "Files/Lesson3/buy1.mp3"},

        {"Từ vựng": "좋아하다", "Nghĩa": "Thích", "audio": "Files/Lesson3/like.mp3"},
        {"Từ vựng": "좋아합니다", "Nghĩa": "Thích", "audio": "Files/Lesson3/like1.mp3"},

        {"Từ vựng": "크다", "Nghĩa": "To, lớn", "audio": "Files/Lesson3/big.mp3"},
        {"Từ vựng": "큽니다", "Nghĩa": "To, lớn", "audio": "Files/Lesson3/big1.mp3"},

        {"Từ vựng": "작다", "Nghĩa": "Nhỏ", "audio": "Files/Lesson3/small.mp3"},
        {"Từ vựng": "작습니다", "Nghĩa": "Nhỏ", "audio": "Files/Lesson3/small1.mp3"},

        {"Từ vựng": "많다", "Nghĩa": "Nhiều", "audio": "Files/Lesson3/many.mp3"},
        {"Từ vựng": "많습니다", "Nghĩa": "Nhiều", "audio": "Files/Lesson3/many1.mp3"},

        {"Từ vựng": "적다", "Nghĩa": "Ít", "audio": "Files/Lesson3/few.mp3"},
        {"Từ vựng": "적습니다", "Nghĩa": "Ít", "audio": "Files/Lesson3/few1.mp3"},

        {"Từ vựng": "좋다", "Nghĩa": "Tốt", "audio": "Files/Lesson3/good.mp3"},
        {"Từ vựng": "좋습니다", "Nghĩa": "Tốt", "audio": "Files/Lesson3/good1.mp3"},

        {"Từ vựng": "나쁘다", "Nghĩa": "Xấu", "audio": "Files/Lesson3/bad.mp3"},
        {"Từ vựng": "나쁩니다", "Nghĩa": "Xấu", "audio": "Files/Lesson3/bad1.mp3"},

        {"Từ vựng": "재미있다", "Nghĩa": "Thú vị", "audio": "Files/Lesson3/really_fun.mp3"},
        {"Từ vựng": "재미있습니다", "Nghĩa": "Thú vị", "audio": "Files/Lesson3/really_fun1.mp3"},

        {"Từ vựng": "재미없다", "Nghĩa": "Không thú vị", "audio": "Files/Lesson3/not_fun.mp3"},
        {"Từ vựng": "재미없습니다", "Nghĩa": "Không thú vị", "audio": "Files/Lesson3/not_fun1.mp3"},

        {"Từ vựng": "차", "Nghĩa": "Trà", "audio": "Files/Lesson3/tea.mp3"},
        {"Từ vựng": "영화", "Nghĩa": "Phim ảnh", "audio": "Files/Lesson3/movie.mp3"},
        {"Từ vựng": "음악", "Nghĩa": "Âm nhạc", "audio": "Files/Lesson3/music.mp3"},
        {"Từ vựng": "신문", "Nghĩa": "Tạp chí", "audio": "Files/Lesson3/newspaper.mp3"},
        {"Từ vựng": "친구", "Nghĩa": "Bạn bè", "audio": "Files/Lesson3/friend.mp3"},

        {"Từ vựng": "누구", "Nghĩa": "Ai (tân ngữ)", "audio": "Files/Lesson3/nugu.mp3"},
        {"Từ vựng": "누가", "Nghĩa": "Ai (chủ ngữ)", "audio": "Files/Lesson3/nuga.mp3"},
        {"Từ vựng": "언제", "Nghĩa": "Khi nào", "audio": "Files/Lesson3/when.mp3"},

        {"Từ vựng": "공원", "Nghĩa": "Công viên", "audio": "Files/Lesson3/park.mp3"},
        {"Từ vựng": "노래", "Nghĩa": "Bài hát", "audio": "Files/Lesson3/song.mp3"},
        {"Từ vựng": "대한빌딩", "Nghĩa": "Tòa nhà Hàn Quốc", "audio": "Files/Lesson3/building.mp3"},
        {"Từ vựng": "방", "Nghĩa": "Phòng", "audio": "Files/Lesson3/room.mp3"},

        {"Từ vựng": "산책하다", "Nghĩa": "Đi dạo", "audio": "Files/Lesson3/walk.mp3"},
        {"Từ vựng": "쇼핑하다", "Nghĩa": "Đi mua sắm", "audio": "Files/Lesson3/shopping.mp3"},

        {"Từ vựng": "시내", "Nghĩa": "Nội thành", "audio": "Files/Lesson3/urban.mp3"},
        {"Từ vựng": "시장", "Nghĩa": "Chợ", "audio": "Files/Lesson3/market.mp3"},
        {"Từ vựng": "식사하다", "Nghĩa": "Ăn uống", "audio": "Files/Lesson3/eatdrink.mp3"},
        {"Từ vựng": "아이스크림", "Nghĩa": "Kem", "audio": "Files/Lesson3/ice_cream.mp3"},
        {"Từ vựng": "아주", "Nghĩa": "Rất", "audio": "Files/Lesson3/very.mp3"},
        {"Từ vựng": "여행", "Nghĩa": "Du lịch", "audio": "Files/Lesson3/travel.mp3"},
        {"Từ vựng": "이메일", "Nghĩa": "Email", "audio": "Files/Lesson3/email.mp3"},
        {"Từ vựng": "위", "Nghĩa": "Trên", "audio": "Files/Lesson3/above.mp3"},
        {"Từ vựng": "전화하다", "Nghĩa": "Gọi điện", "audio": "Files/Lesson3/phone.mp3"},
        {"Từ vựng": "지금", "Nghĩa": "Bây giờ", "audio": "Files/Lesson3/now.mp3"},
        {"Từ vựng": "축구를 하다", "Nghĩa": "Chơi bóng đá", "audio": "Files/Lesson3/soccer.mp3"},
        {"Từ vựng": "카페", "Nghĩa": "Quán cà phê", "audio": "Files/Lesson3/cafe.mp3"},
        {"Từ vựng": "헬스클럽", "Nghĩa": "Gym", "audio": "Files/Lesson3/fitness_club.mp3"},
        {"Từ vựng": "그리고", "Nghĩa": "Và", "audio": "Files/Lesson3/and.mp3"},
        {"Từ vựng": "구두", "Nghĩa": "Giày", "audio": "Files/Lesson3/shoes.mp3"},
        {"Từ vựng": "자주", "Nghĩa": "Thường xuyên", "audio": "Files/Lesson3/often.mp3"},
        {"Từ vựng": "스업하다", "Nghĩa": "Có buổi học", "audio": "Files/Lesson3/has_class.mp3"}


        
    ]

    root = Path(__file__).resolve().parent

    def audio_to_data_uri(path: str) -> str:
        file_path = root / path
        with open(file_path, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        return f"data:audio/mp3;base64,{encoded}"

    table_rows = ""
    for row in rows:
        audio_uri = audio_to_data_uri(row["audio"])
        table_rows += f"""
        <tr>
            <td><strong>{row['Từ vựng']}</strong></td>
            <td>{row['Nghĩa']}</td>
            <td class=\"audio-cell\"><button class=\"play-btn\" data-src=\"{audio_uri}\">▶</button></td>
        </tr>
        """

    table_html = f"""
    <div style=\"overflow-x:auto; width:100%;\">
        <style>
            table tr td {{
                padding: 12px;
                border: 1px solid #ddd;
                vertical-align: middle;
            }}
            table tr th {{
                padding: 12px;
                border: 1px solid #ddd;
                background: #f2f2f2;
                font-weight: bold;
            }}
            .audio-cell .play-btn {{
                font-size: 10px;
                padding: 8px 12px;
                border-radius: 6px;
                border: none;
                background: #007bff;
                color: white;
                cursor: pointer;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                min-width: 22px;
            }}
            .audio-cell .play-btn.playing {{
                background: #28a745;
            }}
            @media (max-width: 720px) {{
                table {{ min-width: 300px; }}
                .audio-cell .play-btn {{
                    font-size: 10px;
                    min-width: 22px;
                    padding: 8px 12px;
                }}
            }}
        </style>

        <table style=\"width:100%; border-collapse: collapse; min-width: 300px;\">
            <thead>
                <tr>
                    <th>Từ vựng</th>
                    <th>Nghĩa</th>
                    <th>Audio</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>

        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                const buttons = document.querySelectorAll('.play-btn');
                let currentAudio = null;
                let currentBtn = null;
                buttons.forEach(btn => {{
                    btn.addEventListener('click', function() {{
                        const src = btn.getAttribute('data-src');
                        if (currentAudio && !currentAudio.paused && currentAudio.src === src) {{
                            currentAudio.pause();
                            btn.classList.remove('playing');
                            return;
                        }}
                        if (currentAudio) {{
                            currentAudio.pause();
                            if (currentBtn) currentBtn.classList.remove('playing');
                        }}
                        const audio = new Audio(src);
                        currentAudio = audio;
                        currentBtn = btn;
                        btn.classList.add('playing');
                        audio.play().catch(() => {{ btn.classList.remove('playing'); }});
                        audio.addEventListener('ended', function() {{ btn.classList.remove('playing'); }});
                        audio.addEventListener('pause', function() {{ btn.classList.remove('playing'); }});
                    }});
                }});
            }});
        </script>
    </div>
    """

    st.iframe(table_html, height=len(rows) * 56)



    st.markdown('### Ngữ pháp')
    st.markdown(
        "**1.** <span style=' font-size: 20px; font-weight: bold;'> V/A + :red[ㅂ]/:blue[습] + 니다/니까?</span>"
        "<span style='color: #555; font-size: 16px;'>: Đuôi kết thúc câu trần thuật, nếu V/A không có patchim thì dùng :red[ㅂ], nếu có patchim thì dùng :blue[습] </span>.",
        # "<span style='font-family: Courier; background-color: #f0f2f6; padding: 2px 6px;'>: là cái gì</span>.", 
        unsafe_allow_html=True
    )
    st.markdown('''**Ví dụ:** ''')
    st.markdown('''- **유진 씨가 잡니다** - Yujin đang ngủ''')
    st.audio(root / "Files/Lesson3/vidu1.mp3", format="audio/mp3")
    st.markdown('''- **학생이 공부합니다** - Học sinh đang học''')
    st.audio(root / "Files/Lesson3/vidu2.mp3", format="audio/mp3")
    st.markdown('''- **친구가 이야기합니다** - Bạn bè đang kể chuyện''')
    st.audio(root / "Files/Lesson3/vidu3.mp3", format="audio/mp3")
    st.markdown('''- **가방이 작습니다** - Cái cặp sách nhỏ''')
    st.audio(root / "Files/Lesson3/vidu4.mp3", format="audio/mp3")
    st.markdown('''- **이 영화는 재미있습니다** - Bộ phim này thú vị''')
    st.audio(root / "Files/Lesson3/vidu5.mp3", format="audio/mp3")
    st.markdown('''- **이 백화점이 아주 큽니다** - Trung tâm thương mại này rất lớn''')
    st.audio(root / "Files/Lesson3/vidu6.mp3", format="audio/mp3")

    st.markdown('''- **지원 씨가 일합니까?** - Ji-won có làm việc không?''')
    st.audio(root / "Files/Lesson3/vidu7.mp3", format="audio/mp3")
    st.markdown('''- **네, 지원 씨가 일합니다** - Vâng, Ji-won làm việc''')
    st.audio(root / "Files/Lesson3/vidu8.mp3", format="audio/mp3")
    st.markdown('''- **오토바이가 좋습니까?** - Xe máy có tốt không?''')
    st.audio(root / "Files/Lesson3/vidu9.mp3", format="audio/mp3")
    st.markdown('''- **네, 오토바이가 좋습니다** - Vâng, xe máy tốt''')
    st.audio(root / "Files/Lesson3/vidu10.mp3", format="audio/mp3")

    st.divider()
    st.markdown(
        "**2.** <span style=' font-size: 20px; font-weight: bold;'> N (:red[patchim]/:blue[không patchim]) + :red[을]/:blue[를]</span>"
        "<span style='color: #555; font-size: 16px;'>: Tiểu từ chỉ tân ngữ</span>.",
        # "<span style='font-family: Courier; background-color: #f0f2f6; padding: 2px 6px;'>: là cái gì</span>.", 
        unsafe_allow_html=True
    )
    st.markdown('''**Ví dụ:** ''')
    st.markdown('''- **책을 읽습니다** - Đọc sách''')
    st.audio(root / "Files/Lesson3/vidu11.mp3", format="audio/mp3")
    st.markdown('''- **음악을 듣습니다** - Nghe nhạc''')
    st.audio(root / "Files/Lesson3/vidu12.mp3", format="audio/mp3")
    st.markdown('''- **영화를 봅니다** - Xem phim''')   
    st.audio(root / "Files/Lesson3/vidu13.mp3", format="audio/mp3")
    st.markdown('''- **저는 친구를 만납니다** - Tôi gặp bạn bè''')
    st.audio(root / "Files/Lesson3/vidu14.mp3", format="audio/mp3")
    st.markdown('''- **흐엉 씨가 아이스크림을 좋아합니다** - Hương thích kem''')
    st.audio(root / "Files/Lesson3/vidu15.mp3", format="audio/mp3")


    st.divider()

    st.markdown(
        "**3.**\n"
        "- <span style='font-size: 20px; font-weight: bold;'> N + :red[에서]</span>"
        "<span style='color: #555; font-size: 16px;'>: Tiểu từ chỉ trạng ngữ: gắn sau danh từ để biểu thị địa điểm xảy ra một hành động nào đó </span>.\n"
        "- <span style='font-size: 20px; font-weight: bold;'> N + :blue[에]</span>"
        "<span style='color: #555; font-size: 16px;'>: chỉ thêm :blue[에] sau danh từ chỉ nơi chốn đối với các động từ: **가다, 오다, 있다, 없다, 다니다** </span>.",
        # "<span style='font-family: Courier; background-color: #f0f2f6; padding: 2px 6px;'>: là cái gì</span>.", 
        unsafe_allow_html=True
    )
    st.markdown('''**Ví dụ:**''')   
    st.markdown('''- **학교에서 공부합니다** - Học ở trường học''')
    st.audio(root / "Files/Lesson3/vidu16.mp3", format="audio/mp3")
    st.markdown('''- **도서관에서 책을 읽습니다** - Đọc sách ở thư viện''')
    st.audio(root / "Files/Lesson3/vidu17.mp3", format="audio/mp3")
    st.markdown('''- **병원에서 일합니다** - Làm việc ở bệnh viện''')
    st.audio(root / "Files/Lesson3/vidu18.mp3", format="audio/mp3")
    st.markdown('''- **학교에 갑니다** - Đi đến trường học''')
    st.audio(root / "Files/Lesson3/vidu19.mp3", format="audio/mp3")
    st.markdown('''- **도서관에 옵니다** - Đến thư viện''')
    st.audio(root / "Files/Lesson3/vidu20.mp3", format="audio/mp3")
    st.markdown('''- **병원에 다닙니다** - Đi lại ở bệnh viện''')
    st.audio(root / "Files/Lesson3/vidu21.mp3", format="audio/mp3")   
    st.markdown('''- **가게에 있습니다** - Có ở cửa hàng''')
    st.audio(root / "Files/Lesson3/vidu22.mp3", format="audio/mp3")

    st.divider()
    st.markdown('''**Ví dụ khác:**''')
    st.markdown('''- **학교에서 친구를 만납니다** - Gặp bạn bè ở trường học''')
    st.audio(root / "Files/Lesson3/vidu23.mp3", format="audio/mp3")
    st.markdown('''- **도서관에서 음악을 듣습니다** - Nghe nhạc ở thư viện''')
    st.audio(root / "Files/Lesson3/vidu24.mp3", format="audio/mp3")
    st.markdown('''- **지금 무엇을 합니까?** - Bây giờ bạn đang làm gì vậy?''')
    st.audio(root / "Files/Lesson3/vidu25.mp3", format="audio/mp3")
    st.markdown('''- **지금 학교에서 공부합니다** - Bây giờ tôi đang học ở trường học''')
    st.audio(root / "Files/Lesson3/vidu26.mp3", format="audio/mp3")
    st.markdown('''- **지금 도서관에서 책을 읽습니다** - Bây giờ tôi đang đọc sách ở thư viện''')
    st.audio(root / "Files/Lesson3/vidu27.mp3", format="audio/mp3")
    st.markdown('''- **유진씨가 어디에서 무엇을 합니까?** - Yujin đang làm gì ở đâu vậy?''')
    st.audio(root / "Files/Lesson3/vidu28.mp3", format="audio/mp3")   
    st.markdown('''- **유진씨가 식당에서 친구를 만납니다** - Yujin gặp bạn bè ở nhà ăn''')
    st.audio(root / "Files/Lesson3/vidu29.mp3", format="audio/mp3")
    st.markdown('''- **유진씨가 공원에서 운동합니다** - Yujin tập thể dục ở công viên''')
    st.audio(root / "Files/Lesson3/vidu30.mp3", format="audio/mp3")


    st.divider()
    st.markdown('''**Ví dụ hội thoại:**''')
    st.markdown('''- 지금 어디에 있습니까? - Bây giờ bạn đang ở đâu vậy?''')
    st.audio(root / "Files/Lesson3/vidu31.mp3", format="audio/mp3")
    st.markdown('''- 지금 집에 있습니다 - Bây giờ tôi đang ở nhà''')
    st.audio(root / "Files/Lesson3/vidu32.mp3", format="audio/mp3")
    st.markdown('''- 집에서 무엇을 합니까? - Ở nhà bạn đang làm gì vậy?''')
    st.audio(root / "Files/Lesson3/vidu33.mp3", format="audio/mp3")
    st.markdown('''- 집에서 쉽니다 - Ở nhà tôi đang nghỉ ngơi''')
    st.audio(root / "Files/Lesson3/vidu34.mp3", format="audio/mp3")
    st.markdown('''- 집에서 무엇을 먹습니까? - Ở nhà bạn đang ăn gì vậy?''')
    st.audio(root / "Files/Lesson3/vidu35.mp3", format="audio/mp3")
    st.markdown('''- 집에서 밥을 먹습니다 - Ở nhà tôi đang ăn cơm''')
    st.audio(root / "Files/Lesson3/vidu36.mp3", format="audio/mp3")
    
    st.divider()
    st.markdown(''' - 민재씨, 오늘 무엇을 합니까? - Min-jae, hôm nay bạn sẽ làm gì vậy?''')
    st.audio(root / "Files/Lesson3/vidu37.mp3", format="audio/mp3")
    st.markdown('''- 오늘 시내에서 쇼핑합니다 - Hôm nay tôi sẽ đi mua sắm ở nội thành''')
    st.audio(root / "Files/Lesson3/vidu38.mp3", format="audio/mp3")
    st.markdown('''- 시내에서 무엇을 삽니까? - Ở nội thành bạn sẽ mua gì vậy?''')
    st.audio(root / "Files/Lesson3/vidu39.mp3", format="audio/mp3")
    st.markdown('''- 시내에서 구두를 삽니다 - Ở nội thành tôi sẽ mua giày''')
    st.audio(root / "Files/Lesson3/vidu40.mp3", format="audio/mp3")
    
    st.divider()
    st.markdown('''- 루이엔 씨, 오늘 무엇을 합니까? - Luyen, hôm nay bạn sẽ làm gì vậy?''')
    st.audio(root / "Files/Lesson3/vidu42.mp3", format="audio/mp3")   
    st.markdown('''- 공원에서 산책합니다.그리고 쇼핑합니다. - Tôi sẽ đi dạo ở công viên. Và đi mua sắm''')
    st.audio(root / "Files/Lesson3/vidu43.mp3", format="audio/mp3")
    st.markdown('''- 어디에서 쇼핑합니까? - Bạn sẽ đi mua sắm ở đâu vậy?''')
    st.audio(root / "Files/Lesson3/vidu44.mp3", format="audio/mp3")
    st.markdown('''- 시내 백화점에서 쇼핑합니다. 흐엉 씨는 오늘 무엇을 합니까? - Tôi sẽ đi mua sắm ở cửa TTTM ở nội thành. Hương, bạn sẽ làm gì vậy?''')
    st.audio(root / "Files/Lesson3/vidu45.mp3", format="audio/mp3")
    st.markdown('''- 트랑극장에서 영화를 봅니다 - Tôi sẽ xem phim ở rạp Trang''')
    st.audio(root / "Files/Lesson3/vidu46.mp3", format="audio/mp3")
    st.markdown('''- 흐엉 씨는 영화를 좋아합니까? - Hương thích xem phim hả?''')
    st.audio(root / "Files/Lesson3/vidu47.mp3", format="audio/mp3")
    st.markdown('''- 네, 아주 좋아합니다. - Vâng, tôi rất thích''')
    st.audio(root / "Files/Lesson3/vidu48.mp3", format="audio/mp3")
    

    
    




    # col1, col2 = st.columns([2,1])
    # with col1:
        
    #     st.markdown('#### N + 입니다? \
    #                   Xin chào'
    #                 )

    # with col2:
    #     # audio_path = root / "Files/Lesson2/annyeonghaseyo.mp3"
    #     if st.button("▶"):
    #     #      st.audio(audio_path, format="audio/mp3")
    #         display_audio_only(root / "Files/Lesson2/annyeonghaseyo.mp3")

        


    # st.markdown("""
    # - **Ngữ pháp**:
    #     - **안녕하세요** (Annyeonghaseyo) - Xin chào
    #     - **저는 [tên]입니다** (Jeoneun [tên] imnida) - Tôi là [tên]
    #     - **만나서 반갑습니다** (Mannaseo bangapseumnida) - Rất vui được gặp bạn
    #             """) 

