import random

R_EATING = "I can't eat anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_CAPABILITIES = (
    "I can respond to greetings, answer a few questions, share advice, "
    "tell jokes, and chat with you using simple keyword matching."
)
R_PYTHON = (
    "Start with Python basics such as variables, conditions, loops, and functions. "
    "Then build small projects and improve them as you learn."
)
R_PROGRAMMING = (
    "Programming is the process of giving a computer clear instructions to solve problems. "
    "The best way to learn it is by writing code and building projects regularly."
)
R_MOTIVATION = (
    "Every programmer gets stuck sometimes. Take a short break, divide the problem into "
    "smaller parts, and keep going one step at a time."
)
R_WEATHER = (
    "I cannot check live weather yet, but a weather API could give me that ability "
    "in a future update."
)


def joke():
    return random.choice([
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the programmer quit their job? Because they didn't get arrays!",
        "A SQL query walks into a bar, approaches two tables, and asks: May I join you?"
    ])


def unknown():
    return random.choice([
        "Could you please rephrase that?",
        "I'm not sure I understand.",
        "Could you explain that in another way?",
        "I don't know how to answer that yet.",
        "That is interesting, but I need a little more context.",
        "What does that mean?"
    ])
