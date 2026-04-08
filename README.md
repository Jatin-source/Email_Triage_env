<div align="center">
  <img src="https://img.icons8.com/color/150/000000/envelope-open.png" alt="Email Triage Logo" width="100"/>
  <h1>✉️ Email Triage Environment</h1>
  <p><i>An advanced simulation & evaluation environment for intelligent email processing agents.</i></p>

  <p align="center">
    <img alt="Python Version" src="https://img.shields.io/badge/python-3.9%2B-blue">
    <img alt="License" src="https://img.shields.io/badge/license-MIT-green">
    <img alt="Backend" src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white">
    <img alt="Docker" src="https://img.shields.io/badge/Docker-Supported-2496ED?logo=docker&logoColor=white">
  </p>
</div>

<br>

## 📖 Overview

**Email Triage Environment** is a comprehensive, simulated infrastructure designed for developing, testing, and evaluating AI agents tasked with managing email inboxes. Built with a high-performance **FastAPI** backend and seamlessly integrated with **OpenAI** language models, it provides dynamic generation of emails, rigorous triage tasks (classification, prioritization, routing), and automated grading systems to consistently score agent performance.

Inspired by robust evaluation frameworks, this project allows you to test LLMs in realistic administrative scenarios to ensure they can flawlessly categorize urgency, route messages to appropriate departments, and respond to common requests.

---

## ✨ Key Features

- **🧠 Dynamic Scenario Generation:** Simulates an influx of varied emails—from high-urgency executive requests to routine IT support tickets.
- **⚡ Advanced Task Framework:** Contains structured task definitions (Easy, Medium, Hard) that stress-test different capabilities of an AI agent.
- **📊 Automated Graders:** Integrated scoring systems that automatically evaluate agent responses, classification accuracy, and action choices.
- **🚀 Scalable Backend:** Powered by FastAPI and Uvicorn for asynchronous, blazingly fast API endpoints.
- **🐳 Docker Ready:** Fully containerized architecture allows you to spin up the entire simulation environment in seconds.

---

## 🛠️ Tech Stack

- **Core & API:** Python 3.9+, FastAPI, Uvicorn
- **AI & Integration:** OpenAI API (`gpt-4`, `gpt-3.5-turbo`), OpenEnv Core
- **Data Schemas:** Pydantic
- **Containerization:** Docker

---

## 🏗️ Project Structure

```text
email_triage_env/
├── app/               # Main application and API logic
├── data/              # Base prompt data, email templates, and configurations
├── graders/           # Automated evaluation logic for agent responses
├── tasks/             # Definitions for easy, medium, and hard triage tasks
├── server/            # Backend server initialization and routing
├── inference.py       # Core logic linking the environment with LLM inference
├── requirements.txt   # Python dependencies
├── openenv.yaml       # OpenEnv configuration setup
└── Dockerfile         # Docker configuration file
```

---

## 🚀 Getting Started

### 1. Prerequisite Setup
Ensure you have **Python 3.9+** or **Docker** installed on your system.
Clone the repository:
```bash
git clone https://github.com/Jatin-source/Email_Triage_env.git
cd Email_Triage_env
```

### 2. Local Installation

Create a virtual environment:
```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate
# On Linux/macOS
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r email_triage_env/requirements.txt
```

Set up your OpenAI API credentials:
```bash
export OPENAI_API_KEY="your-sk-api-key"
```

### 3. Running the Server

Launch the FastAPI backend locally:
```bash
uvicorn email_triage_env.server.main:app --host 0.0.0.0 --port 8000
```
Navigate to `http://localhost:8000/docs` to view the interactive API playground.

### 4. Running via Docker

Alternatively, build and run the entire environment using Docker:
```bash
docker build -t email-triage-env .
docker run -p 8000:8000 -e OPENAI_API_KEY="your-sk-api-key" email-triage-env
```

---

## 🔬 Running Tasks

You can initiate a task evaluation directly through the provided inference engine.
```python
from email_triage_env import inference
# Set up agent and run task evaluations...
```

The system will generate an email scenario, wait for the agent's triage decision, and automatically output a score based on the `graders/` criteria.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

<div align="center">
  <p>Built by <b>Jatin</b>.</p>
</div>
