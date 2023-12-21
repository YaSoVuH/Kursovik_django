from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from .forms import NewsForm, ModerationNewsForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from .utils import AdminStaffRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
import os

# Create your views here.

def news_home(request):
    news = News.objects.order_by('date_create')
    return render(request, 'news/news_home.html', {"news": news})

@login_required
@staff_member_required
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

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if (obj.author != self.request.user) and (not self.request.user.is_staff) and (not self.request.user.is_superuser):
            messages.error(request, "Вы не автор статьи!")
            return redirect(f"/news/{obj.id}")
        messages.success(request, "Вы успешно отредактировали статью!")
        return super(NewsUpdateView, self).dispatch(request, *args, **kwargs)

class NewsUpdateModeratorView(AdminStaffRequiredMixin, UpdateView):
    model = News
    template_name = 'news/update_moderator.html'
    success_url = '/news/NewsModeration'

    form_class  = ModerationNewsForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if (not self.request.user.is_staff) and (not self.request.user.is_superuser):
            return redirect(f"/news/{obj.id}")
        return super(NewsUpdateModeratorView, self).dispatch(request, *args, **kwargs)

class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = '/news/'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if (obj.author != self.request.user) and (not self.request.user.is_staff) and (not self.request.user.is_superuser):
            messages.error(request, "Вы не автор статьи!")
            return redirect(f"/news/{obj.id}")
        messages.success(request, "Успешно удалили статью!")
        if obj.photo:
            try:
                os.remove(f"{settings.MEDIA_ROOT.replace("\\", "/")}/{obj.photo}")
            except FileNotFoundError:
                return super(NewsDeleteView, self).dispatch(request, *args, **kwargs)
        return super(NewsDeleteView, self).dispatch(request, *args, **kwargs)

class NewsCreateView(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/create.html'
    success_url = '/news/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        if (not self.request.user.is_staff) or (not self.request.user.is_staff):
            self.object.is_modarated = False
        else:
            self.object.is_modarated = True
        self.object.save()
        return super().form_valid(form)