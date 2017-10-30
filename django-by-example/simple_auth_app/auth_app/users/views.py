from django.shortcuts import render, redirect
from .forms import RegisterForm


'''
处理表单的经典流程
def form_process_view(request):
    if request.method == 'POST':
        请求为 POST，利用用户提交的数据构造一个绑定了数据的表单
        form = Form(request.POST)

        if form.is_valid():
            表单数据合法
            进行其它处理...
            跳转
            return redirect('/')
    else:
        请求不是 POST，构造一个空表单
        form = Form()

    渲染模板
    如果不是 POST 请求，则渲染的是一个空的表单
    如果用户通过表单提交数据，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'template.html', context={'form': form})
'''

def register(request):
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', context={
        'form': form,
        'next': redirect_to
    })

def index(request):
    return render(request, 'index.html')

