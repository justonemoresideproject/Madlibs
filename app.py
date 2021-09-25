from flask import Flask, request, render_template
from random import randint, choice, sample
from stories import *

app = Flask(__name__)

story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """In a dark stormy {place}, there sleeps a
       large {adjective} {noun}. It often {verb} {plural_noun}."""
)

story3 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """In a {place}, a {adjective} {noun} sleeps tonight. In the rain it {verb} {plural_noun}."""
)

stories = {'1': story1, '2': story2, '3': story3}

@app.route('/')
def madlib_form():
    return render_template('MadlibForm.html')

@app.route('/story')
def madlib_answer():
    story = stories[request.args['story-choice']]
    place = request.args['place']
    noun = request.args['noun']
    verb = request.args['verb']
    adj = request.args['adjective']
    plural = request.args['plural']
    answers = {"place": place, 'noun': noun, 'verb': verb, 'adjective': adj, 'plural_noun': plural}

    return render_template('MadlibAnswers.html', story = story, answers = answers)