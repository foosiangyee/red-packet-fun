import streamlit as st
import time
import random

st.set_page_config(page_title="🧧 Red Packet Fun", page_icon="🧧")

st.title("🧧 新年红包 • New Year Red Packet")

# --- UI ---
name = st.text_input("Enter name 请输入您的富贵名", value="YOU").strip()

st.write("")
if st.button("🧧 Shake to open 红包 | Shake to open red packet", use_container_width=True):

    # suspense lines (bilingual)
    tease_lines = [
        "Searching for your luck… 🍊 | 正在寻找你的好运… 🍊",
        "Checking your 贵人 index… 👀 | 正在检测贵人指数… 👀",
        "Loading 财神 Wi-Fi… 📶 | 正在连接财神 Wi-Fi… 📶",
        "Verifying 好运连连… ✅ | 正在验证好运连连… ✅",
        "Counting pineapple tarts… 🍍 | 正在数黄梨挞… 🍍",
        "Shaking 红包 vigorously… 🧧🫨 | 正在用力摇红包… 🧧🫨",
        "Confirming ‘huat’ permissions… 💰 | 正在确认“发”权限… 💰",
        "Scanning 2026 好运频道… 📡 | 正在扫描 2026 好运频道… 📡",
    ]
    with st.spinner(random.choice(tease_lines)):
        time.sleep(random.choice([0.9, 1.1, 1.2, 1.4]))

    # --- outcomes ---
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

    luck = random.choice([
        "好运连连 ✨ | Good luck keeps coming ✨",
        "贵人护体 👑 | Helpful people support you 👑",
        "稳稳发财 💰 | Steady wealth growth 💰",
        "健康第一 🙏 | Health comes first 🙏",
        "烦恼清零 😌 | Stress reset to zero 😌",
        "事业开挂 🚀 | Career boost activated 🚀",
        "桃花人缘 🌸 | Great vibes & popularity 🌸",
        "客户自动来 🤝 | Clients come to you 🤝",
        "加薪有望 📈 | Raise potential rising 📈",
        "睡眠变好 😴 | Better sleep incoming 😴",
        "家宅平安 🏠 | Peace at home 🏠",
        "偏财小惊喜 🎁 | Small bonus surprises 🎁",
        "机会撞上门 🚪✨ | Opportunities knock 🚪✨",
        "小人退散 🧿 | Negativity blocked 🧿",
        "万事顺遂 🌈 | Everything goes smoothly 🌈",
        "出门就顺 🚗💨 | Smooth travels 🚗💨",
    ])

    keyword = random.choice([
        "稳 (Steady)", "冲 (Go for it)", "顺 (Smooth)", "旺 (Prosper)",
        "新 (New)", "强 (Strong)", "爽 (Good vibes)", "发 (Wealth)",
        "成 (Achieve)", "开 (Open)", "聚 (Gather)", "进 (Advance)", "喜 (Joy)"
    ])

    persona = random.choice([
        "低调爆发型 🚀 | Low-key but will break through 🚀",
        "稳中带旺型 😌📈 | Steady growth & good momentum 😌📈",
        "少drama多贵人 👑 | Less drama, more helpers 👑",
        "先苦后甜 🍊 | Hard first, sweet later 🍊",
        "躺赢但要努力 😆 | Lucky… but still need effort 😆",
        "越忙越旺 💼✨ | The busier, the luckier 💼✨",
        "边玩边赚钱 🕺💰 | Have fun, still earn 🕺💰",
        "主打一个顺 🌈 | Main theme: smooth 🌈",
        "反弹回血 💪 | Bounce back stronger 💪",
        "好运磁铁 🧲✨ | Luck magnet 🧲✨",
        "社交开花 🌸🤝 | Social blossom 🌸🤝",
        "灵感爆棚 💡 | Ideas overflow 💡",
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
    ])
    show_bonus = random.random() < 0.55

    st.success("Opened! 🎉 | 开启成功！🎉")

    msg = f"""🧧 新年红包 | New Year Red Packet 🧧

To / 收件人: {safe_name}
Amount / 红包量: {amount}
Luck / 运势: {luck}
Persona / 角色: {persona}
Keyword / 关键词: {keyword}
Fortune Meter / 好运指数: {fortune_score}/100

{bonus if show_bonus else ""}

马上Huat财 😄😄😄😄😄
"""

    # Clean up extra blank lines if no bonus
    if not show_bonus:
        msg = "\n".join([line for line in msg.splitlines() if "Bonus" not in line and "加成" not in line and line.strip() != ""])

    st.code(msg, language="text")
