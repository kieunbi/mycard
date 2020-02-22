from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Blog,Card

def board(request): 
    blogs = Blog.objects #쿼리셋, 모델로 부터 객체 목록을 전달받게끔 하는 것 / 
    #이 쿼리셋을 어떤 식으로 기능하거나 처리하도록 하는 기능들을 표시해주는 것을 메소드, 쿼리셋을 활용하게끔 하는 것
    return render(request,'board.html',{'blogs':blogs})
# 쿼리셋과 메소드의 형식
# 모델.쿼리셋objects.메소드

def board_detail(request, blog_id):
    board_detail = get_object_or_404(Blog,pk=blog_id)
    return render(request,'board_detail.html',{'blog':board_detail})

def write(request):   
    return render(request,'write.html')

def write_create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save() #데이터 베이스에 저장 
    return redirect('/board_detail/'+str(blog.id))

def board_update(request, blog_id):
    blog = Blog.objects.get(id =blog_id)
    blog.title= request.GET['title'] 
    blog.body= request.GET['body'] 
    blog.save()
    return render(request,'board_detail.html')

def board_delete(request, blog_id):    
    blog = Blog.objects.get(id =blog_id)
    blog.delete()
    return redirect('/board')



def main(request):
    return render(request,'main.html')

def card_recommend(request):
    return render(request,'card_recommend.html')    

def card_result(request): 
    vs=request.GET['category']
    if(request.GET['cate']=='check'):
        cards= Card.objects.filter(card_sort = '체크카드')
    if(request.GET['cate']=='credit'):
        cards= Card.objects.filter(card_sort = '신용카드')
    if(vs=='movie'):
        cards=Card.objects.all().order_by('-card_movie')
    return render(request,'card_result.html',{'cards':cards})   