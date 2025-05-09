import streamlit as st
import random
import time
from sidebar import my_sidebar

# -----------------------------
# --- Config & Initial Setup
# -----------------------------
st.set_page_config(page_title="⌨️ Typing Speed Tester", layout="centered")

st.image("type-bg.png", use_container_width=True)

my_sidebar()

# Sample sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language.",
    "Streamlit makes it easy to build web apps.",
    "Typing speed improves with regular practice.",
    "Artificial Intelligence is the future of tech."
]

# Initialize session state
if "target_sentence" not in st.session_state:
    st.session_state.target_sentence = random.choice(sentences)
if "typed_text" not in st.session_state:
    st.session_state.typed_text = ""
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "end_time" not in st.session_state:
    st.session_state.end_time = None
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# -----------------------------
# --- UI Layout
# -----------------------------
st.title("⌨️ Typing Speed Tester")
st.markdown("Type the sentence below as fast and accurately as you can!")

st.code(st.session_state.target_sentence)

# Reset BEFORE rendering text_area
col1, col2 = st.columns(2)

with col2:
    if st.button("🔁 Reset"):
        st.session_state.update({
            "typed_text": "",
            "target_sentence": random.choice(sentences),
            "start_time": None,
            "end_time": None,
            "submitted": False
        })
        st.rerun()

# Typing input
typed_text = st.text_area("Start typing here...", height=150, key="typed_text")

# Start timer on typing, but only if not submitted
if not st.session_state.submitted:
    if st.session_state.start_time is None and typed_text.strip():
        st.session_state.start_time = time.time()
    elif st.session_state.start_time is not None and not typed_text.strip():
        # Reset start_time if text is cleared
        st.session_state.start_time = None

# Submit button
with col1:
    if st.button("✅ Submit") and not st.session_state.submitted:
        if typed_text.strip():  # Ensure there's text before submitting
            if st.session_state.start_time is not None:
                st.session_state.end_time = time.time()
                st.session_state.submitted = True
            else:
                st.warning("Please start typing to enable the timer.")
        else:
            st.warning("Please type something before submitting.")

# --- Results
# -----------------------------
if st.session_state.submitted and st.session_state.end_time:
    try:
        total_time = st.session_state.end_time - st.session_state.start_time
        total_words = len(st.session_state.typed_text.strip().split())
        wpm = total_words / (total_time / 60) if total_time > 0 else 0

        # Accuracy
        original = st.session_state.target_sentence.strip().split()
        typed = st.session_state.typed_text.strip().split()

        correct_words = sum(1 for o, t in zip(original, typed) if o == t)
        accuracy = (correct_words / len(original)) * 100 if original else 0

        st.subheader("📊 Results")
        st.write(f"⏱️ Time Taken: `{total_time:.2f} seconds`")
        st.write(f"🚀 Words Per Minute (WPM): `{wpm:.2f}`")
        st.write(f"🎯 Accuracy: `{accuracy:.2f}%`")

        # Highlight mismatches
        st.subheader("📝 Comparison")
        output = []
        for i, word in enumerate(original):
            if i < len(typed) and word == typed[i]:
                output.append(f"✅ **{word}**")
            else:
                output.append(f"❌ ~~{word}~~")
        st.markdown(" ".join(output))
    except (AttributeError, TypeError) as e:
        st.error("Please type something and submit to calculate results.")