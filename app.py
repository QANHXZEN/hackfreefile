from flask import Flask, render_template_string, redirect

app = Flask(__name__)

# === LINK CỦA BẠN ===
TRAFFIC_LINKS = {
    "esp_vip": "https://trafficvn.com/links/qanhesp",
    "aimbot": "https://trafficvn.com/links/qanhaimbot",
    "freefire_vip": "https://trafficvn.com/links/qanh",
    "naruto_ping": "https://trafficvn.com/links/qanhv1",
    "henry_ping": "https://trafficvn.com/links/qanhv2"
}

# === HTML ===
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
        .feature-box.vip {
            border: 1px solid #ff00ff;
            background: linear-gradient(135deg, rgba(255,0,255,0.1), rgba(0,0,0,0.3));
        }
        .feature-box.naruto {
            border: 1px solid #ff9900;
            background: linear-gradient(135deg, rgba(255,153,0,0.1), rgba(0,0,0,0.3));
        }
        .feature-box.henry {
            border: 1px solid #00ccff;
            background: linear-gradient(135deg, rgba(0,204,255,0.1), rgba(0,0,0,0.3));
        }
        .feature-name {
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 10px;
            text-align: center;
        }
        .feature-name.esp { color: #ff6b6b; }
        .feature-name.aim { color: #ffd93d; }
        .feature-name.vip { color: #ff00ff; }
        .feature-name.naruto { color: #ff9900; }
        .feature-name.henry { color: #00ccff; }
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
                    
                    <!-- Esp Vip -->
                    <div class="feature-box esp">
                        <div class="feature-name esp">🎯 Esp Vip</div>
                        <div class="account-info">
                            📌 Tài khoản: LIMON-GAMING-OFC<br>
                            🔑 Mật khẩu: 248194848323
                        </div>
                        <button class="btn-download" onclick="window.location.href='/download/esp_vip'">⬇️ Tải xuống</button>
                    </div>

                    <!-- AimBot 90% -->
                    <div class="feature-box aim">
                        <div class="feature-name aim">🎯 AimBot 90%</div>
                        <button class="btn-download" onclick="window.location.href='/download/aimbot'">⬇️ Tải xuống</button>
                    </div>

                    <!-- Menu Free Fire VIP (đã đổi tên) -->
                    <div class="feature-box vip">
                        <div class="feature-name vip">📁 Menu Free Fire VIP</div>
                        <button class="btn-download" onclick="window.location.href='/download/freefire_vip'">⬇️ Tải xuống</button>
                    </div>

                    <!-- Naruto Ping Crack -->
                    <div class="feature-box naruto">
                        <div class="feature-name naruto">🍥 Naruto Ping Crack</div>
                        <button class="btn-download" onclick="window.location.href='/download/naruto_ping'">⬇️ Tải xuống</button>
                    </div>

                    <!-- Henry Ping Crack -->
                    <div class="feature-box henry">
                        <div class="feature-name henry">⚡ Henry Ping Crack</div>
                        <button class="btn-download" onclick="window.location.href='/download/henry_ping'">⬇️ Tải xuống</button>
                    </div>
                </div>

                <!-- iOS -->
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
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/download/<file_type>')
def download(file_type):
    if file_type not in TRAFFIC_LINKS:
        return "Invalid file type", 400
    return redirect(TRAFFIC_LINKS[file_type])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)