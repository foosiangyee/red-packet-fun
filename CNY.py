import streamlit as st
import time
import random

st.set_page_config(page_title="🧧 Red Packet Fun", page_icon="🧧")

st.title("🧧 新年红包 • Shake & Reveal")

# --- UI ---
name = st.text_input("Enter name 请输入您的富贵名", value="YOU").strip()

st.write("")
if st.button("🧧 Shake to open 红包", use_container_width=True):

    # suspense lines (more variety)
    tease_lines = [
        "Searching for your luck… 🍊",
        "Checking your 贵人 index… 👀",
        "Loading 财神 Wi-Fi… 📶",
        "Verifying 好运连连… ✅",
        "Counting pineapple tarts… 🍍",
        "Shaking 红包 vigorously… 🧧🫨",
        "Confirming ‘huat’ permissions… 💰",
        "Scanning 2026 好运频道… 📡",
    ]
    with st.spinner(random.choice(tease_lines)):
        time.sleep(random.choice([0.9, 1.1, 1.2, 1.4]))

    # --- outcomes (expanded) ---
    safe_name = name[:18] if name else "YOU"

    # add some variety to amounts (including “jackpot” rare ones)
    amount_pool = (
        ["🧧"] * 10 +
        ["🧧🧧"] * 8 +
        ["🧧🧧🧧"] * 6 +
        ["🧧🧧🧧🧧"] * 4 +
        ["🧧🧧🧧🧧🧧"] * 2 +
        ["🧧🧧🧧🧧🧧🧧"] * 1
    )
    amount = random.choice(amount_pool)

    luck = random.choice([
        "好运连连 ✨",
        "贵人护体 👑",
        "稳稳发财 💰",
        "健康第一 🙏",
        "烦恼清零 😌",
        "事业开挂 🚀",
        "桃花人缘 🌸",
        "客户自动来 🤝",
        "加薪有望 📈",
        "睡眠变好 😴",
        "家宅平安 🏠",
        "偏财小惊喜 🎁",
        "机会自己撞上门 🚪✨",
        "小人退散 🧿",
        "万事顺遂 🌈",
        "出门就顺 🚗💨",
    ])

    keyword = random.choice([
        "稳", "冲", "顺", "旺", "新", "强", "爽", "发", "成", "开", "聚", "进", "喜"
    ])

    persona = random.choice([
        "低调但会爆发型 🚀",
        "稳中带旺型 😌📈",
        "少 drama，多贵人型 👑",
        "先苦后甜型 🍊",
        "躺赢但要努力型 😆",
        "越忙越旺型 💼✨",
        "边玩边赚钱型 🕺💰",
        "主打一个顺型 🌈",
        "反弹回血型 💪",
        "好运磁铁型 🧲✨",
        "社交开花型 🌸🤝",
        "灵感爆棚型 💡",
    ])

    # Fun meter (makes it feel like a mini game)
    fortune_score = random.randint(68, 99)
    # Rare “100” for extra fun
    if random.random() < 0.06:
        fortune_score = 100

    # Bonus line: appears sometimes to create surprise
    bonus = random.choice([
        "Bonus: 🍍 Pineapple Tart Buff +10",
        "Bonus: 🧧 财神点赞 +1",
        "Bonus: ☕ 贵人请你喝 kopi",
        "Bonus: 🎉 小惊喜掉落",
        "Bonus: 🧿 防小人护盾已开启",
        "Bonus: 🧠 灵感 +20",
        "Bonus: 💪 体力 +15",
        "Bonus: 📈 财运上扬",
    ])
    show_bonus = random.random() < 0.55  # 55% chance

    st.success("Opened! 🎉")

    msg = f"""🧧 新年红包 🧧

To: {safe_name}
Amount: {amount}
Luck: {luck}
Persona: {persona}
2026关键词: {keyword}
Fortune Meter: {fortune_score}/100

{bonus if show_bonus else ""}

（Huat Kueh Friendly 😄）"""

    # clean up extra blank lines when no bonus
    msg = "\n".join([line for line in msg.splitlines() if line.strip() != "" or "Bonus" in msg])

    st.code(msg, language="text")
