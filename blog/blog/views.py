from django.http import HttpResponse
from django.shortcuts import render
from appBlog.models import *
from django.core.paginator import Paginator
import hashlib
from appBlog.forms import Register


def test(request):
    return HttpResponse('tset页面')


def about(request):
    return render(request, 'about.html')


def index(request):
    article = Article.objects.order_by('-data')[:6]
    recommend_article = Article.objects.filter(recommend=1).all()[:7]
    print(recommend_article)
    click_article = Article.objects.order_by('-click')[:12]

    return render(request, 'index.html', locals())


def listpic(request):
    return render(request, 'listpic.html')


def newslistpic(request, page=1):
    article = Article.objects.order_by('-data')
    page = int(page)
    # 每页显示6条数据
    paginator = Paginator(article, 6)
    page_obj = paginator.page(page)
    # 获取当前页
    current_page = page_obj.number
    start = current_page - 3
    if start < 1:
        start = 0
    end = current_page + 2
    if end > paginator.num_pages:
        end = paginator.num_pages
    if start == 0:
        end = 5
    page_range = paginator.page_range[start:end]
    return render(request, 'newslistpic.html', locals())


def base(request):
    return render(request, 'base.html')


def add_article(request):
    for i in range(100):
        article = Article()
        article.title = "title_%s" % i
        article.content = "content_%s" % i
        article.description = "description_%s" % i
        article.author = Author.objects.get(id=1)
        article.save()
        article.type.add(Type.objects.get(id=1))
        article.save()

    return HttpResponse('增加数据')


def fy_test(request):
    # 使用django自带的分页paginator的时候，原数据要增加排序顺序
    article = Article.objects.all().order_by('-data')
    # print(article)
    # 每次显示五条数据
    paginator = Paginator(article, 5)
    # print(paginator.count)
    # print(paginator.page_range)
    # print(paginator.num_pages)
    page_obj = paginator.page(2)
    print(page_obj)
    for one in page_obj:
        print(one.content)
    return HttpResponse('分页功能测试')


def article_detail(request, id):
    id = int(id)
    article = Article.objects.get(id=id)
    return render(request, 'article_detail.html', locals())


def get_test(request):
    # print(dir(request))
    # 用户身份
    # print(request.COOKIES)
    # 请求携带的图片
    # print(request.FILES)
    # get请求携带的参数
    # print(request.GET)
    # post请求携带的参数
    # print(request.POST)
    # 请求协议是https还是http
    # print(request.scheme)
    # 请求方式
    # print(request.method)
    # 请求路径
    # print(request.path)
    # 请求的主体，返回一个字符串
    # print(request.body)
    # 包含了具体的请求数据，包含所有的http请求的信息信息
    # print(request.META)
    # 获取请求的系统
    # print(request.META.get('OS'))
    # 发出请求的浏览器的版本
    # print(request.META.get('HTTP-USER-AGENT'))
    # 请求的主机
    # print(request.META.get('HTTP-HOST'))
    # 请求的来源
    # print(request.META.get('HTTP-REFERER'))

    return HttpResponse('get请求测试')


def form_test(request):
    search = request.GET.get('search')
    # article = Article.objects.filter(title__contains=search)

    data = request.POST
    print(data.get('username'))
    print(data.get('password'))

    return render(request, 'form_test.html', locals())


# md5加密
def set_password(password):
    # 创建一个实例对象
    md5 = hashlib.md5()
    # 进行加密
    md5.update(password.encode())
    result = md5.hexdigest()
    return result


# 注册
def register(request):
    content = ''
    re = ''
    register_form = Register()
    if request.method == 'POST':
        username = request.POST.get('username')
        name = User.objects.filter(name=username).exists()
        if not name:
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            # 判断密码是否相等
            if password != password2:
                content = '两次密码不一样'
            else:
                # 保存数据
                user = User()
                user.name = username
                user.password = set_password(password)
                user.save()
                re = '注册成功'
        else:
            content = '用户名存在'
    return render(request, 'register.html', locals())


# 登录
def enter(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 转换成md5加密
        password = set_password(password)
        name = User.objects.filter(name=username).first().name
        pwd = User.objects.filter(name=username).first().password
        if username == name and password == pwd:
            content = '登陆成功'
    return render(request, 'enter.html', locals())
