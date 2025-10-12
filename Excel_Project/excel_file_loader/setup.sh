#!/bin/bash

echo "===================================="
echo "Excel File Viewer - Django Setup"
echo "===================================="
echo ""

echo "[1/6] Creating virtual environment..."
python3 -m venv env
if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment"
    echo "Please ensure Python 3.11+ is installed"
    exit 1
fi

echo "[2/6] Activating virtual environment..."
source env/bin/activate

echo "[3/6] Upgrading pip..."
python -m pip install --upgrade pip

echo "[4/6] Installing Django..."
pip install "Django>=5.2.7"

echo "[5/6] Installing Excel processing libraries..."
echo "Installing openpyxl..."
pip install openpyxl

echo ""
echo "Attempting to install pandas (this may take a while or fail due to compilation requirements)..."
pip install pandas
if [ $? -ne 0 ]; then
    echo ""
    echo "WARNING: pandas installation failed."
    echo "The application will work with openpyxl for basic Excel processing."
    echo "You can try installing pandas manually later with:"
    echo "pip install pandas"
    echo ""
fi

echo "[6/6] Setting up database..."
python manage.py makemigrations
python manage.py migrate

echo ""
echo "===================================="
echo "Setup Complete!"
echo "===================================="
echo ""
echo "To start the development server:"
echo "1. Activate virtual environment: source env/bin/activate"
echo "2. Run server: python manage.py runserver"
echo "3. Open browser: http://127.0.0.1:8000/"
echo ""
echo "For detailed instructions, see README.md"
echo ""