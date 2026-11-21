# AI Roadmap Generator

A simple Streamlit input/output app that uses Gemini to generate a personalized AI and machine learning learning roadmap.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:GEMINI_API_KEY = "your-gemini-api-key"
python -m streamlit run app.py
```

Enter or edit the roadmap request in the text box, then select **Generate roadmap**. The response appears below the input.
The app reads `GEMINI_API_KEY` from the process environment or from `.venv/.env`.
