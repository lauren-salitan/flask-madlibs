from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)


@app.route('/')
def index():
    """Show form to ask words for the story."""
    prompts = story.prompts
    return render_template("form.html", prompts=prompts)


@app.route('/story')
def show_story():
    """Show story result."""
    text = story.generate(request.args)
    return render_template("story.html", text=text)


if __name__ == "__main__":
    app.run(debug=True)
