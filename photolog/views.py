from django.shortcuts import render, redirect
from .models import Photolog

# Create your views here.

def list(request):
    Photolog_all = Photolog.objects.all()
    context = {"photolog_all" : Photolog_all}
    return render(request, 'photolog/list.html', context)

def create(request):
    if request.method == 'POST':
        #클라이언트 데이터 수신
        input_title = request.POST['title']
        input_image = request.FILES['image']
        input_description = request.POST['description']
        #모델 생성
        Photolog.objects.create(title=input_title, image=input_image, description=input_description)
        #응답
        return redirect('photolog:list')

    else:
        return render(request, 'photolog/form.html')
