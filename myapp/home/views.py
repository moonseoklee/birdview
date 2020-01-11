from django.shortcuts import get_object_or_404, render
from myapp.item import models
from django.core import serializers
from django.core.paginator import Paginator
from django.http import HttpResponse


import json


def index(request):
    
    return render(request, 'index.html', {})

#def getByCategory(category,querySet):


def getByType(skinType):
    if skinType=='oily':
        querySet = models.Item.objects.all().order_by('-forOily','price')
        
    elif skinType=='dry':
        querySet = models.Item.objects.all().order_by('-forDry','price')
        
    elif skinType=='sensitive':
        querySet = models.Item.objects.all().order_by('-forSensitive','price')

    return querySet

def getByType2(skinType,querySet):
    if skinType=='oily':
        querySet = querySet.order_by('-forOily')[:3]
        
    elif skinType=='dry':
        querySet = querySet.order_by('-forDry')[:3]
        
    elif skinType=='sensitive':
        querySet = querySet.order_by('-forSensitive')[:3]

    return querySet

def pagingFunc(pageNum,querySet):
    paginator = Paginator(querySet,50)     

    paged = paginator.page(pageNum)

    return paged

def categoryFunc(categoryd,querySet):
    
        
    querySet = querySet.filter(category=categoryd)

    return querySet

def includeFunc(includeStr,querySet):
    includeList = list(includeStr.split(','))
    for i in includeList:
        querySet = querySet.filter(ingredients__contains=i)

    return querySet
def excludeFunc(excludeStr,querySet):
    excludeList = list(excludeStr.split(','))
    
    for i in excludeList:
        querySet = querySet.exclude(ingredients__contains=i)

    return querySet
def makeJson(obj):
    jsonList = []
    
    for i in obj:
        
        temp = {}
        temp['id'] = i['pk']
        temp['imagUrl'] = 'https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/image/'+i['fields']['imageId']+'.jpg'
        temp['name'] = i['fields']['name']
        temp['price'] =i['fields']['price']
        temp['ingredients'] =i['fields']['ingredients']
        temp['monthlySales'] =i['fields']['monthlySales']
        
        jsonList.append(temp)
    return jsonList

def makeJson2(i):
    jsonList = []
    
    
        
    temp = {}
    temp['id'] = i['id']
    temp['imagUrl'] = 'https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/image/'+i['imageId']+'.jpg'
    temp['name'] = i['name']
    temp['price'] =i['price']
    temp['gender'] =i['gender']
    temp['category'] =i['category']
    temp['ingredients'] =i['ingredients']
    temp['monthlySales'] =i['monthlySales']
     
    jsonList.append(temp)
    return jsonList

def makeJson3(i):
    jsonList = []    
    
        
    temp = {}
    temp['id'] = i['id']
    temp['imagUrl'] = 'https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/thumbnail/'+i['imageId']+'.jpg'
    temp['name'] = i['name']
    temp['price'] =i['price']
   
    jsonList.append(temp)
    print(jsonList)
    return jsonList

def main(request):
    
    querySet = getByType(request.GET['skin_type'])
    
    
    


    ########category##############
    category = request.GET.get('category')
    if category!=None:
        querySet = categoryFunc(category,querySet)

    #####include&exclude############
    include = request.GET.get('include_ingredient')
    exclude = request.GET.get('exclude_ingredient')
    if include!=None:        
        querySet = includeFunc(include,querySet)
    if exclude!=None:        
        querySet = excludeFunc(exclude,querySet)
    





    ##########paging###############
    page = request.GET.get('page')

    if page!=None:
        querySet = pagingFunc(page,querySet)

    ####makeResponse###
    
    querySet = serializers.serialize('json',querySet)
    querySet = (json.loads(querySet))
    querySet = makeJson((querySet))
    ######################
    
    
    #return render(request,'recommendByType2.html',{'item' : querySet})
    return HttpResponse(str(querySet))

def detail(request,id):

    
    

    skinType = request.GET.get('skin_type')
    

    querySet = models.Item.objects.get(id=id)
    
    querySet = querySet.__dict__
    
    
    category = querySet['category']
    querySet = makeJson2((querySet))
    ###########recommendByCategory##############
    
    if skinType!=None:
        queryAll = models.Item.objects.all()    
        
        queryAll = queryAll.filter(category__contains=category)
        
        queryAll = getByType2(skinType,queryAll)    
        
        
        for i in queryAll.values():
            querySet.append(makeJson3(i)[0])
  
    
    return HttpResponse(str(querySet))