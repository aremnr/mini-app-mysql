# mini web application for showing work with mysql

.env file variables:

```
DB_HOST
DB_NAME 
DB_PASS
DB_PORT 
DB_USER 
```

## starting:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 ---port 80 
```