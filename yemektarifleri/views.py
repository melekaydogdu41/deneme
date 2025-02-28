from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import KayitFormu

def kayit_ol(request):
    if request.method == "POST":
        form = KayitFormu(request.POST)
        if form.is_valid():
            kullanici = form.save()
            login(request, kullanici)  
            return redirect("anasayfa")  
    else:
        form = KayitFormu()
    return render(request, "kayit.html", {"form": form})

def hosgeldin(request):
    return render(request, "hesaplar/hosgeldin.html", {"kullanici": request.user})