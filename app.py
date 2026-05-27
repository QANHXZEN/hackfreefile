from flask import Flask, render_template_string, redirect, request

app = Flask(__name__)

# === LINK VUOTNHANH.COM ===
VUOTNHANH_LINKS = {
    # Free Fire - Android
    "ff_max_beta": "https://vuotnhanh.com/LKzm",
    "dinh_vi_hong": "https://vuotnhanh.com/28uK",
    "dinh_vi_xanh_la": "https://vuotnhanh.com/mpfy",
    "dinh_vi_xanh_duong": "https://vuotnhanh.com/xUoW",
    "dinh_vi_vang_dam": "https://vuotnhanh.com/H0SP",
    "dinh_vi_cam_vang": "https://vuotnhanh.com/JkeV",
    "dinh_vi_xanh_vang": "https://vuotnhanh.com/zYKa",
    "dinh_vi_xanh_la_nhat_trong_suot": "https://vuotnhanh.com/UNAP",
    "dinh_vi_do_trang": "https://vuotnhanh.com/vQpe",
    "dinh_vi_xanh_trang": "https://vuotnhanh.com/SGj2",
    "dinh_vi_xanh_la_nhat": "https://vuotnhanh.com/IQn1",
    "dinh_vi_xanh_la_dam": "https://vuotnhanh.com/uU1K",
    "dinh_vi_vip_pro": "https://vuotnhanh.com/IaL8",
    "dinh_vi_vip_pro_v2": "https://vuotnhanh.com/Nc0D",
    "dinh_vi_trang": "https://vuotnhanh.com/lcp3",
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

# ==================== HTML FULL ANIMATIONS ====================
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
            background: #0a0a0f;
            color: #fff;
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }
        
        /* Animated Background Grid */
        .grid-bg {
            position: fixed;
            width: 100%;
            height: 100%;
            background-image: 
                linear-gradient(rgba(0, 255, 136, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 255, 136, 0.03) 1px, transparent 1px);
            background-size: 50px 50px;
            z-index: 0;
        }
        
        /* Animated Gradient Orb */
        .orb {
            position: fixed;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(0,255,136,0.15), transparent 70%);
            border-radius: 50%;
            top: -200px;
            right: -200px;
            animation: orbFloat 15s ease-in-out infinite;
            z-index: 0;
        }
        
        .orb2 {
            bottom: -300px;
            left: -300px;
            top: auto;
            right: auto;
            width: 800px;
            height: 800px;
            background: radial-gradient(circle, rgba(0,184,255,0.1), transparent 70%);
            animation: orbFloat2 20s ease-in-out infinite;
        }
        
        @keyframes orbFloat {
            0%, 100% { transform: translate(0, 0) rotate(0deg); }
            50% { transform: translate(-50px, 50px) rotate(180deg); }
        }
        
        @keyframes orbFloat2 {
            0%, 100% { transform: translate(0, 0) rotate(0deg); }
            50% { transform: translate(50px, -50px) rotate(-180deg); }
        }
        
        /* Floating Particles */
        .particle {
            position: fixed;
            width: 2px;
            height: 2px;
            background: #00ff88;
            border-radius: 50%;
            opacity: 0;
            animation: particleFloat 10s infinite linear;
            z-index: 0;
        }
        
        @keyframes particleFloat {
            0% {
                transform: translateY(100vh) scale(0);
                opacity: 0;
            }
            10% { opacity: 0.6; }
            90% { opacity: 0.6; }
            100% {
                transform: translateY(-100vh) scale(1);
                opacity: 0;
            }
        }
        
        .container {
            position: relative;
            z-index: 1;
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        
        /* Header Animation */
        .header { text-align: center; margin-bottom: 40px; }
        .logo {
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #00ff88, #00b8ff, #ff6b6b, #ff00ff);
            background-size: 400% 400%;
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            animation: gradientShift 4s ease infinite, textGlow 2s ease-in-out infinite;
        }
        
        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        @keyframes textGlow {
            0%, 100% { text-shadow: 0 0 0px rgba(0,255,136,0); }
            50% { text-shadow: 0 0 20px rgba(0,255,136,0.5); }
        }
        
        .slogan {
            color: rgba(255,255,255,0.6);
            font-size: 0.9rem;
            margin-top: 8px;
            animation: fadeInUp 0.8s ease;
            letter-spacing: 1px;
        }
        
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Stats Cards */
        .stats {
            display: flex;
            justify-content: center;
            gap: 25px;
            margin-bottom: 50px;
            flex-wrap: wrap;
        }
        
        .stat-card {
            background: rgba(20, 25, 40, 0.6);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(0,255,136,0.2);
            border-radius: 60px;
            padding: 10px 28px;
            display: flex;
            align-items: center;
            gap: 12px;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            animation: fadeInUp 0.6s ease backwards;
            position: relative;
            overflow: hidden;
        }
        
        .stat-card:nth-child(1) { animation-delay: 0.1s; }
        .stat-card:nth-child(2) { animation-delay: 0.2s; }
        .stat-card:nth-child(3) { animation-delay: 0.3s; }
        .stat-card:nth-child(4) { animation-delay: 0.4s; }
        
        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            transition: left 0.5s;
        }
        
        .stat-card:hover::before { left: 100%; }
        .stat-card:hover {
            transform: translateY(-5px) scale(1.05);
            border-color: #00ff88;
            box-shadow: 0 10px 30px rgba(0,255,136,0.2);
        }
        
        .stat-card i {
            font-size: 1.5rem;
            color: #00ff88;
            transition: transform 0.3s;
        }
        
        .stat-card:hover i { transform: rotateY(180deg); }
        .stat-card span { font-weight: 700; font-size: 1.1rem; }
        .stat-card small { color: rgba(255,255,255,0.5); font-size: 0.8rem; }
        
        /* Game Grid */
        .games-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
            gap: 30px;
        }
        
        /* Game Card 3D Effect */
        .game-card {
            background: rgba(15, 20, 35, 0.5);
            backdrop-filter: blur(12px);
            border-radius: 28px;
            border: 1px solid rgba(0,255,136,0.15);
            overflow: hidden;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            animation: fadeInUp 0.6s ease backwards;
        }
        
        .game-card:nth-child(1) { animation-delay: 0.2s; }
        .game-card:nth-child(2) { animation-delay: 0.3s; }
        .game-card:nth-child(3) { animation-delay: 0.4s; }
        
        .game-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(0,255,136,0.05), transparent);
            opacity: 0;
            transition: opacity 0.5s;
            pointer-events: none;
        }
        
        .game-card:hover {
            transform: translateY(-12px);
            border-color: #00ff88;
            box-shadow: 0 25px 45px rgba(0,255,136,0.15);
        }
        
        .game-card:hover::before { opacity: 1; }
        
        .game-header {
            padding: 25px;
            text-align: center;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            position: relative;
        }
        
        .game-header h2 {
            font-size: 2rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
        }
        
        .game-header.ff h2 { 
            color: #ff6b6b; 
            text-shadow: 0 0 20px rgba(255,107,107,0.3);
        }
        .game-header.rbx h2 { 
            color: #ffd93d; 
            text-shadow: 0 0 20px rgba(255,217,61,0.3);
        }
        .game-header.pubg h2 { 
            color: #6bcbff; 
            text-shadow: 0 0 20px rgba(107,203,255,0.3);
        }
        
        /* Hot Tag */
        .hot-tag {
            position: absolute;
            top: 15px;
            right: 15px;
            background: linear-gradient(135deg, #ff6b6b, #ff0000);
            padding: 5px 14px;
            border-radius: 30px;
            font-size: 0.7rem;
            font-weight: 700;
            animation: hotPulse 1.5s infinite;
            z-index: 2;
            display: flex;
            align-items: center;
            gap: 5px;
        }
        
        @keyframes hotPulse {
            0%, 100% { transform: scale(1); box-shadow: 0 0 0px rgba(255,0,0,0); }
            50% { transform: scale(1.05); box-shadow: 0 0 15px rgba(255,0,0,0.5); }
        }
        
        /* Platform Section */
        .platform-section { padding: 18px; animation: fadeInUp 0.5s ease; }
        .platform-title {
            font-size: 1rem;
            font-weight: 600;
            margin-bottom: 15px;
            padding-left: 12px;
            border-left: 3px solid #00ff88;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.3s;
        }
        
        .platform-section:hover .platform-title { 
            border-left-color: #ff6b6b;
            transform: translateX(5px);
        }
        
        /* Feature Grid */
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
            gap: 12px;
        }
        
        /* Feature Item 3D Hover */
        .feature-item {
            background: rgba(0,0,0,0.35);
            border-radius: 16px;
            padding: 14px;
            text-align: center;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            cursor: pointer;
            border: 1px solid rgba(255,255,255,0.05);
            position: relative;
            overflow: hidden;
            animation: fadeInUp 0.5s ease backwards;
        }
        
        .feature-item:nth-child(1) { animation-delay: 0.05s; }
        .feature-item:nth-child(2) { animation-delay: 0.1s; }
        .feature-item:nth-child(3) { animation-delay: 0.15s; }
        .feature-item:nth-child(4) { animation-delay: 0.2s; }
        
        .feature-item::after {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent);
            transition: left 0.5s;
        }
        
        .feature-item:hover::after { left: 100%; }
        .feature-item:hover {
            transform: translateY(-5px) scale(1.02);
            background: rgba(0,255,136,0.12);
            border-color: #00ff88;
            box-shadow: 0 10px 25px rgba(0,255,136,0.15);
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
        
        .feature-note { font-size: 0.6rem; color: rgba(255,255,255,0.45); margin-top: 4px; }
        .feature-vuot { font-size: 0.6rem; color: #ffd93d; margin-top: 4px; font-weight: 500; display: flex; align-items: center; justify-content: center; gap: 4px; }
        .feature-khongvuot { font-size: 0.6rem; color: #ff6b6b; margin-top: 4px; font-weight: 500; display: flex; align-items: center; justify-content: center; gap: 4px; }
        
        .feature-acc {
            font-size: 0.6rem;
            font-family: monospace;
            background: rgba(0,0,0,0.5);
            padding: 5px 8px;
            border-radius: 8px;
            margin: 8px 0;
            color: rgba(255,255,255,0.7);
        }
        
        /* Button Animation */
        .btn-down {
            width: 100%;
            padding: 10px;
            margin-top: 8px;
            background: linear-gradient(95deg, #00ff88, #0099ff);
            background-size: 200% 200%;
            border: none;
            border-radius: 40px;
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
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transition: left 0.5s;
        }
        
        .btn-down:hover::before { left: 100%; }
        .btn-down:hover {
            background-position: 100% 0;
            transform: scale(1.02);
            box-shadow: 0 5px 20px rgba(0,255,136,0.4);
        }
        
        /* Script Section */
        .script-section {
            margin-top: 16px;
            padding: 12px;
            background: rgba(0,0,0,0.25);
            border-radius: 18px;
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
            grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
            gap: 8px;
        }
        
        .script-item {
            background: rgba(0,0,0,0.35);
            border-radius: 12px;
            padding: 8px 12px;
            font-size: 0.7rem;
            font-family: monospace;
            cursor: pointer;
            transition: all 0.3s;
            border: 1px solid rgba(255,217,61,0.25);
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }
        
        .script-item:hover {
            background: rgba(255,217,61,0.15);
            border-color: #ffd93d;
            transform: translateX(5px);
        }
        
        .script-code { flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: rgba(255,255,255,0.8); font-size: 0.65rem; }
        
        .copy-btn {
            background: rgba(255,217,61,0.2);
            border: none;
            border-radius: 8px;
            padding: 5px 12px;
            color: #ffd93d;
            font-size: 0.65rem;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            gap: 5px;
        }
        
        .copy-btn:hover {
            background: #ffd93d;
            color: #0a0f1e;
            transform: scale(1.05);
        }
        
        /* Toast Message */
        .toast-msg {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            background: linear-gradient(135deg, #00ff88, #00b8ff);
            color: #0a0f1e;
            padding: 12px 28px;
            border-radius: 60px;
            font-size: 0.85rem;
            font-weight: 600;
            z-index: 999;
            display: none;
            align-items: center;
            gap: 10px;
            animation: toastSlide 0.3s ease, toastFadeOut 0.3s ease 1.7s forwards;
            white-space: nowrap;
            box-shadow: 0 5px 25px rgba(0,255,136,0.3);
        }
        
        @keyframes toastSlide {
            from { opacity: 0; transform: translateX(-50%) translateY(30px); }
            to { opacity: 1; transform: translateX(-50%) translateY(0); }
        }
        
        @keyframes toastFadeOut {
            to { opacity: 0; visibility: hidden; }
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 35px;
            margin-top: 45px;
            border-top: 1px solid rgba(255,255,255,0.05);
            color: rgba(255,255,255,0.3);
            font-size: 0.8rem;
        }
        
        /* Scrollbar */
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: rgba(0,0,0,0.3); border-radius: 10px; }
        ::-webkit-scrollbar-thumb { background: #00ff88; border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: #00cc66; }
        
        @media (max-width: 768px) {
            .container { padding: 15px; }
            .logo { font-size: 2rem; }
            .stats { gap: 12px; }
            .stat-card { padding: 6px 18px; font-size: 0.8rem; }
            .stat-card i { font-size: 1.1rem; }
            .games-grid { grid-template-columns: 1fr; gap: 20px; }
            .feature-grid { grid-template-columns: 1fr; }
            .script-grid { grid-template-columns: 1fr; }
            .toast-msg { white-space: normal; text-align: center; font-size: 0.7rem; width: 85%; }
            .game-header h2 { font-size: 1.5rem; }
        }
    </style>
</head>
<body>

<div class="grid-bg"></div>
<div class="orb"></div>
<div class="orb orb2"></div>

<div class="toast-msg" id="toastMsg">
    <i class="fas fa-check-circle"></i> Đã sao chép!
</div>

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
            <!-- ANDROID -->
            <div class="platform-section">
                <div class="platform-title"><i class="fab fa-android"></i> ANDROID</div>
                <div class="feature-grid">
                    <div class="feature-item" onclick="location.href='/download/ff_max_beta'"><div class="feature-name"><i class="fas fa-fire"></i> FF Max Beta</div><div class="feature-khongvuot"><i class="fas fa-times-circle"></i> không vượt</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/dinh_vi_hong'"><div class="feature-name"><i class="fas fa-heart"></i> Định vị Hồng (FF Max)</div><div class="feature-acc"><i class="fas fa-user"></i> LIMON-GAMING-OFC <br> <i class="fas fa-lock"></i> 248194848323</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/dinh_vi_xanh_la'"><div class="feature-name"><i class="fas fa-leaf"></i> Định vị xanh lá (FF Max)</div><div class="feature-acc"><i class="fas fa-key"></i> Pass zip: CHATANMODS</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/dinh_vi_xanh_duong'"><div class="feature-name"><i class="fas fa-water"></i> Định vị xanh dương (FF Global)</div><div class="feature-acc"><i class="fas fa-key"></i> Pass zip: 555</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/dinh_vi_vang_dam'"><div class="feature-name"><i class="fas fa-crown"></i> Định vị vàng đậm (FF Max)</div><div class="feature-acc"><i class="fas fa-key"></i> Pass zip: 666</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/dinh_vi_cam_vang'"><div class="feature-name"><i class="fas fa-map-marker-alt"></i> Định vị cam vàng</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/dinh_vi_xanh_vang'"><div class="feature-name"><i class="fas fa-palette"></i> Định Vị Xanh, Vàng (FF Max)</div><div class="feature-acc"><i class="fas fa-key"></i> Pass zip: 277</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/dinh_vi_xanh_la_nhat_trong_suot'"><div class="feature-name"><i class="fas fa-tint"></i> Định Vị Xanh Lá Nhạt Trong Suốt (FF Global)</div><div class="feature-acc"><i class="fas fa-key"></i> Pass zip: 252</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/dinh_vi_do_trang'"><div class="feature-name"><i class="fas fa-fire"></i> Định Vị Đỏ, Trắng (FF Global)</div><div class="feature-acc"><i class="fas fa-key"></i> Pass zip: 878</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/dinh_vi_xanh_trang'"><div class="feature-name"><i class="fas fa-snowflake"></i> Định Vị Xanh, Trắng (FF Global)</div><div class="feature-acc"><i class="fas fa-key"></i> Pass zip: 111</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/dinh_vi_xanh_la_nhat'"><div class="feature-name"><i class="fas fa-leaf"></i> Định Vị Xanh Lá Nhạt (FF Max)</div><div class="feature-acc"><i class="fas fa-key"></i> Pass zip: 205</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/dinh_vi_xanh_la_dam'"><div class="feature-name"><i class="fas fa-tree"></i> Định Vị Xanh Lá Đậm (FF Max)</div><div class="feature-acc"><i class="fas fa-key"></i> Pass zip: 333</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/dinh_vi_vip_pro'"><div class="feature-name"><i class="fas fa-gem"></i> Định vị vip pro (FF Global)</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/dinh_vi_vip_pro_v2'"><div class="feature-name"><i class="fas fa-crown"></i> Định vị vip pro v2 (FF Global)</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/dinh_vi_trang'"><div class="feature-name"><i class="fas fa-circle"></i> Data Định Vị Trắng (FF Global)</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/eleven_crack'"><div class="feature-name"><i class="fas fa-bolt"></i> Eleven Crack</div><div class="feature-note"><i class="fas fa-skull-crossbones"></i> (cần root)</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/aimbot'"><div class="feature-name"><i class="fas fa-crosshairs"></i> AimBot 90%</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/freefire_vip'"><div class="feature-name"><i class="fas fa-crown"></i> Menu Free Fire VIP</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/naruto_ping'"><div class="feature-name"><i class="fas fa-user-ninja"></i> Naruto Ping Crack</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/henry_ping'"><div class="feature-name"><i class="fas fa-bolt"></i> Henry Ping Crack</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/tangnhay_v1'"><div class="feature-name"><i class="fas fa-tachometer-alt"></i> Tăng Nhạy V1</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/script_doraemon'"><div class="feature-name"><i class="fas fa-robot"></i> Script Doraemon V3</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/xuyen_keo'"><div class="feature-name"><i class="fas fa-ghost"></i> Đi xuyên keo</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/dam_ra_van_go'"><div class="feature-name"><i class="fas fa-fist-raised"></i> Đấm ra ván gỗ</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/xuyen_all_map'"><div class="feature-name"><i class="fas fa-map"></i> Đi xuyên all map, đán ra sàn kính</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/fix_lag'"><div class="feature-name"><i class="fas fa-wrench"></i> Fix lag</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/nhe_tam'"><div class="feature-name"><i class="fas fa-leaf"></i> Nhẹ tâm</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/aim_dau_v2'"><div class="feature-name"><i class="fas fa-bullseye"></i> Aim đầu v2</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/magic_bullet'"><div class="feature-name"><i class="fas fa-magic"></i> Magic Bullet, xuyên keo</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/ff_global'"><div class="feature-name"><i class="fas fa-globe"></i> Free Fire Global</div><div class="feature-khongvuot"><i class="fas fa-times-circle"></i> không vượt</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                </div>
            </div>
            <!-- PC -->
            <div class="platform-section">
                <div class="platform-title"><i class="fas fa-desktop"></i> PC</div>
                <div class="feature-grid">
                    <div class="feature-item" onclick="location.href='/download/ff_max_beta_pc'"><div class="feature-name"><i class="fas fa-fire"></i> FF Max Beta</div><div class="feature-khongvuot"><i class="fas fa-times-circle"></i> không vượt</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/block_defend'"><div class="feature-name"><i class="fas fa-shield-alt"></i> Block Defend</div><div class="feature-acc"><i class="fas fa-key"></i> Pass rar: Z4</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                    <div class="feature-item" onclick="location.href='/download/menu_freefire_pc'"><div class="feature-name"><i class="fas fa-crown"></i> Menu Free Fire PC</div><div class="feature-acc"><i class="fas fa-user"></i> User: Old &nbsp;|&nbsp; <i class="fas fa-lock"></i> Pas: 1<br><i class="fas fa-key"></i> Pass rar: 1</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                </div>
            </div>
            <!-- iOS -->
            <div class="platform-section">
                <div class="platform-title"><i class="fab fa-apple"></i> iOS</div>
                <div style="text-align:center; padding:30px; color:#666;"><i class="fas fa-clock"></i> Đang cập nhật...</div>
            </div>
        </div>

        <!-- ROBLOX -->
        <div class="game-card">
            <div class="game-header rbx"><h2><i class="fab fa-fort-awesome"></i> ROBLOX</h2></div>
            <div class="platform-section"><div class="platform-title"><i class="fab fa-android"></i> ANDROID</div><div class="feature-grid">
                <div class="feature-item" onclick="location.href='/download/delta_x'"><div class="feature-name"><i class="fas fa-dragon"></i> Delta X Quốc Tế</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                <div class="feature-item" onclick="location.href='/download/file_login'"><div class="feature-name"><i class="fas fa-sign-in-alt"></i> File Login</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                <div class="feature-item" onclick="location.href='/download/file_login_vohan'"><div class="feature-name"><i class="fas fa-infinity"></i> File Login Vô Hạn</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                <div class="feature-item" onclick="location.href='/download/delta_x_mod'"><div class="feature-name"><i class="fas fa-cogs"></i> Delta X Mod (không cài đè)</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                <div class="feature-item" onclick="location.href='/download/delta_x_fixlag'"><div class="feature-name"><i class="fas fa-tachometer-alt"></i> Delta X Fix Lag</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                <div class="feature-item" onclick="location.href='/download/arceus_x'"><div class="feature-name"><i class="fas fa-dove"></i> Arceus X Quốc Tế</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
            </div></div>
            <div class="platform-section"><div class="platform-title"><i class="fas fa-code"></i> SCRIPT HUB</div><div class="script-section"><div class="script-grid">
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
            </div></div></div>
            <div class="platform-section"><div class="platform-title"><i class="fas fa-desktop"></i> PC</div><div style="text-align:center; padding:30px; color:#666;"><i class="fas fa-clock"></i> Đang cập nhật...</div></div>
            <div class="platform-section"><div class="platform-title"><i class="fab fa-apple"></i> iOS</div><div style="text-align:center; padding:30px; color:#666;"><i class="fas fa-clock"></i> Đang cập nhật...</div></div>
        </div>

        <!-- PUBG -->
        <div class="game-card">
            <div class="game-header pubg"><h2><i class="fas fa-gun"></i> PUBG</h2></div>
            <div class="platform-section"><div class="platform-title"><i class="fab fa-android"></i> ANDROID</div><div class="feature-grid">
                <div class="feature-item" onclick="location.href='/download/falcon_x'"><div class="feature-name"><i class="fas fa-falcon"></i> Falcon X Loader</div><div class="feature-note"><i class="fas fa-skull-crossbones"></i> (cần root)</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                <div class="feature-item" onclick="location.href='/download/spider_cheat'"><div class="feature-name"><i class="fas fa-spider"></i> Spider Cheat v2</div><div class="feature-note"><i class="fas fa-skull-crossbones"></i> (cần root)</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                <div class="feature-item" onclick="location.href='/download/panda_crack'"><div class="feature-name"><i class="fas fa-panda"></i> Panda Crack</div><div class="feature-note"><i class="fas fa-skull-crossbones"></i> (cần root)</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                <div class="feature-item" onclick="location.href='/download/ali_dev'"><div class="feature-name"><i class="fas fa-code"></i> Ali Dev Loader</div><div class="feature-note"><i class="fas fa-skull-crossbones"></i> (cần root)</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                <div class="feature-item" onclick="location.href='/download/max_loader'"><div class="feature-name"><i class="fas fa-chart-line"></i> Max Loader Crack</div><div class="feature-note"><i class="fas fa-skull-crossbones"></i> (cần root)</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                <div class="feature-item" onclick="location.href='/download/fast_loader'"><div class="feature-name"><i class="fas fa-rocket"></i> Fast Loader Crack</div><div class="feature-note"><i class="fas fa-skull-crossbones"></i> (cần root)</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                <div class="feature-item" onclick="location.href='/download/speedy_loader'"><div class="feature-name"><i class="fas fa-tachometer-alt"></i> Speedy Loader Crack</div><div class="feature-note"><i class="fas fa-skull-crossbones"></i> (cần root)</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                <div class="feature-item" onclick="location.href='/download/naruto_engine_global'"><div class="feature-name"><i class="fas fa-globe-asia"></i> Naruto Engine Global</div><div class="feature-note"><i class="fas fa-file"></i> APK</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                <div class="feature-item" onclick="location.href='/download/naruto_engine_korea'"><div class="feature-name"><i class="fas fa-flag-checkered"></i> Naruto Engine Korea</div><div class="feature-note"><i class="fas fa-file"></i> APK</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                <div class="feature-item" onclick="location.href='/download/naruto_engine_taiwan'"><div class="feature-name"><i class="fas fa-flag"></i> Naruto Engine Taiwan</div><div class="feature-note"><i class="fas fa-file"></i> APK</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
                <div class="feature-item" onclick="location.href='/download/getkey_loaders'"><div class="feature-name"><i class="fas fa-key"></i> Getkey các Loader</div><div class="feature-vuot"><i class="fas fa-forward"></i> vượt 2 lần</div><button class="btn-down"><i class="fas fa-download"></i> TẢI NGAY</button></div>
            </div></div>
            <div class="platform-section"><div class="platform-title"><i class="fas fa-desktop"></i> PC</div><div style="text-align:center; padding:30px; color:#666;"><i class="fas fa-clock"></i> Đang cập nhật...</div></div>
            <div class="platform-section"><div class="platform-title"><i class="fab fa-apple"></i> iOS</div><div style="text-align:center; padding:30px; color:#666;"><i class="fas fa-clock"></i> Đang cập nhật...</div></div>
        </div>
    </div>

    <div class="footer">
        <i class="fas fa-shield-alt"></i> QANH MOD GAME - Uy tín hàng đầu Việt Nam<br>
        © 2026 - All rights reserved
    </div>
</div>

<script>
    // Tạo hạt bụi lấp lánh
    for (let i = 0; i < 80; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 10 + 's';
        particle.style.animationDuration = 5 + Math.random() * 10 + 's';
        particle.style.width = particle.style.height = (Math.random() * 3 + 1) + 'px';
        particle.style.background = `rgba(0, 255, ${100 + Math.random() * 155}, ${0.3 + Math.random() * 0.5})`;
        document.body.appendChild(particle);
    }
    
    // Copy script function
    const scripts = {{ scripts|tojson }};
    function copyScript(scriptKey) {
        const scriptCode = scripts[scriptKey];
        if (!scriptCode) return;
        navigator.clipboard.writeText(scriptCode).then(() => {
            const toast = document.getElementById('toastMsg');
            toast.style.display = 'flex';
            setTimeout(() => { toast.style.display = 'none'; }, 2000);
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