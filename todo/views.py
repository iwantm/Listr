# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import List
from .forms import NewList

# Create your views here.
def list(request):
    data = List.objects.order_by('date_due')
    return render(request, 'todo/list.html', {'data': data})

def task_new(request):
    if request.method == "POST":
        form = NewList(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list)
    else:
        form = NewList()
    return render(request, 'todo/task_edit.html', {'form' : form})

def task_edit(request, pk):
    data = get_object_or_404(List, pk=pk)
    if request.method == "POST":
        form = NewList(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect(list)
    else:
        form = NewList(instance=data)
    return render(request, 'todo/task_edit.html', {'form': form})

def delete(request, pk):
    data = get_object_or_404(List, pk=pk)
    data.delete()
    return redirect(list)
