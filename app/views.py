from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentCreateForm
from .models import Diary


def index(request):
    context = {
        'diary_list': Diary.objects.all(),
        'form': CommentCreateForm(),
    }
    return render(request, 'app/diary_list.html', context)


@require_POST
def create_comment(request, pk):
    form = CommentCreateForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.target = get_object_or_404(Diary, pk=pk)
        comment.save()
        return redirect('app:index')
        # 'index' and 'comment_create' is url name

    context = {
        'diary_list': Diary.objects.all(),
        'error_form': form,
        'form': CommentCreateForm(),
    }
    return render(request, 'app/diary_list.html', context)
