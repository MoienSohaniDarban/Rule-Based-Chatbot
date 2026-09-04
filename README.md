# 🤖 Python Chatbot

A lightweight rule-based chatbot built with Python that processes user messages, evaluates them against predefined response patterns, and selects the most relevant response using a simple probability-based matching system.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Type-Rule--Based%20Chatbot-informational" alt="Rule-Based Chatbot">
  <img src="https://img.shields.io/badge/Dependencies-None-success" alt="No External Dependencies">
</p>

---

## 📖 Overview

This project is a simple conversational chatbot developed in Python.

Instead of relying on machine learning models or external AI APIs, the chatbot uses a lightweight rule-based approach to analyze user input and determine the most appropriate response.

Each incoming message is normalized and split into individual words. The chatbot then compares those words against predefined response patterns, calculates a matching probability for each possible response, and returns the response with the highest score.

If the chatbot cannot confidently match the message to a known pattern, it returns one of several fallback responses.

---

## ✨ Features

- Simple natural-language input processing
- Probability-based response matching
- Required-word validation for more accurate responses
- Support for predefined short and long responses
- Random fallback responses for unknown input
- Case-insensitive message processing
- Lightweight implementation using only Python's standard library
- Easy to extend with new conversation patterns

---

## ⚙️ How It Works

The chatbot follows a simple response-selection pipeline:

```text
User Input
    │
    ▼
Normalize & Split Message
    │
    ▼
Compare Words With Known Patterns
    │
    ▼
Calculate Match Probability
    │
    ▼
Select Highest-Scoring Response
    │
    ├── Match Found ──► Return Response
    │
    └── No Match ─────► Return Random Fallback
```

### 1. Message Processing

The user's input is converted to lowercase and split into individual words using regular expressions.

```python
split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
```

### 2. Response Matching

Each possible response contains a list of recognized words.

The chatbot calculates how many of those words appear in the user's message and converts the result into a percentage score.

### 3. Required Words

Some responses also define required words.

For example, a response may only be considered valid if the word `how` exists in the message.

This prevents responses from being selected based only on weak keyword matches.

### 4. Best Response Selection

All response scores are compared and the response with the highest probability is returned.

If no known response receives a sufficient match, the chatbot returns a random fallback response.

---

## 💬 Example

```text
You: Hello
Bot: Hello!

You: How are you doing?
Bot: I'm doing fine, and you?

You: Give me advice
Bot: If I were you, I would go to the internet and type exactly what you wrote there!

You: Bye
Bot: See you!
```

---

## 📁 Project Structure

```text
Chat_Bot/
│
├── ChatBot.py
└── long_responses.py
```

### `ChatBot.py`

Contains the core chatbot logic, including:

- message preprocessing
- response probability calculation
- response registration
- best-match selection
- command-line conversation loop

### `long_responses.py`

Contains longer predefined responses and fallback responses used when the chatbot cannot recognize the user's message.

---

## 🚀 Getting Started

### Prerequisites

You only need Python 3 installed on your system.

Check your Python installation:

```bash
python --version
```

or:

```bash
python3 --version
```

---

### Installation

Clone the repository:

```bash
git clone https://github.com/MoienSohaniDarban/Chat_Bot.git
```

Move into the project directory:

```bash
cd Chat_Bot
```

No additional packages are required.

---

## ▶️ Running the Chatbot

Run:

```bash
python ChatBot.py
```

or, depending on your system:

```bash
python3 ChatBot.py
```

The chatbot will start directly in your terminal:

```text
You:
```

Type a message and press Enter to interact with it.

---

## 🧩 Adding New Responses

New response patterns can easily be added inside the `check_all_messages()` function.

For example:

```python
response(
    'Hello!',
    ['hello', 'hi', 'hey', 'sup', 'heyo'],
    single_response=True
)
```

You can also require specific words:

```python
response(
    "I'm doing fine, and you?",
    ['how', 'are', 'you', 'doing'],
    required_words=['how']
)
```

This structure makes the chatbot easy to extend without introducing additional libraries or complex configuration.

---

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Core application |
| `re` | User-message parsing and tokenization |
| `random` | Random fallback-response selection |

The project does not require any third-party dependencies.

---

## 🎯 Project Purpose

This project demonstrates the fundamental concepts behind a basic conversational system, including:

- text preprocessing
- keyword matching
- scoring and response selection
- fallback handling
- modular response organization

It can also serve as a simple foundation for experimenting with more advanced chatbot concepts such as intent detection, NLP pipelines, machine-learning classifiers, or AI-powered responses.

---

## 🔮 Possible Improvements

Future versions could include:

- [ ] More conversation patterns
- [ ] Conversation context and memory
- [ ] Intent classification
- [ ] Improved text preprocessing
- [ ] NLP-based similarity matching
- [ ] Unit tests
- [ ] GUI or web interface
- [ ] Integration with machine-learning or language models

---

## 👤 Author

**Moien Sohani Darban**

GitHub: [@MoienSohaniDarban](https://github.com/MoienSohaniDarban)

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a star.