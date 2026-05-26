from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():

    skill = request.form["skill"]
    goal = request.form["goal"]

    roadmap = f"""
🚀 Career Roadmap

Skill: {skill}
Career Goal: {goal}

Step 1:
Learn Advanced {skill}

Step 2:
Build projects related to {goal}

Step 3:
Practice DSA and Aptitude

Step 4:
Create Resume and LinkedIn

Step 5:
Practice Mock Interviews

Step 6:
Apply for internships and jobs
"""

    return f"""
    <!DOCTYPE html>

    <html>

    <head>

        <title>Career Roadmap</title>

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

            pre{{
                white-space: pre-wrap;
                font-size:16px;
                line-height:1.6;
            }}

            a{{
                color:#38bdf8;
                text-decoration:none;
                font-size:18px;
            }}

        </style>

    </head>

    <body>

        <h1>Career Roadmap AI 🚀</h1>

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
    