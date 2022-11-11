from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import todo
from .forms import TodoForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  UpdateView,DeleteView

# Create your views here.

class task_1(ListView):
    model = todo
    template_name='index.html'
    context_object_name='details'

class detail(DetailView):
    model = todo
    template_name = 'detail.html'
    context_object_name = 'details'

class update_class(UpdateView):
    model = todo
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','Date')
    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})

class delete_class(DeleteView):
    model = todo
    template_name = 'delete.html'
    success_url = reverse_lazy('task')




def index(request):
    details=todo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task')
        priority =request.POST.get('Priority')
        date =request.POST.get('date')
        Todo = todo(name=name,priority=priority,Date=date)
        Todo.save()
    return render(request,'index.html',{'details':details})


def delete(request,taskid):
    task = todo.objects.get(id=taskid)
    if request.method =='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    updates =todo.objects.get(id=id)
    form = TodoForm(request.POST or None,instance=updates)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'updates':updates})

