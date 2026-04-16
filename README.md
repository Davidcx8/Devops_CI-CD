# Practica Final DevOps CI/CD

Proyecto academico completo para demostrar un flujo profesional de integracion continua y despliegue continuo con una aplicacion web minima, pruebas automatizadas, Docker, GitHub Actions, Docker Hub y despliegue en Render.

## Objetivo

Construir una aplicacion web "Hola Mundo" que pueda:

- ejecutarse localmente
- validarse con pruebas automatizadas
- construirse como imagen Docker
- publicarse en Docker Hub desde GitHub Actions
- desplegarse automaticamente en produccion mediante Render

## Tecnologias elegidas

- `Python 3.12`
- `Flask`
- `pytest`
- `Docker`
- `GitHub Actions`
- `Docker Hub`
- `Render`

## Por que esta pila

Se eligio `Flask` porque es una opcion ligera, estable y facil de explicar en una sustentacion oral. Permite crear una app pequena, testearla rapidamente y empaquetarla en Docker sin agregar complejidad innecesaria.

## Estructura del proyecto

```text
.
|-- .github/workflows/ci-cd.yml
|-- app/
|   |-- __init__.py
|   `-- main.py
|-- docs/
|   |-- entrega.md
|   `-- evidencias/README.md
|-- tests/test_app.py
|-- .dockerignore
|-- .env.example
|-- .gitignore
|-- Dockerfile
|-- gunicorn.conf.py
|-- requirements-dev.txt
|-- requirements.txt
`-- README.md
```

## Requisitos

- `Python 3.12` o superior
- `pip`
- `Docker Desktop` o Docker Engine
- cuenta de GitHub
- cuenta de Docker Hub
- cuenta de Render

## Instalacion local

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
```

## Variables de entorno

Crea un archivo `.env` a partir de `.env.example` si deseas personalizar el mensaje o el puerto:

```env
APP_MESSAGE=Hola Mundo desde DevOps CI/CD
PORT=8000
GUNICORN_WORKERS=2
```

## Ejecutar la aplicacion

```bash
python -m app.main
```

Abrir en el navegador:

- `http://localhost:8000/`
- `http://localhost:8000/health`

## Pruebas

```bash
pytest -q
```

La prueba valida:

- que la pagina principal responde `200`
- que la aplicacion muestra el mensaje esperado
- que el endpoint `/health` devuelve un JSON correcto

## Docker

### Construir la imagen

```bash
docker build -t devops-ci-cd-final .
```

### Ejecutar el contenedor

```bash
docker run -p 8000:8000 --name devops-ci-cd-final devops-ci-cd-final
```

### Probar el contenedor

- `http://localhost:8000/`
- `http://localhost:8000/health`

## GitHub Actions

El workflow definido en `.github/workflows/ci-cd.yml` se activa con cada `push` y tambien manualmente con `workflow_dispatch`.

### Flujo automatizado

1. instala dependencias
2. ejecuta pruebas con `pytest`
3. construye la imagen Docker
4. si el push llega a `main`, autentica con Docker Hub
5. publica la imagen con tags `latest` y `sha-<commit>`
6. dispara el despliegue en Render mediante `deploy hook`

## Configuracion requerida en GitHub

Configura estos valores en `Settings > Secrets and variables > Actions`:

- `DOCKERHUB_USERNAME`: usuario de Docker Hub
- `DOCKERHUB_TOKEN`: access token de Docker Hub
- `DOCKERHUB_REPOSITORY`: variable o secret con el nombre del repositorio en Docker Hub, por ejemplo `devops_ci-cd`
- `RENDER_DEPLOY_HOOK_URL`: secreto opcional mientras aun no hayas creado Render

## Despliegue en Render

Se recomienda crear un **Web Service image-backed** en Render usando la imagen publicada en Docker Hub con el tag `latest`.

### Configuracion sugerida en Render

- Service Type: `Web Service`
- Runtime: `Docker image`
- Image URL: `docker.io/davidcx8/devops_ci-cd:latest`
- Environment Variable opcional: `APP_MESSAGE`

Una vez creado el servicio:

1. copia el `Deploy Hook URL`
2. guardalo como secreto `RENDER_DEPLOY_HOOK_URL` en GitHub
3. cada push a `main` que pase pruebas actualizara Docker Hub y disparara el despliegue

Si todavia no has creado Render, el workflow seguira funcionando y dejara el despliegue como paso omitido sin fallar.

## Evidencias para la entrega

La carpeta `docs/evidencias/README.md` incluye la lista exacta de capturas recomendadas y su ubicacion.

## Documentacion adicional

- Guia de entrega: `docs/entrega.md`
- Evidencias: `docs/evidencias/README.md`

## Comandos clave para defensa oral

```bash
pytest -q
docker build -t devops-ci-cd-final .
python -m app.main
```

## Estado del proyecto

- App web lista
- Pruebas listas
- Docker listo
- CI/CD listo
- Documentacion lista
- Falta configurar el repositorio de Docker Hub y crear el servicio en Render
