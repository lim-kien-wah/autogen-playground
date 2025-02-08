Setup Ollama

Install the dependencies
1. pip install -r requirements.txt
1. playwright install --with-deps chromium

Start LLM Proxy
litellm --model ollama/deepseek-coder-v2:latest

Set OPENAI_KEY
Run export OPENAI_API_KEY=

Run the script
python ex99-coding-ollama.py

