import os
from flask import Flask, request, jsonify

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

current_names =['Julia','Alice','Karim']


@app.route('/wave', methods=["GET"])
def get_wave():
    name = request.args['name']
    return f"I am waving at {name}"


@app.route('/submit', methods = ["POST"])
def post_submit():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, you sent this message:"{message}"'

@app.route('/count_vowels', methods=["POST"])
def post_count_vowels_eee():
    text = request.form.get('text', '')
    vowel_count = sum(1 for char in text if char.lower() in 'aeiou')
    return f'There are {vowel_count} vowels in "{text}"'



@app.route('/count_vowels', methods=["POST"])
def post_count_vowels_eunoia():
    text = request.form.get('text', '')
    vowel_count = sum(1 for char in text if char.lower() in 'aeiou')
    return f'There are {vowel_count} vowels in "{text}"'


@app.route('/count_vowels', methods=["POST"])
def post_count_vowels_mercurial():
    text = request.form.get('text', '')
    vowel_count = sum(1 for char in text if char.lower() in 'aeiou')
    return 'There are {vowel_count} vowels in "{text}"'

@app.route('/sort-names', methods=["POST"])
def post_sort_names_in_list_of_names():
    names = request.form.get('names', '')
    sorted_names = ','.join(sorted(names.split(',')))
    return sorted_names

@app.route('/names', methods=["GET"])
def add_name():
    new_name = request.args.get('add')
    if new_name:
        current_names.append(new_name)
    return jsonify(current_names)






# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

