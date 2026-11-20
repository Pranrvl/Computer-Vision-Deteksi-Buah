@echo off
title Frutta - Fruit Freshness AI
cd /d "%~dp0"
echo ========================================================
echo         Frutta - Fruit Freshness AI Assistant
echo ========================================================
echo Membuka aplikasi Streamlit di browser...
python -m streamlit run app.py
pause

