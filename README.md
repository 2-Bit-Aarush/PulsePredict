# PulsePredict

**PulsePredict** is a predictive maintenance prototype designed to monitor industrial machine health and detect sustained anomalies before a failure occurs.

The goal of the project is to shift industrial systems from **reactive maintenance (fixing machines after they break)** to **proactive maintenance (detecting degradation early)**.

---

## Demo

Below is a short demonstration of the prototype dashboard:

https://github.com/2-Bit-Aarush/PulsePredict/Demo.mp4

The dashboard shows:
- Real-time monitoring of machine metrics
- Temperature trends
- Vibration patterns
- Motor current changes
- Estimated failure risk gauge
- Alert system with explanation

---

## Problem

In many factories, machines are repaired **only after failure occurs**.  
This leads to:

- Production downtime  
- Financial loss  
- Equipment damage  
- Safety risks  

However, most machine failures are **preceded by gradual changes** such as:

- Increasing vibration
- Rising temperature
- Abnormal current draw

Detecting these trends early can prevent catastrophic failures.

---

## Project Idea

PulsePredict continuously monitors machine sensor streams and detects **sustained deviations from normal behavior**.

Instead of reacting to a single spike, the system tracks **gradual degradation over time** and estimates a failure risk score.

The prototype dashboard visualizes:

- Sensor trends
- Risk estimation
- Anomaly detection alerts
- Maintenance recommendations

---

## Current Prototype

The current implementation focuses on **validating the predictive monitoring logic**.

To demonstrate the system behavior, the dashboard uses **simulated sensor streams** representing:

- Temperature
- Vibration
- Motor current

These streams include **controlled degradation patterns** to emulate real industrial scenarios such as bearing wear or motor overload.

This allows testing of:

- sustained anomaly detection
- rolling baseline comparison
- failure risk scoring

---

## Important Note

⚠️ The current dashboard uses **simulated sensor data**.

This prototype is meant to demonstrate the **predictive monitoring architecture and detection logic**.

Real hardware integration is planned in the next phase.

---

## Future Hardware Integration

The full system is intended to work with real industrial hardware such as:

- **ESP32 / microcontroller edge devices**
- **Temperature sensors**
- **Vibration sensors (accelerometers)**
- **Current sensors**

Sensor data would be transmitted using **MQTT or Kafka streaming pipelines** to the processing system.

---

## Planned Improvements

Future versions of PulsePredict will include:

- Real IoT sensor integration
- MQTT-based sensor communication
- Kafka streaming architecture
- Machine learning–based failure prediction
- LLM-powered maintenance assistant
- Historical maintenance log analysis

---

## Tech Stack

- Python
- Streamlit
- Plotly
- Pandas
- Simulated IoT data streams

---

## Repository Structure

```
PulsePredict
│
├── pulsepredict_app.py      # Streamlit monitoring dashboard
├── requirements.txt         # Python dependencies
├── demo.mp4                 # Dashboard demonstration
├── architecture.png         # System architecture diagram
│
├── presentation
│   └── PulsePredict_Presentation.pdf
│
└── docs
    └── future_hardware_plan.md
```

---

## Authors

Developed as part of a hackathon project by:

- Aarush Sharma  
- Arpit Raj  
- Sandip Pancharia  
- Keshav Nand Ray  

---

## Final Note

PulsePredict is an **early-stage prototype**, but it demonstrates the core concept of detecting machine degradation before failure.

The long-term vision is to build a **scalable predictive maintenance platform for industrial systems**.
