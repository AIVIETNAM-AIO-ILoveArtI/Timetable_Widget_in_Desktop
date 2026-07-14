import os
import re
import datetime
import asyncio
import websockets
from groq import Groq

k = "your_API" 
sf = "your txt file source for AI reading your timetable"
cl = Groq(api_key=k)

def get_mem():
    if not os.path.exists(sf): 
        return "Error: No data file directory."
    with open(sf, "r", encoding="utf-8") as f: 
        return f.read()

async def hndl(ws):
    print(f"🐾 One chat bot connect from: {ws.remote_address}")
    try:
        async for m in ws:
            if m.startswith("SEND_PROMPT"):
                p = m.split('\n', 1)[1]
                print(f"\n📩 Typing input: {p}")

                if not p.strip():
                    continue

                try:
                    mem = get_mem()
                    n = datetime.datetime.now()
                    
                    cd = ["T2", "T3", "T4", "T5", "T6", "T7", "CN"]
                    tc = cd[n.weekday()]
                    sd = n.strftime("%d/%m/%y")

                    dm = re.search(r'(\d{1,2})[/-](\d{1,2})', p)
                    if dm:
                        try:
                            d, mn = int(dm.group(1)), int(dm.group(2))
                            cd_dt = datetime.date(2026, mn, d)
                            tc = cd[cd_dt.weekday()]
                            sd = cd_dt.strftime("%d/%m/%y")
                        except: 
                            pass
                    elif "mai" in p.lower():
                        tmr = n + datetime.timedelta(days=1)
                        tc = cd[tmr.weekday()]
                        sd = tmr.strftime("%d/%m/%y")

                    res = cl.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {
                                "role": "system", 
                                "content": (
                                    "Bạn là Trợ lý Mèo 🐾. Trả lời ngắn gọn, trực diện.\n"
                                    "LUẬT TÌM LỊCH BẮT BUỘC:\n"
                                    f"1. Ngày người dùng muốn tra cứu: '{sd}' (Thuộc mã: {tc}).\n"
                                    f"2. ĐIỀU KIỆN SỐNG CÒN: Bạn CHỈ được phép liệt kê môn học nếu chuỗi '{sd}' xuất hiện CHÍNH XÁC trong mảng `Ngay_hoc` của môn đó.\n"
                                    "3. VÍ DỤ MINH HỌA CÁCH LỌC (Rất quan trọng):\n"
                                    f"   - Môn Điện tử số có Ngay_hoc: ['12/03/26', '09/04/26']. Vì không có '{sd}' -> BẮT BUỘC BỎ QUA MÔN NÀY.\n"
                                    f"   - Môn Tiếng Trung có Ngay_hoc: ['23/04/26', '{sd}']. Vì có '{sd}' -> IN RA MÔN NÀY.\n"
                                    "4. Nếu sau khi lọc mà DgA hoặc A không còn môn nào, hãy mạnh dạn trả lời: 'Hôm nay DgA (hoặc A) không có lịch, được nghỉ meo~'.\n\n"
                                    "CƠ SỞ DỮ LIỆU CỦA BẠN:\n"
                                    f"{mem}"
                                )
                            },
                            {
                                "role": "user", 
                                "content": f"Câu hỏi ban đầu: '{p}'\n\nNhiệm vụ: Hãy rà soát thật kỹ các mảng `Ngay_hoc` trong CSDL để trả lời lịch ngày {sd} của DgA và A."
                            }
                        ],
                        max_tokens=250,
                        temperature=0.0
                    )

                    ans = res.choices[0].message.content
                    print(f"✅ Python đã tính ra {tc}. Mèo trả lời: {ans}")
                    
                    await ws.send(f"CHATBOT_RESPONSE:{ans}")

                except Exception as e:
                    err = f"Meo~ Lỗi gòi: {str(e)}"
                    print(err)
                    await ws.send(f"CHATBOT_RESPONSE:{err}")

    except websockets.exceptions.ConnectionClosed:
        print("🐾 Bé mèo đã ngắt kết nối tạm thời.")

async def main():
    async with websockets.serve(hndl, "localhost", 8080, reuse_address=True):
        print("🚀 CHÚ MÈO THẦN ĐỒNG ĐÃ SẴN SÀNG TẠI CỔNG 8080 (WEBSOCKET)!")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
