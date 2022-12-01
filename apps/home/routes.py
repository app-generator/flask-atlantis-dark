# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from plotly.graph_objs import *

import random
import json
import plotly
import pandas as pd
from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
import plotly.graph_objects as go

import pandas as pd
def evaluate_soft(strats,player,showing):
    print(player,showing)

    if player==[11,11]:
        player=[12]
    while player.count(11)>1 and sum(player)>21:
        for i,x in enumerate(player):
            if x==11:
                player[i]=1
                break
    if sum(player)>21 and 11 in player:
        player=list(map(lambda x: int(str(x).replace('11', '1')), player))
    #player=[sum(player)-(player.count(11)*10)]
    print(player, showing)
    
   
    if showing==11:
        showing="Ace"
    return strats[f"{showing}_{sum(player)}_Soft"]

def evaluate_hard(strats,player,showing):

    if showing==11:
        showing="Ace"
    return strats[f"{showing}_{sum(player)}_Hard"]
    
def evaluate_pair(strats,player,showing):
    if showing==11:
        showing="Ace"
    if 11 in player:
        return strats[f"{showing}_Ace_Pair"]
    else:
        return strats[f"{showing}_{player[0]}_Pair"]
class sim_game:
    def __init__(self,deck,bet,strats):
        self.player=[deck.hit()]
        self.dealer_shows=deck.hit()
        self.player.append(deck.hit())
        self.dealer_hides=deck.hit()
        self.dealer=[self.dealer_hides,self.dealer_shows]
        if 11 == self.dealer_shows:
            print("Dealer shows Ace")
        else:
            print(f"Dealer Shows {self.dealer_shows}")
        if 11 in self.player:
            if self.player==[11,11]:
                print(f"You have {self.player} for {sum(self.player)-10} or {sum(self.player) - 20}")
            else:
                print(f"You have {self.player} for {sum(self.player)} or {sum(self.player)-10}")

        else:
            print(f"You have {self.player} for {sum(self.player)}")

        if sum(self.dealer) == 21:
            if sum(self.player)==21:
                print("Push")
                self.win=0
            else:
                print("Dealer has 21")
                print("You lose")
                self.win=-bet
        elif sum(self.player)==21:
            print("You win")
            self.win=bet*1.5
        elif self.player[0] == self.player[1] and evaluate_pair(strats,self.player,self.dealer_shows) =="Y":


            self.hands=[[self.player[0]],[self.player[1]]]
            self.bets=[bet,bet]
            self.win=0

            for i ,hand in enumerate(self.hands):
                self.hands[i].append(deck.hit())
                if 11 in self.hands[i] and sum(self.hands[i])>21:
                    print(f"Hand {i+1} is {sum(self.hands[i])-10} or {sum(list(map(lambda x: int(str(x).replace('11', '1')), self.hands[i])))}")
                elif 11 in self.hands[i]:
                    print(f"Hand {i+1} is {sum(self.hands[i])} or {sum(list(map(lambda x: int(str(x).replace('11', '1')), self.hands[i])))}")

                else:
                    print(f"Hand {i+1} is {sum(self.hands[i])}")
                stay = False
                while sum(list(map(lambda x: int(str(x).replace('11', '1')), self.hands[i]))) < 21 and stay == False:
                    #hit = input("Type and Enter to hit, Enter nothing to stay")
                    if 11 in self.hands[i]:
                        eval=evaluate_soft(strats,self.hands[i],self.dealer_shows)
                    else:
                        eval=evaluate_hard(strats,self.hands[i],self.dealer_shows)

                    if eval == "S":

                        stay = True
                    elif eval.upper()=="D":
                        self.bets[i]=bet*2
                        self.hands[i].append(deck.hit())
                        print(f"Hand {i+1} is {sum(self.hands[i])}")
                        stay=True
                    else:
                        self.hands[i].append(deck.hit())
                        if 11 in self.hands[i] and sum(self.hands[i]) > 21:
                            print(
                                f"Hand {i + 1} is {sum(self.hands[i]) - (10*(self.hands[i].count(11)-1))} or {sum(list(map(lambda x: int(str(x).replace('11', '1')), self.hands[i])))}")
                        else:
                            print(f"Hand {i+1} {sum(self.hands[i])}")
                if sum(self.hands[i]) > 21 and sum(list(map(lambda x: int(str(x).replace('11', '1')), self.hands[i])))>21:
                    self.win-=self.bets[i]
                elif sum(self.hands[i])>21:
                    self.hands[i]=list(map(lambda x: int(str(x).replace('11', '1')), self.hands[i]))

            if sum(self.dealer) > 21:
                print(f"Dealer has {sum(self.hands[i]) - (10 * (self.dealer.count(11) - 1))} or {sum(list(map(lambda x: int(str(x).replace('11', '1')), self.dealer)))}")
                self.dealer=[11,1]
                while sum(self.dealer) <= 16:
                    hit=deck.hit()
                    if hit==11:

                        self.dealer.append(1)
                    else:
                        self.dealer.append(hit)
                    print(f"Dealer has {sum(self.dealer)} or {sum(self.dealer)-10}")
                if sum(self.dealer)>21 and sum(list(map(lambda x: int(str(x).replace('11', '1')), self.dealer)))<21:
                    while sum(list(map(lambda x: int(str(x).replace('11', '1')), self.dealer)))<=16:
                        hit = deck.hit()
                        if hit == 11:

                            self.dealer.append(1)
                        else:
                            self.dealer.append(hit)
                        print(f"Dealer has {sum(list(map(lambda x: int(str(x).replace('11', '1')), self.dealer)))}")


            else:
                print(f"Dealer has {sum(self.dealer)}")
            while sum(self.dealer) <= 16 or sum(list(map(lambda x: int(str(x).replace('11', '1')), self.dealer)))<=16:


                self.dealer.append(deck.hit())
                print(f"Dealer has {sum(self.dealer)}")
            for i ,hand in enumerate(self.hands):
                if sum(self.dealer) > 21:
                    print("You Win")
                    self.win+=self.bets[i]
                elif sum(self.dealer) > sum(self.hands[i]):
                    print("You lose")
                    self.win-=self.bets[i]
                elif sum(self.dealer) == sum(self.hands[i]):
                    print("Push")

        else:
            stay=False
            if self.player==[11,11]:
                self.player=[1,11]
            while sum(self.player)<=21 and stay==False:
                if 11 in self.player:
                    eval=evaluate_soft(strats,self.player,self.dealer_shows)
                else:
                    try:
                        eval=evaluate_hard(strats,self.player,self.dealer_shows)
                    except Exception as e:
                        print(dfs["Hard"])
                        eval = evaluate_hard(strats, self.player, self.dealer_shows)

                if eval=="S":
                    stay=True
                elif eval.upper()=="D":
                    if len(self.player)>2:
                        pass
                    else:
                        bet=bet*2
                        self.player.append(deck.hit())
                        print(f"You have {sum(self.player)}")

                    stay=True
                elif eval=="R":
                    self.win = -bet/2
                    break

                else:
                    hit=deck.hit()
                    if hit==11 and 11 in self.player:
                        self.player.append(1)
                    else:
                        self.player.append(hit)
                    if sum(self.player)>21 and self.player.count(11)==1 :

                        self.player = list(map(lambda x: int(str(x).replace('11', '1')), self.player))
                    print(f"You have {sum(self.player)} {self.player}")
            if sum(self.player)>21:
                print("You Lose")
                self.win= -bet
            else:
                print(f"Dealer has {sum(self.dealer)}")
                while sum(self.dealer)<=16:
                    self.dealer.append(deck.hit())
                    if sum(self.dealer)>21 and 11 in self.player:
                        self.dealer = list(map(lambda x: int(str(x).replace('11', '1')), self.dealer))
                    print(f"Dealer has {sum(self.dealer)}")
                if sum(self.dealer)>21:
                    print("You Win")
                    self.win= bet
                elif sum(self.dealer)>sum(self.player):
                    print("You lose")

                    self.win= -bet
                elif sum(self.dealer)==sum(self.player):
                    print("Push")
                    self.win= 0
                else:
                    print("You win")
                    self.win=bet
