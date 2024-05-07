# Vecino Vigilante microservice template

A lightweight FastAPI scaffolding base to bootstrap App/API development

- Recommended python version: 3.11

## For running on development:

1. Create enviroment:

```bash
python -m venv env
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




## For running database:

1. Run database

```bash
docker compose -f docker-compose.mysql.yml up --build
```

2. Navigate to localhost:8080

3. Login:
```bash
user: root
password: password
```

4. Create db vecino-vigilante

5. Create enviroment:

```bash
python -m venv env
```

6. Activate enviroment:

On Windows:

```bash
env\Scripts\activate
```

On Unix or MacOS:

```bash
source env/bin/activate
```

7. Install dependencies

```bash
pip install -r requirements.txt
```

8. Migrate db
```bash
python3 -m app.infrastructure.configs.migrate_database
```




## For running with docker:

6. Run api
```bash
docker compose -f docker-compose.yml up --build
```
