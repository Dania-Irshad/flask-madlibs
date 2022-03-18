from flask import Flask, render_template, request
from stories import *

app = Flask(__name__)

dict_of_stories = {}
for i in range(len(lst_of_stories)):
        dict_of_stories[[j for j in range(1, len(lst_of_stories) + 1)][i]] = lst_of_stories[i]

@app.route('/')
def home():
    """Return homepage with choices of stories."""
    story_choices = dict_of_stories.keys()
    return render_template("home.html", story_choices=story_choices)

@app.route('/prompts')
def prompts():
    """Return form with prompts."""
    story_choice = request.args["story_choice"]
    story = dict_of_stories.get(int(story_choice))
    prompts = story.prompts
    return render_template("prompts.html", prompts=prompts, story_choice=story_choice)

@app.route('/your-story')
def your_story():
    """Return resulting story from form."""
    story_choice = request.args["story_choice"]
    story = dict_of_stories.get(int(story_choice))
    new_story = story.generate(request.args)
    return render_template("your_story.html", new_story=new_story)