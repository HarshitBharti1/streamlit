import os
from dotenv import load_dotenv

load_dotenv()

#HF_API_KEY = "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"
HF_API_KEY = os.getenv("HF_API_KEY", "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")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")