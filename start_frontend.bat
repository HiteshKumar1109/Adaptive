@echo off
title Adaptive Learning AI - Frontend (Port 5173)
echo ========================================================
echo   Starting Adaptive Learning AI Frontend (React + Vite)
echo   UI running on: http://localhost:5173
echo ========================================================
cd /d %~dp0
if exist adaptive-learning-main\src (
    cd adaptive-learning-main
)
npm run dev
pause
