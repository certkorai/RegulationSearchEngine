
# Agentic RAG System

This repository implements an **Agentic Retrieval-Augmented Generation (RAG) System** built using [CrewAI]. It supports both local and remote LLMs (e.g., Gemini API, Hugging Face), and offers a modular Streamlit interface, markdown-based output, and Docker compatibility.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [File Descriptions](#file-descriptions)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Setup (.env)](#environment-setup-env)
- [Docker Instructions](#docker-instructions)
- [Version Check](#version-check)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Overview

The system provides:
- Agent-driven control and validation pipeline using CrewAI
- Streamlit interface for input and result visualization
- Flexible integration with local (`Ollama`, `HF`) or remote (`Gemini`) LLMs
- Output written to markdown format
- Portable containerization with Docker

---

## Features

- Runs on Python 3.10
- Gemini API and Hugging Face integration
- Gemini config is controlled through `.env`
- Conditional logic to run either API-based or local LLMs
- Markdown summary of each agent's work
- Audit logs and clear task delegation

---

## System Architecture

- **Agent Logic**: Uses CrewAI’s agents, processes, and tasks modules
- **LLM Handler**: Abstracted interface for local, HF, and Gemini models
- **UI**: Built in Streamlit, allows inputs and outputs through browser
- **CLI Option**: Supports terminal runs for faster execution
- **Docker**: Full support with exposed port 8501 for UI

---

## File Descriptions


Here is a complete table of all files and folders in your project, with corrected and detailed descriptions:

| File/Folder | Description |
|-------------|-------------|
| `.env` | Environment variable configuration for Gemini/HF models (manual setup required). |
| `.gitignore` | Lists files and folders to be ignored by Git version control. |
| `Agentic RAG System.ipynb` | Jupyter Notebook used for experimentation and prototyping the RAG system. |
| `Local LLM Streamlit_app.py` | Streamlit UI that uses local or Hugging Face-based LLMs for agentic execution. |
| `Local LLM.py` | CLI-based execution using open-source or local LLMs, produces markdown output. |
| `desktop.ini` | System file (not required for execution, can be ignored). |
| `dockerfile` | Docker definition to containerize and deploy the entire app. |
| `final.md` | Final markdown output generated by the agents. |
| `initial_data_collection_crew.log` | Log capturing task-level execution from the early stages of agentic runs. |
| `pyproject.toml` | Python project configuration using Poetry (for dependency and version control). |
| `report.md` | Possibly a working or intermediate report documentation (user-generated). |
| `requirements.txt` | Dependency file for `pip` installation (alternative to Poetry). |
| `security_compliance_crew.log` | Log file capturing specific security and compliance agent outputs. |
| `streamlit_app.py` | Streamlit-based interface tailored for remote (e.g., Gemini) LLM execution. |
| `user_preference.txt` | Text file capturing user's configuration or preferences (can be used for routing logic). |
| `uv.lock` | Lock file for Poetry (ensures reproducible builds). |
| `README.md` | Main documentation file for understanding and using the system. |

### Subfolders and Structured Files:

#### `logs/`
| File | Description |
|------|-------------|
| `logs/coreCrew.md` | Agent-level summary of internal `coreCrew` logic and outputs. |
| `logs/final_validation_log.md` | Log of final validation agents’ decision-making process. |
| `logs/phase3.md` | Captures execution trace of the third phase in the agent workflow. |

#### `output/`
| File | Description |
|------|-------------|
| `output/fairness.md` | Markdown file detailing fairness compliance extraction results. |
| `output/final.md` | Final agent output copied here (likely same as `final.md`). |
| `output/privacy.md` | Privacy-related compliance summaries. |
| `output/security.md` | Security-related compliance summaries. |
| `output/transparency.md` | Transparency control insights generated by the system. |

#### `src/angentic_base/`
| File | Description |
|------|-------------|
| `app.py` | Main Streamlit or CLI integration hub that loads config and routes tasks. |
| `crew.py` | Defines agent groupings, process logic, and interaction methods. |
| `main.py` | Entrypoint script that connects tasks to CrewAI and launches the flow. |
| `__init__.py` | Package initialization file for `angentic_base`. |

#### `src/angentic_base/config/Final_validation/`
| File | Description |
|------|-------------|
| `agents.yaml` | YAML configuration for final validation agents. |
| `tasks.yaml` | Task definitions linked to final compliance validation. |

#### `src/angentic_base/config/compliance_router/`
| File | Description |
|------|-------------|
| `agents.yaml` | YAML config for agents that route based on compliance dimensions. |
| `tasks.yaml` | Task logic used in routing compliance-related decisions. |

#### `src/angentic_base/tools/`
| File | Description |
|------|-------------|
| `custom_tool.py` | Utility functions or tools used by agents during task execution. |
| `__init__.py` | Initialization for the tools module. |

---


























---

## Installation

```bash
git clone https://github.com/yourname/crewai.git
cd crewai
python -m venv env
source env/bin/activate    # or .\env\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## Environment Setup (.env)

Before running the system, create a `.env` file in the root directory with the following content:

```
MODEL=gemini/gemini-1.5-flash
GEMINI_API_KEY="YOUR API KEY"
HF_TOKEN=your_huggingface_token_here
```

> If running with Gemini, ensure `MODEL` and `GEMINI_API_KEY` are correctly set.
> If running with Hugging Face, use `HF_TOKEN`.

---

## Usage

### 1. Streamlit UI

#### With Gemini API
```bash
streamlit run "Local LLM Streamlit_app.py"
```

#### With HF or local LLM
Edit `llm_handler.py` and set `llm_mode = "hf"` or `"local"`

---

### 2. Command Line (CrewAI CLI)

```bash
crewai run  # runs crew-based config via CrewAI directly
```

Or manually with:
```bash
python "Local LLM.py"
```

---

## Docker Instructions

```bash
docker build -t compliance-app .
docker run -p 8501:8501 compliance-app
```

---

## Version Check

Ensure you are using the correct CrewAI version:

```bash
crewai --version
```

> Recommended version: `0.102.0`  
> To install:  
```bash
pip install crewai==0.102.0
```

---

## Troubleshooting

- **Gemini API Failure**: Ensure correct API key and network access.
- **HF Token Missing**: Populate `.env` with `HF_TOKEN`.
- **Streamlit not loading**: Make sure port `8501` is free.
- **Docker on Windows**: Enable Linux containers:
  ```powershell
  Enable-WindowsOptionalFeature -Online -FeatureName $("Containers-DisposableClientVM")
  ```

---

## License

It is Certkor.ai's project. It is subjected to copyright.

---

For detailed deployment support or advanced customization, please raise an issue.
