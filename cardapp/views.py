from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Blog,Card
import queue
from django.db.models import Q
from django.core.paginator import Paginator

def board(request): 
    blogs = Blog.objects.order_by('-pub_date') #쿼리셋, 모델로 부터 객체 목록을 전달받게끔 하는 것 / 
    #이 쿼리셋을 어떤 식으로 기능하거나 처리하도록 하는 기능들을 표시해주는 것을 메소드, 쿼리셋을 활용하게끔 하는 것
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3) 
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request,'board.html',{'blogs':blogs, 'posts':posts})
# 쿼리셋과 메소드의 형식
# 모델.쿼리셋objects.메소드

def board_detail(request, blog_id):
    board_detail = get_object_or_404(Blog,pk=blog_id)
    return render(request,'board_detail.html',{'blog':board_detail})

def board_write(request):   
    return render(request,'board_write.html')

def write_create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title=request.GET['title']
    blog.card_name=request.GET['card_name']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save() #데이터 베이스에 저장 
    return redirect('/board')

def board_search_result(request):   
    return render(request,'board_search_result.html')

def board_update(request, blog_id):
    if request.method == "GET":
        blog = Blog.objects.get(id=blog_id)
        context={
            "blog":blog
        }
        return render(request, "board_update.html", context)
    elif request.method=="POST":
        blog = Blog.objects.get(id =blog_id)
        blog.title= request.POST['title'] 
        blog.body= request.POST['body'] 
        blog.save()
        return redirect('/board_detail/'+str(blog.id))

def board_delete(request, blog_id):    
    blog = Blog.objects.get(id =blog_id)
    blog.delete()
    return redirect('/board')


def main(request):
    return render(request,'main.html')

def card_recommend(request):
    return render(request,'card_recommend.html')    

def card_result(request): 
    price=request.GET['price']
    vs=request.GET['category']
    if(request.GET['cate']=='check'):
        if(price=='300000'):
            if(vs=='영화 할인률'):
                cards=Card.objects.filter(card_sort = '체크카드',card_price_min='300000').order_by('-card_movie')
            elif(vs=='bus'):
                cards=Card.objects.filter(card_sort = '체크카드',card_price_min='300000').order_by('-card_bus')   
            elif(vs=='coffee'):
                cards=Card.objects.filter(card_sort = '체크카드',card_price_min='300000').order_by('-card_coffee')
            elif(vs=='mart'):
                cards=Card.objects.filter(card_sort = '체크카드',card_price_min='300000').order_by('-card_mart')
        if(price=='500000'):
            if(vs=='영화 할인률'):
                cards=Card.objects.filter(card_sort = '체크카드').order_by('-card_movie')
            elif(vs=='bus'):
                cards=Card.objects.filter(card_sort = '체크카드').order_by('-card_bus')   
            elif(vs=='coffee'):
                cards=Card.objects.filter(card_sort = '체크카드').order_by('-card_coffee')
            elif(vs=='mart'):
                cards=Card.objects.filter(card_sort = '체크카드').order_by('-card_mart')          

    elif(request.GET['cate']=='credit'):
        if(price=='300000'):
            if(vs=='영화 할인률'):
                cards= Card.objects.filter(card_sort = '신용카드',card_price_min='300000').order_by('-card_movie')
                name=card_movie
            elif(vs=='bus'):
                cards=Card.objects.filter(card_sort = '신용카드',card_price_min='300000').order_by('-card_bus')   
            elif(vs=='coffee'):
                cards=Card.objects.filter(card_sort = '신용카드',card_price_min='300000').order_by('-card_coffee')
            elif(vs=='mart'):
                cards=Card.objects.filter(card_sort = '신용카드',card_price_min='300000').order_by('-card_mart')
        if(price=='500000'):
            if(vs=='영화 할인률'):
                cards=Card.objects.filter(card_sort = '신용카드').order_by('-card_movie')
            elif(vs=='bus'):
                cards=Card.objects.filter(card_sort = '신용카드').order_by('-card_bus')   
            elif(vs=='coffee'):
                cards=Card.objects.filter(card_sort = '신용카드').order_by('-card_coffee')
            elif(vs=='mart'):
                cards=Card.objects.filter(card_sort = '신용카드').order_by('-card_mart')   
                            
    return render(request,'card_result.html',{'cards':cards,'vs':vs})   
 

def search(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products= Blog.objects.all().filter(Q(card_name__icontains=query))
    return render(request,'board_search_result.html',{'products':products,'query':query}) 