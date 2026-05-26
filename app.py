from flask import Flask, render_template_string, request, jsonify
import requests

app = Flask(__name__)

# === CẤU HÌNH API (ĐÃ ĐÚNG THEO TOKEN BẠN CUNG CẤP) ===
LINK4M_TOKEN = "65c47d157fbdff4d79625e57"
TRAFFIC_TOKEN = "ee4f080ff90f6180b109ecc4"

# Link MediaFire
MEDIAFIRE_LINKS = {
    "esp_vip": "https://www.mediafire.com/file/hbrs6rr26flgz7z/FF+MAX+INJECTOR+MAIN+ID+SAFE+(1).zip/file",
    "aimbot": "https://www.mediafire.com/file/oged4p8u6blci0k/LEHER+HS+METADATA.7z/file"
}

# === QUY TRÌNH ĐÚNG: MediaFire → Link4m → TrafficVN ===
def create_link4m_url(mediafire_url):
    """Tạo link Link4m từ MediaFire (bước 1)"""
    try:
        # Theo ảnh của bạn, Link4m dùng GET request
        api_url = f"https://link4m.com/api?api={LINK4M_TOKEN}&url={mediafire_url}"
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            # Link4m trả về shorturl hoặc shortened_url
            return data.get("shorturl") or data.get("shortened_url") or data.get("url")
        return mediafire_url
    except Exception as e:
        print(f"Lỗi Link4m: {e}")
        return mediafire_url

