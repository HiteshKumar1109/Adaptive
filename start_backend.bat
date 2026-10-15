@echo off
title Adaptive Learning AI - Backend (Port 8000)
echo ========================================================
echo   Starting Adaptive Learning AI Backend (FastAPI)
echo   API running on: http://localhost:8000
echo   API Docs available at: http://localhost:8000/docs
echo ========================================================
cd /d %~dp0
if exist adaptive-learning-main\backend (
    cd adaptive-learning-main\backend
) else (
    cd backend
)
python run.py
pause
