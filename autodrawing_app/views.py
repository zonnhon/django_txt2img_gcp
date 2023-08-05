from django.shortcuts import render
from .models import DateSelect, News_content, News_comment, Game_content, Game_comment, Comic_content, Comic_comment
import datetime
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.http import require_POST
import json

# Create your views here.
# def index(request):
#     return render(request, 'autodrawing_app/index.html')

# def index(request, tag):
#     images = Image.objects.filter(tag=tag)
#     context = {
#         'images': images,
#         'tag': tag
#     }
#     return render(request, 'autodrawing_app/index.html', context)
dates = DateSelect.objects.all().order_by('-datestr')
def page1_view(request):
    dates = DateSelect.objects.all().order_by('-datestr')
    return render(request, 'autodrawing_app/select.html', {'page_name': 'news', 'dates': dates})
def page2_view(request):
    dates = DateSelect.objects.all().order_by('-datestr')
    return render(request, 'autodrawing_app/select.html', {'page_name': 'game', 'dates': dates})

def page3_view(request):
    dates = DateSelect.objects.all().order_by('-datestr')
    return render(request, 'autodrawing_app/select.html', {'page_name': 'comic', 'dates': dates})


@require_POST
def update_content(request):
    # 從POST請求中獲取數據
    data = json.loads(request.body)
    selected_date = data.get('selected_date')
    page_name = data.get('page_name')
    page_num = data.get('page_num')
    print(selected_date, page_name, page_num)
    # 處理你的數據
    s_dtime = datetime.datetime.strptime(selected_date, '%Y-%m-%d')-datetime.timedelta(hours=8)
    e_dtime = datetime.datetime.strptime(selected_date, '%Y-%m-%d')
    if page_name == 'news':
        selected_content = News_content.objects.filter(date__range=(s_dtime, e_dtime), type='content', page=page_num).order_by('-id').first()
        selected_comment = News_comment.objects.filter(date__range=(s_dtime, e_dtime), type='comment', page=page_num).order_by('-id').first()
        selected_content_prompt = News_content.objects.filter(date__range=(s_dtime, e_dtime), type='prompt', page=page_num).order_by('-id').first()
        selected_comment_prompt = News_comment.objects.filter(date__range=(s_dtime, e_dtime), type='prompt', page=page_num).order_by('-id').first()
        selected_dateinfo=DateSelect.objects.filter(datestr=selected_date).order_by('-id').first()
        pagenum = selected_dateinfo.newspage
    elif page_name == 'game':
        selected_content = Game_content.objects.filter(date__range=(s_dtime, e_dtime), type='content', page=page_num).order_by('-id').first()
        selected_comment = Game_comment.objects.filter(date__range=(s_dtime, e_dtime), type='comment', page=page_num).order_by('-id').first()
        selected_content_prompt = Game_content.objects.filter(date__range=(s_dtime, e_dtime), type='prompt', page=page_num).order_by('-id').first()
        selected_comment_prompt = Game_comment.objects.filter(date__range=(s_dtime, e_dtime), type='prompt', page=page_num).order_by('-id').first()
        selected_dateinfo = DateSelect.objects.filter(datestr=selected_date).order_by('-id').first()
        pagenum = selected_dateinfo.gamepage
    elif page_name == 'comic':
        selected_content = Comic_content.objects.filter(date__range=(s_dtime, e_dtime), type='content', page=page_num).order_by('-id').first()
        selected_comment = Comic_comment.objects.filter(date__range=(s_dtime, e_dtime), type='comment', page=page_num).order_by('-id').first()
        selected_content_prompt = Comic_content.objects.filter(date__range=(s_dtime, e_dtime), type='prompt', page=page_num).order_by('-id').first()
        selected_comment_prompt = Comic_comment.objects.filter(date__range=(s_dtime, e_dtime), type='prompt', page=page_num).order_by('-id').first()
        selected_dateinfo = DateSelect.objects.filter(datestr=selected_date).order_by('-id').first()
        pagenum = selected_dateinfo.comicpage
    else:
        selected_content = News_content.objects.filter(date__range=(s_dtime, e_dtime), type='content', page=page_num).order_by('-id').first()
        selected_comment = News_comment.objects.filter(date__range=(s_dtime, e_dtime), type='comment', page=page_num).order_by('-id').first()
        selected_content_prompt = News_content.objects.filter(date__range=(s_dtime, e_dtime), type='prompt', page=page_num).order_by('-id').first()
        selected_comment_prompt = News_comment.objects.filter(date__range=(s_dtime, e_dtime), type='prompt', page=page_num).order_by('-id').first()
        selected_dateinfo = DateSelect.objects.filter(datestr=selected_date).order_by('-id').first()
        pagenum = selected_dateinfo.newspage

    content_data = {'type':str(selected_content.type),
                    'title':str(selected_content.title),
                    'content':str(selected_content.content),
                    'prompt':'Prompt: '+str(selected_content_prompt.content),
                    'date':str(selected_content)}
    comment_data = {'type': str(selected_comment.type),
                    'title': str(selected_comment.title),
                    'content': str(selected_comment.content),
                    'prompt': 'Prompt: '+str(selected_comment_prompt.content),
                    'date': str(selected_comment.date)}

    return JsonResponse({'content': content_data, 'comment': comment_data, 'pagenum': pagenum})
