import random
from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    print "Hello Index"
    return render_template('index.html')

@app.route('/roll', methods=["POST"])
def roll():
    print "Hello after submit"
    fname = request.form['name']
    typeofdice = int(request.form['typeofdice'])
    numberofdice = int(request.form['numberofdice'])
    diceresult=0
    result=0
    flag = 0
    for i in range(numberofdice):
        while flag is 0:
            dicetoss = random.random()
            diceresult = int(dicetoss * 10)
            if diceresult > 0 and diceresult <= typeofdice:
                flag = 1
                print diceresult
        result = result + diceresult
        flag=0
    return render_template('roll.html',name=fname, results=result, td=typeofdice, nd=numberofdice )

@app.route('/sur', methods=["POST"])
def sur():
    import re
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    nname = request.form['name']
    loc = request.form['location']
    lang = request.form['language']
    comm = request.form['comments']
    eml = request.form['email']

    if len(nname) < 1:
        flash("Name is blank,  Please Enter Name")
        return render_template('survey.html')
    if len(eml) < 1:
        flash("Email cannot be blank!")
    if not EMAIL_REGEX.match(eml):
        flash("Invalid Email Address!")
    if len(comm) < 1 or len(comm) > 120:
        flash("Comment should be less than 120 characters or cannot be blank")
        return render_template('survey.html')

    return render_template('surveyresult.html',name=nname, results=comm, language=lang, location=loc, eml=eml)


@app.route('/ninjas')
def ninjas():
    print "Hello after submit"
    return render_template('yb.html')

@app.route('/dojos/new')
def dojos():
    print "Hello after submit"
    return render_template('index.html')

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/show')
def show_user():
  return render_template('show.html', name=session['name'], email=session['email'])

@app.route('/users', methods=['POST'])
def create_user():
    import re, datetime
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    NAME_REGEX = re.compile(r'[a-zA-Z0-9]')
    NUM_REGEX = re.compile(r'\d')
    NUM_CHECK = re.compile(r'[0-9]')
    firstname = request.form['fname']
    lastname = request.form['lname']
    password =  request.form['pass']
    passwordc =  request.form['passc']
    eml = request.form['email']
    dts = date(request.form['bday'])
    flag=0
    today = datetime.date.today()


    if len(firstname) < 1 or len(lastname) < 1:
        flash("Names cannot be blank,  Please Enter Name")
        flag = 1
    if not NAME_REGEX.match(firstname):
        flash("First Name contains non-alpha characters.  Please Enter Alpha Characters only")
        flag = 1
    if not NAME_REGEX.match(lastname):
        flash("Last Name contains non-alpha characters.  Please Enter Alpha Characters only")
        flag = 1
    if len(eml) < 1:
        flash("Email cannot be blank!")
        flag = 1
    if not EMAIL_REGEX.match(eml):
       flash("Invalid Email Address!, Need atleast one number")
       flag = 1
    if not NAME_REGEX.match(password):
        flash("Invalid password!,Enter alphabets and numbers")
        flag = 1
    numcheck = NUM_REGEX.search(password)
    if numcheck is None:
        flash("Invalid password!,password needs atleast 1 number")
        flag = 1
    if len(password) < 8:
        flash("Password should be more than 8 characters")
        flag = 1
    if password != passwordc:
        flash("Password do not match, pls. renter password")
        flag = 1
    print dts
    print today
    if dts >= today:
        flash("Date must be in the past   ")
        flag = 1
    if flag == 1:
        return render_template('users.html')
    else:
        flash("Thanks for submitting your information")

    return render_template('users.html')

@app.route('/createuser')
def createuser():
    return render_template('users.html')

@app.route('/counter')
def counter():
    counter = 1
    session['counters'] =  session['counters'] + counter
    return render_template('counter.html', counterk = session['counters'])

@app.route('/up2', methods=['POST'])
def counter2():
    counter = 2
    session['counters'] =  session['counters'] + counter
    return render_template('counter.html', counterk = session['counters'])

@app.route('/reset1', methods=['POST'])
def reset1():
    session['counters'] =  1
    return render_template('counter.html', counterk = session['counters'])

@app.route('/great')
def great():
    session['randomnum'] = random.randrange(0, 101)
    return render_template('guess.html', rn = session['randomnum'])

@app.route('/ninjag')
def ninjag():
    session['visit'] = 1
    return render_template('ninja.html')

@app.route('/greatgame', methods=['POST'])
def greatgame():
    errors = []
    try:
        guessednumber = int(request.form['guess'])
    except:
        errors.append("Enter your Guess")

    if errors:
		for error in errors:
			flash(error)

		for key, value in request.form.items():
			session[key] = value
			print session[key], session
		return render_template('guess.html', rn = session['randomnum'])

    print session['randomnum']
    print session
    if guessednumber < session['randomnum']:
        session['result'] = "Too low!"
        session['color'] = "red"
    elif guessednumber > session['randomnum']:
        session['result'] = "Too high!"
        session['color'] = "red"
    elif guessednumber == session['randomnum']:
        session['result'] = str(session['randomnum']) + " was the correct number!"
        session['color'] = "green"
    return render_template('guess.html', rslt = session['result'], clr = session['color'], rn = session['randomnum'])

@app.route('/process_money', methods=['POST'])
def processmoney():

    import datetime

    checkedin = request.form['building']
    print checkedin
    winloss = 1
    ninjapot = 0
    activitiesw = []
    activitiesl = []
    msg1 =""
    msg2=""
    print "session['visit'] ----" , session['visit']
    if session['visit'] == 1:
        session['actsw'] = []
        session['actsl'] = []
        session['ninjabalance'] = 0


    if checkedin == "farm":
        ninjapot = random.randint(10, 20)
        print "farm", ninjapot
    elif checkedin == "cave":
        ninjapot = random.randint(5, 10)
        print "cave", ninjapot
    elif checkedin == "house":
        ninjapot = random.randint(2, 5)
        print "house", ninjapot
    elif checkedin == "casino" :
        ninjapot = random.randint(0, 50)
        winloss = random.randint(0,1)
        print "casino", ninjapot
    print winloss
    print ninjapot
    if winloss == 0:
        msg1 = "Entered a casino and lost " + str(ninjapot) + " golds... Ouch.. " + str(datetime.datetime.now())
        session['ninjabalance'] = session['ninjabalance'] - ninjapot
    else:
        msg2 = "Earned " + str(ninjapot) + " golds from the" + checkedin + "! " + str(datetime.datetime.now())
        session['ninjabalance'] = session['ninjabalance'] + ninjapot


    session['actsw'].insert(0,msg2)
    session['actsl'].insert(0,msg1)

    session['visit'] = session['visit'] + 1

    return render_template('ninja.html', ninjapot = ninjapot, balance = session['ninjabalance'])

app.run(debug=True)
