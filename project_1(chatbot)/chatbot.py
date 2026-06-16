from datetime import datetime

#  KNOWLEDGE BASE

RESPONSES = {
    # Greetings
    "hello"         : "Hey there! NEXUS online and ready.",
    "hi"            : "Hi! Great to see you. What's on your mind?",
    "hey"           : "Hey! NEXUS here — what can I help you with?",
    "good morning"  : "Good morning! Let's build something great today.",
    "good evening"  : "Good evening! Still coding at this hour? Respect.",

    # Identity
    "who are you"       : "I'm NEXUS — a Rule-Based AI Chatbot built by an AI Engineer intern at DecodeLabs.",
    "what is your name" : "My name is NEXUS. Nice to meet you!",
    "who made you"      : "I was architected by a DecodeLabs intern using Python control flow — no ML, pure logic.",
    "are you human"     : "Nope! 100% deterministic logic. Zero hallucinations.",
    "are you an ai"     : "I'm a Rule-Based AI — a white-box system where every decision is traceable.",

    # AI & Tech Knowledge
    "what is ai"        : "AI (Artificial Intelligence) is the simulation of human intelligence by machines using logic, data, and learning.",
    "what is ml"        : "ML (Machine Learning) is a subset of AI where systems learn patterns from data without being explicitly programmed.",
    "what is python"    : "Python is a high-level, readable programming language — the #1 language for AI and Data Science.",
    "what is a chatbot" : "A chatbot is a program designed to simulate conversation with humans, like me! I use rules; others use LLMs.",
    "what is an llm"    : "LLM stands for Large Language Model — like GPT or Claude. They're probabilistic, unlike my deterministic design.",
    "what is rule based": "Rule-based AI uses explicit if-else logic and dictionaries. Fast, safe, and 100% explainable.",
    "difference between ai and ml": "AI is the broad concept of machines being smart. ML is one technique to achieve AI using data and algorithms.",

    # DecodeLabs
    "what is decodelabs" : "DecodeLabs is an AI training organization based in Greater Lucknow, India. They run hands-on AI internships.",
    "what is project 1"  : "Project 1 is the Rule-Based Chatbot — your foundation milestone to earn your intern badge at DecodeLabs.",

    # Emotions / Small Talk
    "how are you"       : "Running at 100% efficiency. No bugs detected today! How about you?",
    "i am fine"         : "Great to hear! Let's keep the momentum going.",
    "i am good"         : "Awesome! What are we building today?",
    "i am sad"          : "Hey, don't be sad. Every bug you fix makes you stronger!",
    "i am bored"        : "Boredom is a sign you need a new project. Want me to give you a challenge?",
    "thank you"         : "You're welcome! That's what I'm here for.",
    "thanks"            : "Anytime! Happy to help.",

    # Help
    "help"              : (
        "\n NEXUS Command Menu:\n"
        "  → hello / hi / hey          — Greetings\n"
        "  → who are you               — About NEXUS\n"
        "  → what is ai / ml / python  — Tech knowledge\n"
        "  → how are you               — Small talk\n"
        "  → joke                      — Tell me a joke!\n"
        "  → time                      — Current time\n"
        "  → exit / quit               — End session\n"
    ),

    # Fun
    "joke" : "Why do programmers prefer dark mode? Because light attracts bugs!",
    "tell me a joke": "Why did the AI cross the road? It was trained on data from the other side.",
    "motivate me": "You are building something most people only talk about. Keep going!",
    "give me advice": "Master the fundamentals. Control flow today → Neural Networks tomorrow. One rule at a time.",
}

#  PARTIAL MATCH ENGINE — Keyword Scanning
#  Catches: "tell me about ai" → triggers "ai"

KEYWORD_MAP = {
    "python"     : "what is python",
    "machine learning": "what is ml",
    " ml "       : "what is ml",
    "artificial intelligence": "what is ai",
    " ai "       : "what is ai",
    "chatbot"    : "what is a chatbot",
    "decodelabs" : "what is decodelabs",
    "project 1"  : "what is project 1",
    "joke"       : "joke",
    "motivat"    : "motivate me",
    "advice"     : "give me advice",
    "llm"        : "what is an llm",
    "rule"       : "what is rule based",
}

EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye", "see you", "cya"}

#  HELPER — Timestamp Logger

def timestamp():
    return datetime.now().strftime("[%H:%M:%S]")

#  CORE — Response Engine

def get_response(clean_input):
    # 1. Special command: time
    if clean_input in ("time", "what time is it", "current time"):
        return f"Current time is {datetime.now().strftime('%I:%M %p')}"

    # 2. Exact match lookup — O(1)
    if clean_input in RESPONSES:
        return RESPONSES[clean_input]

    # 3. Partial keyword match — scans for embedded keywords
    for keyword, mapped_key in KEYWORD_MAP.items():
        if keyword in f" {clean_input} ":
            return RESPONSES.get(mapped_key, None) or RESPONSES[keyword]

    # 4. Fallback
    return (
        "I don't recognize that input.\n"
        "Type 'help' to see what I can understand."
    )

#  MAIN — The Infinite Heartbeat Loop

def chatbot():
    # Startup Banner
    print("\n" + "═" * 52)
    print(" NEXUS — Rule-Based AI Chatbot")
    print("  DecodeLabs | AI Industrial Training | 2026")
    print("═" * 52)
    print(f"  {timestamp()} System Online. Type 'help' to begin.")
    print("═" * 52 + "\n")

    session_start = datetime.now()
    message_count = 0

    while True:
        try:
            # ── PHASE 1: INPUT & SANITIZATION ──
            raw_input    = input("  You: ")
            clean_input  = raw_input.lower().strip()

            # Skip blank input
            if not clean_input:
                continue

            message_count += 1

            # ── EXIT STRATEGY ──
            if clean_input in EXIT_COMMANDS:
                duration = (datetime.now() - session_start).seconds
                print(f"\n  {timestamp()} NEXUS: Goodbye!")
                print(f" Session Stats: {message_count} messages | {duration}s duration")
                print("\n" + "═" * 52 + "\n")
                break

            # ── PHASE 2 & 3: PROCESS & OUTPUT ──
            reply = get_response(clean_input)
            print(f"\n  {timestamp()} NEXUS: {reply}\n")

        except KeyboardInterrupt:
            print("\n\n Keyboard interrupt detected. NEXUS shutting down.\n")
            break

#  ENTRY POINT

if __name__ == "__main__":
    chatbot()