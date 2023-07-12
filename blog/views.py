from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Article, Category, Tag
from .forms import CommentForm


def index(request):
    articles = Article.objects.order_by('id')
    ctx = {
        'object_list': articles
    }
    return render(request, 'readit/index.html', ctx)


def article_list(request):
    articles = Article.objects.all().order_by('-id')
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    if search:
        articles = articles.filter(search__icontains=search)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 2)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    ctx = {
        "object_list": page_obj,
    }
    return render(request, 'readit/blog.html', ctx)


def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    tag = Tag.objects.all()
    categories = Category.objects.all()
    last_3_articles = Article.objects.order_by('-id')[:3]
    form = CommentForm()
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(reverse('blog:detail', kwargs={'pk': pk}))
        form = CommentForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author_id = request.user.profile.id
            obj.article_id = article.id
            obj.save()
            return redirect(".")
    ctx = {
        'object': article,
        'categories': categories,
        'last_3_articles': last_3_articles,
        'form': form,
        'tags': tag
    }
    return render(request, 'readit/blog-single.html', ctx)


