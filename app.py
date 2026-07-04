import os
import tempfile
import streamlit as st
from shopping_agent import agent
# ===========================================================================
# 1. PAGE INITIALIZATION & CATCHY THEME DESIGN
# ===========================================================================
st.set_page_config(
    page_title="Haya Shop - AI Assistant", 
    page_icon="🛍️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom premium UI styling overrides
st.markdown("""
    <style>
    /* Global App Background and Base Adjustments */
    .main { background-color: #f8fafc; }
    
    /* Header Custom Typography styling */
    .main-title { color: #1e3a8a; font-weight: 800; font-size: 2.5rem; margin-bottom: 5px; }
    .subtitle-caption { color: #64748b; font-size: 1.05rem; margin-bottom: 25px; }
    
    /* Chat layout styling tweaks */
    .stChatMessage { border-radius: 12px; margin-bottom: 12px; padding: 15px; }
    
    /* Elegant card grouping style */
    .info-card { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 12px; 
        border: 1px solid #e2e8f0; 
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    
    /* Image preview card style */
    .sidebar-img-container {
        border-radius: 8px;
        border: 1px dashed #cbd5e1;
        padding: 8px;
        background: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Main Dashboard Branding Header
st.markdown('<div class="main-title">🛍️ Haya AI Smart Retail Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-caption">Automated multimodal parsing, real-time product cross-referencing, and continuous session order checkout tracking.</div>', unsafe_allow_html=True)

# ===========================================================================
# 2. SIDEBAR PANEL — INTERACTIVE IMAGE INGESTION
# ===========================================================================
with st.sidebar:
    st.markdown("### 📷 Visual Product Discovery")
    st.caption("Upload an image of any item label or grocery container to locate matches instantly across our warehouse stores.")
    st.markdown("---")
    
    uploaded_file = st.file_uploader(
        "Drop file or click to upload", 
        type=["jpg", "jpeg", "png", "webp"],
        label_visibility="collapsed"
    )

    if uploaded_file:
        st.markdown('<div class="sidebar-img-container">', unsafe_allow_html=True)
        st.image(uploaded_file, use_container_width=True, caption="Active Upload Preview")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(" ")

        if st.button("🔍 Analyze Image & Match Products", type="primary", use_container_width=True):
            suffix = os.path.splitext(uploaded_file.name)[1] or ".jpg"
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                tmp.write(uploaded_file.getvalue())
                image_path = tmp.name

            prompt = f"I uploaded a product image. Please analyze it and find similar products in the store. Image path: {image_path}"
            
            if "messages" not in st.session_state:
                st.session_state.messages = []
                
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.session_state.pending_image = uploaded_file.name
            st.rerun()

# ===========================================================================
# 3. CONVERSATIONAL TIMELINE & PERSISTENCE STATE MANAGEMENT
# ===========================================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# Welcome greeting widget if timeline conversation sequence is currently blank
if not st.session_state.messages:
    welcome_cols = st.columns(3)
    with welcome_cols[0]:
        st.markdown('<div class="info-card">🤖 <b>Natural Search</b><br><span style="color:#64748b; font-size:0.9rem;">"Find me organic honey under $20 rated higher than 4.5"</span></div>', unsafe_allow_html=True)
    with welcome_cols[1]:
        st.markdown('<div class="info-card">👁️ <b>Multimodal Vision</b><br><span style="color:#64748b; font-size:0.9rem;">Upload any label to scan specifications, categories, and inventory.</span></div>', unsafe_allow_html=True)
    with welcome_cols[2]:
        st.markdown('<div class="info-card">⚡ <b>Instant Checkout</b><br><span style="color:#64748b; font-size:0.9rem;">Confirm orders directly via chat text turns to write records instantly.</span></div>', unsafe_allow_html=True)

# Render conversation timeline elements cleanly
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "user" and msg["content"].startswith("I uploaded a product image"):
            # Clean up display text for image-search logs
            st.markdown("🖼️ **Visual Search Action Initialized**")
            st.caption("Piped binary matrix sequence array directly to vision LLM processor core.")
        else:
            # Escape dollar marks to preserve markdown formatting
            st.markdown(msg["content"].replace("$", r"\$"))

# ===========================================================================
# 4. MUTABLE LOGIC PIPELINE RUNNERS
# ===========================================================================

# Pipeline Trigger Option A: Unprocessed Image Data
if (
    st.session_state.messages
    and st.session_state.messages[-1]["role"] == "user"
    and "pending_image" in st.session_state
):
    with st.chat_message("assistant"):
        with st.spinner("🤖 Intercepting visual attributes and query routing..."):
            result = agent.invoke({"messages": st.session_state.messages})
            response = result["messages"][-1].content.replace("`", "")
        st.markdown(response.replace("$", r"\$"))

    st.session_state.messages.append({"role": "assistant", "content": response})
    del st.session_state.pending_image
    st.rerun()

# Pipeline Trigger Option B: Standard User Conversational Chat Input
if prompt := st.chat_input("Ask me about items, product scores, ratings, or issue checkouts..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("🧠 Querying database and tracking conversation history..."):
            result = agent.invoke({"messages": st.session_state.messages})
            response = result["messages"][-1].content.replace("`", "")
        st.markdown(response.replace("$", r"\$"))

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()