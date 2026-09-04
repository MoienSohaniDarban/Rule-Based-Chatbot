<div align="center">

# 🤖 Chat Bot

### A lightweight rule-based conversational chatbot built with Python

A simple and extensible chatbot that processes user messages, evaluates predefined response patterns, and selects the most relevant answer using probability-based keyword matching.

<br>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/MoienSD/Chat_Bot?style=for-the-badge&logo=github)](https://github.com/MoienSD/Chat_Bot/stargazers)
[![Forks](https://img.shields.io/github/forks/MoienSD/Chat_Bot?style=for-the-badge&logo=github)](https://github.com/MoienSD/Chat_Bot/network/members)

<br>

[Overview](#-overview) •
[Features](#-features) •
[How It Works](#-how-it-works) •
[Getting Started](#-getting-started) •
[Latest Update](#-latest-update) •
[Roadmap](#-roadmap)

</div>

---

## 📌 Overview

**Chat Bot** is a lightweight conversational system implemented entirely in Python.

Unlike modern AI chatbots that depend on large language models or external APIs, this project uses a deterministic, rule-based approach. Incoming messages are processed and compared with predefined word patterns. Each possible response receives a matching score, and the chatbot selects the response with the highest probability.

When no suitable response can be found, the system returns a randomized fallback message. The project demonstrates the fundamental mechanics behind simple conversational systems while remaining easy to understand, modify, and extend.

---

## ✨ Features

- 💬 Interactive command-line conversation
- 🔍 Keyword-based message analysis
- 📊 Probability-based response selection
- ✅ Required-word validation for more accurate matching
- 👋 Greetings, farewells, and everyday conversation
- 🤖 Identity, creator, age, location, and capability responses
- 🐍 Python learning and programming explanations
- 💡 Advice and motivational responses
- 😂 Randomly selected programming jokes
- 🌦️ Weather-related limitation response
- 🎲 Varied fallback responses for unknown messages
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

This allows the chatbot to evaluate messages regardless of capitalization or basic punctuation.

### Probability Calculation

Each possible response has a set of recognized words. The chatbot checks how many of those words occur in the user's message and calculates a matching percentage:

```text
Matched Words
────────────── × 100
Recognized Words
```

The response with the highest score is considered the best candidate.

### Required Words

Some responses require specific words to be present before they are considered valid:

```python
response(
    "I'm doing fine, and you?",
    ['how', 'are', 'you', 'doing'],
    required_words=['how']
)
```

Even if several words match, this response is only considered when the required word `how` is present. More specific responses use multiple required words to reduce incorrect matches.

### Fallback Handling

If the chatbot cannot associate the user's input with an existing pattern, it returns one of several random fallback messages from `long_responses.py`. This prevents the application from returning an empty response when it encounters unfamiliar input.

---

## 💬 Example Conversation

```console
You: Hello
Bot: Hello!

You: What is your name?
Bot: I'm a simple Python chatbot!

You: Who created you?
Bot: I was created as a Python learning project.

You: What can you do?
Bot: I can respond to greetings, answer a few questions, share advice, tell jokes, and chat with you using simple keyword matching.

You: How can I learn Python?
Bot: Start with Python basics such as variables, conditions, loops, and functions. Then build small projects and improve them as you learn.

You: Tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!

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
                 Long or Random Response
                             │
                             ▼
                    ┌─────────────────┐
                    │long_responses.py│
                    │                 │
                    │ Long Responses  │
                    │ Random Jokes    │
                    │ Fallback Logic  │
                    └─────────────────┘
```

This separation keeps the main conversational logic independent from longer, randomized, and fallback responses.

---

## 📁 Project Structure

```text
Chat_Bot/
│
├── ChatBot.py
│   └── Input processing, response scoring, intent patterns, and conversation loop
│
├── long_responses.py
│   └── Long-form replies, random jokes, and fallback responses
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
- Registering short and long response patterns
- Calculating matching probabilities
- Checking required words
- Selecting the most appropriate response
- Running the command-line conversation loop

</details>

<details>
<summary><strong>📄 long_responses.py</strong></summary>

<br>

This module contains longer educational and conversational responses. It also provides random programming jokes and varied fallback messages for inputs the chatbot cannot recognize.

</details>

---

## 🚀 Getting Started

### Prerequisites

The project requires Python 3.x. Check whether Python is installed:

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

### Clone the Repository

```bash
git clone https://github.com/MoienSD/Chat_Bot.git
cd Chat_Bot
```

### Dependencies

No external packages are required. The project relies only on Python's standard library:

```python
import re
import random
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

Once started, the terminal displays `You:`. Enter a message and press **Enter** to interact with the chatbot. Use `Ctrl+C` to stop the program.

---

## 🧩 Extending the Chatbot

Additional conversational patterns can be added with minimal code.

### Simple Response

Use `single_response=True` when any recognized keyword should be enough to activate a response:

```python
response(
    'Hello!',
    ['hello', 'hi', 'hey', 'sup', 'heyo'],
    single_response=True
)
```

### Response With Required Words

Use `required_words` when particular words must be present:

```python
response(
    'Good morning! I hope you have a great day.',
    ['good', 'morning'],
    required_words=['good', 'morning']
)
```

### Long Response

Define longer text in `long_responses.py`:

```python
R_NEW_RESPONSE = (
    "Your longer response can be stored here to keep "
    "the main chatbot file easy to read."
)
```

Then register it in `ChatBot.py`:

```python
response(
    lr.R_NEW_RESPONSE,
    ['relevant', 'keywords'],
    required_words=['relevant']
)
```

### Random Response

A function can return a randomly selected response:

```python
def joke():
    return random.choice([
        "First joke",
        "Second joke"
    ])
```

---

## 🛠️ Tech Stack

| Technology | Usage |
| :--- | :--- |
| **Python** | Core application language |
| **Regular Expressions** | Message parsing and tokenization |
| **Random Module** | Joke and fallback response selection |
| **Terminal / CLI** | User interaction |

---

## ⚡ Technical Highlights

This project demonstrates several foundational programming concepts:

- Text preprocessing and normalization
- Tokenization with regular expressions
- Keyword matching
- Probability-based scoring
- Required-word validation
- Modular code organization
- Random response selection
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
| Deterministic intent selection | Probabilistic generation |
| No training required | Model training or API access required |
| Extremely lightweight | Higher computational cost |
| Fully local | Often depends on external models |

This makes the project useful for learning the core logic of conversational systems without requiring machine-learning infrastructure.

---

## 🆕 Latest Update

- Added new greetings for morning and night
- Added identity, creator, age, location, and favorite-language responses
- Added chatbot capability information
- Added Python learning and programming explanations
- Added motivational and weather-related responses
- Added three randomly selected programming jokes
- Expanded and improved fallback responses
- Refined required keywords to reduce incorrect intent matches

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

- [x] Expand available conversation patterns
- [x] Add varied fallback responses
- [x] Add randomized programming jokes
- [ ] Add a built-in exit command
- [ ] Add conversation context
- [ ] Add short-term conversational memory
- [ ] Separate intents into a JSON data file
- [ ] Improve tokenization
- [ ] Add similarity-based matching
- [ ] Implement NLP-based intent classification
- [ ] Add automated tests
- [ ] Create a graphical interface
- [ ] Add a web-based chat interface
- [ ] Add REST API support
- [ ] Connect to a live weather API
- [ ] Integrate an LLM as an optional advanced response engine

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add new feature"
   ```

4. Push your branch:

   ```bash
   git push origin feature/your-feature
   ```

5. Open a pull request.

---

## 👤 Author

<div align="center">

### Moien Sohani Darban

[![GitHub](https://img.shields.io/badge/GitHub-MoienSD-181717?style=for-the-badge&logo=github)](https://github.com/MoienSD)

</div>

---

<div align="center">

### ⭐ If you find this project useful, consider giving it a star.

**Built with Python 🐍**

</div>
