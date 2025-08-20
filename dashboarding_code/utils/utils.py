from matplotlib import pyplot as plt
import json
from matplotlib.patches import Arc


with open('dashboarding_code/data/matchResultsMappings.json', 'r') as matchRes_File:
    matchResults = json.load(matchRes_File)

def plotTeamsData(teams, plottingValues, plotTitle, yLabel):
    fig, ax = plt.subplots()
    ax.bar(teams, plottingValues, color='blue', width=0.5)
    plt.xticks(rotation=55, ha='right', fontsize=10)
    ax.set_title(plotTitle)
    ax.set_ylabel(yLabel)
    
    return fig

def getMatchPoints(matchResults, filtered_Event_Data):
    allPoints = []

    for results in matchResults.values():
        points_Against_Current_Team = 0

        for matchResult in results:
            matchResLoc = filtered_Event_Data.loc[filtered_Event_Data['label'] == matchResult]
            points_Against_Current_Team += int(matchResLoc['points'].iloc[0])
            continue

        allPoints.append(points_Against_Current_Team)
    
    return allPoints

def get_Turnover_Recovery_Data(matchResultData, event_Data, team):
    opponentBallTurnover_Events = {}
    opponentBallRecovery_Events = {}

    for result in matchResultData[team]:
      matchEvents = event_Data.loc[event_Data['label'] == result]

      for primaryEvent, secondaryEvents in zip(matchEvents['type.primary'], matchEvents['type.secondary']):
        if 'loss' in secondaryEvents:
          if primaryEvent not in opponentBallTurnover_Events: opponentBallTurnover_Events[primaryEvent] = 1
          else: opponentBallTurnover_Events[primaryEvent] += 1

        if 'loss' not in secondaryEvents and 'recovery' in secondaryEvents:
          if primaryEvent not in opponentBallRecovery_Events: opponentBallRecovery_Events[primaryEvent] = 1
          else: opponentBallRecovery_Events[primaryEvent] += 1
    
    return opponentBallTurnover_Events, opponentBallRecovery_Events

def get_Loss_Recovery_Coordinates(team_Name, event_Data):
    team_Events = event_Data['team.name'] == team_Name
    filtered_Events = event_Data[team_Events][['location.x', 'location.y', 'type.secondary']]
    X_loss = []
    Y_loss = []
    X_recovery = []
    Y_recovery = []

    for loc_x, loc_y, secondaryEvents in zip(filtered_Events['location.x'], filtered_Events['location.y'], filtered_Events['type.secondary']):
        if 'loss' in secondaryEvents:
            X_loss.append(loc_x)
            Y_loss.append(loc_y)

        if 'recovery' in secondaryEvents:
            X_recovery.append(loc_x)
            Y_recovery.append(loc_y)

    return X_loss, Y_loss, X_recovery, Y_recovery

def plot_Loss_Recovery_HeatMap(draw_ax):
  #Pitch Outline & Centre Line
  draw_ax.plot([0,0],[0,90], color="black")
  draw_ax.plot([0,130],[90,90], color="black")
  draw_ax.plot([130,130],[90,0], color="black")
  draw_ax.plot([130,0],[0,0], color="black")
  draw_ax.plot([65,65],[0,90], color="black")

  #Left Penalty Area
  draw_ax.plot([16.5,16.5],[65,25],color="black")
  draw_ax.plot([0,16.5],[65,65],color="black")
  draw_ax.plot([16.5,0],[25,25],color="black")

  #Right Penalty Area
  draw_ax.plot([130,113.5],[65,65],color="black")
  draw_ax.plot([113.5,113.5],[65,25],color="black")
  draw_ax.plot([113.5,130],[25,25],color="black")

  #Left 6-yard Box
  draw_ax.plot([0,5.5],[54,54],color="black")
  draw_ax.plot([5.5,5.5],[54,36],color="black")
  draw_ax.plot([5.5,0.5],[36,36],color="black")

  #Right 6-yard Box
  draw_ax.plot([130,124.5],[54,54],color="black")
  draw_ax.plot([124.5,124.5],[54,36],color="black")
  draw_ax.plot([124.5,130],[36,36],color="black")

  #Prepare Circles
  centreCircle = plt.Circle((65,45),9.15,color="black",fill=False)
  centreSpot = plt.Circle((65,45),0.8,color="black")
  leftPenSpot = plt.Circle((11,45),0.8,color="black")
  rightPenSpot = plt.Circle((119,45),0.8,color="black")

  #Draw Circles
  draw_ax.add_patch(centreCircle)
  draw_ax.add_patch(centreSpot)
  draw_ax.add_patch(leftPenSpot)
  draw_ax.add_patch(rightPenSpot)

  #Prepare Arcs
  leftArc = Arc((11,45),height=18.3,width=18.3,angle=0,theta1=310,theta2=50,color="black")
  rightArc = Arc((119,45),height=18.3,width=18.3,angle=0,theta1=130,theta2=230,color="black")

  #Draw Arcs
  draw_ax.add_patch(leftArc)
  draw_ax.add_patch(rightArc)

  #Tidy Axes
  draw_ax.axis('off')

  draw_ax.set_ylim(0, 90)
  draw_ax.set_xlim(0, 130)