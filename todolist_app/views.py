from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem  # todolist_app의 models에서 TodoItem 모델을 가져옵니다.

def index(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'todolist_app/todo_list.html', {'todo_items': todo_items})
    # 템플릿 경로를 수정합니다.


def add_item(request):
    if request.method == 'POST':
        new_item_text = request.POST.get('new_item', '')
        new_description = request.POST.get('new_description', '')
        if new_item_text:
            TodoItem.objects.create(text=new_item_text, description=new_description)
            return redirect('index')  # index 뷰로 리디렉션

def toggle_complete(request, item_id):
    item = get_object_or_404(TodoItem, pk=item_id)
    item.completed = not item.completed
    item.save()
    return HttpResponse("Toggle complete successfully", content_type="text/plain")

def delete_item(request, item_id):
    item = get_object_or_404(TodoItem, pk=item_id)
    item.delete()
    return (
        HttpResponse("Item deleted successfully", content_type="text/plain"))

