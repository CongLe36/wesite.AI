import os
import sys
import django

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.settings')
django.setup()

from django.shortcuts import render
from django.http import JsonResponse
from .models import OutgoingDocument, IncomingDocument  # revert to relative import
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_outgoing_document(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        document = OutgoingDocument.objects.create(
            title=data['title'],
            recipient=data['recipient'],
            date_sent=data['date_sent'],
            file=data['file']
        )
        return JsonResponse({'id': document.id}, status=201)

@csrf_exempt
def create_incoming_document(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        document = IncomingDocument.objects.create(
            title=data['title'],
            sender=data['sender'],
            date_received=data['date_received'],
            file=data['file']
        )
        return JsonResponse({'id': document.id}, status=201)

def list_outgoing_documents(request):
    documents = OutgoingDocument.objects.all().values()
    return JsonResponse(list(documents), safe=False)

def list_incoming_documents(request):
    documents = IncomingDocument.objects.all().values()
    return JsonResponse(list(documents), safe=False)

def get_outgoing_document(request, document_id):
    try:
        document = OutgoingDocument.objects.get(id=document_id)
        return JsonResponse({
            'id': document.id,
            'title': document.title,
            'recipient': document.recipient,
            'date_sent': document.date_sent,
            'file': document.file.url
        })  
    except OutgoingDocument.DoesNotExist:
        return JsonResponse({'error': 'Document not found'}, status=404)

def get_incoming_document(request, document_id):
    try:
        document = IncomingDocument.objects.get(id=document_id)
        return JsonResponse({
            'id': document.id,
            'title': document.title,
            'sender': document.sender,
            'date_received': document.date_received,
            'file': document.file.url
        })
    except IncomingDocument.DoesNotExist:
        return JsonResponse({'error': 'Document not found'}, status=404)

def update_outgoing_document(request, document_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        try:
            document = OutgoingDocument.objects.get(id=document_id)
            document.title = data['title']
            document.recipient = data['recipient']
            document.date_sent = data['date_sent']
            document.file = data['file']
            document.save()
            return JsonResponse({'message': 'Document updated successfully'})
        except OutgoingDocument.DoesNotExist:
            return JsonResponse({'error': 'Document not found'}, status=404)