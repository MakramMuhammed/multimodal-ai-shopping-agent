# 🛍️ Multimodal AI Shopping Agent

**A production-grade single-agent system for end-to-end e-commerce workflows.**

Powered by LangGraph, Groq, and multimodal LLMs, this agent handles natural language queries, product image analysis, database searches, ratings lookup, and secure transactional checkouts — all within a persistent conversational memory.

<!-- Add screenshot here after uploading an image to your repo -->
![Streamlit Dashboard](https://via.placeholder.com/800x400?text=Add+Screenshot+of+the+App+Here)

## ✨ Features

- **Multimodal Vision**: Upload product images → Vision LLM extracts attributes → intelligent search.
- **Intelligent Product Search**: Keyword + filters (price, organic, rating).
- **Real-time Ratings**: Fetches customer reviews via dedicated API.
- **Secure Checkout**: Multi-turn confirmation before writing to SQLite orders table.
- **Production Guardrails**: Budget constraints, explicit user verification, deterministic routing (low temperature).
- **Streamlit UI**: Clean, responsive dashboard with sidebar image upload and chat history.

## 🏗️ System Architecture

The system uses a unified **ReAct (Reasoning + Action)** loop orchestrated with LangGraph:

- **Multimodal Parsing Layer**: `llama-4-scout` (via Groq) analyzes uploaded images and returns structured JSON attributes.
- **Tool Belt**: Custom LangChain tools for database search, ratings, checkout, and vision.
- **Deterministic Reasoning**: `qwen3-32b` at temperature=0 for reliable tool routing and response formatting.
- **Persistence**: SQLite for products/orders + conversation memory.

## 📁 Repository Structure

```bash
multimodal-ai-shopping-agent/
├── app.py                    # Streamlit frontend dashboard
├── shopping_agent.py         # Core LangGraph agent + tools
├── reviews_api.py            # Product ratings connector
├── shopping_agent.ipynb      # Prototyping & experimentation notebook
├── .env.example              # Environment variables template
├── requirements.txt
├── .gitignore
└── README.md

🛠️ Tech Stack

Orchestration: LangChain, LangGraph
LLMs: Groq (qwen/qwen3-32b for text, meta-llama/llama-4-scout-17b-16e-instruct for vision)
Frontend: Streamlit
Data: SQLite3, Pandas
Others: python-dotenv, base64 image handling

🚀 Quick Start
1. Clone & Install
Bashgit clone https://github.com/MakramMuhammed/multimodal-ai-shopping-agent.git
cd multimodal-ai-shopping-agent
pip install -r requirements.txt
2. Environment Setup
Bashcp .env.example .env
Add your Groq API key in .env:
envGROQ_API_KEY=your_groq_api_key_here
3. Database Setup
Make sure the following files exist in the project root:

store.db (SQLite database with products and orders tables)
Product data CSV (you can generate it from store.xlsx using the notebook)

4. Launch the App
Bashstreamlit run app.py
Open http://localhost:8501 in your browser.
🔧 Key Implementation Highlights

Strict prompt engineering for consistent numbered product lists with IDs.
Secure image handling with temporary files.
Transaction safety — no checkout without explicit user confirmation.
Robust error handling and deterministic behavior.

🎯 Skills Demonstrated

Production-ready AI agents with LangGraph
Multimodal tool-calling pipelines
End-to-end system integration (UI + LLM + Database)
Responsible AI practices and guardrails

🤝 Contributing
Feel free to open issues or pull requests!
📄 License
MIT License

Made with ❤️ by Makram Muhammed