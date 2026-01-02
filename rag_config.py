# config/rag_config.py

# ==============================
# RAG 分割・検索設定
# ==============================

# --- チャンク分割設定 ---
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
CHUNK_SEPARATOR = "\n"

# --- Retriever 設定 ---
RETRIEVER_TOP_K = 5
