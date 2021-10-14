from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import News, Category
from .forms import NewsForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Success registration!')
            return redirect('home')
        else:
            messages.error(request, 'Registration error!')
    else:
        form = UserCreationForm()
    return render(request, "news/register.html", {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    return render(request, 'news/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


class HomeNews(ListView):
    model = News
    template_name = "news/home_news_list.html"
    context_object_name = "news"
    paginate_by = 3


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = " Main page"
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related("category")


class NewsByCategory(ListView):
    model = News
    template_name = "news/home_news_list.html"
    context_object_name = "news"
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = Category.objects.get(pk=self.kwargs["category_id"])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs["category_id"], is_published=True).select_related("category")


class ViewNews(DetailView):
    model = News
    context_object_name = "news_item"

class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = "news/add_news.html"

def get_category(request, category_id):
    news = News.objects.filter(category_id= category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, template_name="news/category.html", context={"news":news, "category":category})

def get_category_for_home(request, category_id):
    news = News.objects.all()
    context = {"news": news,
               "title": " List of news",
               }
    return render(request, "news/index.html", context=context)

