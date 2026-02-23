import streamlit as st
import time
import random
import urllib.parse
import html

st.set_page_config(page_title="🧧 Red Packet Fun", page_icon="🧧")

st.title("🧧 新年红包 🧧")

# --- UI ---
name = st.text_input("Enter name 请输入您的富贵名", value="YOU").strip()

st.write("")
if st.button("🧧 Click to open 红包 (Red Packet) 🧧", use_container_width=True):

    tease_lines = [
        "Searching for your luck… 🍊 | 正在寻找你的好运… 🍊",
        "Checking your 贵人 index… 👀 | 正在检测贵人指数… 👀",
        "Loading 财神 Wi-Fi… 📶 | 正在连接财神 Wi-Fi… 📶",
        "Verifying 好运连连… ✅ | 正在验证好运连连… ✅",
        "Counting pineapple tarts… 🍍 | 正在数黄梨挞… 🍍",
        "Shaking 红包 vigorously… 🧧 | 正在用力摇红包… 🧧",
        "Confirming huat permissions… 💰 | 正在确认发权限… 💰",
        "Scanning 2026 好运频道… 📡 | 正在扫描 2026 好运频道… 📡",
        "Charging luck battery… 🔋 | 正在给好运充电… 🔋",
        "Sending ping to 财神… 📮 | 正在给财神发消息… 📮",
        "Rolling fortune dice… 🎲 | 正在掷运势骰子… 🎲",
        "Opening prosperity portal… 🚪✨ | 正在开启发财之门… 🚪✨",
        "Aligning fengshui… 🧭 | 正在校准风水… 🧭",
        "Loading 好运皮肤… 🎨 | 正在加载好运皮肤… 🎨",
        "Blessing packet… 🙏 | 正在加持红包… 🙏",
        "Finalizing 好运签名… 🖊️ | 正在签收好运… 🖊️",
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

    luck = random.choice([
        "好运连连 ✨ | Good luck keeps coming ✨",
        "贵人护体 👑 | Helpful people support you 👑",
        "稳稳发财 💰 | Steady wealth growth 💰",
        "健康第一 🙏 | Health comes first 🙏",
        "烦恼清零 😌 | Stress reset to zero 😌",
        "事业开挂 🚀 | Career boost activated 🚀",
        "桃花人缘 🌸 | Great vibes and popularity 🌸",
        "客户自动来 🤝 | Clients come to you 🤝",
        "加薪有望 📈 | Raise potential rising 📈",
        "睡眠变好 😴 | Better sleep incoming 😴",
        "家宅平安 🏠 | Peace at home 🏠",
        "偏财小惊喜 🎁 | Small bonus surprises 🎁",
        "机会撞上门 🚪✨ | Opportunities knock 🚪✨",
        "小人退散 🧿 | Negativity blocked 🧿",
        "万事顺遂 🌈 | Everything goes smoothly 🌈",
        "出门就顺 🚗💨 | Smooth travels 🚗💨",
        "灵感暴增 💡 | Creativity spikes 💡",
        "效率爆表 ⚡ | Super productive mode ⚡",
        "贵人来电 📞👑 | Helper contacts you 📞👑",
        "财运上扬 📈💰 | Wealth trend rising 📈💰",
        "好消息连发 📨 | Good news incoming 📨",
        "心情超稳 😌 | Calm and steady mind 😌",
        "状态拉满 🔥 | Peak energy 🔥",
        "小确幸不断 🍀 | Many small wins 🍀",
    ])

    keyword = random.choice([
        "稳 (Steady)", "冲 (Go for it)", "顺 (Smooth)", "旺 (Prosper)",
        "新 (New)", "强 (Strong)", "爽 (Good vibes)", "发 (Wealth)",
        "成 (Achieve)", "开 (Open)", "聚 (Gather)", "进 (Advance)", "喜 (Joy)",
        "福 (Blessing)", "乐 (Happiness)", "安 (Peace)", "升 (Rise)",
        "赢 (Win)", "富 (Rich)", "合 (Harmony)", "光 (Bright)",
        "敢 (Bold)", "准 (Accurate)", "稳赢 (Steady win)",
    ])

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
    ])
    show_bonus = random.random() < 0.55

    is_jackpot = random.random() < 0.01

    st.success("Opened! 🎉 | 开启成功！🎉")
    st.balloons()

    share_text = (
        "🧧 新年红包 | New Year Red Packet 🧧\n\n"
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
    mail_subject = urllib.parse.quote("🧧 New Year Red Packet | 新年红包")
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

    card_html = (
        '<div style="background:linear-gradient(135deg,#7a0000 0%,#d00000 45%,#860000 100%);'
        'border:2px solid rgba(255,215,0,0.75);border-radius:18px;padding:18px 18px 14px 18px;'
        'color:#fff;position:relative;overflow:hidden;box-shadow:0 10px 22px rgba(0,0,0,0.18);max-width:820px;">'

        '<div style="position:absolute;right:-18px;top:-18px;font-size:130px;opacity:0.10;'
        'color:rgba(255,215,0,0.95);transform:rotate(10deg);font-weight:900;pointer-events:none;">福</div>'

        '<div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">'
        '<div style="font-size:26px;">🧧</div>'
        '<div style="font-size:22px;font-weight:900;">新年红包 <span style="opacity:0.85;">•</span> New Year Red Packet</div>'
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

        '<div style="margin-top:14px;font-size:13px;opacity:0.95;">Copy &amp; share • 复制分享 😄</div>'
        '</div>'
    )

    st.markdown(card_html, unsafe_allow_html=True)
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
    ])

    st.caption(closing)
