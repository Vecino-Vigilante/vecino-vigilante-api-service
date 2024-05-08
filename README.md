# Vecino Vigilante API Service

- Recommended python version: 3.11

## For running on development:

1. Create enviroment:

```bash
python3 -m venv env
```

2. Activate enviroment:

On Windows:

```bash
env\Scripts\activate
```

On Unix or MacOS:

```bash
source env/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the server

```bash
uvicorn app.main:app --reload
```

5. Check for API docs at:

http://127.0.0.1:8000/docs

## For running with docker:

6. Run api
```bash
docker compose -f docker-compose.yml up --build
```
