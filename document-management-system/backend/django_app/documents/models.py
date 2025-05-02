import os
import sys
import django

# Add the correct project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')  # Update to the correct settings module
django.setup()

from django.db import models

class OutgoingDocument(models.Model):
    document_number = models.CharField(max_length=100, unique=True)
    date_sent = models.DateField()
    recipient = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    attachment = models.FileField(upload_to='outgoing_documents/')

    def __str__(self):
        return f"{self.document_number} - {self.title}"


class IncomingDocument(models.Model):
    document_number = models.CharField(max_length=100, unique=True)
    date_received = models.DateField()
    sender = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    attachment = models.FileField(upload_to='incoming_documents/')

    def __str__(self):
        return f"{self.document_number} - {self.title}"


class Note(models.Model):
    document = models.ForeignKey(OutgoingDocument, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.document.title} - {self.created_at}"


class Metadata(models.Model):
    document = models.ForeignKey(IncomingDocument, on_delete=models.CASCADE, related_name='metadata')
    key = models.CharField(max_length=100)
    value = models.TextField()

    def __str__(self):
        return f"{self.key}: {self.value}"