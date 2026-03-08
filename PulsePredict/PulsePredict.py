import streamlit as st
import random
import pandas as pd
import plotly.graph_objects as go
from collections import deque
import time

st.set_page_config(page_title="PulsePredict Factory Monitor", layout="wide")

st.title("PulsePredict - Simulation Run")

WINDOW_SIZE = 20
ABNORMAL_DURATION_REQUIRED = 5

machines = {
    "Machine A": {"base_temp": 65, "base_vib": 1.0, "base_current": 8},
    "Machine B": {"base_temp": 60, "base_vib": 0.8, "base_current": 7},
    "Machine C": {"base_temp": 70, "base_vib": 1.2, "base_current": 9},
}

if "machine_state" not in st.session_state:
    st.session_state.machine_state = {}

if "time_step" not in st.session_state:
    st.session_state.time_step = 0

for name in machines:
    if name not in st.session_state.machine_state:
        st.session_state.machine_state[name] = {
            "data": pd.DataFrame(columns=["Time","Temperature","Vibration","Current"]),
            "temp_window": deque(maxlen=WINDOW_SIZE),
            "vib_window": deque(maxlen=WINDOW_SIZE),
            "current_window": deque(maxlen=WINDOW_SIZE),
            "abnormal_counter": 0
        }

def create_gauge(value):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': "Failure Risk (%)"},
        gauge={
            'axis': {'range': [0,100]},
            'bar': {'color': "red"},
            'steps': [
                {'range':[0,40],'color':"green"},
                {'range':[40,70],'color':"yellow"},
                {'range':[70,100],'color':"red"}
            ]
        }
    ))
    return fig

t = st.session_state.time_step

for name, config in machines.items():

    st.subheader(name)

    state = st.session_state.machine_state[name]

    # Generate sensor values
    temp = config["base_temp"] + random.uniform(-1,1)
    vibration = config["base_vib"] + random.uniform(-0.1,0.1)
    current = config["base_current"] + random.uniform(-0.5,0.5)

    # Gradual degradation after 20 seconds
    if t > 20:
        temp += (t - 20) * 0.15
        vibration += (t - 20) * 0.05
        current += (t - 20) * 0.1

    # Save data
    new_row = {
        "Time": t,
        "Temperature": temp,
        "Vibration": vibration,
        "Current": current
    }

    state["data"] = pd.concat(
        [state["data"], pd.DataFrame([new_row])],
        ignore_index=True
    ).tail(100)

    state["temp_window"].append(temp)
    state["vib_window"].append(vibration)
    state["current_window"].append(current)

    # Plot graphs
    col1, col2, col3 = st.columns(3)

    col1.line_chart(state["data"].set_index("Time")["Temperature"])
    col2.line_chart(state["data"].set_index("Time")["Vibration"])
    col3.line_chart(state["data"].set_index("Time")["Current"])

    failure_prob = 0

    if len(state["temp_window"]) == WINDOW_SIZE:

        avg_temp = sum(state["temp_window"]) / WINDOW_SIZE
        avg_vib = sum(state["vib_window"]) / WINDOW_SIZE
        avg_current = sum(state["current_window"]) / WINDOW_SIZE

        temp_dev = temp - avg_temp
        vib_dev = vibration - avg_vib
        current_dev = current - avg_current

        # Progressive scoring
        if temp > 75 or temp_dev > 3:
            failure_prob += 20

        if vibration > 1.8 or vib_dev > 0.3:
            failure_prob += 25

        if current > 11 or current_dev > 0.7:
            failure_prob += 25

        if temp > 85:
            failure_prob += 20

        failure_prob = min(failure_prob, 100)

        if failure_prob > 50:
            state["abnormal_counter"] += 1
        else:
            state["abnormal_counter"] = 0

    # Gauge
    st.plotly_chart(create_gauge(failure_prob),
                    use_container_width=True,
                    key=name)

    # Alerts
    if state["abnormal_counter"] >= ABNORMAL_DURATION_REQUIRED:
        st.error("🚨 HIGH FAILURE RISK - Maintenance Required")

        explanation = "AI Insight: "

        if vibration > 1.8:
            explanation += "Excessive vibration detected. "
        if temp > 75:
            explanation += "Overheating observed. "
        if current > 11:
            explanation += "Motor overload observed. "

        explanation += "Immediate inspection recommended."

        st.warning(explanation)
    else:
        st.success(f"System Stable | Risk: {failure_prob}%")

st.session_state.time_step += 1
time.sleep(1)
st.rerun()