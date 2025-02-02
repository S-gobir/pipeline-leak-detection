import os

framework = os.getenv("FRAMEWORK", "fastapi").lower()

if framework == "fastapi":
    from fastapi import FastAPI
    import uvicorn

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"message": "Hello, Render!"}

    if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=8000)

elif framework == "flask":
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello, Render!"

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8000)

else:
    raise ValueError("Unsupported framework. Set the FRAMEWORK environment variable to 'fastapi' or 'flask'.")
