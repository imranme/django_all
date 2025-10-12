from django import forms
from django.core.exceptions import ValidationError
from .models import ExcelFile

class ExcelUploadForm(forms.Form):
    """
    Form for uploading three Excel files.
    This form handles the upload of exactly three Excel files at once.
    """
    
    # Three file upload fields
    file1 = forms.FileField(
        label='Excel File 1',
        help_text='Choose first Excel file (.xlsx or .xls)',
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.xlsx,.xls'
        })
    )
    
    file2 = forms.FileField(
        label='Excel File 2',
        help_text='Choose second Excel file (.xlsx or .xls)',
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.xlsx,.xls'
        })
    )
    
    file3 = forms.FileField(
        label='Excel File 3',
        help_text='Choose third Excel file (.xlsx or .xls)',
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.xlsx,.xls'
        })
    )
    
    def clean_file1(self):
        """Validate first file"""
        return self._validate_excel_file(self.cleaned_data.get('file1'), 'File 1')
    
    def clean_file2(self):
        """Validate second file"""
        return self._validate_excel_file(self.cleaned_data.get('file2'), 'File 2')
    
    def clean_file3(self):
        """Validate third file"""
        return self._validate_excel_file(self.cleaned_data.get('file3'), 'File 3')
    
    def _validate_excel_file(self, file, file_label):
        """
        Helper method to validate Excel files
        """
        if file:
            # Check file extension
            valid_extensions = ['.xlsx', '.xls']
            file_extension = '.' + file.name.split('.')[-1].lower()
            
            if file_extension not in valid_extensions:
                raise ValidationError(
                    f'{file_label} must be an Excel file (.xlsx or .xls)'
                )
            
            # Check file size (max 50MB)
            max_size = 50 * 1024 * 1024  # 50MB in bytes
            if file.size > max_size:
                raise ValidationError(
                    f'{file_label} is too large. Maximum size is 50MB.'
                )
            
            # Check if file is not empty
            if file.size == 0:
                raise ValidationError(
                    f'{file_label} is empty. Please choose a valid Excel file.'
                )
        
        return file

class SingleExcelUploadForm(forms.ModelForm):
    """
    Alternative form for uploading a single Excel file using the model
    """
    class Meta:
        model = ExcelFile
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.xlsx,.xls'
            })
        }