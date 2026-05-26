from flask import Flask, render_template, request
from google import genai

app = Flask(__name__)

# Gemini API Client
client = genai.Client(
    api_key="AIzaSyCox7vYwFy85pkXPJPvHY3VB0ZjmwzAx4A"
)

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
    1. Skills to learn
    2. Projects to build
    3. Certifications
    4. Interview preparation
    5. Internship guidance

    Give step-by-step roadmap.
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    roadmap = response.text

    return f"""
    <!DOCTYPE html>

    <html>

    <head>

        <title>AI Career Roadmap</title>

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
                box-shadow:0px 0px 20px rgba(0,0,0,0.5);
            }}

            h1{{
                color:#38bdf8;
            }}

            a{{
                color:#38bdf8;
                text-decoration:none;
                font-size:18px;
            }}

            pre{{
                white-space: pre-wrap;
                font-size:16px;
                line-height:1.6;
            }}

        </style>

    </head>

    <body>

        <h1>AI Career Roadmap 🚀</h1>

        <div class="box">

            <pre>{roadmap}</pre>

        </div>

        <br>

        <a href="/">← Go Back</a>

    </body>

    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)