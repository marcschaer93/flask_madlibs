from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from stories import story
from own_stories import stories

from random import randint, choice, sample


app = Flask(__name__)

app.config['SECRET_KEY'] = 'hyptoKrypto'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

# @app.route('/', methods=['GET', 'POST'])
# def generate_questions():
#     """Generate and shows Questions"""
#     if request.method == 'POST':
#         # Handle form submission here
#         text = story.generate(request.args)
#         return render_template('story.html', text=text)
#     else:
#         # Display the form
#             prompts = story.prompts
#             return render_template("home.html", prompts=prompts)

# @app.route('/')
# def generate_questions():
#     """Generate and shows Questions"""
#         # Display the form
#     prompts = story.prompts
#     return render_template("home.html", prompts=prompts)

@app.route('/')
def generate_questions():
    """Show storylist as a dropdown menu."""
    return render_template ('select_story.html', stories = stories.values())

# @app.route('/story')
# def generate_story():
#     """Generate and shows Story"""
#     text = story.generate(request.args)
#     return render_template('story.html', text=text)

@app.route('/question')
def generate_question():
    story_id = request.args['story_id']
    story = stories[story_id]

    prompts = story.prompts

    return render_template('question.html', story_id=story_id, prompts=prompts, title=story.title)

@app.route('/story')
def generate_story():
    """Generate and shows Story"""

    story_id = request.args['story_id']
    story = stories[story_id]

    text = story.generate(request.args)

    return render_template('story.html', title=story.title, text=text)



# @app.route('/hello')
# def say_hello():
#     return render_template('hello.html')


# @app.route('/old-home-page')
# def redirect_to_home():
#     """Redirects to new home page"""
#     return redirect('/')

# @app.route('/form')
# def show_form():
#     return render_template('form.html')

# @app.route('/form-2')
# def show_form_2():
#     return render_template('form_2.html')



# COMPLIMENTS = ['cool', 'lame', 'awesome']

# @app.route('/greet')
# def get_greeting():
#     username = request.args['username']
#     nice_thing = choice(COMPLIMENTS)
#     return render_template('greet.html', username=username, compliment=nice_thing)

# @app.route('/greet-2')
# def get_greeting_2():
#     username = request.args['username']
#     wants = request.args.get('wants_compliments')
#     nice_things = sample(COMPLIMENTS, 2)
#     return render_template('greet_2.html', wants_compliments=wants, compliments=nice_things, username=username)


# @app.route('/spell/<word>')
# def spell_word(word):
#     caps_word = word.upper()
#     return render_template('spell_word.html', word=caps_word)

# @app.route('/lucky')
# def lucky_number():
#     num = randint(1,100)
#     greeting1 = 'Hello first part'
#     return render_template('lucky.html', lucky_num=num, msg=greeting1)

# @app.route('/goodbye')
# def say_goodbye():
#     return "GOOD BYE"


# @app.route('/search')
# def search():
#     term = request.args["term"]
#     return f"<h1>Search results For: {term}</h1>"



# @app.route("/add-comment")
# def add_comment_form():
#     """Show form for adding a comment."""

#     return """
#       <form method="POST">
#         <input type="text" placeholder="comment" name="comment">
#         <input type="text" name="username" placeholder="username" name="comment">
#         <button>Submit</button>
#       </form>
#       """


# @app.route("/add-comment", methods=["POST"])
# def add_comment():
#     """Handle adding comment."""

#     comment = request.form["comment"]
#     username = request.form["username"]

#     # TODO: save that into a database!

#     return f""""
#       <h1>SAVED YOUR COMMENT</h1>
#       <ul>
#         <li> Comment: {comment} </li>
#         <li> Username: {username} </li>
#       </ul>
#       """


