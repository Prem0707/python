from app import app
from flask import render_template, request, redirect
from app.models import demo
import logging

@app.route('/')
def index():
    todos = demo.objects.all()
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST', ])
def add():
    content = request.form.get("content")
    todo = demo(content=content)
    todo.save()
    return redirect('/')



@app.route('/done/<string:todo_id>')
def done(todo_id):
    todo = demo.objects.get_or_404(id = todo_id)
    todo.status = 1
    todo.save()
    return redirect('/')

@app.route('/undone/<string:todo_id>')
def undone(todo_id):
    todo = demo.objects.get_or_404(id=todo_id)
    todo.status = 0
    todo.save()
    return redirect('/')

@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    todo = demo.objects.get_or_404(id=todo_id)
    todo.delete()
    return redirect('/')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404
