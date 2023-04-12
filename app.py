from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_from_docker():
    return """
    <br>
    <br>
    <h1 style="text-align:center">
        Hello from a Docker container 🐳 🐋!
    </h1>
        <h3 style="text-align:center">
            I'm a Flask app, running in a container on port 5000, but you can't reach me there.
        </h3>
        <h3 style="text-align:center">
            I'm behind another, Nginx container which is my reverse proxy. You're currently on port 80.
        </h3>
    """

# This is a commit, you know.
# Hello, Jenkins

if __name__ == "__main__":
    app.run('0.0.0.0')
