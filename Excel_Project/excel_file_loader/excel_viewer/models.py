from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class ExcelFile(models.Model):
    """
    Model to store information about uploaded Excel files.
    This model stores metadata about the files but doesn't store the actual file content
    in the database - we'll process files in memory for security.
    """
    
    # File upload field with validation for Excel file types
    file = models.FileField(
        upload_to='excel_files/',  # Files will be stored in media/excel_files/
        validators=[FileExtensionValidator(allowed_extensions=['xlsx', 'xls'])],
        help_text="Upload Excel files (.xlsx or .xls format only)"
    )
    
    # Original filename for display purposes
    original_filename = models.CharField(max_length=255)
    
    # Timestamps for tracking when files were uploaded
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    # File size in bytes
    file_size = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-uploaded_at']  # Show newest files first
        verbose_name = "Excel File"
        verbose_name_plural = "Excel Files"
    
    def __str__(self):
        return f"{self.original_filename} (uploaded: {self.uploaded_at.strftime('%Y-%m-%d %H:%M')})"
    
    def save(self, *args, **kwargs):
        """
        Override save method to store original filename and file size
        """
        if self.file:
            self.original_filename = self.file.name
            self.file_size = self.file.size
        super().save(*args, **kwargs)
