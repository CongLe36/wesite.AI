from django.contrib import admin
from .models import Document, IncomingDocument, OutgoingDocument

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'description')

class IncomingDocumentAdmin(admin.ModelAdmin):
    list_display = ('document_number', 'sender', 'received_date')
    search_fields = ('document_number', 'sender')

class OutgoingDocumentAdmin(admin.ModelAdmin):
    list_display = ('document_number', 'recipient', 'sent_date')
    search_fields = ('document_number', 'recipient')

admin.site.register(Document, DocumentAdmin)
admin.site.register(IncomingDocument, IncomingDocumentAdmin)
admin.site.register(OutgoingDocument, OutgoingDocumentAdmin)