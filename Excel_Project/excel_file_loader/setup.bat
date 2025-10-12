@echo off
echo ====================================
echo Excel File Viewer - Django Setup
echo ====================================
echo.

echo [1/6] Creating virtual environment...
python -m venv env
if %errorlevel% neq 0 (
    echo Error: Failed to create virtual environment
    echo Please ensure Python 3.11+ is installed
    pause
    exit /b 1
)

echo [2/6] Activating virtual environment...
call env\Scripts\activate.bat

echo [3/6] Upgrading pip...
python -m pip install --upgrade pip

echo [4/6] Installing Django...
pip install Django>=5.2.7

echo [5/6] Installing Excel processing libraries...
echo Installing openpyxl...
pip install openpyxl
echo.
echo Attempting to install pandas (this may take a while or fail due to compilation requirements)...
pip install pandas
if %errorlevel% neq 0 (
    echo.
    echo WARNING: pandas installation failed.
    echo The application will work with openpyxl for basic Excel processing.
    echo You can try installing pandas manually later with:
    echo pip install pandas
    echo.
)

echo [6/6] Setting up database...
python manage.py makemigrations
python manage.py migrate

echo.
echo ====================================
echo Setup Complete!
echo ====================================
echo.
echo To start the development server:
echo 1. Activate virtual environment: env\Scripts\activate
echo 2. Run server: python manage.py runserver
echo 3. Open browser: http://127.0.0.1:8000/
echo.
echo For detailed instructions, see README.md
echo.
pause