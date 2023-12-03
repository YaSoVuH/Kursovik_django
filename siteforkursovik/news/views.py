from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.

def news_home(request):
    news = News.objects.order_by('date')
    return render(request, 'news/news_home.html', {"news": news})

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detais_view.html'
    context_object_name = 'news'

class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/update.html'

    form_class  = NewsForm

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = '/news/'

def create(request):
    error = ''

    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Форма была неверной'

    form = NewsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)
