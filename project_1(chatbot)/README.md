<div align="center">

```
╔══════════════════════════════════════════════╗
║   NEXUS — Rule-Based AI Chatbot              ║
║   DecodeLabs | AI Industrial Training Kit    ║
║   Project 1  | Batch 2026                    ║
╚══════════════════════════════════════════════╝
```

# NEXUS — Rule-Based AI Chatbot

**Project 1 of the DecodeLabs AI Industrial Training Kit**

## Overview

NEXUS is a **Rule-Based AI Chatbot** built using pure Python — no external libraries, no machine learning, no API calls. It demonstrates the power of **deterministic, white-box AI systems** using the IPO (Input → Process → Output) model taught in the DecodeLabs AI Industrial Training Kit.

> *"Before you build systems that learn on their own, you must master the art of teaching a machine through explicit if-else instructions."*
> — DecodeLabs, Project 1 Briefing

This project is the **foundation milestone** of the training program. Completing it proves you can design a continuous digital loop that simulates human interaction through pure programmatic decision-making.

## The Two Minds of AI — Why This Matters

| System | Type | Behavior |
|---|---|---|
| **System 1 — The Artist** | Probabilistic (LLMs) | Flexible, creative, but can hallucinate |
| **System 2 — The Engineer** | Deterministic (Rules) | Precise, traceable, zero hallucination risk |

> *"Before you can manage the chaos of a probability engine, you must master the precision of a logic engine."*

NEXUS is a **System 2** implementation — the skeleton that holds intelligence together.

---

## Features

### Core (Project Spec Requirements)
-  **Infinite Input Loop** — Continuous `while True` cycle (the heartbeat)
-  **Input Sanitization** — `.lower().strip()` normalizes all input
-  **Knowledge Base** — Dictionary with 35+ intents (O(1) lookup)
-  **Fallback Response** — Graceful default for unknown inputs
-  **Exit Strategy** — Clean `break` command on exit keywords

### Bonus (Enhanced Features)
-  **Partial Keyword Matching** — Catches embedded keywords ("tell me about python" → triggers python response)
-  **Timestamp Logger** — Every exchange is logged with `[HH:MM:SS]`
-  **Live Time Command** — Ask "what time is it" for real-time response
-  **Session Statistics** — Message count + session duration on exit
-  **Synonym Triggers** — "hello", "hi", "hey" all mapped to greeting
-  **Personality** — Jokes, motivation, emotional responses
-  **Keyboard Interrupt Handling** — Graceful `Ctrl+C` shutdown

---

## Architecture — The IPO Model

```
┌─────────────────────────────────────────────────────┐
│                   USER INPUT                        │
│                       ↓                             │
│  ┌─────────────────────────────────────────────┐   │
│  │  PHASE 1: INPUT & SANITIZATION              │   │
│  │  raw_input.lower().strip()                  │   │
│  │  "HeLLo" → "hello"  "  hi  " → "hi"        │   │
│  └─────────────────────────────────────────────┘   │
│                       ↓                             │
│  ┌─────────────────────────────────────────────┐   │
│  │  PHASE 2: PROCESS (Logic Skeleton)          │   │
│  │  1. Exit check                              │   │
│  │  2. Exact match  → O(1) dict lookup         │   │
│  │  3. Partial match → keyword scan            │   │
│  │  4. Fallback     → default response         │   │
│  └─────────────────────────────────────────────┘   │
│                       ↓                             │
│  ┌─────────────────────────────────────────────┐   │
│  │  PHASE 3: OUTPUT (Feedback Loop)            │   │
│  │  [HH:MM:SS] NEXUS: <response>               │   │
│  └─────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

### Why Dictionary over If-Elif?

```
If-Elif Chain  →  O(n) Linear  →  Slow, high technical debt  
Dictionary     →  O(1) Constant →  Instant, scalable          
```

The if-elif ladder is an **anti-pattern** — it creates structural weakness and cascading failures as the knowledge base grows. NEXUS uses `dict.get()` for atomic lookup + fallback in a single operation.

---

##  Project Structure

```
nexus-chatbot/
│
├── chatbot.py        # Main chatbot engine
└── README.md         # This file
```

---

## Getting Started

### Prerequisites
- Python 3.x (no external libraries required)

### Sample Session

```
════════════════════════════════════════════════════
     NEXUS — Rule-Based AI Chatbot
  DecodeLabs | AI Industrial Training | 2026
════════════════════════════════════════════════════
  [10:30:00] System Online. Type 'help' to begin.
════════════════════════════════════════════════════

  You: hello
  [10:30:02] NEXUS: Hey there! NEXUS online and ready. 

  You: what is ai
  [10:30:05] NEXUS: AI (Artificial Intelligence) is the simulation
             of human intelligence by machines using logic, data, and learning.

  You: tell me about python
  [10:30:09] NEXUS: Python is a high-level, readable programming
             language — the #1 language for AI and Data Science.

  You: joke
  [10:30:12] NEXUS: Why do programmers prefer dark mode?
             Because light attracts bugs! 

  You: bye
  [10:30:15] NEXUS: Goodbye! 
   Session Stats: 4 messages | 15s duration
```

---

##  Supported Commands

| Category | Commands |
|---|---|
| **Greetings** | `hello`, `hi`, `hey`, `good morning`, `good evening` |
| **Identity** | `who are you`, `what is your name`, `who made you`, `are you human` |
| **Tech Knowledge** | `what is ai`, `what is ml`, `what is python`, `what is a chatbot`, `what is an llm` |
| **DecodeLabs** | `what is decodelabs`, `what is project 1` |
| **Small Talk** | `how are you`, `i am fine`, `i am sad`, `i am bored`, `thank you` |
| **Utilities** | `time`, `help`, `joke`, `motivate me`, `give me advice` |
| **Exit** | `exit`, `quit`, `bye`, `goodbye` |

---

##  Key Concepts Demonstrated

| Concept | Implementation |
|---|---|
| **Control Flow** | `while True` loop with `break` exit |
| **Data Structures** | Dictionary as knowledge base (Hash Map) |
| **String Methods** | `.lower()`, `.strip()` for sanitization |
| **Algorithmic Efficiency** | O(1) dictionary lookup vs O(n) if-elif |
| **IPO Model** | Input sanitization → Logic processing → Output generation |
| **White-Box AI** | Every decision is fully traceable and explainable |
| **Fallback Handling** | `dict.get(key, default)` atomic operation |

---

## 🔭 The Conceptual Bridge — What Comes Next

```
Project 1 (This)              Project 2 (Next)
─────────────────             ──────────────────────────
Discrete Mapping         →    Continuous Mapping
Exact Match Lookup       →    Semantic / Approximate Match
Hardcoded Key:Value      →    Vector Embeddings [0.2, 0.9, 0.4]
Rule-Based Logic         →    ML / NLP Models
```

This project builds the **skeleton**. Future projects add the intelligence.

---

##  The White Box Advantage

Rule-based systems are strategically necessary in the real world:

- **TRACEABILITY** — Input → Logic → Output. No mystery.
- **SAFETY** — Zero hallucination risk. 100% hard-coded responses.
- **COMPLIANCE** — Essential for Finance & Healthcare applications.

Frameworks like NVIDIA NeMo and Llama Guard use this exact principle as guardrails over LLMs. NEXUS is your first implementation of that control layer.

---

</div>
