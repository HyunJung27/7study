from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewBlog
from .models import Blog
from django.utils import timezone
# Create your views here.
def post(request):
    if request.method == "POST":
        form = NewBlog(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.update_date = timezone.now()
            board.save()
            return redirect('show')

    else:
        form = NewBlog()
        return render(request, 'post.html', {'form': form})


def show(request):
    boards = Blog.objects.all()
    return render(request, 'show.html', {'boards': boards})


def detail(request, board_id): #board_id // pk=board_id
    board_detail = get_object_or_404(Blog, pk=board_id)
    return render(request, 'detail.html', {'board': board_detail})

def edit(request, pk):
    board = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = NewBlog(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.update_date = timezone.now()
            board.save()
            return redirect('show')

    else:
        form = NewBlog()
        return render(request, 'edit.html', {'form': form})

def delete(request, pk):
    board = Blog.objects.get(id=pk)
    board.delete()
    return redirect('show')

def slide(request):
        return render(request, 'slide.html')


def map(request):
        return render(request, 'map.html')

