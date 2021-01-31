from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story

app = Flask(__name__)

app.config['SECRET_KEY'] = 'idkwhatever'
debug = DebugToolbarExtension(app)

@app.route('/')
def madlib_home():
    prompts = story.prompts
    return render_template('index.html', prompts=prompts)

@app.route('/story')
def madlib_story():
    responses = request.args
    newstory = story.generate(responses)
    return render_template('story.html', story=newstory)