class deck:
    def __init__(self,ndecks):
        faces=[i for i in range(1,14)]
        faces[0]=11
        faces[-1]=10
        faces[-2]=10
        faces[-3]=10
        faces=faces*4
        faces=faces*ndecks
        random.shuffle(faces)
        self.next_card=0
        self.cards=faces

        #print(faces*4)
    def hit(self):
        card=self.cards[self.next_card]
        self.next_card+=1
        #print(f"Hit {card}")
        return card
class Simulation:
    def __init__(self,sbr,bet_size,n_simulations,ngame,strats,ndecks) -> None:
        self.brrs={}
        self.ebrs={}
        self.sbr=sbr
        self.bet_size=bet_size
        self.n_simulations=n_simulations
        self.brs=[]
        self.br=sbr
        self.games=0
        self.ndecks=ndecks
        self.strats=strats
        self.ngame=ngame
        self.winss={}
    def simulate(self):
        for n in range(self.n_simulations):
            self.brs=[]
            self.br=self.sbr
            self.games=0
            self.wins=[]
            
            
            cards = deck(self.ndecks)
            for nn in range(self.ngame):
                if cards.next_card>len(cards.cards)-52:
                    cards=deck(self.ndecks)
                self.games+=1
                
                win = sim_game(cards, self.bet_size,self.strats).win
                self.br += win
                print("Result: "+str(win))
                self.wins.append(win)
                self.brs.append(self.br)
                if self.br<0:
                    break
            self.brrs[str(n)]=self.brs
            self.ebrs[str(n)]=self.br
            self.winss[str(n)]=self.wins
