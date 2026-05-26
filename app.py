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
    AI Career Roadmap 🚀

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
    Apply for Internships and Jobs
    """

    return f"""
    <html>
    <body style='font-family:Arial;padding:40px;background:#f5f5f5;'>

        <h1>Career Roadmap AI 🚀</h1>

        <div style='background:white;padding:20px;border-radius:10px;'>

            <pre style='white-space: pre-wrap;'>{roadmap}</pre>

        </div>

        <br>

        <a href='/'>← Go Back</a>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)