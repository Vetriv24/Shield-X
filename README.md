# Shield-X 🛡️

**Shield-X** is a lightweight web prototype for checking whether a URL appears in Google's Safe Browsing threat database. It was developed as a college hackathon project to explore practical web security and threat-intelligence workflows.

## ✨ Features

- URL input and validation at the UI level.
- FastAPI endpoint for URL analysis.
- Google Safe Browsing API integration.
- Checks for malware and social-engineering threats.
- Simple frontend risk-status display.
- Responsive, minimal interface.
- Demo screenshot and GIF included in the repository.

## 🏗️ Architecture

```text
Browser 
   │
   │ GET /check_url/?url=...
   ▼
FastAPI Backend
   │
   │ threatMatches:find
   ▼
Google Safe Browsing API
   │
   ▼
Threat result
   │
   ▼
Browser UI
```

## 🛠️ Tech Stack

**Frontend**
- HTML5
- CSS3
- Vanilla JavaScript

**Backend**
- Python
- FastAPI
- Requests

**Security / Threat Intelligence**
- Google Safe Browsing API

## 📁 Project Structure

```text
Shield-X/
├── backend.py
├── index.html
├── script.js
├── style.css
├── requirements.txt
├── .env.example
├── screenshot.png
├── output-onlinegiftools.gif
├── test.py
└── README.md
```

## 🚀 Local Setup

### 1. Clone

```bash
git clone "Paste link of this repository"
cd Shield-X
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Configure the API key

Create a local `.env` file or configure the environment variable directly:

```env
GOOGLE_API_KEY=your_api_key_here
```

The application reads `GOOGLE_API_KEY` from the environment. Never commit `.env` or real API credentials.

### 4. Start the API

```bash
uvicorn backend:app --reload --port 8000
```

The frontend currently expects the backend at `http://127.0.0.1:8000`.

## ⚠️ Security Note

**Never commit API keys to GitHub.** If an API key was previously committed to this repository, revoke/rotate that credential and use a replacement stored in an environment variable. Removing a key from the latest file does not remove it from Git history.

## 🔍 How It Works

1. The user enters a URL.
2. The browser sends it to the FastAPI `/check_url/` endpoint.
3. FastAPI queries Google Safe Browsing for malware/social-engineering matches.
4. The backend returns whether matches were found.
5. The frontend displays the result.

## 📌 Project Status

Hackathon/educational prototype. It demonstrates the core URL threat-checking workflow but is not a complete production security product.

## 👥 Team

- Vettrivelan G
- Veeraarun V
- Ammu Krishnaprasad
- Roshni A


