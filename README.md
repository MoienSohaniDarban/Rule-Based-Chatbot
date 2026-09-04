<div align="center">

# 🤖 Chat Bot

### A lightweight rule-based conversational chatbot built with Python

A simple yet extensible chatbot that processes user messages, evaluates predefined response patterns, and selects the most relevant answer using probability-based keyword matching.

<br>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/MoienSohaniDarban/Chat_Bot?style=for-the-badge&logo=github)](https://github.com/MoienSohaniDarban/Chat_Bot/stargazers)
[![Forks](https://img.shields.io/github/forks/MoienSohaniDarban/Chat_Bot?style=for-the-badge&logo=github)](https://github.com/MoienSohaniDarban/Chat_Bot/network/members)

<br>

[Overview](#-overview) •
[How It Works](#-how-it-works) •
[Getting Started](#-getting-started) •
[Project Structure](#-project-structure) •
[Roadmap](#-roadmap)

</div>

---

## 📌 Overview

**Chat Bot** is a lightweight conversational system implemented entirely in Python.

Unlike modern AI chatbots that depend on large language models or external APIs, this project uses a deterministic, rule-based approach.

Incoming messages are processed and compared with predefined word patterns. Each possible response receives a matching score, and the chatbot selects the response with the highest probability.

When no suitable response can be found, the system returns a randomized fallback message.

The project demonstrates the fundamental mechanics behind simple conversational systems while remaining easy to understand, modify, and extend.

---

## ✨ Features

- 💬 Interactive command-line conversation
- 🔍 Keyword-based message analysis
- 📊 Probability-based response selection
- ✅ Required-word validation
- 🧠 Multiple predefined conversation patterns
- 🎲 Random fallback responses
- 🔡 Case-insensitive input processing
- 📦 No third-party dependencies
- 🧩 Easy-to-extend response system

---

## 🧠 How It Works

The chatbot follows a simple message-processing pipeline:

```text
┌─────────────────────┐
│     User Input      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Normalize & Tokenize│
│      Message        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Compare Against     │
│ Known Word Patterns │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Calculate Matching  │
│    Probability      │
└──────────┬──────────┘
           │
           ▼
     ┌─────────────┐
     │ Match Found?│
     └──────┬──────┘
        Yes │     │ No
            ▼     ▼
      ┌────────┐ ┌─────────────┐
      │ Return │ │ Random      │
      │ Best   │ │ Fallback    │
      │ Answer │ │ Response    │
      └────────┘ └─────────────┘
```

### Message Processing

The incoming message is converted to lowercase and separated into individual words:

```python
split_message = re.split(
    r'\s+|[,;?!.-]\s*',
    user_input.lower()
)
```

This allows the chatbot to evaluate user messages regardless of capitalization or basic punctuation.

### Probability Calculation

Each possible response has a set of recognized words.

The chatbot checks how many of those words occur in the user's message and calculates a matching percentage.

Conceptually:

```text
Matched Words
────────────── × 100
Recognized Words
```

The response with the highest score is considered the best candidate.

### Required Words

Some responses require specific words to be present before they are considered valid.

For example:

```python
response(
    "I'm doing fine, and you?",
    ['how', 'are', 'you', 'doing'],
    required_words=['how']
)
```

Even if several words match, the response will only be considered if the required word `how` is present.

### Fallback Handling

If the chatbot cannot confidently associate the user's input with an existing pattern, it uses a random fallback response stored in:

```text
long_responses.py
```

This prevents the application from failing or returning an empty response when encountering unfamiliar input.

---

## 💬 Example Conversation

```console
You: Hello
Bot: Hello!

You: How are you doing?
Bot: I'm doing fine, and you?

You: Give me some advice
Bot: If I were you, I would go to the internet and type exactly what you wrote there!

You: Bye
Bot: See you!
```

---

## 🏗️ Architecture

The project intentionally uses a minimal architecture:

```text
                    ┌─────────────────┐
                    │      User       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   ChatBot.py    │
                    │                 │
                    │ Input Handling  │
                    │ Tokenization    │
                    │ Matching        │
                    │ Scoring         │
                    │ Response Logic  │
                    └────────┬────────┘
                             │
                    Unknown Message
                             │
                             ▼
                    ┌─────────────────┐
                    │long_responses.py│
                    │                 │
                    │ Long Responses  │
                    │ Fallback Logic  │
                    └─────────────────┘
```

This separation keeps the main conversational logic independent from longer and fallback responses.

---

## 📁 Project Structure

```text
Chat_Bot/
│
├── ChatBot.py
│   └── Core chatbot logic and conversation loop
│
├── long_responses.py
│   └── Long-form and fallback chatbot responses
│
└── README.md
    └── Project documentation
```

<details>
<summary><strong>📄 ChatBot.py</strong></summary>

<br>

The main application file is responsible for:

- Receiving user input
- Normalizing and tokenizing messages
- Registering available responses
- Calculating matching probabilities
- Checking required words
- Selecting the most appropriate response
- Running the command-line conversation loop

</details>

<details>
<summary><strong>📄 long_responses.py</strong></summary>

<br>

This module separates longer responses from the primary chatbot logic.

It also provides randomized fallback messages when the chatbot cannot recognize a user's input.

</details>

---

## 🚀 Getting Started

### Prerequisites

The project requires:

```text
Python 3.x
```

Check whether Python is installed:

```bash
python --version
```

or:

```bash
python3 --version
```

---

### Clone the Repository

```bash
git clone https://github.com/MoienSohaniDarban/Chat_Bot.git
```

Navigate into the project:

```bash
cd Chat_Bot
```

---

### Dependencies

No external packages are required.

The project currently relies only on Python's standard library:

```python
import re
import random
```

Therefore, there is no need to run:

```text
pip install ...
```

---

## ▶️ Run the Application

Run:

```bash
python ChatBot.py
```

On some systems:

```bash
python3 ChatBot.py
```

Once started, the terminal will display:

```console
You:
```

Enter a message and press **Enter** to interact with the chatbot.

---

## 🧩 Extending the Chatbot

One of the main advantages of the project is that additional conversational patterns can be added with minimal code.

### Simple Response

```python
response(
    'Hello!',
    ['hello', 'hi', 'hey', 'sup', 'heyo'],
    single_response=True
)
```

### Response With Required Words

```python
response(
    "I'm doing fine, and you?",
    ['how', 'are', 'you', 'doing'],
    required_words=['how']
)
```

### Concept

Each response defines:

```text
Response Text
     │
     ├── Recognized Words
     │
     ├── Required Words
     │
     └── Single-Response Behavior
```

This makes it straightforward to expand the chatbot's vocabulary and conversational capabilities.

---

## 🛠️ Tech Stack

| Technology | Usage |
| :--- | :--- |
| **Python** | Core application language |
| **Regular Expressions** | Message parsing and tokenization |
| **Random Module** | Fallback response selection |
| **Terminal / CLI** | User interaction |

---

## ⚡ Technical Highlights

This project demonstrates several foundational programming concepts:

- Text preprocessing
- String normalization
- Tokenization
- Keyword matching
- Probability-based scoring
- Rule validation
- Modular code organization
- Fallback handling
- Interactive CLI applications

Although intentionally simple, these concepts provide a useful foundation for understanding how more advanced conversational systems process and classify user input.

---

## 🆚 Rule-Based vs AI Chatbot

This project is intentionally a **rule-based chatbot**.

| This Project | AI / LLM Chatbot |
| :--- | :--- |
| Predefined responses | Generated responses |
| Keyword matching | Semantic understanding |
| Deterministic behavior | Probabilistic generation |
| No training required | Model training/API required |
| Extremely lightweight | Higher computational cost |
| Fully local | Often depends on external models |

This makes the project particularly useful for learning the core logic of conversational systems without requiring machine-learning infrastructure.

---

## 🎯 Project Goals

The project was created to explore the fundamentals of chatbot development and conversational logic through a lightweight Python implementation.

Key learning areas include:

- Processing natural-language-like input
- Mapping messages to predefined intents
- Ranking possible responses
- Handling unknown input
- Structuring conversational logic cleanly

---

## 🗺️ Roadmap

Potential improvements for future versions:

- [ ] Expand available conversation patterns
- [ ] Add conversation context
- [ ] Add short-term conversational memory
- [ ] Separate intents from response logic
- [ ] Improve tokenization
- [ ] Add similarity-based matching
- [ ] Implement NLP-based intent classification
- [ ] Add automated tests
- [ ] Create a graphical interface
- [ ] Add a web-based chat interface
- [ ] Add REST API support
- [ ] Explore machine-learning-based response classification
- [ ] Integrate an LLM as an optional advanced response engine

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you would like to improve the project:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/your-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature/your-feature
```

5. Open a Pull Request

---

## 👤 Author

<div align="center">

### Moien Sohani Darban

[![GitHub](https://img.shields.io/badge/GitHub-MoienSohaniDarban-181717?style=for-the-badge&logo=github)](https://github.com/MoienSohaniDarban)

</div>

---

<div align="center">

### ⭐ If you find this project useful, consider giving it a star.

**Built with Python 🐍**

</div>