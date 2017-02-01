from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "keep_it_secret_keep_it_safe"

mysql = MySQLConnector(app, 'mydb')

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users_list = mysql.query_db(query)
    return render_template('index2.html', users=users_list)

@app.route('/users/create', methods=['POST'])
def create():
    # let's hang onto the two inputs from the form
    name = request.form['name']
    email = request.form['email']
    # write query first (insert)
    query = "INSERT INTO users (name, email, created_at, updated_at) VALUES (:name, :email, NOW(), NOW())"
    data = {
        'name': name,
        'email': email
    }
    # call the database (mysql)
    user_id = mysql.query_db(query, data)
    print user_id
    # redirect out
    return redirect('/')

@app.route('/users/<num>')
def show(num):
    query = "SELECT * FROM users where id= {}".format(num)
    users_list = mysql.query_db(query)
    return render_template('index3.html', users=users_list, id=num)

@app.route('/users/<num>/edit')
def edit(num):
    query = "SELECT * FROM users where id= {}".format(num)
    users_list = mysql.query_db(query)
    return render_template('index4.html', users=users_list, id=num)

@app.route('/users/<num>', methods=['POST'])
def udate(num):
    query = "update users SET name = :name, email = :email, updated_at = NOW() where id= :id "
    data = { 'name' : request.form['name'],
             'email' : request.form['email'],
             'id' : num
    }
    user_id = mysql.query_db(query, data)
    return redirect('/users/'+str(num))

@app.route('/users/<num>/destroy')
def destroy(num):
    query = "delete FROM users where id= {}".format(num)

    users_list = mysql.query_db(query)
    return redirect('/')

@app.route('/users/new')
def new():
    return render_template('index5.html')

app.run(debug=True)
