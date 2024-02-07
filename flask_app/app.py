from flask import Flask, request

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/kill')
def killserver():
    shutdown_server()
    return 'Server shutting down...'


@app.route('/hello/<name>')
def hello_person(name: str):
    return f'Hello, {name}!'


@app.route('/recipe/<int:recipe_id>')
def get_recipe(recipe_id: int):
    # get recipe title from enum based on id
    recipe_title = {
        1: 'Pizza',
        2: 'Pasta',
        3: 'Salad',
        4: 'Burger'
    }

    #recipe = db.execute(f"SELECT * FROM recipes WHERE id = {recipe_id}")
    #return f'Recipe for a {recipe.title}!'


#recipe/1; DROP TABLE recipes;