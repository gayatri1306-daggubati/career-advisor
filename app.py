from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Configure your Gemini API key
genai.configure(api_key="AIzaSyAXy1hretw9bWBAf87GSwrN6-hsEhyCn54")

# Use a lightweight model to avoid hitting strict quotas
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    advice = ""
    if request.method == "POST":
        prompt = request.form.get("prompt")
        if prompt:
            try:
                response = model.generate_content(prompt)
                advice = response.text
            except Exception as e:
                advice = (
                    "❌ API limit reached or error occurred.\n\n"
                    "👉 Sample Response: You can consider careers in software development, AI/ML, or cybersecurity. "
                    "Start with small certifications or internships to build your profile."
                )
        else:
            advice = "⚠️ Please enter a prompt."
    return render_template("index.html", advice=advice)

if __name__ == "__main__":
    app.run(debug=True)
