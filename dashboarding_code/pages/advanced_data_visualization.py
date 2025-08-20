import pandas as pd
from matplotlib import pyplot as plt
import streamlit as st
from utils.utils import get_Turnover_Recovery_Data, matchResults, plotTeamsData, get_Loss_Recovery_Coordinates, plot_Loss_Recovery_HeatMap
import seaborn as sns

st.title('Advanced data visualization (ball recoveries, ball turnovers, heatmaps)')

teams_Data = pd.read_csv('data/Team_DefenseMetrics_Profiles.csv')
event_Data = pd.read_csv('data/Opponent_Event_Data.csv')

option = st.selectbox(
    "Select a team for which you would like to see the defensive metrics and profile",
    (teamName for teamName in teams_Data['team.name'] if teamName != 'Dinamo Bucuresti'),
)

col1, col2, col3 = st.columns(3)

with col1:
    button1 = st.button('Ball recovery actions')

with col2:
    button2 = st.button('Ball turnover actions')

with col3:
    button3 = st.button('Heatmaps loss-recovery')

if button1:
    _, opp_Recovery_Events = get_Turnover_Recovery_Data(matchResults, event_Data, option)
    fig = plotTeamsData(opp_Recovery_Events.keys(), opp_Recovery_Events.values(), f'{option} ball recovery events against Dinamo Bucuresti across all matches played', 'Ball recovery events')
    st.pyplot(fig)
    st.text(f'The events that led to ball recoveries by {option} across all the matches played against Dinamo Bucuresti last season. You can watch the plot in fullscreen for a better visualization')

if button2:
    opp_Turnover_Events, _ = get_Turnover_Recovery_Data(matchResults, event_Data, option)
    fig = plotTeamsData(opp_Turnover_Events.keys(), opp_Turnover_Events.values(), f'{option} ball turnover events against Dinamo Bucuresti across all matches played', 'Ball turnover events')
    st.pyplot(fig)
    st.text(f'The events that led to ball turnovers by {option} across all the matches played against Dinamo Bucuresti last season. You can watch the plot in fullscreen for a better visualization')

if button3:
    X_loss, Y_loss, X_recovery, Y_recovery = get_Loss_Recovery_Coordinates(option, event_Data)
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    axs[0].set_title(f'{option} ball recovery heat map')
    axs[1].set_title(f'{option} ball turnover heat map')

    plot_Loss_Recovery_HeatMap(axs[0])
    sns.kdeplot(x=X_recovery, y=Y_recovery, fill=True, n_levels=50, ax=axs[0])

    plot_Loss_Recovery_HeatMap(axs[1])
    sns.kdeplot(x=X_loss, y=Y_loss, fill=True, n_levels=50, ax=axs[1])
    plt.tight_layout()
    st.pyplot(fig)

    st.text(f'The heatmaps for every match Dinamo Bucuresti has played against {option} last season. The spotlighted blue zones represent the area where most of the actions happened. You can watch the heatmap in fullscreen for a better visualization')





