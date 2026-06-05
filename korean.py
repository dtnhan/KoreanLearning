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



tab1, tab2, tab3 = st.tabs([
    "📜Bài 1",
    "📜Bài 2",
    "📜Bài 3"
])

with tab1:
    st.header("Bài 1: Giới thiệu bản thân")
    st.markdown(""" **Từ vựng**:""")

    # --- Define data (data layer) ---
    rows = [
        {"Từ vựng": "바다", "Nghĩa": "Biển", "audio": "Files/bien.mp3"},
        {"Từ vựng": "오이", "Nghĩa": "Dưa leo", "audio": "Files/oi.mp3"},
        {"Từ vựng": "우유", "Nghĩa": "Sữa", "audio": "Files/uyu.mp3"},
        {"Từ vựng": "아이", "Nghĩa": "Trẻ em", "audio": "Files/ai.mp3"},
        {"Từ vựng": "여우", "Nghĩa": "Con cáo", "audio": "Files/yeou.mp3"},
        {"Từ vựng": "고기", "Nghĩa": "Thịt", "audio": "Files/gogi.mp3"},
        {"Từ vựng": "나무", "Nghĩa": "Cây cối", "audio": "Files/namu.mp3"},
        {"Từ vựng": "기구", "Nghĩa": "Dụng cụ", "audio": "Files/gigu.mp3"},
        {"Từ vựng": "소", "Nghĩa": "Con bò", "audio": "Files/so.mp3"},
        {"Từ vựng": "소고기", "Nghĩa": "Thịt bò", "audio": "Files/so_gogi.mp3"},
        {"Từ vựng": "버스", "Nghĩa": "Xe buýt", "audio": "Files/bose.mp3"},
        {"Từ vựng": "커피", "Nghĩa": "Cà phê", "audio": "Files/coffee.mp3"},
        {"Từ vựng": "스키", "Nghĩa": "Trượt tuyết", "audio": "Files/ski.mp3"},
        {"Từ vựng": "오토바이", "Nghĩa": "Xe máy", "audio": "Files/otobai.mp3"},
        {"Từ vựng": "아파트", "Nghĩa": "Chung cư", "audio": "Files/apart.mp3"},
        {"Từ vựng": "파", "Nghĩa": "Hành lá", "audio": "Files/par.mp3"},
        {"Từ vựng": "치마", "Nghĩa": "Váy", "audio": "Files/chim.mp3"},
        {"Từ vựng": "포도", "Nghĩa": "Nho", "audio": "Files/podo.mp3"},
        {"Từ vựng": "피자", "Nghĩa": "Pizza", "audio": "Files/pizza.mp3"},
        {"Từ vựng": "기차", "Nghĩa": "Tàu hỏa", "audio": "Files/gicha.mp3"},
        {"Từ vựng": "아저씨", "Nghĩa": "Chú, ông chú", "audio": "Files/ajusshi.mp3"},
        {"Từ vựng": "토끼", "Nghĩa": "Con thỏ", "audio": "Files/tori.mp3"},
        {"Từ vựng": "아빠", "Nghĩa": "Cha", "audio": "Files/appa.mp3"},
        {"Từ vựng": "오빠", "Nghĩa": "Anh trai", "audio": "Files/oppa.mp3"},
        {"Từ vựng": "떡", "Nghĩa": "Bánh gạo", "audio": "Files/duk.mp3"},
        {"Từ vựng": "빵", "Nghĩa": "Bánh mì", "audio": "Files/bang.mp3"},
        {"Từ vựng": "딸기", "Nghĩa": "Dâu tây", "audio": "Files/ddakgi.mp3"},
        {"Từ vựng": "배", "Nghĩa": "Tàu, quả lê", "audio": "Files/bae.mp3"},
        {"Từ vựng": "개", "Nghĩa": "Chó", "audio": "Files/gae.mp3"},
        {"Từ vựng": "게", "Nghĩa": "Cua", "audio": "Files/ge.mp3"},


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

    st.iframe(table_html, height=len(rows) * 65)

    st.markdown("""
    - **Từ vựng**:
        - **안녕하세요** (Annyeonghaseyo) - Xin chào
        - **저는 [tên]입니다** (Jeoneun [tên] imnida) - Tôi là [tên]
        - **만나서 반갑습니다** (Mannaseo bangapseumnida) - Rất vui được gặp bạn
                """) 

