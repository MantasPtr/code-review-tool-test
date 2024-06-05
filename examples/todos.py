from flask import Flask, request, redirect, url_for

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    todo_list_items = ''.join(
        f'<li>{todo["title"]}</li>' for todo in todos
    )
    index_html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>To-Do List</title>
    </head>
    <body>
        <h1>To-Do Items</h1>
        <ul>
            {todo_list_items}
        </ul>
        <a href="/new_todo">Create New To-Do Item</a>
    </body>
    </html>
    '''
    return index_html

@app.route('/new_todo', methods=['GET', 'POST'])
def new_todo():
    if request.method == 'POST':
        title = request.form['title']
        todos.append({'title': title})
        return redirect(url_for('index'))

    new_todo_html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Create New To-Do Item</title>
    </head>
    <body>
        <h1>Create New To-Do Item</h1>
        <form action="/new_todo" method="post">
            <label for="title">Title</label>
            <input type="text" id="title" name="title" required>
            <br>
            <button type="submit">Create To-Do Item</button>
        </form>
        <a href="/">Back to To-Do Items</a>
    </body>
    </html>
    '''
    return new_todo_html

if __name__ == '__main__':
    app.run(debug=False)
