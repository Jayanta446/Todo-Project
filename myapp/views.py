from django.shortcuts import render
from .models import TodoModel
from .forms import TodoForm
from django.shortcuts import redirect
def todo_list(request):
    if request.method == 'GET':
        form_obj = TodoForm()
        todos = TodoModel.objects.all()
        return render(request, 'myapp/todo.html', {'todo':todos, 'form':form_obj})

    if request.method == 'POST':
        form_obj = TodoForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            print(form_obj.cleaned_data['todo'])
            return redirect('/todo')
        return redirect('/todo')

def delete_todo(request, id):
    model = TodoModel.objects.get(id = id)
    model.delete()
    print(f"The id is {id}")
    return redirect('/todo')
