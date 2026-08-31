from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps CI/CD Project</title>
        </head>
        <body>
            <h1>Hello from my DevOps CI/CD Pipeline 🚀</h1>
            <p>Application deployed using Jenkins, Docker and AWS EC2.</p>
            <p>Version: 1.0</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "DevOps CI/CD Demo"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
