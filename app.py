from flask import Flask, render_template_string, redirect, request

app = Flask(__name__)

# === LINK VUOTNHANH.COM ===
VUOTNHANH_LINKS = {
    # Free Fire - Android
    "esp_hong": "https://vuotnhanh.com/28uK",
    "esp_xanh": "https://vuotnhanh.com/mpfy",
    "eleven_crack": "https://vuotnhanh.com/i9D3",
    "aimbot": "https://vuotnhanh.com/CRKh",
    "freefire_vip": "https://vuotnhanh.com/MFCO",
    "naruto_ping": "https://vuotnhanh.com/x24C",
    "henry_ping": "https://vuotnhanh.com/vmqo",
    "tangnhay_v1": "https://vuotnhanh.com/cXXE",
    "script_doraemon": "https://vuotnhanh.com/KYhj",
    "xuyen_keo": "https://vuotnhanh.com/vh8w",
    "dam_ra_van_go": "https://vuotnhanh.com/WuFE",
    "xuyen_all_map": "https://vuotnhanh.com/xc3u",
    "fix_lag": "https://vuotnhanh.com/OYSE",
    "nhe_tam": "https://vuotnhanh.com/sMvv",
    "aim_dau_v2": "https://vuotnhanh.com/0n1q",
    "magic_bullet": "https://vuotnhanh.com/YswI",
    "ff_global": "https://vuotnhanh.com/mu6L",
    "ff_max_beta_android": "https://vuotnhanh.com/LKzm",
    
    # Free Fire - PC
    "ff_max_beta_pc": "https://vuotnhanh.com/LKzm",
    "block_defend": "https://vuotnhanh.com/tDis",
    "menu_freefire_pc": "https://vuotnhanh.com/kTrZ",
    
    # Roblox - Android
    "delta_x": "https://vuotnhanh.com/XWxu",
    "file_login": "https://vuotnhanh.com/hErc",
    "file_login_vohan": "https://vuotnhanh.com/ngYP",
    "delta_x_mod": "https://vuotnhanh.com/7LPd",
    "delta_x_fixlag": "https://vuotnhanh.com/IKqj",
    "arceus_x": "https://trafficvn.com/links/robloxv6",
    
    # PUBG - Android
    "falcon_x": "https://vuotnhanh.com/sUac",
    "spider_cheat": "https://vuotnhanh.com/gwKh",
    "panda_crack": "https://vuotnhanh.com/2ZJH",
    "ali_dev": "https://vuotnhanh.com/6YoS",
    "max_loader": "https://vuotnhanh.com/tVpa",
    "fast_loader": "https://vuotnhanh.com/m0eq",
    "speedy_loader": "https://vuotnhanh.com/iqdT",
    "naruto_engine_global": "https://vuotnhanh.com/0q2m",
    "naruto_engine_korea": "https://vuotnhanh.com/q62r",
    "naruto_engine_taiwan": "https://vuotnhanh.com/Ni3g",
    "getkey_loaders": "https://vuotnhanh.com/CWzp"
}

