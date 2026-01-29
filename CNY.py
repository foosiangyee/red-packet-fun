import streamlit as st
import time
import random
import unicodedata

st.set_page_config(page_title="🧧 Red Packet Fun", page_icon="🧧")

st.title("🧧 新年红包 • Shake & Reveal")
##st.caption("Fun, fast, and WhatsApp-friendly 😄")

# --- Helpers to reduce "out of line" issues for ASCII boxes ---
def display_width(s: str) -> int:
    """
    Approx display width:
    - CJK wide chars count as 2
    - Others count as 1
    Note: Emojis are tricky across platforms; this keeps it "good enough".
    """
    w = 0
    for ch in s:
        if unicodedata.east_asian_width(ch) in ("W", "F"):
            w += 2
        else:
            w += 1
    return w

def pad_to_width(s: str, width: int) -> str:
    pad = max(0, width - display_width(s))
    return s + (" " * pad)

# --- UI ---
col1, col2 = st.columns([2, 1])

with col1:
    name = st.text_input("Enter name 请输入您的富贵名", value="YOU")
with col2:
    mode = st.selectbox("Style", ["WhatsApp Compact (recommended)", "ASCII Box (monospace)"])

st.write("")
if st.button("🧧 Shake to open 红包", use_container_width=True):
    # suspense
    tease_lines = [
        "Searching for your luck… 🍊",
        "Checking your 贵人 index… 👀",
        "Loading 财神 Wi-Fi… 📶",
        "Verifying 好运连连… ✅",
    ]
    with st.spinner(random.choice(tease_lines)):
        time.sleep(1.2)

    # outcomes
    amount = random.choice(["🧧", "🧧🧧", "🧧🧧🧧", "🧧🧧🧧🧧"])
    luck = random.choice([
        "好运连连 ✨",
        "贵人护体 👑",
        "稳稳发财 💰",
        "健康第一 🙏",
        "烦恼清零 😌",
        "事业开挂 🚀",
        "桃花人缘 🌸",
    ])
    keyword = random.choice(["稳", "冲", "顺", "旺", "新", "强", "爽"])
    persona = random.choice([
        "低调但会爆发型 🚀",
        "稳中带旺型 😌📈",
        "少 drama，多贵人型 👑",
        "先苦后甜型 🍊",
        "躺赢但要努力型 😆",
        "越忙越旺型 💼✨",
    ])

    # Keep name short to avoid ugly wrapping in WhatsApp
    safe_name = name.strip()[:14] if name.strip() else "YOU"

    st.success("Opened! 🎉")

    if mode.startswith("WhatsApp"):
        # WhatsApp-friendly, no alignment issues
        msg = f"""🧧 新年红包 🧧

To: {safe_name}
Amount: {amount}
Luck: {luck}
Persona: {persona}
2026关键词: {keyword}

（Huat Kueh Friendly 😄）"""
        st.code(msg, language="text")

    else:
        # ASCII box in monospace
        # NOTE: emojis still vary by device font; this is more stable than before.
        inner_w = 20  # inside width
        line1 = pad_to_width("新年快乐!", inner_w)
        line2 = pad_to_width(amount, inner_w)
        line3 = pad_to_width(f"To: {safe_name}", inner_w)
        line4 = pad_to_width(luck, inner_w)

        box = (
            "╔" + "═" * inner_w + "╗\n"
            "║" + line1 + "║\n"
            "║" + line2 + "║\n"
            "║" + line3 + "║\n"
            "║" + line4 + "║\n"
            "╚" + "═" * inner_w + "╝"
        )

        st.code(box, language="text")
        #st.caption("Tip: If alignment still looks off on WhatsApp, use the Compact style above.")

#st.divider()
#st.caption("Idea: share your Streamlit link on WhatsApp so friends can generate their own 🧧")
