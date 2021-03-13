from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from . models  import *


def index(request):
	return HttpResponseRedirect("home")

def home(request):
	return render(request, "articles/home.html")

def help(request):
	return render(request, "articles/help.html")

def setting(request):
	return render(request, "articles/setting.html")

def idea(request):
	idea = Idea.objects.order_by('-pub_date')
	return render(request, "post/idea.html", {'idea':idea})

def idea_checklist(request, idea_id):
	try:
		ic = Idea.objects.get(id = idea_id)
	except:
		raise Http404("Статья не найдена!!!")
	latest_comments_list = i.comment_set.order_by('-id')[:10]

	ic.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

	return render(request, 'list.html', {'ic':ic, 'latest_comments_list':latest_comments_list}, args = (ic.id))

def gallery(request):
	g = Gallery.objects.order_by('-pub_date')
	return render(request, "post/gallery.html", {'g':g})

def gallery_checklist(request, gallery_id):
	try:
		gc = Gallery.objects.get(id = gallery_id)
	except:
		raise Http404("Статья не найдена!!!")
	latest_comments_list = gc.comment_set.order_by('-id')[:10]

	gc.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

	return render(request, 'list.html', {'gc':gc, 'latest_comments_list':latest_comments_list}, args = (gc.id))

def learn(request):
	l = Learn.objects.order_by('-pub_date')
	return render(request, "post/learn.html", {'l':l})

def learn_checklist(request, learn_id):
	try:
		lc = Learn.objects.get(id = gallery_id)
	except:
		raise Http404("Статья не найдена!!!")
	latest_comments_list = lc.comment_set.order_by('-id')[:10]

	lc.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

	return render(request, 'list.html', {'lc':lc, 'latest_comments_list':latest_comments_list}, args = (lc.id))

def motiv(request):
	m = Motiv.objects.order_by('-pub_date')
	return render(request, "post/motiv.html", {'m':m})

def motiv_checklist(request, motiv_id):
	try:
		mc = Motiv.objects.get(id = motiv_id)
	except:
		raise Http404("Статья не найдена!!!")
	latest_comments_list = mc.comment_set.order_by('-id')[:10]

	mc.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

	return render(request, 'list.html', {'mc':mc, 'latest_comments_list':latest_comments_list}, args = (mc.id))
