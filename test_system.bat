@echo off
title Adaptive Learning AI - System Test Suite
echo ========================================================
echo   Running Automated Test Suite for Adaptive Learning System
echo ========================================================
cd /d %~dp0
if exist adaptive-learning-main\backend (
    cd adaptive-learning-main\backend
) else (
    cd backend
)
python test_api.py
pause
