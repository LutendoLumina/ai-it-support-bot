# 🤖 SmartDesk Bot (AI-Powered IT Support Chatbot)

![CI](https://github.com/LutendoLumina/ai-it-support-bot/actions/workflows/ci.yml/badge.svg)

```mermaid
flowchart TD
    A[START / GREETING] --> B[CATEGORY_SELECTION]
    B --> C[ISSUE_DETAILS]
    C --> D[TROUBLESHOOTING]
    D -->|Worked| E[RESOLUTION]
    D -->|Didn't Work| F[ESCALATION]
    E -->|More Issues| B
    E -->|No More Issues| G[END]
    F --> G[END]
```


SmartDesk Bot is a **Python-based, state-driven IT support chatbot** designed to assist users with common IT issues such as Wi‑Fi connectivity, printers, password resets, and email login errors.

This project demonstrates **state-machine design, clean architecture, and incremental AI integration**

---

## ✨ Key Features (V1)

* Guided, conversational troubleshooting
* Deterministic **state-machine architecture**
* Clear separation of concerns (states, routing, utilities)
* Safe handling of invalid input and unfinsihed states

---

## 🏗️ Architecture Overview

SmartDesk Bot uses a **finite state machine (FSM)** pattern.


### High-Level Flow

```
User Input
   ↓
main.py (Main Loop)
   ↓
Flow Controller
   ↓
State Handler (START, CATEGORY_SELECTION, etc.)
   ↓
Next State Returned
   ↓
Main Loop Continues
```

### Core Principles

* Each state:

  * Displays output
  * Accepts **one type of input**
  * Returns **exactly one next state**
* The main loop never contains business logic
* The flow controller is the single source of truth for routing

* Detailed architecture and design notes are available in docs/architecture.md

---

## 📁 Project Structure

```
ai-chatbot/
│
├── main.py                  # Application entry point & main loop
│
├── bot/                     # All chatbot logic
│   ├── __init__.py
│   ├── flow_controller.py   # Central state router
│   ├── utils.py             # Shared helpers (validation, formatting)
│   └── states/              # Individual conversation states
│       ├── __init__.py
│       ├── start_state.py       # State 1: Greeting
│       ├── category_state.py    # State 2: Category selection
│       ├── issue_state.py       # State 3: Issue details
│       ├── troubleshoot.py      # State 4: Troubleshooting
│       └── end_state.py         # State 6: Exit & feedback
│
└── README.md
```

---

## 🔁 State Machine Design (V1)

### State 1: START / GREETING

**Purpose**

* Welcome the user
* Explain what SmartDesk Bot can help with

**Transitions**

* ➡️ `CATEGORY_SELECTION`

---

### State 2: CATEGORY_SELECTION

**Purpose**

* Let the user select a problem category

**Transitions**

* Valid selection ➡️ `ISSUE_DETAILS`
* Invalid / unclear input ➡️ `CATEGORY_SELECTION`

---

### State 3: ISSUE_DETAILS

**Purpose**

* Collect free-text details about the selected issue

**Transitions**

* ➡️ `TROUBLESHOOTING`

---

### State 4: TROUBLESHOOTING

**Purpose**

* Provide structured, step-by-step troubleshooting
* Confirm whether each step resolves the issue

**Transitions**

* Resolved ➡️ `RESOLUTION`
* Not resolved ➡️ `ESCALATION`

---

### State 5: RESOLUTION / ESCALATION

**Purpose**

* Close the issue gracefully
* Escalate to human support if required

**Transitions**

* More help ➡️ `CATEGORY_SELECTION`
* Exit ➡️ `END`

---

### State 6: END

**Purpose**

* End the conversation cleanly
* Optionally collect feedback (1-5 rating)

---

* Full debugging notes, lessons learned, and AI/NLU plans are in docs/debugging.md and docs/ai_plan.md.

---

### 🧪 Testing Strategy

This project uses **targeted unit testing** focused on logic-heavy components.

* Written using pytest and monkeypatch to simulate user input.
* Ensures state transitions are correct and loops exit as expected.
* Optional tests handle invalid input in END state

**Tested Components**

* `category_state` — input parsing & routing
* `flow_controller` — state transitions & fallbacks
* `troubleshoot_state` — looping and decision logic
* `issue_state` - free-text issue collection, proper transition to troubleshooting
* `end state` - feedback collection, exit logic, rating validation

**Why Not Test Everything?**

* Output-only states (e.g. greetings) are low risk
* I/O-heavy loops are validated manually
* Focus is on behavioral correctness, not line coverage

### Running Tetss Locally

```bash
pytest

```

---

### ⚙️ CI/CD & Code Quality

SmartDesk Bot uses **GitHub Actions** and **pre-commit** hooks to enforce quality.

**Local (Pre-commit)**
* Black (Python formatter)
* Prevents bad commits before push

**CI Pipeline (GitHub Actions)**
* Runs on every push & PR
* Checks formatting (`black --check`)
* Runs unit tests
* Blocks broken or unformatted code
* Successful runs show green CI badge in README

This simulates `professional code review and build gates`2az, similar to industry workflows.

---

## 🚀 Project Goals

* Build a production-quality conversational system
* Demonstrate mastery of state-machine design
* Apply clean architecture principles in Python
* Create a portfolio-ready AI-focused project

---

## 🧑‍💻 Author

**Lutendo Matshidze**
Computer Science Graduate | Aspiring AI & Software Engineer

---

## 📌 Project Status

🚧 **In Progress** — Incremental development by chatbot state
