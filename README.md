# 🏥 Hospital OpenEnv AI

## Overview
This project simulates real-world hospital workflows using an OpenEnv-compatible environment.

It includes tasks like:
- Patient triage
- Medical report correction
- Data cleaning

## Tasks

### 1. Patient Triage (Easy)
Classify urgency based on symptoms.

### 2. Medical Report Review (Medium)
Correct errors in clinical text.

### 3. Data Cleaning (Hard)
Remove duplicates and handle missing values.

## OpenEnv Compliance
- step(action) → (observation, reward, done, info)
- reset()
- state()
- Pydantic models for structured interaction

## Setup

pip install -r requirements.txt

## Run

python scripts/run_inference.py

## Docker

docker build -t hospital-env .
docker run hospital-env

## Why This Matters
Hospitals face challenges like patient overload and data inconsistency.
This environment enables AI agents to learn real-world decision-making workflows.