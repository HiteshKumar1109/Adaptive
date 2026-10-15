@echo off
title Launch Adaptive Learning System
echo ========================================================
echo   Launching Full Adaptive Learning System
echo   1. Backend (FastAPI + RAG + Learner Model): http://localhost:8000
echo   2. Frontend (React + TypeScript + Tailwind): http://localhost:5173
echo ========================================================
start "Adaptive Backend" cmd /c start_backend.bat
timeout /t 3 /nobreak >nul
start "Adaptive Frontend" cmd /c start_frontend.bat
echo System started! Opening browser in 3 seconds...
timeout /t 3 /nobreak >nul
start http://localhost:5173
