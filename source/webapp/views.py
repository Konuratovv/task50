from django.shortcuts import render
from django.http import HttpResponseRedirect
from random import randint
from webapp.articles_db import ArticlesDB

HAPPY = "happy.jpg"
UNHAPPY = "unhappy.jpg"
ASLEEP = "asleep.jgp"


# Create your views here.
def cat_name(request):
    if request.method == "GET":
        return render(request, 'cat_name.html')
    else:
        article = {
            'name': request.POST.get('cat_name'),
            'age': 1,
            'happiness': 40,
            'hunger': 40,
            'sleep': 0,
            'image': UNHAPPY
        }
        ArticlesDB.articles.append(article)
        return HttpResponseRedirect('cat_stats/')


def cat_stats(request):
    articles = ArticlesDB.articles
    context = {'articles': articles}
    if request.method == "GET":
        return render(request, "cat_stats.html", context)
    else:
        action = request.POST.get('action')
        for article in articles:
            if action == "Покормить":
                if article['sleep'] == 0:
                    if article['hunger'] < 100 and article['happiness'] < 100:
                        article['hunger'] += 15
                        article['happiness'] += 5
                    else:
                        article['hunger'] -= (article['hunger'] - 100)
                        article['happiness'] -= (article['happiness'] - 100)
                else:
                    article['hunger'] += 0
                    article['happiness'] += 0
            elif action == "Поиграть":
                if randint(1, 3) != 1:
                    if article['happiness'] < 100:
                        article['happiness'] += 15
                    else:
                        article['happiness'] -= (article['happiness'] - 100)
                else:
                    article['happiness'] = 0
                article['hunger'] -= 10
                if article['sleep'] == 1:
                    article['sleep'] = 0
                else:
                    pass
            elif action == "Усыпить":
                article['sleep'] = 1

            if article['happiness'] > 50:
                article['image'] = HAPPY
            elif article['happiness'] < 50:
                article['image'] = UNHAPPY
            elif article['sleep'] == 1:
                article['image'] = ASLEEP

        return render(request, "cat_stats.html", context)
