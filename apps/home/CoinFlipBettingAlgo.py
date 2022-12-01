from random import randrange
import pandas as pd
import plotly.express as px
import json
from flask import Flask, render_template, request, redirect, url_for, flash,json
import plotly.graph_objects as go
import plotly
app = Flask(__name__ )
#delcare initial variables
df=pd.read_csv("roulette.csv",index_col=0)
results={}
for i,num in enumerate(df["Strait"]):
    add={}
    for col in df:
        add[col]=df[col][i]
    results[num]=add
df=pd.read_csv("betslip.csv",index_col=0)
bs={}
for col in df:
    bs[col]=df[col][0]
print(bs,results)
class Simulation:
    def __init__(self,simulations, sbr,bs,results) -> None:
        self.simulations=simulations
        self.total_bankroll=sbr
        self.results=self.run_simulation(bs,results)
    def run_simulation(self,bs,results):
        g=Game(self.total_bankroll)
        for x in range(self.simulations):
            g.game(bs,results)
        
        return g.total_bankroll,self.total_bankroll,g.histbr,g.hist_trials

class Game:
    def __init__(self,br) -> None:
        self.trials=0
        self.total_bankroll=br
        self.histbr=[]
        self.hist_trials=[]
        pass
    

    def game(self,bs,results):
        self.trials+=1
       
        self.histbr.append(self.total_bankroll)
        
        
        num=randrange(0,38,1)
        self.evaluate(num,bs,results)
    def evaluate(self,num,bs,results):
        prev_bankroll=self.total_bankroll
        res=results[num]
        for bet in bs.keys():
            try:
                strait=int(bet)
                if strait==num:
                    self.total_bankroll+=bs[bet]*35
                else:
                    self.total_bankroll-=bs[bet]

            except:
                if bet=="Black":
                    if res["Red"]==bet:
                        self.total_bankroll+=bs[bet]
                    else:
                        self.total_bankroll-=bs[bet]
                elif bet=="Red":
                    if res["Red"]==bet:
                        self.total_bankroll+=bs[bet]
                    else:
                        self.total_bankroll-=bs[bet]
                elif bet=="High":
                    if res["High"]==bet:
                        self.total_bankroll+=bs[bet]
                    else:
                        self.total_bankroll-=bs[bet]
                elif bet=="Low":
                    if res["High"]==bet:
                        self.total_bankroll+=bs[bet]
                    else:
                        self.total_bankroll-=bs[bet]
                elif bet=="Even":
                    if res["Even"]==bet:
                        self.total_bankroll+=bs[bet]
                    else:
                        self.total_bankroll-=bs[bet]
                elif bet=="Odd":
                    if res["Even"]==bet:
                        self.total_bankroll+=bs[bet]
                    else:
                        self.total_bankroll-=bs[bet]
        self.hist_trials.append(self.total_bankroll-prev_bankroll)
@app.route("/", methods=["GET"])
def run():
    sim=Simulation(10000,10000,bs,results)
    fig = go.Figure(data=go.Scatter(x=[i for i in range(len(sim.results[2]))], y=sim.results[2]))
    return render_template("index.html",graphJSON=json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder))
@app.route("/runSimulation", methods=["POST"])
def run_form():
    form = request.form
    for key in bs.keys():
        try:
            bs[key]=int(form[key])
        except:
            pass
   
    simulations=int(form["simulations"])

    sbr=int(form["sbr"])
            
    sim=Simulation(simulations,sbr,bs,results)
    fig = go.Figure(data=go.Scatter(x=[i for i in range(len(sim.results[2]))], y=sim.results[2]))
    return render_template("index.html",graphJSON=json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder))

if __name__ == '__main__':
    app.run(debug=True)#, host="0.0.0.0")
    