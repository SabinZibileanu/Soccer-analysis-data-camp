import streamlit as st
import pandas as pd
from utils.utils import plotTeamsData, getMatchPoints, matchResults
import os

event_Data = pd.read_csv(os.path.join('data, Opponent_Event_Data.csv'))
teams_Data = pd.read_csv(os.path.join('data, Team_DefenseMetrics_Profiles.csv'))
Dinamo_Team_Points = getMatchPoints(matchResults, event_Data)

st.title('Data visualization (team points against every opponent, metrics)')
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    button1 = st.button('Dinamo Bucuresti points')

with col2:
    button2 = st.button('Own half loss rates')

with col3:
    button3 = st.button('Defensive error rates')

with col4:
    button4 = st.button('Intercept recovery rates')

with col5:
    button5 = st.button('Pressing intensity rates')


if button1:
    fig = plotTeamsData(matchResults.keys(), Dinamo_Team_Points, 'Dinamo Bucuresti points against each team in the league', 'Points')
    st.pyplot(fig)
if button2:
    fig = plotTeamsData(teams_Data['team.name'], teams_Data['ownHalfLossRate'], 'Own half loss rate per team', 'Own half loss rates (%)')
    st.pyplot(fig)

if button3:
    fig = plotTeamsData(teams_Data['team.name'], teams_Data['defensiveErrorRates'], 'Defensive error rate per team', 'Defensive error rates (%)')
    st.pyplot(fig)

if button4:
    fig = plotTeamsData(teams_Data['team.name'], teams_Data['interceptionRecoveryRate'], 'Interception recovery rate per team', 'Interception recovery rates(%)')
    st.pyplot(fig)

if button5:
    fig = plotTeamsData(teams_Data['team.name'], teams_Data['pressingIntensityRate'], 'Pressing intensity rate per team', 'Pressing intensity rate(%)')
    st.pyplot(fig)


    
