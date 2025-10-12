from django.contrib import admin
from .models import ExcelFile

# Register your models here.

@admin.register(ExcelFile)
class ExcelFileAdmin(admin.ModelAdmin):
    """
    Admin interface for ExcelFile model.
    This allows viewing uploaded files in the Django admin panel.
    """
    list_display = ['original_filename', 'file_size', 'uploaded_at']
    list_filter = ['uploaded_at']
    search_fields = ['original_filename']
    readonly_fields = ['original_filename', 'file_size', 'uploaded_at']
    
    def has_add_permission(self, request):
        # Disable adding files through admin (use upload form instead)
        return False
