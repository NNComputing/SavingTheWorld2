from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# configure the database connection
db = sqlite3.connect(data.db)
  host="localhost",
  user="teacher",
  password="password",
  database="Homework"
)

# create a cursor object for executing SQL statements
cursor = db.cursor()

# define a route for the form
@app.route('/form', methods=['POST'])
def form():
    # get the form data
    Class = request.form['Class']
    duedate = request.form['duedate']
    homework = request.form['homework']

    # store the data in the database
    cursor.execute("INSERT INTO messages (class, duedate, homework) VALUES (class, duedate, homework)", (Class, duedate, homework))
    db.commit()

    # return a response to the user
    return 'Successfully assigned'

# define a route for displaying the messages
@app.route('/homework')
def homework():
    # retrieve the messages from the database
    cursor.execute("SELECT * FROM homework")
    homework = cursor.fetchall('homework')

    # display the responses in the HTML page
    return render_template('result.html', result=result)

if __name__ == '__main__':
  
    app.run(debug='true', host='0.0.0.0')