def runsimulation(args):
    strats={}
    for key in request.form.keys():
        if "_" in key:
            strats[key]=request.form[key]
    print(strats)
    sbr=int(args["bankroll"])
    bet=int(args["betSize"])
    nsim=int(args["nSim"])
    ngame=int(args["nGame"])
    ndecks=int(args["nDecks"])
    s=Simulation(sbr,bet,nsim,ngame,strats,ndecks)
    s.simulate()
    layout = Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)')
    fig = go.Figure(layout=layout)
    i=0
    d1=[]
    for game in s.brrs.keys():
        i=0
        for win, br in zip(s.brrs[game],s.winss[game]):
            
            d2=[game,i+1,br,win]
            d1.append(d2)
            i+=1
        fig.add_trace(go.Scatter(x=[x for x in range(len(s.brrs[game]))], y=s.brrs[game],
                    mode='lines',
                    name=f"Sim #{int(game)+1}"))

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')


@blueprint.route('/<template>',methods=["POST","GET"])
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)
        print(template)
        # Serve the file (if exists) from app/templates/home/FILE.html
        
        if template == "simulate.html":
            print("callback")
            strats=pd.read_csv("bjstrat.csv")
            new_header = strats.iloc[0]  # grab the first row for the header
            df = strats[1:]  # take the data less the header row
            df.columns = new_header
            #st.write(df)
            hard=df[:18]
            #st.write(hard)
            soft_cols=df.iloc[19]
            soft=df[20:30]

            soft.columns=soft_cols
            #st.write(soft)
            split_cols = df.iloc[31]
            split = df[32:42]
            split.columns = split_cols
            #st.write(hard,soft,split)
            dfs={"Soft":soft,"Hard":hard,"Pair":split}

            for key,df in dfs.items():
                print(df.columns)
                print(df.iloc[0][-1],df.loc)
                #df=df.reset_index()

                dfs[key]=df
            all_html="<form action='/simulate' method='post'>"
            tables={}
            htmll=""
            for key in dfs.keys():
                ids=[]

                for y in dfs[key].set_index(key).index.to_list() :
                    
                    if y==key:
                        continue
                    for x in dfs[key]:
                        
                        if x==key:
                            continue
                        else:
                            ids.append(str(x)+"_"+str(y))
                #print(render_template("select.html",id=ids[0]))
                
                new=dfs[key].set_index(key).to_html(classes="table-responsive table-bordered")
                splits=new.split("<th>")
                splits[1]="Dealer Has:</th>"
                new="<th>".join(splits)
                if key!="Pair":
                    new=new.replace("<td>H</td>",render_template("inputs.html",id="aa",default="H"))
                    new=new.replace("<td>S</td>",render_template("inputs.html",id="aa",default="S"))
                    new=new.replace("<td>D</td>",render_template("inputs.html",id="aa",default="D"))
                    new=new.replace("<td>R</td>",render_template("inputs.html",id="aa",default="R"))
                else:
                    new=new.replace("<td>Y</td>",render_template("input_soft.html",id="aa",default="Y"))
                    new=new.replace("<td>N</td>",render_template("input_soft.html",id="aa",default="N"))
                #html+=new
                html=""
                splits=new.split("<select name=\"aa\" id=\"aa\" >")
                for i,x in enumerate(splits):
                    if i==len(splits)-1:
                        html+=x
                        break
                    html+=x+render_template("select.html",id=ids[i]+"_"+key)
                all_html+=html
                tables[key]=html
                htmll+=html
                
            return render_template("home/simulate.html",segment=segment,tables=tables,graphJSON=runsimulation(request.form),values=request.form)
                    
        elif template=="blackjack.html":
            
            strats=pd.read_csv("bjstrat.csv")

            #st.write(strats)
            new_header = strats.iloc[0]  # grab the first row for the header
            df = strats[1:]  # take the data less the header row
            df.columns = new_header
            #st.write(df)
            hard=df[:18]
            #st.write(hard)
            soft_cols=df.iloc[19]
            soft=df[20:30]

            soft.columns=soft_cols
            #st.write(soft)
            split_cols = df.iloc[31]
            split = df[32:42]
            split.columns = split_cols
            #st.write(hard,soft,split)
            dfs={"Soft":soft,"Hard":hard,"Pair":split}

            for key,df in dfs.items():
                print(df.columns)
                print(df.iloc[0][-1],df.loc)
                #df=df.reset_index()

                dfs[key]=df
            all_html="<form action='/simulate' method='post'>"
            tables={}
            htmll=""
            for key in dfs.keys():
                ids=[]

                for y in dfs[key].set_index(key).index.to_list() :
                    
                    if y==key:
                        continue
                    for x in dfs[key]:
                        
                        if x==key:
                            continue
                        else:
                            ids.append(str(x)+"_"+str(y))
                #print(render_template("select.html",id=ids[0]))
                
                new=dfs[key].set_index(key).to_html(classes="table-responsive table-bordered")
                splits=new.split("<th>")
                splits[1]="Dealer Has:</th>"
                new="<th>".join(splits)
                if key!="Pair":
                    new=new.replace("<td>H</td>",render_template("inputs.html",id="aa",default="H"))
                    new=new.replace("<td>S</td>",render_template("inputs.html",id="aa",default="S"))
                    new=new.replace("<td>D</td>",render_template("inputs.html",id="aa",default="D"))
                    new=new.replace("<td>R</td>",render_template("inputs.html",id="aa",default="R"))
                else:
                    new=new.replace("<td>Y</td>",render_template("input_soft.html",id="aa",default="Y"))
                    new=new.replace("<td>N</td>",render_template("input_soft.html",id="aa",default="N"))
                #html+=new
                html=""
                splits=new.split("<select name=\"aa\" id=\"aa\" >")
                for i,x in enumerate(splits):
                    if i==len(splits)-1:
                        html+=x
                        break
                    html+=x+render_template("select.html",id=ids[i]+"_"+key)
                all_html+=html
                tables[key]=html
                htmll+=html
                
            return render_template("home/blackjack.html",segment=segment,tables=tables,values=request.form)
            
        else:

            return render_template("home/" + template, segment=segment)
        

    #except TemplateNotFound:
        #return render_template('home/page-404.html'), 404

    except Exception as e:
        import sys
        import traceback
        e=traceback.format_exc().replace("\n",'<br>')
        return f"<h1>{e}</h1>"


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
