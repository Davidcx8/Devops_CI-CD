import os

from flask import Flask, jsonify, render_template_string


HOME_TEMPLATE = """
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>DevOps CI/CD Final</title>
    <style>
      :root {
        color-scheme: light;
        --bg: #f6f3ee;
        --card: #fffdf9;
        --text: #1d1d1b;
        --accent: #146356;
        --border: #d6cec1;
      }

      body {
        margin: 0;
        min-height: 100vh;
        display: grid;
        place-items: center;
        background:
          radial-gradient(circle at top left, rgba(20, 99, 86, 0.12), transparent 35%),
          linear-gradient(135deg, #f6f3ee 0%, #ece5db 100%);
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        color: var(--text);
      }

      main {
        width: min(92vw, 680px);
        padding: 2.5rem;
        border: 1px solid var(--border);
        border-radius: 24px;
        background: var(--card);
        box-shadow: 0 18px 50px rgba(29, 29, 27, 0.08);
      }

      h1 {
        margin: 0 0 0.5rem;
        font-size: clamp(2rem, 4vw, 3rem);
      }

      p {
        font-size: 1.05rem;
        line-height: 1.6;
      }

      .badge {
        display: inline-block;
        padding: 0.35rem 0.8rem;
        border-radius: 999px;
        background: rgba(20, 99, 86, 0.12);
        color: var(--accent);
        font-weight: 600;
        margin-bottom: 1rem;
      }
    </style>
  </head>
  <body>
    <main>
      <span class="badge">Practica final DevOps CI/CD</span>
      <h1>{{ message }}</h1>
      <p>
        Aplicacion web minima construida con Flask, preparada para pruebas,
        Docker, integracion continua y despliegue continuo.
      </p>
    </main>
  </body>
</html>
"""


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["APP_MESSAGE"] = os.getenv(
        "APP_MESSAGE", "Hola Mundo desde DevOps CI/CD"
    )

    @app.get("/")
    def home():
        return render_template_string(
            HOME_TEMPLATE, message=app.config["APP_MESSAGE"]
        )

    @app.get("/health")
    def health():
        return jsonify(status="ok", message=app.config["APP_MESSAGE"])

    return app


app = create_app()
