#pylint:disable=print-statement


from flask import Flask, render_template, request, redirect, session
import random,math
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
# our index route will handle rendering our form
@app.route('/')
def index():
    setstats()
    print session['Win']
    print session['Lose']
    print session['Tie']
    return render_template("rps.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/rock')
def rock():
    print "Threw rock"
    choice = setpick()
    result = ""
    if(choice == "Scissors"):
        result = 'Win'
    elif(choice == "Rock"):
        result = 'Tie'
    else:
        result = 'Lose'
    session[result] += 1
    session['Message'] = "The computer picked "+choice+" and you picked rock, you "+result+"!"
    return redirect('/')
   
@app.route('/paper')
def paper():
    print "Threw paper"
    choice = setpick()
    result = ""
    if(choice == "Scissors"):
        result = 'Lose'
    elif(choice == "Rock"):
        result = 'Win'
    else:
        result = 'Tie'
    session[result] += 1
    session['Message'] = "The computer picked "+choice+" and you picked paper, you "+result+"!"
    return redirect('/')



@app.route('/scissors')
def scissors():
    print "Threw scissors"
    choice = setpick()
    result = ""
    if(choice == "Scissors"):
        result = 'Tie'
    elif(choice == "Rock"):
        result = 'Lose'
    else:
        result = 'Win'
    session[result] += 1
    session['Message'] = "The computer picked "+choice+" and you picked scissors, you "+result+"!"
    return redirect('/')


def setstats():
    if "Win" in session:
        return
    else:
        session['Win'] = 0
        session['Lose'] = 0
        session['Tie'] = 0
        session['Message'] = ""
        print "Setting stats to 0!"
    
def setpick():
    num = math.floor(random.randrange(0,3))
    if(num == 0):
        choice = "Paper"
    elif(num == 1):
        choice = "Scissors"
    else:
        choice = "Rock"
    print "The computer threw",choice
    return choice
app.run(debug=True) # run our server