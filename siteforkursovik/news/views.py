from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm, ModerationNewsForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

# Create your views here.

def news_home(request):
    news = News.objects.order_by('date_create')
    return render(request, 'news/news_home.html', {"news": news})

def Moderation_News(request):
    news = News.objects.order_by('date_create')
    return render(request, 'news/news_moderation_list.html', {"news": news})

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detais_view.html'
    context_object_name = 'news'

class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/update.html'
    
    form_class  = NewsForm

class NewsUpdateModeratorView(UpdateView):
    model = News
    template_name = 'news/update_moderator.html'

    form_class  = ModerationNewsForm

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = '/news/'

class NewsCreateView(CreateView):
    form_class = NewsForm
    template_name = 'news/create.html'
    success_url = '/news/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.is_modarated = False
        self.object.save()
        return super().form_valid(form)


'''
def create(request):
    if not request.user.is_authenticated:
        return redirect('login')

    error = ''

    if request.method == 'POST':
        form = NewsForm()
    else:
        redirect('/')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post_author = self.request.user
        self.object.save()
        return super(PostCreate, self).form_valid(form)

    form = NewsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)
'''