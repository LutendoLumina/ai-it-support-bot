# 🧠 SmartDesk Bot – AI Integration Plan

### Future AI Goals
* Integrate **Natural Language Understanding (NLU)** to parse full sentences
* Implement **AI-powered intent detection** to map user input to categories
* Provide **smarter troubleshooting suggestions**
* Handle **messy or ambiguous queries**

---

### Potential Frameworks

* **LangChain** – for building AI-powered conversational flows

* **OpenAI / LLM APIs** – for intent recognition and context-aware responses

* **Hybrid approach** – rule-based FSM + AI NLU for gradual integration

---

### Implementation Roadmap

1. Replace keyword-based matching in `CATEGORY_SELECTION` with AI intent recognition

2. Enhance `ISSUE_DETAILS` to summarize user input for the troubleshooting engine

3. Integrate AI recommendations in `TROUBLESHOOTING` state

4. Persist AI-enhanced logs for future analytics and learning