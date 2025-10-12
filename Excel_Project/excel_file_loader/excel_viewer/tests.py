from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
import io
import os

# Create your tests here.

class ExcelViewerTestCase(TestCase):
    """
    Test cases for the Excel Viewer application
    """
    
    def setUp(self):
        """Set up test client"""
        self.client = Client()
    
    def test_home_page(self):
        """Test home page loads correctly"""
        response = self.client.get(reverse('excel_viewer:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Excel File Viewer')
        self.assertContains(response, 'Upload and View Excel Files')
    
    def test_upload_page(self):
        """Test upload page loads correctly"""
        response = self.client.get(reverse('excel_viewer:upload'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Upload Excel Files')
        self.assertContains(response, 'Excel File 1')
        self.assertContains(response, 'Excel File 2')
        self.assertContains(response, 'Excel File 3')
    
    def test_show_data_no_session(self):
        """Test show data page redirects when no session data"""
        response = self.client.get(reverse('excel_viewer:show_data'))
        # Should redirect to upload page when no data in session
        self.assertEqual(response.status_code, 302)
    
    def test_clear_session(self):
        """Test clear session functionality"""
        # Add some data to session
        session = self.client.session
        session['excel_data'] = [{'test': 'data'}]
        session.save()
        
        # Clear session
        response = self.client.get(reverse('excel_viewer:clear_session'))
        self.assertEqual(response.status_code, 302)
        
        # Check session is cleared
        self.assertNotIn('excel_data', self.client.session)
    
    def test_upload_form_validation(self):
        """Test upload form validation"""
        # Test empty form submission
        response = self.client.post(reverse('excel_viewer:upload'), {})
        self.assertEqual(response.status_code, 200)
        # Form should have errors for missing files
        self.assertContains(response, 'This field is required')
    
    def create_test_excel_content(self):
        """Create simple Excel-like content for testing"""
        # This is a minimal test - in real testing you'd create actual Excel files
        return b'PK\x03\x04'  # Excel file magic bytes (simplified)
    
    def test_file_validation(self):
        """Test file validation"""
        # Create test files with wrong extensions
        txt_file = SimpleUploadedFile(
            "test.txt", 
            b"not excel content", 
            content_type="text/plain"
        )
        
        response = self.client.post(reverse('excel_viewer:upload'), {
            'file1': txt_file,
            'file2': txt_file,
            'file3': txt_file
        })
        
        self.assertEqual(response.status_code, 200)
        # Should contain validation errors
        self.assertContains(response, 'must be an Excel file')

class ExcelModelTestCase(TestCase):
    """
    Test cases for Excel models
    """
    
    def test_excel_file_model(self):
        """Test ExcelFile model"""
        from .models import ExcelFile
        
        # Test model creation (without actual file)
        excel_file = ExcelFile(
            original_filename='test.xlsx',
            file_size=1024
        )
        
        # Test string representation
        self.assertIn('test.xlsx', str(excel_file))
    
    def test_model_validation(self):
        """Test model field validation"""
        from .models import ExcelFile
        from django.core.exceptions import ValidationError
        
        # Test with empty filename
        excel_file = ExcelFile()
        
        # Model should require original_filename
        with self.assertRaises(ValidationError):
            excel_file.full_clean()

class ExcelFormTestCase(TestCase):
    """
    Test cases for Excel forms
    """
    
    def test_excel_upload_form(self):
        """Test ExcelUploadForm"""
        from .forms import ExcelUploadForm
        
        # Test empty form
        form = ExcelUploadForm({})
        self.assertFalse(form.is_valid())
        self.assertIn('file1', form.errors)
        self.assertIn('file2', form.errors)
        self.assertIn('file3', form.errors)
    
    def test_form_file_validation(self):
        """Test form file validation"""
        from .forms import ExcelUploadForm
        
        # Create test files
        valid_file = SimpleUploadedFile(
            "test.xlsx", 
            b"some excel content", 
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        
        invalid_file = SimpleUploadedFile(
            "test.txt", 
            b"not excel content", 
            content_type="text/plain"
        )
        
        # Test with invalid file
        form = ExcelUploadForm({}, {
            'file1': invalid_file,
            'file2': valid_file,
            'file3': valid_file
        })
        
        self.assertFalse(form.is_valid())
        self.assertIn('file1', form.errors)