def create_trafficvn_url(link4m_url):
    """Tạo link TrafficVN từ Link4m (bước 2 - link cuối cùng user click)"""
    try:
        api_url = "https://trafficvn.com/api/v1/shorten"
        payload = {"token": TRAFFIC_TOKEN, "url": link4m_url}
        response = requests.post(api_url, json=payload, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("shortened_url") or data.get("shorturl")
        return link4m_url
    except Exception as e:
        print(f"Lỗi TrafficVN: {e}")
        return link4m_url

def create_download_link(mediafire_url):
    """Quy trình hoàn chỉnh: MediaFire → Link4m → TrafficVN"""
    step1 = create_link4m_url(mediafire_url)      # Bước 1: Tạo link Link4m
    step2 = create_trafficvn_url(step1)           # Bước 2: Tạo link TrafficVN từ Link4m
    return step2  # Đây là link user click (TrafficVN)

# === HTML + CSS + JAVASCRIPT ===
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QANHNO1 - Chia Sẻ Tool Game</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0a0f1e 0%, #0d1525 100%);
            color: #fff;
            padding: 20px;
        }
        .container { max-width: 1400px; margin: 0 auto; }
        h1 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #00ff88, #00b8ff);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        .sub { text-align: center; color: #888; margin-bottom: 40px; }
        .games-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }
        .game-card {
            background: rgba(20, 30, 45, 0.7);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 20px;
            border: 1px solid rgba(0, 255, 136, 0.2);
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .game-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 255, 136, 0.2);
            border-color: #00ff88;
        }
        .game-title {
            font-size: 2rem;
            text-align: center;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #00ff88;
        }
        .game-title.ff { color: #ff6b6b; text-shadow: 0 0 10px #ff6b6b; }
        .game-title.rbx { color: #ffd93d; text-shadow: 0 0 10px #ffd93d; }
        .game-title.pubg { color: #6bcbff; text-shadow: 0 0 10px #6bcbff; }
        .platform-section {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px;
            padding: 15px;
            margin-bottom: 20px;
        }
        .platform-title {
            font-size: 1.3rem;
            margin-bottom: 15px;
            padding-left: 10px;
            border-left: 4px solid #00ff88;
        }
        .feature-box {
            background: rgba(0, 0, 0, 0.5);
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 15px;
            transition: all 0.3s;
        }
        .feature-box.esp {
            border: 1px solid #ff6b6b;
            background: linear-gradient(135deg, rgba(255,107,107,0.1), rgba(0,0,0,0.3));
        }
        .feature-box.aim {
            border: 1px solid #ffd93d;
            background: linear-gradient(135deg, rgba(255,217,61,0.1), rgba(0,0,0,0.3));
        }
        .feature-name {
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 10px;
            text-align: center;
        }
        .feature-name.esp { color: #ff6b6b; }
        .feature-name.aim { color: #ffd93d; }
        .account-info {
            background: rgba(0,0,0,0.6);
            border-radius: 8px;
            padding: 10px;
            margin: 10px 0;
            font-size: 0.85rem;
            text-align: center;
            font-family: monospace;
        }
        .btn-download {
            display: block;
            width: 100%;
            padding: 12px;
            margin-top: 10px;
            background: linear-gradient(135deg, #00ff88, #00b8ff);
            border: none;
            border-radius: 25px;
            color: #0a0f1e;
            font-weight: bold;
            font-size: 1rem;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .btn-download:hover {
            transform: scale(1.02);
            box-shadow: 0 5px 20px rgba(0,255,136,0.4);
        }
        .loading {
            text-align: center;
            color: #00ff88;
            margin-top: 10px;
            display: none;
        }
        @media (max-width: 768px) {
            .games-grid { grid-template-columns: 1fr; }
            h1 { font-size: 1.8rem; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>⚡ QANHNO1 ⚡</h1>
        <div class="sub">Chia sẻ tool, mod, skin miễn phí</div>
        <div class="games-grid">
            <!-- FREE FIRE -->
            <div class="game-card">
                <div class="game-title ff">🔥 FREE FIRE</div>
                <div class="platform-section">
                    <div class="platform-title">📱 ANDROID</div>
                    <div class="feature-box esp">
                        <div class="feature-name esp">🎯 Esp Vip</div>
                        <div class="account-info">
                            📌 Tài khoản: LIMON-GAMING-OFC<br>
                            🔑 Mật khẩu: 248194848323
                        </div>
                        <button class="btn-download" onclick="downloadFile('esp_vip')">⬇️ Tải xuống</button>
                        <div id="loading-esp" class="loading">⏳ Đang tạo link...</div>
                    </div>
                    <div class="feature-box aim">
                        <div class="feature-name aim">🎯 AimBot 90%</div>
                        <button class="btn-download" onclick="downloadFile('aimbot')">⬇️ Tải xuống</button>
                        <div id="loading-aim" class="loading">⏳ Đang tạo link...</div>
                    </div>
                </div>
                <div class="platform-section">
                    <div class="platform-title">🍎 iOS</div>
                    <div style="text-align: center; padding: 20px; color: #888;">⏳ Đang cập nhật...</div>
                </div>
            </div>
            <!-- ROBLOX -->
            <div class="game-card">
                <div class="game-title rbx">🎮 ROBLOX</div>
                <div class="platform-section"><div class="platform-title">📱 ANDROID</div><div style="text-align: center; padding: 20px; color: #888;">⏳ Đang cập nhật...</div></div>
                <div class="platform-section"><div class="platform-title">🍎 iOS</div><div style="text-align: center; padding: 20px; color: #888;">⏳ Đang cập nhật...</div></div>
            </div>
            <!-- PUBG -->
            <div class="game-card">
                <div class="game-title pubg">🎯 PUBG</div>
                <div class="platform-section"><div class="platform-title">📱 ANDROID</div><div style="text-align: center; padding: 20px; color: #888;">⏳ Đang cập nhật...</div></div>
                <div class="platform-section"><div class="platform-title">🍎 iOS</div><div style="text-align: center; padding: 20px; color: #888;">⏳ Đang cập nhật...</div></div>
            </div>
        </div>
    </div>
    <script>
        async function downloadFile(type) {
            const loadingId = type === 'esp_vip' ? 'loading-esp' : 'loading-aim';
            const loader = document.getElementById(loadingId);
            loader.style.display = 'block';
            try {
                const response = await fetch('/get_download_link', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ file_type: type })
                });
                const data = await response.json();
                if (data.success && data.download_url) {
                    window.location.href = data.download_url;
                } else {
                    alert('Lỗi: ' + (data.error || 'Không thể tạo link tải'));
                }
            } catch (error) {
                alert('Lỗi kết nối: ' + error.message);
            } finally {
                loader.style.display = 'none';
            }
        }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/get_download_link', methods=['POST'])
def get_download_link():
    try:
        data = request.get_json()
        file_type = data.get('file_type')
        if file_type not in MEDIAFIRE_LINKS:
            return jsonify({'success': False, 'error': 'Loại file không hợp lệ'})
        mediafire_url = MEDIAFIRE_LINKS[file_type]
        download_url = create_download_link(mediafire_url)
        return jsonify({'success': True, 'download_url': download_url})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)