@echo off

REM Run python code4.py
python code_4.py
if %errorlevel% neq 0 (
    echo Error: Python code4.py failed
    exit /b %errorlevel%
)

REM Run python code1.py
python code_1.py
if %errorlevel% neq 0 (
    echo Error: Python code1.py failed
    exit /b %errorlevel%
)

REM Run python code2.py
python code_2_1.py
if %errorlevel% neq 0 (
    echo Error: Python code2.py failed
    exit /b %errorlevel%
)

echo Execution completed successfully


REM Delete instagram.html and output.html
del /q instagram.html
del /q output.html
