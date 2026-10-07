import os

import requests
from fastapi import FastAPI, HTTPException

app = FastAPI()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SAFE_BROWSING_URL = "https://safebrowsing.googleapis.com/v4/threatMatches:find"


@app.get("/check_url/")
def check_url(url: str):
    if not GOOGLE_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="GOOGLE_API_KEY environment variable is not configured",
        )

    payload = {
        "client": {"clientId": "threat-monitor", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}],
        },
    }

    response = requests.post(
        f"{SAFE_BROWSING_URL}?key={GOOGLE_API_KEY}",
        json=payload,
        timeout=10,
    )

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="API Error")

    threats = response.json().get("matches", [])
    return {"url": url, "status": "unsafe" if threats else "safe"}
