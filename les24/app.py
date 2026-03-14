from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('task')
        date = request.form.get('date')
        time = request.form.get('time')
        priority = request.form.get('priority')

        if title:
            task = {
                "id": len(tasks) + 1,
                "title": title,
                "date": date,
                "time": time,
                "priority": priority
            }

            tasks.append(task)

        return redirect(url_for('index'))

    return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:task_id>')
def delete(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for('index'))


@app.route('/clear')
def clear():
    global tasks
    tasks.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)