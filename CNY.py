import streamlit as st
import streamlit.components.v1 as components
import time
import random
import datetime
import urllib.parse
import html
import os

st.set_page_config(page_title="🧧 Red Packet Fun", page_icon="🧧")

# --- Optional tip jar config ---
# To enable: generate your own PayNow QR code from your banking app
# (DBS/OCBC/UOB etc. all have a "Share/Save PayNow QR" option) and save
# the image at the path below. Or set TIP_LINK to a Ko-fi/Buy Me a Coffee
# URL instead. Both are optional — leave as-is to skip the tip jar entirely.
TIP_QR_IMAGE_PATH = "assets/paynow_qr.png"
TIP_LINK = ""  # e.g. "https://ko-fi.com/yourname"

# --- Dynamic year & zodiac ---
CURRENT_YEAR = datetime.datetime.now().year

ZODIAC_ANIMALS = [
    "鼠 Rat", "牛 Ox", "虎 Tiger", "兔 Rabbit", "龙 Dragon", "蛇 Snake",
    "马 Horse", "羊 Goat", "猴 Monkey", "鸡 Rooster", "狗 Dog", "猪 Pig",
]
# 2020 was the Year of the Rat (庚子年) — use it as the anchor for the 12-year cycle
zodiac = ZODIAC_ANIMALS[(CURRENT_YEAR - 2020) % 12]


