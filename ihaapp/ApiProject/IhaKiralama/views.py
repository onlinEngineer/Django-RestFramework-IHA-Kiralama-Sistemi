from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


## LOGIN İŞLEMLERİ ##
@login_required(login_url="login")

#Home Page
def home(request):
    return render(request, "home/home.html")


#Kullanıcı Kayıt işlemi
def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"{user.username} hesabınız oluşturuldu.")
            return redirect("login")  # Kayıt tamamlandıktan sonra giriş sayfasına yönlendir
    else:
       
        form = UserCreationForm()
        

    return render(request, "registration/register.html", {"form": form})


#Kullanıcı Login işlemi
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"{user.username} olarak giriş yapıldı.")
            return redirect("home")  # Giriş yapıldıktan sonra ana sayfaya yönlendir
        else:
            messages.error(request, "Kullanıcı adı veya parola hatalı.")
    return render(request, "login/login.html")

#Kullanıcı Logout işlemi

from django.contrib.auth import logout
def logout_user(request):
    logout(request)
    return redirect("login")  # Çıkış yapıldıktan sonra ana sayfaya yönlendir



from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from IhaKiralama.models import IHA,Kiralama
from IhaKiralama.serializers import IHASerializer,KiralamaSerializer,UserSerializer


from django.contrib.auth.models import User
from rest_framework import viewsets


class IHAViewSet(viewsets.ModelViewSet):
    queryset = IHA.objects.all()
    serializer_class = IHASerializer


class KiraViewSet(viewsets.ModelViewSet):
    queryset = Kiralama.objects.all()
    serializer_class = KiralamaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



from django.shortcuts import render
from .models import IHA,Kiralama

##Tüm ihaları getir.

@login_required(login_url="login")
def all_iha_list(request):
    get_all_iha_list = IHA.objects.all()
    context = {'iha_list': get_all_iha_list}

    return render(request, 'view/iha_list.html', context)

##Tüm Kiralama işlemlerini getir.

@login_required(login_url="login")
def all_kira_list(request):
    get_all_kira_list = Kiralama.objects.all()
 
    context = {'kira_list': get_all_kira_list}

    return render(request, 'view/kira_list.html', context)


##Tüm Kullanıcıları getir.
@login_required(login_url="login")
def all_user_list(request):
    get_all_user_list = User.objects.all()
 
    context = {'user_list': get_all_user_list}

    return render(request, 'view/user_list.html', context)

##Login olmuş kullanıcının kiralama bilgilerini getir.
@login_required(login_url="login")
def user_kira_list(request):
    user_id = request.user.id
    
    # Kullanıcının kiralama verilerini çek
    user_kiralama_list = Kiralama.objects.filter(kiralayan_uye=user_id)
    user_id = request.user.id
    context = {
        'kiralama_list': user_kiralama_list,
        'user_id':user_id
    }
    
    return render(request, 'view/user_kira_list.html', context)


## Kiralama API GET,POST,PUT,DELETE işlemleri
#http://127.0.0.1:8000/api/kirala

# @csrf_exempt
# def kiralamaApi(request,id=0):
#     if request.method=='GET':
#         get_all_data = Kiralama.objects.all()
#         Kiralama_serializer=KiralamaSerializer(get_all_data,many=True)
#         return JsonResponse(Kiralama_serializer.data,safe=False)
#     elif request.method=='POST':
#         kiralamaData=JSONParser().parse(request)
#         Kiralama_serializer=KiralamaSerializer(data=kiralamaData)
#         if Kiralama_serializer.is_valid():
#             Kiralama_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
#     elif request.method=='PUT':
#         kiralamaData=JSONParser().parse(request)
#         KiralamaSerializer.objects.get(kiralama_id=kiralamaData['kiralama_id'])
#         Kiralama_serializer=KiralamaSerializer(kiralamaData=kiralamaData)
#         if Kiralama_serializer.is_valid():
#             Kiralama_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update")
#     elif request.method=='DELETE':
#         KiralamaSerializer.objects.get(kiralama_id=id)
#         Kiralama.delete()
#         return JsonResponse("Deleted Successfully",safe=False)



## IHA API GET,POST,PUT,DELETE işlemleri
#http://127.0.0.1:8000/api/iha


# @csrf_exempt
# def ihaApi(request,id=0):
#     if request.method=='GET':
#         get_all_iha = IHA.objects.all()
#         ihas_serializer=IHASerializer(get_all_iha,many=True)
#         print(ihas_serializer)
#         return JsonResponse(ihas_serializer.data,safe=False)
    
#     elif request.method=='POST':
#         iha_data=JSONParser().parse(request)
#         ihas_serializer=IHASerializer(data=iha_data)
#         if ihas_serializer.is_valid():
#             ihas_serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)
#     elif request.method=='PUT':
#         iha_data=JSONParser().parse(request)
#         iha=IHA.objects.get(iha_id=iha_data['iha_id'])
#         ihas_serializer=IHASerializer(iha,data=iha_data)
#         if ihas_serializer.is_valid():
#             ihas_serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update")
#     elif request.method=='DELETE':
#         iha=IHA.objects.get(iha_id=id)
#         iha.delete()
#         return JsonResponse("Deleted Successfully",safe=False)