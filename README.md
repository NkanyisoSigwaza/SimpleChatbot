# Chatbot CLI with OpenAI

This is a simple command-line chatbot that interacts with users using the OpenAI Chat API (GPT-4.1). The conversation is maintained in memory during the session, and responses are strictly based on the system prompt provided.

---

## Features

- Command-line chat interface
- Supports continuous back-and-forth conversation
- Powered by OpenAI's GPT-4.1 model
- Easy setup with `.env` support for API key management

---

## Requirements

- Python 3.8 or higher
- OpenAI API key

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Environment Setup
Create a .env file in the root directory of your project and add your OpenAI API key:

```
OPEN_AI_API_KEY=your_openai_api_key_here
```

## Usage
Run the chatbot using:
```bash
python bot.py
```
