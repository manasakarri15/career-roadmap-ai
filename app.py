from flask import Flask, render_template, request
from google import genai

app = Flask(__name__)

# Gemini Client
client = genai.Client(api_key="AIzaSyCox7vYwFy85pkXPJPvHY3VB0ZjmwzAx4A")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():

    skill = request.form["skill"]
    goal = request.form["goal"]

    prompt = f"""
    Create a detailed career roadmap.

    Skill: {skill}
    Career Goal: {goal}

    Include:
    - Skills to learn
    - Projects to build
    - Certifications
    - Interview preparation
    - Internship guidance
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    roadmap = response.text

    return f"""
    <html>

    <head>
        <title>AI Roadmap</title>

        <style>
            body{{
                font-family:Arial;
                background:#0f172a;
                color:white;
                padding:40px;
            }}

            .box{{
                background:#1e293b;
                padding:30px;
                border-radius:15px;
            }}

            a{{
                color:#38bdf8;
                text-decoration:none;
            }}
        </style>

    </head>

    <body>

        <h1>AI Career Roadmap 🚀</h1>

        <div class="box">

            <pre style="white-space: pre-wrap;">{roadmap}</pre>

        </div>

        <br>

        <a href="/">← Go Back</a>

    </body>

    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)