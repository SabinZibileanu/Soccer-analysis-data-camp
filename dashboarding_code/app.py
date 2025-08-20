import streamlit as st
import pandas as pd

st.title('Defensive scouting analysis report for teams')
teams_Data = pd.read_csv('data/Team_DefenseMetrics_Profiles.csv')
option = st.selectbox(
    "Select a team for which you would like to see the defensive metrics and profile",
    (teamName for teamName in teams_Data['team.name']),
)

filtered_df = teams_Data[teams_Data['team.name'] == option]
st.dataframe(filtered_df, width = 1000)
st.header('Team metrics definitions (The rates were created in comparison to the league average):')
st.subheader('total.losses: How many times did the team lose the ball across the season', divider=True)
st.subheader('total.recoveries: How many ball recoveries did the team have across the season', divider=True)
st.subheader('average.opponentOffsides: The average number of offsides that a team has caught their opponent with', divider=True)
st.subheader('ownHalfLossRate: The percentage of dangerous own half losses of a team', divider=True)
st.subheader('defensiveErrorRates: It takes into account the number of goals that a team conceded across the season reported to the number of total successful actions across the season', divider=True)
st.subheader('interceptionRecoveryRate: The percentage of ball recoveries made through interceptions only', divider=True)
st.subheader('pressingIntensityRate: How many duels were created through pressing, giving an overview of which team is a high pressure one and which team is a laid back patient one', divider=True)
st.subheader('teamProfile: Detailed team profiles based on the insights in order to see the weaknesses and the strengths of a team', divider=True)




