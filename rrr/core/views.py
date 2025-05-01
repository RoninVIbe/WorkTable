from django.shortcuts import render
from .models import Project, Task, Document, Message
from .forms import TaskForm
from django.http import FileResponse, Http404
import os

def download_document(request, document_id):
    from .models import Document  # Импорт модели
    try:
        doc = Document.objects.get(id=document_id)
        filepath = doc.file.path
        return FileResponse(open(filepath, 'rb'), as_attachment=True, filename=os.path.basename(filepath))
    except Document.DoesNotExist:
        raise Http404("Файл не найден")

def home(request):
    return render(request, 'home.html')

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {'documents': documents})

def message_list(request):
    messages = Message.objects.all()
    return render(request, 'message_list.html', {'messages': messages})

# Create your views here.
