# Vecino Vigilante API Service

- Recommended python version: 3.11

## For running the server you can do it in two ways:

### With docker (Recommended):

1. Copy the .example-docker.env file to .env and fill the variables

```bash
cp .example-docker.env .env
```

2. Run the server with docker
```bash
docker compose up -d --build
```

### Manually:

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

4. Copy the .example-manual.env file to .env and fill the variables

```bash
cp .example-manual.env .env
```

5. Run tests

```bash
python -m unittest discover -s tests -p "test_*.py"
```

6. Run the server

```bash
uvicorn app.main:app --reload
```

### After running the server:

7. Check for API docs at:

http://127.0.0.1:8000/docs
