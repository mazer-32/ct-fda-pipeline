# Notes - Day 1: Python install needed a PowerShell restart before PATH worked.
- Day 2: PowerShell blocked the venv activation script. Fixed with Set-ExecutionPolicy -Scope CurrentUser RemoteSigned.
- Day 3: Typing print(...) directly in PowerShell triggers the Windows PRN printer error. Code goes in a .py file, run with python file.py.