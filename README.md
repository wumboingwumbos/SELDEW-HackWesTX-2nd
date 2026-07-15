# SELDEW Water Tracker  
### 2nd Place Overall — HackWesTX 2024

This project was built during **HackWesTX 2024** as a rapid prototype to track and visualize household water usage behavior.  
Our team earned **2nd Place Overall** for the project.

## Project Purpose

The goal of SELDEW Water Tracker is to encourage water conservation by collecting usage data and turning it into clear, actionable visualizations.  
By tracking when and where water is used, users can better understand patterns and identify opportunities to reduce waste.

## How It Works

The project has two main components:

1. **Arduino-based usage tracking (`WaterTrackerV1.ino`)**  
   - Uses an ultrasonic sensor to detect water-use sessions.
   - Generates session records that include:
     - user name
     - duration of use
     - location
     - date
   - Outputs session data through serial in CSV-style format.

2. **Python analytics + graphing (`GraphMaker.py`)**  
   - Reads usage data from `data.csv`.
   - Aggregates water usage by:
     - user over time
     - location over time
     - a specific user over time
   - Produces visual graphs using Matplotlib.

## Visual Outputs

Example generated charts:

- Water usage grouped by location  
- Water usage grouped by user  
- Water usage for a specific user  

![Water usage by location](https://github.com/wumboingwumbos/HackathonWaterTracker/blob/main/location_grouped%20(1).png)  
![Water usage by user](https://github.com/wumboingwumbos/HackathonWaterTracker/blob/main/name_grouped%20(1).png)  
![Water usage for one user](https://github.com/wumboingwumbos/HackathonWaterTracker/blob/main/specific%20user_usage%20(1).png)

## Tech Stack

- **Arduino (C/C++)**
- **Python 3**
- **Matplotlib**
- **CSV data processing**

## Hackathon Context

This was a hackathon prototype focused on speed, clarity, and impact.  
It demonstrates how low-cost sensing + simple analytics can support better daily resource habits.

---
Built for HackWesTX 2024 — **2nd Place Overall**
