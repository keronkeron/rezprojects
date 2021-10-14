from django import template
from django.db.models import Count, F
from news.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag("news/list_categories.html")
def show_categories(arg1 = "hello", arg2 = "world"):
    categories = Category.objects.annotate(cnt=Count('get_news', filter=F('get_news__is_published'))).filter(cnt__gt=0)
    # categories = Category.objects.annotate(cnt=Count('get_news')).filter(cnt__gt=0)

    # return {"categories": categories, 'arg1':arg1, 'arg2':arg2}
    return {"categories": categories, 'arg1':arg1, 'arg2':arg2}


