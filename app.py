import streamlit as st

def calculate_leveraged_loss(entry, sl, lev, position):
    try:
        entry = float(entry)
        sl = float(sl)
        lev = float(lev)
        if position == "Long":
            sl_pct = ((entry - sl) / entry) * 100
        else:
            sl_pct = ((sl - entry) / entry) * 100

        leveraged_loss = round(sl_pct * lev, 2)
        return leveraged_loss, round(100 / sl_pct, 2) if sl_pct != 0 else None
    except:
        return None, None

st.set_page_config(page_title="SL Risk Calculator", page_icon="⚙️", layout="centered")

st.markdown("""
    <style>
    body { background-color: #1e1e1e; }
    .stApp { background-color: #1e1e1e; color: white; }
    input, textarea, select, button { font-size: 1.2rem !important; }
    .result-box { font-size: 1.5rem; font-weight: bold; margin-top: 1rem; }
    </style>
""", unsafe_allow_html=True)

st.title("🔻 Futures SL % Calculator")

entry = st.text_input("Entry Price")
sl = st.text_input("Stop-Loss Price")
lev = st.text_input("Leverage (e.g., 20)")
position = st.radio("Position Type", ["Long", "Short"], horizontal=True)

if st.button("Calculate"):
    leveraged_loss, suggested_lev = calculate_leveraged_loss(entry, sl, lev, position)
    if leveraged_loss is not None:
        color = "green" if leveraged_loss <= 130 else "red"
        col1, col2, col3 = st.columns([1, 5, 1])
        with col2:
            st.markdown(f"<div class='result-box' style='color:{color};'>● Leveraged Loss: {leveraged_loss}% ●</div>", unsafe_allow_html=True)
        if leveraged_loss > 130:
            st.markdown(f"<div class='result-box' style='color:#bbb;'>Suggested Leverage: {suggested_lev}x</div>", unsafe_allow_html=True)
    else:
        st.error("Please enter valid numeric values.")
