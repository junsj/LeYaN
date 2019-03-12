from django.shortcuts import render

# Create your views here.

from website.functions import *

'''
====================================================================================
|  Functions:                                                                      |
====================================================================================
'''
def home(request):
   c={}
   c['pics_list'] = Pics.objects.filter(pixs='640x402').order_by("?")[:5]
   c['pre300_list'] = Pics.objects.filter(pixs='300x402').order_by("?")[:6]

   return render_to_response('index.html',c,context_instance=RequestContext(request))
'''
====================================================================================
|  Functions:                                                                      |
====================================================================================
'''
def crawlers(request):
   c={}
   c['article_list'] = Article.objects.filter(title='test1').order_by("?")[:5]
   return render_to_response('crawlers.html',c,context_instance=RequestContext(request))

'''
====================================================================================
|  Functions:                                                                      |
====================================================================================
'''
def new(request):
   c={}



   return render_to_response('new.html',c,context_instance=RequestContext(request))