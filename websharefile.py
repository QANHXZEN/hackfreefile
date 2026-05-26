from flask import Flask, render_template_string, request, redirect, url_for
import requests
import json
import urllib.parse
import time
import hashlib

app = Flask(__name__)

# Cấu hình API
TRAFFIC_VN_TOKEN = "eef4080ff90f6180b109ecc46a78f33b"

# Link MediaFire cho từng khung
MEDIAFIRE_LINKS = {
    "esp_vip": "https://www.mediafire.com/file/hbrs6rr26flgz7z/FF+MAX+INJECTOR+MAIN+ID+SAFE+(1).zip/file",
    "aimbot": "https://www.mediafire.com/file/oged4p8u6blci0k/LEHER+HS+METADATA.7z/file"
}

# Thông tin tài khoản cho khung Esp Vip
ESP_ACCOUNT = {
    "username": "LIMON-GAMING-OFC",
    "password": "248194848323"
}

def create_link4m_url(mediafire_url):
    """Tạo link link4m từ mediafire_url (mock - cần API thực tế)"""
    # Giả lập tạo link4m, thực tế cần gọi API link4m
    encoded_url = urllib.parse.quote(mediafire_url, safe='')
    return f"https://link4m.com/create?url={encoded_url}"

def create_trafficvn_url(final_url):
    """Tạo link trafficvn từ final_url (link4m hoặc trực tiếp)"""
    # Giả lập API trafficvn - thực tế cần gọi đúng API
    timestamp = int(time.time())
    # Mô phỏng tạo link rút gọn
    fake_code = hashlib.md5(f"{final_url}{timestamp}".encode()).hexdigest()[:8]
    return f"https://traffic.vn/go/{fake_code}"

def create_download_link(mediafire_url):
    """Tạo chuỗi link hoàn chỉnh: trafficvn -> link4m -> mediafire"""
    # Bước 1: Tạo link link4m từ mediafire
    link4m_url = create_link4m_url(mediafire_url)
    # Bước 2: Tạo link trafficvn từ link4m
    trafficvn_url = create_trafficvn_url(link4m_url)
    return trafficvn_url

# HTML + CSS + JavaScript
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QanhNo1 - Chia Sẻ Tool Game</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0a0f1e 0%, #0d1525 100%);
            color: #fff;
            padding: 20px;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
        }

        h1 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 10px;
            background: linear-gradient(135deg, #00ff88, #00b8ff);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .sub {
            text-align: center;
            color: #888;
            margin-bottom: 40px;
        }

        /* 3 cột game */
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

        /* Responsive */
        @media (max-width: 768px) {
            .games-grid {
                grid-template-columns: 1fr;
            }
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
                
                <!-- Android -->
                <div class="platform-section">
                    <div class="platform-title">📱 ANDROID</div>
                    
                    <!-- Khung ESP VIP -->
                    <div class="feature-box esp">
                        <div class="feature-name esp">🎯 Esp Vip</div>
                        <div class="account-info">
                            📌 Tài khoản: LIMON-GAMING-OFC<br>
                            🔑 Mật khẩu: 248194848323
                        </div>
                        <button class="btn-download" onclick="downloadFile('esp_vip')">⬇️ Tải xuống</button>
                        <div id="loading-esp" class="loading">⏳ Đang tạo link...</div>
                    </div>

                    <!-- Khung AimBot 90% -->
                    <div class="feature-box aim">
                        <div class="feature-name aim">🎯 AimBot 90%</div>
                        <button class="btn-download" onclick="downloadFile('aimbot')">⬇️ Tải xuống</button>
                        <div id="loading-aim" class="loading">⏳ Đang tạo link...</div>
                    </div>
                </div>

                <!-- iOS (tạm thời chưa có nội dung) -->
                <div class="platform-section">
                    <div class="platform-title">🍎 iOS</div>
                    <div style="text-align: center; padding: 20px; color: #888;">
                        ⏳ Đang cập nhật...
                    </div>
                </div>
            </div>

            <!-- ROBLOX -->
            <div class="game-card">
                <div class="game-title rbx">🎮 ROBLOX</div>
                
                <div class="platform-section">
                    <div class="platform-title">📱 ANDROID</div>
                    <div style="text-align: center; padding: 20px; color: #888;">
                        ⏳ Đang cập nhật...
                    </div>
                </div>

                <div class="platform-section">
                    <div class="platform-title">🍎 iOS</div>
                    <div style="text-align: center; padding: 20px; color: #888;">
                        ⏳ Đang cập nhật...
                    </div>
                </div>
            </div>

            <!-- PUBG -->
            <div class="game-card">
                <div class="game-title pubg">🎯 PUBG</div>
                
                <div class="platform-section">
                    <div class="platform-title">📱 ANDROID</div>
                    <div style="text-align: center; padding: 20px; color: #888;">
                        ⏳ Đang cập nhật...
                    </div>
                </div>

                <div class="platform-section">
                    <div class="platform-title">🍎 iOS</div>
                    <div style="text-align: center; padding: 20px; color: #888;">
                        ⏳ Đang cập nhật...
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Hàm xử lý tải file - tạo link trafficvn -> link4m -> mediafire
        async function downloadFile(type) {
            const loadingId = type === 'esp_vip' ? 'loading-esp' : 'loading-aim';
            const loader = document.getElementById(loadingId);
            loader.style.display = 'block';
            
            try {
                const response = await fetch('/get_download_link', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ file_type: type })
                });
                
                const data = await response.json();
                
                if (data.success && data.download_url) {
                    // Chuyển hướng sang link trafficvn
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
            return {'success': False, 'error': 'Loại file không hợp lệ'}
        
        mediafire_url = MEDIAFIRE_LINKS[file_type]
        download_url = create_download_link(mediafire_url)
        
        return {'success': True, 'download_url': download_url}
    except Exception as e:
        return {'success': False, 'error': str(e)}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)