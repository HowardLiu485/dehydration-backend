# Dehydration Detection Backend (Flask API)

## Endpoint
POST /predict

## Input JSON
{
  "hr": number,
  "temp": number,
  "activity": number
}

## Output JSON (mock for now)
{
  "risk": "NORMAL" | "MILD" | "HIGH",
  "score": 0-100
}

## Project Structure
- app.py                → Flask backend API
- model/model.pkl       → Machine learning model (added later by Student 1)
- streaming/stream_data.py → Simulated real-time sensor data

## Run Backend
python app.py

## Run Streaming Script
python streaming/stream_data.py