zodiac_zh, zodiac_en = zodiac.split(" ", 1)
st.markdown(
    f"""
    <div style="text-align:left;padding:0.25rem 0 0.75rem;">
      <div style="font-size:clamp(24px,7vw,40px);line-height:1.2;font-weight:800;
        white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">
        🧧 {CURRENT_YEAR} 新年红包
      </div>
      <div style="font-size:clamp(14px,4vw,20px);color:#d4af37;margin-top:2px;font-weight:600;">
        {zodiac_zh} · Year of the {zodiac_en}
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- UI ---
name = st.text_input("Enter name 请输入您的富贵名", value="YOU").strip()

st.write("")
if st.button("🧧 Shake to open 红包 (Red Packet)", use_container_width=True):

    tease_lines = [
        "Searching for your luck… 🍊 | 正在寻找你的好运… 🍊",
        "Checking your 贵人 index… 👀 | 正在检测贵人指数… 👀",
        "Loading 财神 Wi-Fi… 📶 | 正在连接财神 Wi-Fi… 📶",
        "Verifying 好运连连… ✅ | 正在验证好运连连… ✅",
        "Counting pineapple tarts… 🍍 | 正在数黄梨挞… 🍍",
        "Shaking 红包 vigorously… 🧧 | 正在用力摇红包… 🧧",
        "Confirming huat permissions… 💰 | 正在确认发权限… 💰",
        f"Scanning {CURRENT_YEAR} 好运频道… 📡 | 正在扫描 {CURRENT_YEAR} 好运频道… 📡",
        "Charging luck battery… 🔋 | 正在给好运充电… 🔋",
        "Sending ping to 财神… 📮 | 正在给财神发消息… 📮",
        "Rolling fortune dice… 🎲 | 正在掷运势骰子… 🎲",
        "Opening prosperity portal… 🚪✨ | 正在开启发财之门… 🚪✨",
        "Aligning fengshui… 🧭 | 正在校准风水… 🧭",
        "Loading 好运皮肤… 🎨 | 正在加载好运皮肤… 🎨",
        "Blessing packet… 🙏 | 正在加持红包… 🙏",
        "Finalizing 好运签名… 🖊️ | 正在签收好运… 🖊️",
        "Pulling up your 财运 chart… 📊 | 正在调取你的财运图… 📊",
        "Whispering to the 门神… 🚪 | 正在跟门神咬耳朵… 🚪",
        "Polishing your lucky coin… 🪙 | 正在擦亮你的幸运硬币… 🪙",
        "Untangling red string of fate… 🧵 | 正在解开姻缘红线… 🧵",
        "Warming up the lion dance… 🦁 | 正在热身舞狮… 🦁",
        "Refilling the tea pot… 🍵 | 正在续茶… 🍵",
        "Syncing with the lunar calendar… 🌙 | 正在同步农历… 🌙",
        "Adjusting your luck antenna… 📡 | 正在调整好运天线… 📡",
        "Double-checking huat levels… 🔍 | 正在复查发财指数… 🔍",
    ]
    with st.spinner(random.choice(tease_lines)):
        time.sleep(random.choice([0.9, 1.1, 1.2, 1.4]))

    safe_name = name[:18] if name else "YOU"

    amount_pool = (
        ["🧧"] * 10 +
        ["🧧🧧"] * 8 +
        ["🧧🧧🧧"] * 6 +
        ["🧧🧧🧧🧧"] * 4 +
        ["🧧🧧🧧🧧🧧"] * 2 +
        ["🧧🧧🧧🧧🧧🧧"] * 1
    )
    amount = random.choice(amount_pool)

    # --- Flourish layer: a rarity/intensity prefix that sometimes decorates the luck line ---
    # Stored as (zh, en) tuples so it can be composed cleanly with any luck phrase.
    flourishes = [
        ("超级", "Super"), ("巨型", "Mega"), ("涡轮", "Turbo"), ("豪华", "Deluxe"),
        ("尊享", "Premium"), ("VIP", "VIP"), ("传奇", "Legendary"), ("稀有", "Rare"),
        ("限量", "Limited-Edition"), ("独家", "Exclusive"), ("精英", "Elite"), ("超强", "Ultra"),
        ("究极", "Ultimate"), ("排位", "Ranked-Up"), ("提升", "Boosted"), ("增幅", "Amplified"),
        ("超稀有", "Ultra-Rare"), ("顶级", "Top-Tier"), ("满级", "Max-Level"), ("满满", "Overflowing"),
        ("双倍", "Double"), ("三倍", "Triple"), ("隐藏", "Hidden"), ("秘密", "Secret"),
        ("加成", "Bonus"), ("额外", "Extra"), ("至尊", "Supreme"), ("尊贵", "Prestige"),
        ("皇家", "Royal"), ("神级", "Godlike"), ("S级", "S-Tier"), ("爆率", "Jackpot-Grade"),
        ("宇宙级", "Cosmic"), ("星际", "Stellar"), ("黄金", "Golden"), ("钻石", "Diamond"),
        ("白金", "Platinum"), ("锦鲤", "Koi-Blessed"), ("财神认证", "Wealth-God-Certified"), ("天选", "Chosen-One"),
    ]

    # Luck pool stored as (zh, en) tuples so a flourish can be composed onto the front cleanly
    luck_pairs = [
        ("好运连连 ✨", "Good luck keeps coming ✨"),
        ("贵人护体 👑", "Helpful people support you 👑"),
        ("稳稳发财 💰", "Steady wealth growth 💰"),
        ("健康第一 🙏", "Health comes first 🙏"),
        ("烦恼清零 😌", "Stress reset to zero 😌"),
        ("事业开挂 🚀", "Career boost activated 🚀"),
        ("桃花人缘 🌸", "Great vibes and popularity 🌸"),
        ("客户自动来 🤝", "Clients come to you 🤝"),
        ("加薪有望 📈", "Raise potential rising 📈"),
        ("睡眠变好 😴", "Better sleep incoming 😴"),
        ("家宅平安 🏠", "Peace at home 🏠"),
        ("偏财小惊喜 🎁", "Small bonus surprises 🎁"),
        ("机会撞上门 🚪✨", "Opportunities knock 🚪✨"),
        ("小人退散 🧿", "Negativity blocked 🧿"),
        ("万事顺遂 🌈", "Everything goes smoothly 🌈"),
        ("出门就顺 🚗💨", "Smooth travels 🚗💨"),
        ("灵感暴增 💡", "Creativity spikes 💡"),
        ("效率爆表 ⚡", "Super productive mode ⚡"),
        ("贵人来电 📞👑", "Helper contacts you 📞👑"),
        ("财运上扬 📈💰", "Wealth trend rising 📈💰"),
        ("好消息连发 📨", "Good news incoming 📨"),
        ("心情超稳 😌", "Calm and steady mind 😌"),
        ("状态拉满 🔥", "Peak energy 🔥"),
        ("小确幸不断 🍀", "Many small wins 🍀"),
        ("学业进步 📚", "Studies improve steadily 📚"),
        ("旅途平安 🧳", "Safe and smooth travels 🧳"),
        ("存款上涨 💵", "Savings grow nicely 💵"),
        ("债务清零 🧾", "Debts clear away 🧾"),
        ("升职加薪 🎖️", "Promotion and raise 🎖️"),
        ("考试顺利 📖", "Exams go smoothly 📖"),
        ("创业顺利 🏗️", "New ventures take off 🏗️"),
        ("人脉扩展 🌐", "Your network expands 🌐"),
        ("团队和睦 🤗", "Harmony in the team 🤗"),
        ("婚姻美满 💍", "Marriage stays sweet 💍"),
        ("家人懂事 👨‍👩‍👧", "Family stays close-knit 👨‍👩‍👧"),
        ("父母健康 🧓", "Parents stay healthy 🧓"),
        ("老友相聚 🍻", "Old friends reunite 🍻"),
        ("心态年轻 🌱", "A youthful mindset 🌱"),
        ("作息规律 🌙", "Better sleep routine 🌙"),
        ("状态回升 🔋", "Energy bounces back 🔋"),
        ("贵人相助 🧑‍🤝‍🧑", "A helper appears just in time 🧑‍🤝‍🧑"),
        ("好评不断 ⭐", "Great reviews keep coming ⭐"),
        ("谈判顺利 🤝", "Negotiations go your way 🤝"),
        ("项目落地 📦", "Projects land successfully 📦"),
        ("心愿成真 🌠", "Wishes come true 🌠"),
        ("出行顺畅 🚦", "Smooth commutes ahead 🚦"),
        ("抽奖手气好 🎰", "Great luck in lucky draws 🎰"),
        ("人缘极佳 🌟", "People are drawn to you 🌟"),
        ("好点子不断 💭", "Good ideas keep flowing 💭"),
        ("平安喜乐 🕊️", "Peace and quiet joy 🕊️"),
    ]

    luck_zh, luck_en = random.choice(luck_pairs)
    if random.random() < 0.6:
        flourish_zh, flourish_en = random.choice(flourishes)
        luck_zh = f"{flourish_zh}{luck_zh}"
        luck_en = f"{flourish_en} {luck_en}"
    luck = f"{luck_zh} | {luck_en}"

    persona = random.choice([
        "低调爆发型 🚀 | Low-key but will break through 🚀",
        "稳中带旺型 😌📈 | Steady growth and good momentum 😌📈",
        "少drama多贵人 👑 | Less drama, more helpers 👑",
        "先苦后甜 🍊 | Hard first, sweet later 🍊",
        "躺赢但要努力 😆 | Lucky but still need effort 😆",
        "越忙越旺 💼✨ | The busier, the luckier 💼✨",
        "边玩边赚钱 🕺💰 | Have fun, still earn 🕺💰",
        "主打一个顺 🌈 | Main theme: smooth 🌈",
        "反弹回血 💪 | Bounce back stronger 💪",
        "好运磁铁 🧲✨ | Luck magnet 🧲✨",
        "社交开花 🌸🤝 | Social blossom 🌸🤝",
        "灵感爆棚 💡 | Ideas overflow 💡",
        "稳准狠 🎯 | Calm, accurate, decisive 🎯",
        "贵人雷达开 ✅ | Helper radar on ✅",
        "越做越顺 🧠 | Smoother as you go 🧠",
        "默默发财型 💰 | Quietly getting richer 💰",
        "好运开局型 🎉 | Strong start energy 🎉",
        "逢凶化吉型 🧿 | Turns bad to good 🧿",
        "稳中求进型 📊 | Steady and always improving 📊",
        "逆风翻盘型 🔄 | Turns things around against the odds 🔄",
        "细水长流型 💧 | Slow and steady wins it 💧",
        "团队担当型 🛡️ | The reliable one on the team 🛡️",
        "幕后军师型 🧠 | The quiet strategist behind the scenes 🧠",
        "行动派 🏃 | Gets things done fast 🏃",
        "佛系但幸运 🍃 | Chill vibes, lucky outcomes 🍃",
        "稳扎稳打型 🧱 | Builds success brick by brick 🧱",
        "转运锦鲤型 🐟 | The lucky charm of the group 🐟",
        "越挫越勇型 💥 | Gets stronger after setbacks 💥",
        "人气担当型 🎤 | The crowd favourite 🎤",
        "低调实力派 🎯 | Quiet but genuinely skilled 🎯",
        "机会捕手型 🎣 | Always catches the right opportunity 🎣",
        "温柔但坚定型 🌷 | Gentle but unshakeable 🌷",
        "直觉超准型 🔮 | Instincts are almost always right 🔮",
        "万事包容型 🌊 | Goes with the flow, handles anything 🌊",
        "财运锁定型 🔒 | Wealth locked in for the year 🔒",
        "好奇心爆棚型 🔭 | Endless curiosity fuels growth 🔭",
        "关键先生/女士型 🔑 | The one who makes the difference 🔑",
        "幸运附体型 🍀 | Luck seems to follow everywhere 🍀",
        "稳赢心态型 🧘‍♂️ | Calm confidence, steady wins 🧘‍♂️",
        "高能量型 ⚡ | Runs on high energy all year ⚡",
        "贵人体质型 🧲 | Naturally attracts helpful people 🧲",
        "说到做到型 ✅ | Follows through on every promise ✅",
        "逆袭黑马型 🐎 | The dark horse everyone underestimated 🐎",
        "天生乐观型 ☀️ | Naturally optimistic outlook ☀️",
        "幸福感爆表型 💛 | Overflowing with contentment 💛",
    ])

    keyword = random.choice([
        "稳 (Steady)", "冲 (Go for it)", "顺 (Smooth)", "旺 (Prosper)",
        "新 (New)", "强 (Strong)", "爽 (Good vibes)", "发 (Wealth)",
        "成 (Achieve)", "开 (Open)", "聚 (Gather)", "进 (Advance)", "喜 (Joy)",
        "福 (Blessing)", "乐 (Happiness)", "安 (Peace)", "升 (Rise)",
        "赢 (Win)", "富 (Rich)", "合 (Harmony)", "光 (Bright)",
        "敢 (Bold)", "准 (Accurate)", "稳赢 (Steady win)",
        "稳健 (Stable)", "蜕变 (Transform)", "突破 (Breakthrough)", "沉淀 (Settle)",
        "蓄力 (Recharge)", "拓展 (Expand)", "精进 (Refine)", "圆满 (Fulfilled)",
        "升级 (Upgrade)", "从容 (Composed)", "果断 (Decisive)", "焕新 (Renew)",
        "深耕 (Cultivate)", "突围 (Breakout)", "稳步 (Steady Pace)", "蓄势 (Poised)",
        "通达 (Open-Minded)", "惊喜 (Surprise)", "珍惜 (Cherish)", "感恩 (Grateful)",
        "自在 (At Ease)", "拼搏 (Strive)", "蓬勃 (Thriving)", "澄澈 (Clear-Minded)",
        "圆梦 (Dream Fulfilled)", "长红 (Ever-Thriving)",
    ])

    fortune_score = random.randint(68, 99)
    if random.random() < 0.06:
        fortune_score = 100

    bonus = random.choice([
        "Bonus: 🍍 Pineapple Tart Buff +10 | 加成：🍍 黄梨挞 Buff +10",
        "Bonus: 🧧 财神点赞 +1 | 加成：🧧 财神点赞 +1",
        "Bonus: ☕ Kopi treat from 贵人 | 加成：☕ 贵人请你喝 kopi",
        "Bonus: 🎉 Small surprise drop | 加成：🎉 小惊喜掉落",
        "Bonus: 🧿 Anti-bad-vibes shield | 加成：🧿 防小人护盾已开启",
        "Bonus: 🧠 Creativity +20 | 加成：🧠 灵感 +20",
        "Bonus: 💪 Energy +15 | 加成：💪 体力 +15",
        "Bonus: 📈 Wealth trend up | 加成：📈 财运上扬",
        "Bonus: 🧲 贵人吸引力+10 | 加成：🧲 Helper magnet +10",
        "Bonus: 🏆 好运连胜 Buff | 加成：🏆 Win streak buff",
        "Bonus: 🧘 心态稳定+10 | 加成：🧘 Calm mind +10",
        "Bonus: ⚡ 执行力+10 | 加成：⚡ Execution +10",
        "Bonus: 🎯 精准直觉 +10 | 加成：🎯 Sharp instincts +10",
        "Bonus: 🧳 旅行顺利 buff | 加成：🧳 Smooth-travel buff",
        "Bonus: 📚 学习力+15 | 加成：📚 Study power +15",
        "Bonus: 💌 好消息预告 | 加成：💌 Good-news preview",
        "Bonus: 🛡️ 防疲惫护盾 | 加成：🛡️ Anti-fatigue shield",
        "Bonus: 🌙 好梦连连 | 加成：🌙 Sweet dreams streak",
        "Bonus: 🎁 神秘礼物预定 | 加成：🎁 Mystery gift reserved",
        "Bonus: 🧊 冷静buff | 加成：🧊 Cool-headed buff",
        "Bonus: 🔑 机会钥匙 | 加成：🔑 Opportunity key unlocked",
        "Bonus: 🐟 锦鲤附体 | 加成：🐟 Koi spirit attached",
        "Bonus: 🎈 心情+20 | 加成：🎈 Mood +20",
        "Bonus: 🧩 灵活应变+10 | 加成：🧩 Adaptability +10",
        "Bonus: 🌻 正能量+15 | 加成：🌻 Positivity +15",
        "Bonus: 🥮 团圆加成 | 加成：🥮 Reunion bonus",
        "Bonus: 🧧 双份红包气场 | 加成：🧧 Double red-packet aura",
        "Bonus: 🚀 效率+20 | 加成：🚀 Efficiency +20",
        "Bonus: 🎇 惊喜连击 | 加成：🎇 Surprise combo",
        "Bonus: 🧘 内心平静+10 | 加成：🧘 Inner calm +10",
        "Bonus: 🌈 好运彩虹 | 加成：🌈 Rainbow of luck",
        "Bonus: 🦋 蜕变 buff | 加成：🦋 Transformation buff",
        "Bonus: 🕯️ 心愿加持 | 加成：🕯️ Wish-blessing applied",
        "Bonus: 📈 人气+10 | 加成：📈 Popularity +10",
        "Bonus: 🍵 静心茶 buff | 加成：🍵 Calming-tea buff",
        "Bonus: 🧨 好运炸开 | 加成：🧨 Luck burst",
        "Bonus: 🪙 偏财运+10 | 加成：🪙 Extra windfall +10",
        "Bonus: 🌤️ 心情晴朗 | 加成：🌤️ Bright mood",
        "Bonus: 🎊 全场最佳 buff | 加成：🎊 MVP-of-the-day buff",
        "Bonus: 🧿 护身符启动 | 加成：🧿 Amulet activated",
    ])
    show_bonus = random.random() < 0.55

    is_jackpot = random.random() < 0.01

    st.success("Opened! 🎉 | 开启成功！🎉")

    # --- Tiered gold coin burst: same effect family, scaled by rarity ---
    if is_jackpot:
        tier = "jackpot"
    elif fortune_score >= 90:
        tier = "high"
    else:
        tier = "normal"

    burst_config = {
        "normal": {
            "burst_count": 12, "burst_spread": 90, "burst_duration": 800,
            "rain_count": 18, "rain_duration": 1400,
            "particles": ["🪙"],
        },
        "high": {
            "burst_count": 20, "burst_spread": 120, "burst_duration": 1000,
            "rain_count": 34, "rain_duration": 1800,
            "particles": ["🪙", "✨"],
        },
        "jackpot": {
            "burst_count": 30, "burst_spread": 170, "burst_duration": 1200,
            "rain_count": 60, "rain_duration": 2400,
            "particles": ["🪙", "✨", "🐉"],
        },
    }
    burst = burst_config[tier]

    share_text = (
        f"🧧 {CURRENT_YEAR} 新年红包 · {zodiac} | New Year Red Packet {CURRENT_YEAR} 🧧\n\n"
        f"To / 收件人: {safe_name}\n"
        f"Amount / 红包量: {amount}\n"
        f"Luck / 运势: {luck}\n"
        f"Persona / 角色: {persona}\n"
        f"Keyword / 关键词: {keyword}\n"
        f"Fortune Meter / 好运指数: {fortune_score}/100\n\n"
        f"{bonus if show_bonus else ''}\n\n"
        "马上HUAT财 😄😄😄😄😄\n"
    )

    wa_text = urllib.parse.quote(share_text)
    mail_subject = urllib.parse.quote(f"🧧 {CURRENT_YEAR} New Year Red Packet | 新年红包")
    mail_body = urllib.parse.quote(share_text)

    # Escape all variables before injecting into HTML
    safe_name_html  = html.escape(safe_name)
    amount_html     = html.escape(amount)
    luck_html       = html.escape(luck)
    persona_html    = html.escape(persona)
    keyword_html    = html.escape(keyword)
    bonus_line      = bonus if show_bonus else "Bonus: ✨ Hidden this round | 加成：✨ 本轮隐藏"
    bonus_line_html = html.escape(bonus_line)

    jackpot_banner = ""
    if is_jackpot:
        jackpot_banner = (
            '<div style="background:rgba(255,215,0,0.20);border:1px solid rgba(255,215,0,0.65);'
            'padding:8px 10px;border-radius:12px;font-weight:900;margin-bottom:10px;">'
            '🐉 JACKPOT! 龙运爆发 • Legendary Luck!'
            '</div>'
        )

    jackpot_style = (
        '<style>@keyframes jackpotPulse {'
        '0%,100% { box-shadow: 0 10px 22px rgba(0,0,0,0.18), 0 0 0px rgba(255,215,0,0.0); }'
        '50% { box-shadow: 0 10px 22px rgba(0,0,0,0.18), 0 0 24px rgba(255,215,0,0.85); }'
        '}</style>'
    ) if is_jackpot else ""

    card_html = (
        jackpot_style +
        '<div id="rp-card" style="background:linear-gradient(135deg,#7a0000 0%,#d00000 45%,#860000 100%);'
        'border:2px solid rgba(255,215,0,0.75);border-radius:18px;padding:18px 18px 14px 18px;'
        'color:#fff;position:relative;overflow:visible;box-shadow:0 10px 22px rgba(0,0,0,0.18);'
        'width:100%;max-width:820px;box-sizing:border-box;'
        + ('animation:jackpotPulse 1.4s ease-in-out 3;' if is_jackpot else '') +
        '">'

        '<div style="position:absolute;right:-18px;top:-18px;font-size:130px;opacity:0.10;'
        'color:rgba(255,215,0,0.95);transform:rotate(10deg);font-weight:900;pointer-events:none;">福</div>'

        '<div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">'
        '<div style="font-size:26px;">🧧</div>'
        f'<div style="font-size:22px;font-weight:900;">{CURRENT_YEAR} 新年红包 · {zodiac} <span style="opacity:0.85;">•</span> New Year Red Packet</div>'
        '</div>'

        + jackpot_banner +

        '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;font-size:16px;line-height:1.35;">'
        f'<div><b>To / 收件人:</b><br>{safe_name_html}</div>'
        f'<div><b>Amount / 红包量:</b><br>{amount_html}</div>'
        f'<div style="grid-column:1/span 2"><b>Luck / 运势:</b><br>{luck_html}</div>'
        f'<div style="grid-column:1/span 2"><b>Persona / 角色:</b><br>{persona_html}</div>'
        f'<div><b>Keyword / 关键词:</b><br>{keyword_html}</div>'
        f'<div><b>Fortune / 好运指数:</b><br>{fortune_score}/100</div>'
        '</div>'

        '<div style="margin-top:12px;">'
        '<div style="height:10px;background:rgba(255,255,255,0.20);border-radius:999px;overflow:hidden;">'
        f'<div style="width:{fortune_score}%;height:100%;'
        'background:linear-gradient(90deg,rgba(255,215,0,0.95),rgba(255,255,255,0.85));'
        'border-radius:999px;"></div>'
        '</div>'
        f'<div style="margin-top:10px;font-size:14px;opacity:0.95;">{bonus_line_html}</div>'
        '</div>'

        '</div>'
    )

    particles_js = str(burst["particles"]).replace("'", '"')
    stage_height = {"normal": 760, "high": 820, "jackpot": 900}[tier]
    rain_fall_y = min(stage_height - 140, 600)

    animated_html = f"""
    <html><head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>html,body{{margin:0;background:transparent;overflow:visible;}}</style></head>
    <body>
    <div id="rp-stage" style="position:relative;width:100%;max-width:820px;margin:0 auto;overflow:visible;box-sizing:border-box;padding-bottom:20px;">
        {card_html}
        <div style="display:flex;justify-content:center;margin-top:16px;gap:10px;align-items:center;flex-wrap:wrap;">
          <button id="dl-btn" style="background:#111;color:#fff;border:none;padding:10px 18px;
            border-radius:10px;font-weight:600;font-size:14px;cursor:pointer;">Download image / 下载图片</button>
          <span id="dl-status" style="font-size:12px;color:#888;"></span>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script>
    (function() {{
        const stage = document.getElementById('rp-stage');
        const particles = {particles_js};

        function makeParticle() {{
            const p = document.createElement('div');
            p.textContent = particles[Math.floor(Math.random() * particles.length)];
            p.style.position = 'absolute';
            p.style.fontSize = (14 + Math.random() * 14) + 'px';
            p.style.opacity = '1';
            p.style.zIndex = '10';
            p.style.pointerEvents = 'none';
            return p;
        }}

        // Phase 1: quick radial burst from the card center
        const burstCount = {burst['burst_count']};
        const burstSpread = {burst['burst_spread']};
        const burstDuration = {burst['burst_duration']};
        for (let i = 0; i < burstCount; i++) {{
            const p = makeParticle();
            p.style.left = '50%';
            p.style.top = '30%';
            p.style.transition = `transform ${{burstDuration}}ms cubic-bezier(.15,.7,.3,1), opacity ${{burstDuration}}ms ease-out`;
            p.style.transform = 'translate(-50%,-50%)';
            stage.appendChild(p);
            const angle = Math.random() * Math.PI * 2;
            const dist = burstSpread * (0.6 + Math.random() * 0.6);
            const dx = Math.cos(angle) * dist;
            const dy = Math.sin(angle) * dist * 0.6 + burstSpread * 0.4;
            requestAnimationFrame(() => {{
                p.style.transform = `translate(calc(-50% + ${{dx}}px), calc(-50% + ${{dy}}px)) rotate(${{Math.random() * 360}}deg)`;
                p.style.opacity = '0';
            }});
            setTimeout(() => p.remove(), burstDuration + 50);
        }}

        // Phase 2: a fuller shower of coins raining down across the card width, staggered over time
        const rainCount = {burst['rain_count']};
        const rainDuration = {burst['rain_duration']};
        const rainFallY = {rain_fall_y};
        for (let i = 0; i < rainCount; i++) {{
            const delay = Math.random() * rainDuration * 0.7;
            setTimeout(() => {{
                const p = makeParticle();
                const startX = 5 + Math.random() * 90;
                const fallDuration = rainDuration * (0.5 + Math.random() * 0.5);
                p.style.left = startX + '%';
                p.style.top = '-24px';
                p.style.transition = `top ${{fallDuration}}ms linear, opacity ${{fallDuration}}ms ease-in, transform ${{fallDuration}}ms linear`;
                p.style.transform = 'rotate(0deg)';
                stage.appendChild(p);
                requestAnimationFrame(() => {{
                    p.style.top = rainFallY + 'px';
                    p.style.transform = `rotate(${{(Math.random() * 480) - 240}}deg) translateX(${{(Math.random() * 40) - 20}}px)`;
                    p.style.opacity = '0.15';
                }});
                setTimeout(() => p.remove(), fallDuration + 60);
            }}, delay);
        }}

        document.getElementById('dl-btn').addEventListener('click', function() {{
            const status = document.getElementById('dl-status');
            status.textContent = 'Rendering...';
            html2canvas(document.getElementById('rp-card'), {{scale: 2, backgroundColor: null}}).then(function(canvas) {{
                const link = document.createElement('a');
                link.download = 'red-packet-{CURRENT_YEAR}.png';
                link.href = canvas.toDataURL('image/png');
                link.click();
                status.textContent = 'Downloaded';
            }}).catch(function(err) {{
                status.textContent = 'Could not render image';
            }});
        }});
    }})();
    </script>
    </body></html>
    """

    components.html(animated_html, height=stage_height, scrolling=False)
    st.write("")

    colA, colB = st.columns(2)
    with colA:
        st.markdown(
            f'<a href="https://wa.me/?text={wa_text}" target="_blank" style="text-decoration:none;">'
            '<div style="background:#25D366;color:white;padding:12px 14px;border-radius:12px;'
            'text-align:center;font-weight:900;">📱 Share on WhatsApp</div></a>',
            unsafe_allow_html=True
        )
    with colB:
        st.markdown(
            f'<a href="mailto:?subject={mail_subject}&body={mail_body}" target="_blank" style="text-decoration:none;">'
            '<div style="background:#111;color:white;padding:12px 14px;border-radius:12px;'
            'text-align:center;font-weight:900;">✉️ Share via Email</div></a>',
            unsafe_allow_html=True
        )

    with st.expander("Plain text (copy manually) / 纯文字（手动复制）"):
        st.text(share_text)

    closing = random.choice([
        "恭喜发财，万事如意! | Gong Xi Fa Cai, all the best!",
        "新年快乐，平安顺遂! | Happy New Year, peace & smooth days!",
        "身体健康，笑口常开! | Good health and lots of smiles!",
        "福气满满，天天好运! | Blessings & daily luck!",
        "心想事成，事事顺心! | May wishes come true!",
        "财运滚滚来! | Wealth rolling in!",
        "好运开局，全年旺! | Strong start, prosperous year!",
        "少烦恼，多开心! | Less stress, more joy!",
        "贵人多多，机会多多! | More helpers, more opportunities!",
        "开工大吉! | Great start to work!",
        "岁岁平安，年年有余! | Peace every year, abundance every year!",
        "心想事成，步步高升! | May wishes come true, step by step higher!",
        "龙马精神，活力满满! | Vigorous spirit, full of energy!",
        "招财进宝，年年好运! | Wealth and treasures, year after year!",
        "喜气洋洋，好运常在! | Joyful spirits, luck that stays!",
        "万事顺意，心想事成! | Everything goes your way!",
        "财源广进，步步高! | Wealth flows in, rising step by step!",
        "阖家欢乐，幸福美满! | Family joy and happiness!",
        "生意兴隆，通四海! | Business thrives far and wide!",
        "好运连连，笑口常开! | Good luck keeps coming, keep smiling!",
    ])
    st.caption(closing)

# --- Optional tip jar footer (always visible, low-key, purely voluntary) ---
st.write("")
st.divider()
tip_col1, tip_col2 = st.columns([3, 1])
with tip_col1:
    st.caption(
        "Enjoyed this? Support is always optional — thanks for playing! 🙏 | "
        "觉得好玩的话，欢迎随意支持一下（纯自愿）🙏"
    )
with tip_col2:
    if os.path.exists(TIP_QR_IMAGE_PATH):
        st.image(TIP_QR_IMAGE_PATH, width=110, caption="Scan to PayNow")
    elif TIP_LINK:
        st.markdown(
            f'<a href="{TIP_LINK}" target="_blank" style="text-decoration:none;">'
            '<div style="background:#7a0000;color:white;padding:8px 12px;border-radius:10px;'
            'text-align:center;font-size:13px;font-weight:700;">☕ Tip</div></a>',
            unsafe_allow_html=True
        )

