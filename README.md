# Multimodal AI Shopping Agent Architecture

A production-grade, single-agent system designed to handle end-to-end e-commerce workflows. Powered by state-of-the-art LLMs, the agent seamlessly executes natural language browsing, tabular database data mining, multimodal vision searches, tool usage, and transactional multi-turn checkouts via memory persistence.

---

## 🏗️ System Architecture

The core architecture uses a unified ReAct (Reasoning and Action) loop that bridges a user-facing front-end interface with specialized data streams:

* **Multimodal Parsing Layer**: Converts raw product images via a Vision LLM (`llama-4-scout`) to generate structured attributes.
* **Structured Tool Belt**: Interrogates decoupled operational tools hooked into CSV data metrics and local SQLite instances.
* **Deterministic Reasoning Layer**: Run via high-speed inference engines (`qwen3-32b`) at low temperature to ensure strict tool routing constraints.

---

## 📁 Repository Structure

```text
10_project_shopping_agent/
├── .gitignore                   # Workspace rule declarations
├── app.py                      # Interactive Streamlit Frontend Dashboard
├── reviews_api.py              # Pure-python product database metrics connector 
├── shopping_agent.ipynb        # Prototyping scratchpad notebook 
├── shopping_agent.py           # Core LangGraph compilation environment
└── README.md                   # System configuration blueprints

🛠️ Tech Stack & Dependencies
Orchestration: LangChain, LangGraph Core

Inference Compute: Groq API Cloud Ecosystem

Models: qwen/qwen3-32b (Text Router), meta-llama/llama-4-scout-17b-16e-instruct (Vision)

Data Tier: SQLite3, Pandas DataFrames

Application Layer: Streamlit Engine

🚀 Getting Started
1. Environment Setup
Clone this repository to your workspace and install your packages:

Bash
git clone [https://github.com/](https://github.com/)<YOUR_GITHUB_USERNAME>/multimodal-ai-shopping-agent.git
cd multimodal-ai-shopping-agent
pip install -r requirements.txt
2. Configure API Credentials
Create a .env file in the root directory:

GROQ_API_KEY=your_production_level_groq_api_key_here
3. Initialize Databases
Ensure your local backend structures are initialized:

Place store.xlsx - Sheet1.csv into your designated working directory path.

Verify your store.db file is present in the root folder.

4. Launch the Dashboard Interface
Execute the following to bring the dashboard online:

Bash
streamlit run app.py
🛡️ Production Control Guardrails
Deterministic Pricing Constraints: The system evaluates structured budget boundaries (max_price), refusing to surface items exceeding specified financial ceilings.

Visual Ingestion Pipeline: Converts binary image arrays via automated base64 encoders directly into short-form contextual query tokens.

Transaction Isolation: Order placements require explicit verification strings from the user before executing commits against the database orders table.