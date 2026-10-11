# Number Info API — Vercel-ready

A small Flask API with a home endpoint and phone-number format validation.

## Files
- `main.py` — Flask application
- `requirements.txt` — Python dependency
- `vercel.json` — Vercel Python runtime configuration

## Deploy
1. Extract this ZIP.
2. Upload the three project files (`main.py`, `requirements.txt`, `vercel.json`) to the root of a GitHub repository.
3. Import the repository at https://vercel.com/new.
4. Deploy with the default settings for a Python project.

## Test
- `GET /`
- `GET /info?number=9876543210`

The `/info` endpoint validates formatting only. It intentionally does not scrape third-party sites or disclose private subscriber details, addresses, live locations, device identifiers, or tracking history.

## Run locally
```bash
pip install -r requirements.txt
python main.py
```
Then visit `http://127.0.0.1:5000/`.
