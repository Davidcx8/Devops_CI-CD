# Guia de Entrega y Sustentacion

## Resumen ejecutivo

Este proyecto implementa una practica completa de DevOps CI/CD con una aplicacion web minima en Flask. La solucion demuestra un flujo profesional pero sencillo:

1. desarrollo local
2. pruebas automatizadas
3. construccion de imagen Docker
4. publicacion de imagen en Docker Hub
5. despliegue automatico en Render

## Arquitectura resumida

```text
Desarrollador
   |
   v
GitHub repository
   |
   v
GitHub Actions
   |- instala dependencias
   |- ejecuta pytest
   |- construye Docker image
   |- publica en Docker Hub
   `- llama Render Deploy Hook
              |
              v
         Produccion en Render
```

## Decisiones tecnicas

### Flask

Se uso Flask porque:

- es facil de entender
- requiere pocas dependencias
- permite pruebas rapidas
- es ideal para una practica academica sin sobreingenieria

### pytest

Se eligio `pytest` por ser el estandar mas simple y claro para validar el comportamiento principal de la app.

### Docker

Se crea una imagen reproducible sobre `python:3.12-slim`, con un usuario no root y `gunicorn` para ejecucion en un entorno de produccion sencillo.

### Render

Se usa Render por su facilidad de configuracion y porque permite activar despliegues mediante deploy hook, lo que encaja muy bien con GitHub Actions.

## Checklist de entrega

- [x] aplicacion web Hola Mundo
- [x] prueba unitaria
- [x] Dockerfile
- [x] workflow de GitHub Actions
- [x] README principal
- [x] carpeta de evidencias
- [x] instrucciones de despliegue

## Pasos manuales obligatorios antes de presentar

### 1. Crear el repositorio remoto en GitHub

- crear un repositorio nuevo
- subir este contenido
- verificar que la rama principal sea `main`

### 2. Crear el repositorio en Docker Hub

- nombre sugerido: `devops_ci-cd`
- mantenerlo en minusculas

### 3. Configurar secretos en GitHub

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
- `DOCKERHUB_REPOSITORY`
- `RENDER_DEPLOY_HOOK_URL`

Valores recomendados para este proyecto:

- `DOCKERHUB_USERNAME=davidcx8`
- `DOCKERHUB_REPOSITORY=devops_ci-cd`

### 4. Configurar el servicio en Render

- crear un Web Service basado en imagen
- apuntar a `docker.io/<usuario>/<repositorio>:latest`
- copiar el deploy hook
- pegarlo en GitHub como secreto

## Guion breve para la sustentacion oral

1. Explicar el objetivo: automatizar build, test, empaquetado y despliegue.
2. Mostrar la ruta `/` y el endpoint `/health`.
3. Ejecutar `pytest -q`.
4. Mostrar el `Dockerfile` y explicar por que se usa `python:3.12-slim`.
5. Mostrar el workflow y explicar el orden de CI/CD.
6. Mostrar Docker Hub con la imagen publicada.
7. Mostrar Render en produccion.

## Que evidencia debe verse clara

- que el repositorio existe
- que las pruebas pasan
- que Docker construye sin errores
- que GitHub Actions corre
- que Docker Hub recibe la imagen
- que la app esta desplegada y responde
