# Excel File Viewer - Django Web Application

A Django web application that allows users to upload three Excel files simultaneously and display their contents in beautiful HTML tables on a single webpage.

## Features

- ✅ **Multiple File Upload**: Upload exactly 3 Excel files at once
- ✅ **File Validation**: Supports .xlsx and .xls formats with size validation (up to 50MB each)
- ✅ **Secure Processing**: Files are processed in memory without permanent storage
- ✅ **Beautiful Display**: Data is displayed in responsive HTML tables with Bootstrap styling
- ✅ **Export Options**: Export individual tables or summary data to CSV
- ✅ **Session Management**: Data persists during your session
- ✅ **Error Handling**: Comprehensive error handling and user feedback
- ✅ **Responsive Design**: Works on desktop, tablet, and mobile devices

## Technology Stack

- **Backend**: Django 5.2.7
- **Frontend**: HTML5, CSS3, Bootstrap 5.1.3, JavaScript
- **Excel Processing**: pandas (preferred) or openpyxl (fallback)
- **Database**: SQLite (development)
- **Python**: 3.11+

## Project Structure

```
excel_file_loader/
├── excel_file_loader/          # Main Django project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Project settings
│   ├── urls.py                # Main URL configuration
│   └── wsgi.py
├── excel_viewer/              # Django app for Excel functionality
│   ├── migrations/            # Database migrations
│   ├── templates/            # HTML templates
│   │   └── excel_viewer/
│   │       ├── base.html     # Base template
│   │       ├── home.html     # Home page
│   │       ├── upload.html   # File upload page
│   │       └── show_data.html # Data display page
│   ├── __init__.py
│   ├── admin.py              # Django admin configuration
│   ├── apps.py               # App configuration
│   ├── forms.py              # Forms for file upload
│   ├── models.py             # Database models
│   ├── tests.py              # Unit tests
│   ├── urls.py               # App URL patterns
│   └── views.py              # View functions
├── media/                     # Media files directory
├── db.sqlite3                # SQLite database
└── manage.py                 # Django management script
```

## Installation & Setup

### Prerequisites

- Python 3.11 or higher
- Virtual environment (recommended)

### Step 1: Clone and Setup Virtual Environment

```bash
cd "your_project_directory"
python -m venv env

# Activate virtual environment
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install django pandas openpyxl
```

**Note**: If you encounter issues installing pandas (due to compilation requirements), you can use the application with openpyxl only, which provides basic Excel processing functionality.

### Step 3: Database Setup

```bash
cd excel_file_loader
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Create Admin User (Optional)

```bash
python manage.py createsuperuser
```

### Step 5: Run the Development Server

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## Usage Instructions

### 1. Home Page
- Visit `http://127.0.0.1:8000/` to see the home page
- Learn about the application features
- Navigate to upload or view data

### 2. Upload Excel Files
- Click "Start Uploading Files" or visit `/upload/`
- Select three Excel files (.xlsx or .xls format)
- Files are validated for format and size
- Click "Upload and Process Files"

### 3. View Data
- After successful upload, you're redirected to the data display page
- View all three files' data in organized tables
- See file information (size, rows, columns)
- Export individual tables or summary data

### 4. Additional Features
- **Toggle Visibility**: Hide/show individual tables
- **Export to CSV**: Download tables as CSV files
- **Print**: Print-friendly page formatting
- **Session Management**: Data persists during your session
- **Clear Data**: Start fresh with new uploads

## File Requirements

- **Formats**: Excel files (.xlsx or .xls)
- **Size Limit**: 50MB per file
- **Quantity**: Exactly 3 files required
- **Content**: Files must not be empty

## Security Features

- Files are processed in memory only
- No permanent file storage on server
- File extension and size validation
- CSRF protection on all forms
- Session-based data management

## Error Handling

The application handles various error scenarios:
- Invalid file formats
- File size exceeded
- Empty files
- Corrupted Excel files
- Missing dependencies
- Session timeout

## Customization

### Adding More File Slots
To support more than 3 files, modify:
1. `forms.py` - Add more file fields
2. `views.py` - Update file processing loop
3. `upload.html` - Add more file input fields

### Changing File Size Limits
Update in `settings.py`:
```python
FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50MB in bytes
DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800
```

### Database Storage
To store files in database instead of session:
1. Update `models.py` to include file content
2. Modify `views.py` to save/retrieve from database
3. Update templates to work with database queries

## Development

### Running Tests
```bash
python manage.py test
```

### Debug Mode
Debug mode is enabled by default in `settings.py`:
```python
DEBUG = True
```

### Admin Interface
Access Django admin at: `http://127.0.0.1:8000/admin/`
- View uploaded file metadata
- Manage application data

## Troubleshooting

### pandas Installation Issues
If pandas fails to install due to compilation issues:
1. The app will automatically fall back to openpyxl
2. Basic Excel processing will still work
3. Try installing pre-compiled wheels:
   ```bash
   pip install --only-binary=all pandas
   ```

### Media Files Not Serving
Ensure `MEDIA_URL` and `MEDIA_ROOT` are configured in `settings.py` and URLs include media serving in development.

### Session Data Lost
Session data is stored in memory and will be lost when:
- Server restarts
- Session expires
- Browser cookies are cleared

## Production Deployment

For production deployment:
1. Set `DEBUG = False` in settings.py
2. Configure proper database (PostgreSQL, MySQL)
3. Set up static file serving
4. Configure media file serving
5. Use production WSGI server (Gunicorn, uWSGI)
6. Set up proper security settings

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For issues, questions, or contributions, please refer to the project documentation or create an issue in the repository.