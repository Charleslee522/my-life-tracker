# My Life Tracker

## Before you begin

1.  Create a project in the [Google Cloud Platform Console](https://console.cloud.google.com/) and make note of the project ID.
2.  Install the [Google Cloud SDK](https://cloud.google.com/sdk/)

## Install dependencies

```sh
pip install -r requirements.txt
```

## Deployment

### Environment setting

Modify ./app.yaml

```yaml
env_variables:
  API_KEY: "api_key"
  SECRET_KEY: "secret_key"
  ENV_NAME:
  BOT_TOKEN:
```

### Gcloud

#### Run server

- local

```sh
gunicorn -b :$PORT main:app
```

- gcloud
  
```sh
gcloud app deploy
```

#### Run client

You should send client `POST` body with `Form URL-Encoded`

- local
To localhost:$PORT

- gcloud
To [YOUR_PROJECT_ID].ue.r.appspot.com
