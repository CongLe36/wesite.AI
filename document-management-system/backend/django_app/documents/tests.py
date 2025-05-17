import os
import sys

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from django.test import TestCase
from .models import OutgoingDocument

class OutgoingDocumentModelTest(TestCase):
    def setUp(self):
        OutgoingDocument.objects.create(
            document_number="DOC001",
            date_sent="2023-10-01",
            recipient="Test Recipient",
            title="Test Document",
            attachment="test_attachment.pdf"
        )

    def test_document_creation(self):
        document = OutgoingDocument.objects.get(document_number="DOC001")
        self.assertEqual(document.title, "Test Document")
        self.assertEqual(document.recipient, "Test Recipient")

    def test_document_str(self):
        document = OutgoingDocument.objects.get(document_number="DOC001")
        self.assertEqual(str(document), "DOC001 - Test Document")