# === SCRIPT LUA CHO ROBLOX ===
SCRIPTS = {
    "redz_hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/huy384/redzHub/refs/heads/main/redzHub.lua"))()',
    "speedx_hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/AhmadV99/Speed-Hub-X/main/Speed%20Hub%20X.lua"))()',
    "neru_hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/NeroHubClub/AutoMythicFruitFinder/refs/heads/main/NeroHubFruitFinder"))()',
    "teddy_hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Teddyseetink/Haidepzai/refs/heads/main/TeddyHub.lua"))()',
    "thanhub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/thantzy/thanhub/refs/heads/main/thanv1"))()',
    "vxeze_hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Dex-Bear/Vxezehub/refs/heads/main/VxezeHubMain"))()',
    "banana_hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/obiiyeuem/vthangsitink/main/BananaHub.lua"))()',
    "hoho_hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/acsu123/HOHO_H/main/Loading_UI"))()',
    "bulex_hub": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/Dev-BlueX/BlueX-Hub/refs/heads/main/Main.lua"))()',
    "datthg_v2": 'loadstring(game:HttpGet("https://raw.githubusercontent.com/LuaCrack/DatThg/refs/heads/main/DatThgV2"))()'
}

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>QANH MOD GAME - Hack Game</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Poppins', sans-serif;
            background: radial-gradient(circle at 10% 20%, #0a0a1a, #03030f);
            color: #fff;
            min-height: 100vh;
            overflow-x: hidden;
        }

        /* Animated background particles */
        .bg-animation {
            position: fixed;
            width: 100%;
            height: 100%;
            z-index: 0;
            overflow: hidden;
        }

        .bg-animation span {
            position: absolute;
            width: 4px;
            height: 4px;
            background: rgba(0, 255, 136, 0.3);
            border-radius: 50%;
            animation: floatStar 8s infinite linear;
        }

        @keyframes floatStar {
            0% { transform: translateY(100vh) scale(0); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translateY(-100vh) scale(1); opacity: 0; }
        }

        /* Neon glow animation */
        @keyframes neonGlow {
            0%, 100% { text-shadow: 0 0 5px #00ff88, 0 0 10px #00ff88; }
            50% { text-shadow: 0 0 20px #00ff88, 0 0 30px #00b8ff; }
        }

        @keyframes borderGlow {
            0% { border-color: rgba(0,255,136,0.2); box-shadow: 0 0 0px rgba(0,255,136,0); }
            50% { border-color: rgba(0,255,136,0.8); box-shadow: 0 0 20px rgba(0,255,136,0.3); }
            100% { border-color: rgba(0,255,136,0.2); box-shadow: 0 0 0px rgba(0,255,136,0); }
        }

        @keyframes slideIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes scalePulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        .container {
            position: relative;
            z-index: 1;
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            animation: slideIn 0.6s ease-out;
        }

        /* Header animations */
        .header { text-align: center; margin-bottom: 40px; }
        .logo { 
            font-size: 3rem; 
            font-weight: 800; 
            background: linear-gradient(135deg, #00ff88, #00b8ff, #ff6b6b, #ff00ff);
            background-size: 300% 300%;
            -webkit-background-clip: text; 
            background-clip: text; 
            color: transparent; 
            animation: gradientShift 4s ease infinite;
        }
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .slogan { color: rgba(255,255,255,0.5); font-size: 0.9rem; margin-top: 8px; animation: fadeInUp 0.8s ease; }
        @keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

        /* Stats with hover effects */
        .stats {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-bottom: 40px;
            flex-wrap: wrap;
        }

        .stat-card {
            background: rgba(255,255,255,0.03);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(0,255,136,0.2);
            border-radius: 60px;
            padding: 8px 24px;
            display: flex;
            align-items: center;
            gap: 12px;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            animation: float 3s ease-in-out infinite;
        }
        .stat-card:nth-child(1) { animation-delay: 0s; }
        .stat-card:nth-child(2) { animation-delay: 0.2s; }
        .stat-card:nth-child(3) { animation-delay: 0.4s; }
        .stat-card:nth-child(4) { animation-delay: 0.6s; }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-5px); }
        }
        
        .stat-card:hover { 
            border-color: #00ff88; 
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 5px 25px rgba(0,255,136,0.3);
        }
        .stat-card i { font-size: 1.4rem; color: #00ff88; transition: transform 0.3s; }
        .stat-card:hover i { transform: rotate(360deg); }
        .stat-card span { font-weight: 600; }
        .stat-card small { color: rgba(255,255,255,0.5); font-size: 0.8rem; }

        .games-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 25px;
        }

        /* Game card with neon border animation */
        .game-card {
            background: rgba(15, 20, 35, 0.6);
            backdrop-filter: blur(12px);
            border-radius: 24px;
            border: 1px solid rgba(0,255,136,0.2);
            overflow: hidden;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
        }
        
        .game-card::before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: linear-gradient(45deg, #00ff88, #00b8ff, #ff6b6b, #ff00ff);
            background-size: 400% 400%;
            border-radius: 26px;
            opacity: 0;
            z-index: -1;
            transition: opacity 0.5s;
        }
        
        .game-card:hover::before {
            opacity: 0.3;
            animation: borderGlowMove 3s ease infinite;
        }
        
        @keyframes borderGlowMove {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .game-card:hover { 
            transform: translateY(-10px) scale(1.01);
            box-shadow: 0 20px 40px rgba(0,255,136,0.2);
        }

        .game-header { 
            padding: 20px; 
            text-align: center; 
            border-bottom: 1px solid rgba(255,255,255,0.05);
            transition: all 0.3s;
        }
        .game-card:hover .game-header { background: rgba(0,255,136,0.05); }
        
        .game-header h2 { font-size: 1.8rem; display: flex; align-items: center; justify-content: center; gap: 12px; }
        .game-header.ff h2 { color: #ff6b6b; text-shadow: 0 0 10px rgba(255,107,107,0.5); }
        .game-header.rbx h2 { color: #ffd93d; text-shadow: 0 0 10px rgba(255,217,61,0.5); }
        .game-header.pubg h2 { color: #6bcbff; text-shadow: 0 0 10px rgba(107,203,255,0.5); }

        /* Hot tag animation */
        .hot-tag {
            position: absolute;
            top: 15px;
            right: 15px;
            background: linear-gradient(135deg, #ff6b6b, #ff0000);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.7rem;
            font-weight: 700;
            animation: pulse 1.5s infinite;
            z-index: 2;
        }
        @keyframes pulse { 
            0%, 100% { opacity: 1; transform: scale(1); box-shadow: 0 0 0px rgba(255,0,0,0); }
            50% { opacity: 0.9; transform: scale(1.05); box-shadow: 0 0 15px rgba(255,0,0,0.5); }
        }

        .platform-section { padding: 16px; animation: fadeInUp 0.5s ease; }
        .platform-title { 
            font-size: 1rem; 
            font-weight: 600; 
            margin-bottom: 12px; 
            padding-left: 10px; 
            border-left: 3px solid #00ff88; 
            display: flex; 
            align-items: center; 
            gap: 8px;
            transition: all 0.3s;
        }
        .platform-section:hover .platform-title { border-left-color: #ff6b6b; }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 10px;
        }

        /* Feature item with 3D hover effect */
        .feature-item {
            background: rgba(0,0,0,0.4);
            border-radius: 14px;
            padding: 12px;
            text-align: center;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            cursor: pointer;
            border: 1px solid rgba(255,255,255,0.05);
            position: relative;
            overflow: hidden;
        }
        
        .feature-item::after {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            transition: left 0.5s;
        }
        
        .feature-item:hover::after {
            left: 100%;
        }
        
        .feature-item:hover { 
            transform: translateY(-5px) scale(1.02);
            background: rgba(0,255,136,0.15);
            border-color: #00ff88;
            box-shadow: 0 5px 20px rgba(0,255,136,0.2);
        }

        .feature-name {
            font-size: 0.85rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            margin-bottom: 6px;
        }
        .feature-name i { font-size: 1rem; transition: transform 0.3s; }
        .feature-item:hover .feature-name i { transform: scale(1.2); }

        .feature-note {
            font-size: 0.6rem;
            color: rgba(255,255,255,0.5);
            margin-top: 4px;
        }

        .feature-acc {
            font-size: 0.6rem;
            font-family: monospace;
            background: rgba(0,0,0,0.5);
            padding: 4px 8px;
            border-radius: 8px;
            margin: 6px 0;
            color: rgba(255,255,255,0.7);
        }

        /* Button animation */
        .btn-down {
            width: 100%;
            padding: 8px;
            margin-top: 8px;
            background: linear-gradient(135deg, #00ff88, #0099ff);
            border: none;
            border-radius: 30px;
            color: #0a0f1e;
            font-weight: 700;
            font-size: 0.75rem;
            cursor: pointer;
            transition: all 0.3s;
            position: relative;
            overflow: hidden;
        }
        
        .btn-down::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transition: left 0.5s;
        }
        
        .btn-down:hover::before { left: 100%; }
        .btn-down:hover { transform: scale(1.02); box-shadow: 0 5px 20px rgba(0,255,136,0.5); background: linear-gradient(135deg, #00cc66, #0088cc); }

        /* Script section */
        .script-section {
            margin-top: 16px;
            padding: 12px;
            background: rgba(0,0,0,0.3);
            border-radius: 16px;
        }

        .script-title {
            font-size: 0.9rem;
            font-weight: 600;
            margin-bottom: 12px;
            color: #ffd93d;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .script-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 8px;
        }

        .script-item {
            background: rgba(0,0,0,0.4);
            border-radius: 10px;
            padding: 8px 12px;
            font-size: 0.7rem;
            font-family: monospace;
            cursor: pointer;
            transition: all 0.3s;
            border: 1px solid rgba(255,217,61,0.3);
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }
        .script-item:hover { 
            background: rgba(255,217,61,0.2); 
            border-color: #ffd93d;
            transform: translateX(5px);
        }
        .script-code { flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: rgba(255,255,255,0.8); }
        .copy-btn { 
            background: rgba(255,217,61,0.3); 
            border: none; 
            border-radius: 6px; 
            padding: 4px 8px; 
            color: #ffd93d; 
            font-size: 0.65rem; 
            cursor: pointer; 
            transition: all 0.3s;
        }
        .copy-btn:hover { background: #ffd93d; color: #0a0f1e; transform: scale(1.05); }

        /* Toast message */
        .toast-msg {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            background: linear-gradient(135deg, #00ff88, #00b8ff);
            color: #0a0f1e;
            padding: 12px 24px;
            border-radius: 50px;
            font-size: 0.85rem;
            font-weight: 600;
            z-index: 999;
            display: none;
            animation: toastSlide 0.3s ease, fadeOut 0.3s ease 1.7s forwards;
            white-space: nowrap;
        }
        @keyframes toastSlide {
            from { opacity: 0; transform: translateX(-50%) translateY(20px); }
            to { opacity: 1; transform: translateX(-50%) translateY(0); }
        }
        @keyframes fadeOut {
            to { opacity: 0; visibility: hidden; }
        }

        .footer {
            text-align: center;
            padding: 30px;
            margin-top: 40px;
            border-top: 1px solid rgba(255,255,255,0.05);
            color: rgba(255,255,255,0.3);
            font-size: 0.8rem;
        }

        @media (max-width: 768px) {
            .container { padding: 15px; }
            .logo { font-size: 2rem; }
            .stats { gap: 12px; }
            .stat-card { padding: 5px 16px; font-size: 0.8rem; }
            .games-grid { grid-template-columns: 1fr; }
            .feature-grid { grid-template-columns: 1fr; }
            .script-grid { grid-template-columns: 1fr; }
            .toast-msg { white-space: normal; text-align: center; font-size: 0.7rem; width: 80%; }
        }
    </style>
</head>
<body>

<div class="bg-animation" id="stars"></div>
<div class="toast-msg" id="toastMsg"><i class="fas fa-check-circle"></i> Đã sao chép!</div>

<div class="container">
    <div class="header">
        <div class="logo">⚡ QANH MOD GAME ⚡</div>
        <div class="slogan"><i class="fas fa-gem"></i> Hack Game - Mod Skin - Script Hub - Hỗ trợ 24/7 <i class="fas fa-gem"></i></div>
    </div>

    <div class="stats">
        <div class="stat-card"><i class="fas fa-users"></i> <span>10,000+</span> <small>Thành viên</small></div>
        <div class="stat-card"><i class="fas fa-download"></i> <span>50,000+</span> <small>Lượt tải</small></div>
        <div class="stat-card"><i class="fas fa-star"></i> <span>4.9</span> <small>Đánh giá</small></div>
        <div class="stat-card"><i class="fas fa-shield-alt"></i> <span>Uy tín</span> <small>#1</small></div>
    </div>

    <div class="games-grid">
        <!-- FREE FIRE -->
        <div class="game-card">
            <div class="hot-tag"><i class="fas fa-fire"></i> HOT</div>
            <div class="game-header ff">
                <h2><i class="fas fa-gamepad"></i> FREE FIRE <i class="fas fa-skull"></i></h2>
            </div>
            
            <!-- Android -->
            <div class="platform-section">
                <div class="platform-title"><i class="fab fa-android"></i> ANDROID</div>
                <div class="feature-grid">
                    <div class="feature-item" onclick="location.href='/download/ff_max_beta_android'">
                        <div class="feature-name"><i class="fas fa-fire"></i> FF Max Beta</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/esp_hong'">
                        <div class="feature-name"><i class="fas fa-heart"></i> Esp Hồng</div>
                        <div class="feature-acc"><i class="fas fa-user"></i> LIMON-GAMING-OFC <br> <i class="fas fa-lock"></i> 248194848323</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/esp_xanh'">
                        <div class="feature-name"><i class="fas fa-leaf"></i> Esp Xanh</div>
                        <div class="feature-acc"><i class="fas fa-key"></i> Pass zip: CHATANMODS</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/eleven_crack'">
                        <div class="feature-name"><i class="fas fa-bolt"></i> Eleven Crack</div>
                        <div class="feature-note"><i class="fas fa-skull-crossbones"></i> (cần root)</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/aimbot'">
                        <div class="feature-name"><i class="fas fa-crosshairs"></i> AimBot 90%</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/freefire_vip'">
                        <div class="feature-name"><i class="fas fa-crown"></i> Menu Free Fire VIP</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/naruto_ping'">
                        <div class="feature-name"><i class="fas fa-user-ninja"></i> Naruto Ping Crack</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/henry_ping'">
                        <div class="feature-name"><i class="fas fa-bolt"></i> Henry Ping Crack</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/tangnhay_v1'">
                        <div class="feature-name"><i class="fas fa-tachometer-alt"></i> Tăng Nhạy V1</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/script_doraemon'">
                        <div class="feature-name"><i class="fas fa-robot"></i> Script Doraemon V3</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/xuyen_keo'">
                        <div class="feature-name"><i class="fas fa-ghost"></i> Đi xuyên keo</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/dam_ra_van_go'">
                        <div class="feature-name"><i class="fas fa-fist-raised"></i> Đấm ra ván gỗ</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/xuyen_all_map'">
                        <div class="feature-name"><i class="fas fa-map"></i> Đi xuyên all map, đán ra sàn kính</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/fix_lag'">
                        <div class="feature-name"><i class="fas fa-wrench"></i> Fix lag</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/nhe_tam'">
                        <div class="feature-name"><i class="fas fa-leaf"></i> Nhẹ tâm</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/aim_dau_v2'">
                        <div class="feature-name"><i class="fas fa-bullseye"></i> Aim đầu v2</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/magic_bullet'">
                        <div class="feature-name"><i class="fas fa-magic"></i> Magic Bullet, xuyên keo</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/ff_global'">
                        <div class="feature-name"><i class="fas fa-globe"></i> Free Fire Global</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                </div>
            </div>
            
            <!-- PC -->
            <div class="platform-section">
                <div class="platform-title"><i class="fas fa-desktop"></i> PC (Bluestacks)</div>
                <div class="feature-grid">
                    <div class="feature-item" onclick="location.href='/download/ff_max_beta_pc'">
                        <div class="feature-name"><i class="fas fa-fire"></i> FF Max Beta</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/block_defend'">
                        <div class="feature-name"><i class="fas fa-shield-alt"></i> Block Defend</div>
                        <div class="feature-acc"><i class="fas fa-key"></i> Pass rar: Z4</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/menu_freefire_pc'">
                        <div class="feature-name"><i class="fas fa-crown"></i> Menu Free Fire PC</div>
                        <div class="feature-acc"><i class="fas fa-user"></i> User: Old &nbsp;|&nbsp; <i class="fas fa-lock"></i> Pas: 1<br><i class="fas fa-key"></i> Pass rar: 1</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                </div>
            </div>
            
            <!-- iOS -->
            <div class="platform-section">
                <div class="platform-title"><i class="fab fa-apple"></i> iOS</div>
                <div style="text-align:center; padding:20px; color:#666;"><i class="fas fa-clock"></i> Đang cập nhật...</div>
            </div>
        </div>

        <!-- ROBLOX -->
        <div class="game-card">
            <div class="game-header rbx">
                <h2><i class="fab fa-fort-awesome"></i> ROBLOX</h2>
            </div>
            
            <!-- Android -->
            <div class="platform-section">
                <div class="platform-title"><i class="fab fa-android"></i> ANDROID</div>
                <div class="feature-grid">
                    <div class="feature-item" onclick="location.href='/download/delta_x'">
                        <div class="feature-name"><i class="fas fa-dragon"></i> Delta X Quốc Tế</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/file_login'">
                        <div class="feature-name"><i class="fas fa-sign-in-alt"></i> File Login</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/file_login_vohan'">
                        <div class="feature-name"><i class="fas fa-infinity"></i> File Login Vô Hạn</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/delta_x_mod'">
                        <div class="feature-name"><i class="fas fa-cogs"></i> Delta X Mod (không cài đè)</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/delta_x_fixlag'">
                        <div class="feature-name"><i class="fas fa-tachometer-alt"></i> Delta X Fix Lag</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/arceus_x'">
                        <div class="feature-name"><i class="fas fa-dove"></i> Arceus X Quốc Tế</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                </div>
            </div>
            
            <!-- Script Hub -->
            <div class="platform-section">
                <div class="platform-title"><i class="fas fa-code"></i> SCRIPT HUB</div>
                <div class="script-section">
                    <div class="script-grid">
                        <div class="script-item" onclick="copyScript('redz_hub')"><span class="script-code">🔴 RedZ Hub No Key</span><button class="copy-btn"><i class="fas fa-copy"></i> Sao chép</button></div>
                        <div class="script-item" onclick="copyScript('speedx_hub')"><span class="script-code">⚡ SpeedX Hub</span><button class="copy-btn"><i class="fas fa-copy"></i> Sao chép</button></div>
                        <div class="script-item" onclick="copyScript('neru_hub')"><span class="script-code">🌀 Neru Hub</span><button class="copy-btn"><i class="fas fa-copy"></i> Sao chép</button></div>
                        <div class="script-item" onclick="copyScript('teddy_hub')"><span class="script-code">🧸 Teddy Hub [Beta]</span><button class="copy-btn"><i class="fas fa-copy"></i> Sao chép</button></div>
                        <div class="script-item" onclick="copyScript('thanhub')"><span class="script-code">💎 Thanhub Freemium</span><button class="copy-btn"><i class="fas fa-copy"></i> Sao chép</button></div>
                        <div class="script-item" onclick="copyScript('vxeze_hub')"><span class="script-code">🐉 Vxeze Hub</span><button class="copy-btn"><i class="fas fa-copy"></i> Sao chép</button></div>
                        <div class="script-item" onclick="copyScript('banana_hub')"><span class="script-code">🍌 Banana Hub</span><button class="copy-btn"><i class="fas fa-copy"></i> Sao chép</button></div>
                        <div class="script-item" onclick="copyScript('hoho_hub')"><span class="script-code">🎭 Hoho Hub</span><button class="copy-btn"><i class="fas fa-copy"></i> Sao chép</button></div>
                        <div class="script-item" onclick="copyScript('bulex_hub')"><span class="script-code">🔵 BuleX Hub</span><button class="copy-btn"><i class="fas fa-copy"></i> Sao chép</button></div>
                        <div class="script-item" onclick="copyScript('datthg_v2')"><span class="script-code">📀 DatThg V2</span><button class="copy-btn"><i class="fas fa-copy"></i> Sao chép</button></div>
                    </div>
                </div>
            </div>
            
            <!-- PC -->
            <div class="platform-section">
                <div class="platform-title"><i class="fas fa-desktop"></i> PC</div>
                <div style="text-align:center; padding:20px; color:#666;"><i class="fas fa-clock"></i> Đang cập nhật...</div>
            </div>
            
            <!-- iOS -->
            <div class="platform-section">
                <div class="platform-title"><i class="fab fa-apple"></i> iOS</div>
                <div style="text-align:center; padding:20px; color:#666;"><i class="fas fa-clock"></i> Đang cập nhật...</div>
            </div>
        </div>

        <!-- PUBG -->
        <div class="game-card">
            <div class="game-header pubg">
                <h2><i class="fas fa-gun"></i> PUBG</h2>
            </div>
            
            <!-- Android -->
            <div class="platform-section">
                <div class="platform-title"><i class="fab fa-android"></i> ANDROID</div>
                <div class="feature-grid">
                    <div class="feature-item" onclick="location.href='/download/falcon_x'">
                        <div class="feature-name"><i class="fas fa-falcon"></i> Falcon X Loader</div>
                        <div class="feature-note"><i class="fas fa-skull-crossbones"></i> (cần root)</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/spider_cheat'">
                        <div class="feature-name"><i class="fas fa-spider"></i> Spider Cheat v2</div>
                        <div class="feature-note"><i class="fas fa-skull-crossbones"></i> (cần root)</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/panda_crack'">
                        <div class="feature-name"><i class="fas fa-panda"></i> Panda Crack</div>
                        <div class="feature-note"><i class="fas fa-skull-crossbones"></i> (cần root)</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/ali_dev'">
                        <div class="feature-name"><i class="fas fa-code"></i> Ali Dev Loader</div>
                        <div class="feature-note"><i class="fas fa-skull-crossbones"></i> (cần root)</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/max_loader'">
                        <div class="feature-name"><i class="fas fa-chart-line"></i> Max Loader Crack</div>
                        <div class="feature-note"><i class="fas fa-skull-crossbones"></i> (cần root)</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/fast_loader'">
                        <div class="feature-name"><i class="fas fa-rocket"></i> Fast Loader Crack</div>
                        <div class="feature-note"><i class="fas fa-skull-crossbones"></i> (cần root)</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/speedy_loader'">
                        <div class="feature-name"><i class="fas fa-tachometer-alt"></i> Speedy Loader Crack</div>
                        <div class="feature-note"><i class="fas fa-skull-crossbones"></i> (cần root)</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/naruto_engine_global'">
                        <div class="feature-name"><i class="fas fa-globe-asia"></i> Naruto Engine Global</div>
                        <div class="feature-note"><i class="fas fa-file"></i> APK</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/naruto_engine_korea'">
                        <div class="feature-name"><i class="fas fa-flag-checkered"></i> Naruto Engine Korea</div>
                        <div class="feature-note"><i class="fas fa-file"></i> APK</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/naruto_engine_taiwan'">
                        <div class="feature-name"><i class="fas fa-flag"></i> Naruto Engine Taiwan</div>
                        <div class="feature-note"><i class="fas fa-file"></i> APK</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                    <div class="feature-item" onclick="location.href='/download/getkey_loaders'">
                        <div class="feature-name"><i class="fas fa-key"></i> Getkey các Loader</div>
                        <button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button>
                    </div>
                </div>
            </div>
            
            <!-- PC -->
            <div class="platform-section">
                <div class="platform-title"><i class="fas fa-desktop"></i> PC</div>
                <div style="text-align:center; padding:20px; color:#666;"><i class="fas fa-clock"></i> Đang cập nhật...</div>
            </div>
            
            <!-- iOS -->
            <div class="platform-section">
                <div class="platform-title"><i class="fab fa-apple"></i> iOS</div>
                <div style="text-align:center; padding:20px; color:#666;"><i class="fas fa-clock"></i> Đang cập nhật...</div>
            </div>
        </div>
    </div>

    <div class="footer">
        <i class="fas fa-shield-alt"></i> QANH MOD GAME - Uy tín hàng đầu Việt Nam<br>
        © 2026 - All rights reserved
    </div>
</div>

<script>
    // Tạo hiệu ứng sao bay
    const starsContainer = document.getElementById('stars');
    for (let i = 0; i < 150; i++) {
        const star = document.createElement('span');
        star.style.left = Math.random() * 100 + '%';
        star.style.animationDelay = Math.random() * 8 + 's';
        star.style.animationDuration = 3 + Math.random() * 7 + 's';
        star.style.width = star.style.height = (Math.random() * 4 + 1) + 'px';
        star.style.background = `rgba(0, 255, ${100 + Math.random() * 155}, ${0.2 + Math.random() * 0.6})`;
        starsContainer.appendChild(star);
    }

    // Script data từ backend
    const scripts = {{ scripts|tojson }};

    function copyScript(scriptKey) {
        const scriptCode = scripts[scriptKey];
        if (!scriptCode) return;
        
        navigator.clipboard.writeText(scriptCode).then(() => {
            const toast = document.getElementById('toastMsg');
            toast.style.display = 'block';
            setTimeout(() => {
                toast.style.display = 'none';
            }, 2000);
        });
    }
</script>

</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, scripts=SCRIPTS)

@app.route('/download/<file_type>')
def download(file_type):
    if file_type not in VUOTNHANH_LINKS:
        return "Invalid file type", 400
    return redirect(VUOTNHANH_LINKS[file_type])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)