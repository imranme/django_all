from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
import os
import io
from .forms import ExcelUploadForm
from .models import ExcelFile

# Try to import pandas, but provide fallback if not available
try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    
# Try to import openpyxl as fallback
try:
    import openpyxl
    OPENPYXL_AVAILABLE = True
except ImportError:
    OPENPYXL_AVAILABLE = False

# Create your views here.

def upload_excel_files(request):
    """
    View to handle the upload of three Excel files.
    This view shows the upload form and processes the uploaded files.
    """
    # Check if pandas is available
    if not PANDAS_AVAILABLE and not OPENPYXL_AVAILABLE:
        messages.error(
            request, 
            'Excel processing libraries (pandas and openpyxl) are not installed. '
            'Please install them using: pip install pandas openpyxl'
        )
        return render(request, 'excel_viewer/upload.html', {
            'form': ExcelUploadForm(),
            'page_title': 'Upload Excel Files - Setup Required'
        })
    
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Get the uploaded files
            files = [
                request.FILES['file1'],
                request.FILES['file2'],
                request.FILES['file3']
            ]
            
            # Process all three files and store their data in session
            excel_data = []
            
            try:
                for i, uploaded_file in enumerate(files, 1):
                    if PANDAS_AVAILABLE:
                        # Use pandas for processing (preferred method)
                        file_content = uploaded_file.read()
                        excel_buffer = io.BytesIO(file_content)
                        df = pd.read_excel(excel_buffer, engine='openpyxl')
                        
                        # Convert DataFrame to HTML table for display
                        html_table = df.to_html(
                            classes='table table-striped table-bordered table-hover',
                            table_id=f'excel-table-{i}',
                            escape=False,
                            index=False
                        )
                        
                        # Store file information and data
                        file_info = {
                            'filename': uploaded_file.name,
                            'size': uploaded_file.size,
                            'rows': len(df),
                            'columns': len(df.columns),
                            'column_names': list(df.columns),
                            'html_table': html_table,
                            'file_number': i
                        }
                        
                    elif OPENPYXL_AVAILABLE:
                        # Fallback to openpyxl only (basic processing)
                        file_content = uploaded_file.read()
                        excel_buffer = io.BytesIO(file_content)
                        
                        # Load workbook with openpyxl
                        wb = openpyxl.load_workbook(excel_buffer)
                        ws = wb.active
                        
                        # Get data from worksheet
                        data = []
                        headers = []
                        
                        for row_num, row in enumerate(ws.iter_rows(values_only=True), 1):
                            if row_num == 1:
                                headers = [str(cell) if cell is not None else f'Column{i}' 
                                         for i, cell in enumerate(row, 1)]
                            else:
                                data.append([str(cell) if cell is not None else '' 
                                           for cell in row])
                        
                        # Create HTML table manually
                        html_table = f'<table class="table table-striped table-bordered table-hover" id="excel-table-{i}">'
                        html_table += '<thead><tr>'
                        for header in headers:
                            html_table += f'<th>{header}</th>'
                        html_table += '</tr></thead><tbody>'
                        
                        for row in data:
                            html_table += '<tr>'
                            for cell in row:
                                html_table += f'<td>{cell}</td>'
                            html_table += '</tr>'
                        html_table += '</tbody></table>'
                        
                        # Store file information and data
                        file_info = {
                            'filename': uploaded_file.name,
                            'size': uploaded_file.size,
                            'rows': len(data),
                            'columns': len(headers),
                            'column_names': headers,
                            'html_table': html_table,
                            'file_number': i
                        }
                    else:
                        # Neither library available
                        raise Exception("No Excel processing library available")
                    
                    excel_data.append(file_info)
                    wb.close() if 'wb' in locals() else None  # Clean up workbook
                
                # Store data in session for display
                request.session['excel_data'] = excel_data
                
                # Add success message
                messages.success(
                    request, 
                    f'Successfully uploaded and processed {len(files)} Excel files!'
                )
                
                # Redirect to display page
                return redirect('excel_viewer:show_data')
                
            except Exception as e:
                # Handle errors in file processing
                messages.error(
                    request, 
                    f'Error processing Excel files: {str(e)}'
                )
        else:
            # Form validation failed
            messages.error(
                request, 
                'Please correct the errors below and try again.'
            )
    else:
        # GET request - show empty form
        form = ExcelUploadForm()
    
    context = {
        'form': form,
        'page_title': 'Upload Excel Files',
        'pandas_available': PANDAS_AVAILABLE,
        'openpyxl_available': OPENPYXL_AVAILABLE
    }
    
    return render(request, 'excel_viewer/upload.html', context)

def show_excel_data(request):
    """
    View to display the data from the uploaded Excel files.
    This view retrieves the processed data from the session and displays it.
    """
    # Get data from session
    excel_data = request.session.get('excel_data', [])
    
    if not excel_data:
        # No data in session - redirect to upload page
        messages.warning(
            request, 
            'No Excel data found. Please upload files first.'
        )
        return redirect('excel_viewer:upload')
    
    context = {
        'excel_data': excel_data,
        'page_title': 'Excel Data Display',
        'total_files': len(excel_data)
    }
    
    return render(request, 'excel_viewer/show_data.html', context)

def clear_session_data(request):
    """
    View to clear the Excel data from session.
    This allows users to start fresh with new uploads.
    """
    if 'excel_data' in request.session:
        del request.session['excel_data']
    
    messages.info(request, 'Session data cleared. You can now upload new files.')
    return redirect('excel_viewer:upload')

def home_view(request):
    """
    Simple home page view that explains the application.
    """
    context = {
        'page_title': 'Excel File Viewer - Home'
    }
    return render(request, 'excel_viewer/home.html', context)
