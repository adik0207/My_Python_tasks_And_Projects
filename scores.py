def bat_point(players):
    runs= players["runs"]
    fours= players['4']
    sixes= players['6']
    balls= players["balls"]

    points = runs/2
    if runs>50:
        points += 5
    if runs>100:
        points += 10
    if 80<=(runs/balls)<=100:
        points +=2
    elif (runs/balls)>100:
        points +=4
    points += fours
    points += 2*sixes
    return points

def ball_point(players):
    wickets= players["wkts"]
    runs= players["runs"]
    overs= players["overs"]
    
    points = wickets*10
    if wickets>=3:
        points += 5
    if wickets>=5:
        points += 10
    if 3.5<=(runs/overs)<=4.5:
        points +=4
    elif 2<=(runs/overs)<3.5:
        points +=7
    elif (runs/overs)<2 :
        points +=10
    return points
