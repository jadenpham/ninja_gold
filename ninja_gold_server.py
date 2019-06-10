from flask import Flask, render_template, session, request, redirect
import random
app=Flask(__name__)
app.secret_key="keep this hidden"

@app.route('/')
def index():
    if "total_gold" not in session:
        session['total_gold']=0
    if "activities" not in session:
        session['activities']=[]    
    return render_template("index.html", gold=session['total_gold'], activities=session['activities'])

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form.get('building')=='farm':
        gold_earned= random.randrange(10,20)
        session['total_gold']+=gold_earned
        session['activities']=["You've earned "+str(gold_earned)+" gold from farm"]
    if request.form.get('building')=='cave':
        gold_earned= random.randrange(5,10)
        session['total_gold']+=gold_earned
        session['activities']=["You've earned "+str(gold_earned)+" gold from cave"]
    if request.form.get('building')=='house':
        gold_earned= random.randrange(2,5)
        session['total_gold']+=gold_earned
        session['activities']=["You've earned "+str(gold_earned)+" gold from house"]
    if request.form.get('building')=='casino':
        gold_earned=random.randrange(-50,50)
        session['total_gold']+=gold_earned
        session['activities']=["You've earned "+str(gold_earned)+" gold from casino"]
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)