from django.shortcuts import render,redirect

# Create your views here.
from .models import *


def bulimlar(requests):
    return render(requests, 'bulimlar.html')




def client_update(requests, c):
    d = Clients.objects.get(id=c)
    if requests.method == "POST":
        Clients.objects.filter(id=c).update(
            fio=requests.POST.get('client_name'),
            dokon_nomi=requests.POST.get('client_shop'),
            telefon_raqami=requests.POST.get('client_phone'),
            manzil=requests.POST.get('client_address')
        )
        return redirect('/clients/')
    data = {
        "client": d
    }
    return render(requests, 'client_update.html', data)



def clients(requests):
    if requests.method == "POST":
        Clients.objects.create(
        fio=requests.POST.get('client_name'),
        dokon_nomi=requests.POST.get('client_shop'),
        telefon_raqami=requests.POST.get('client_phone'),
        manzil=requests.POST.get('client_address')

        )
    data = {
        "clients": Clients.objects.all()
    }
    return render(requests, 'clients.html', data)




def home(requests):
    return render(requests, 'home.html')




def product_update(requests, a):
    b = Products.objects.get(id=a)
    if requests.method == "POST":
        Products.objects.filter(id=a).update(
        nomi=requests.POST.get('pr_name'),
        brendi=requests.POST.get('pr_brend'),
        narxi=requests.POST.get('pr_price'),
        miqdori=requests.POST.get('pr_amount')
        )
        return redirect('/products/')

    data = {
        "product": b
    }

    return render(requests, 'product_update.html', data)






def stats(requests):
    if requests.method == "POST":
        Stats.objects.create(
        product=requests.POST.get('product'),
        client=requests.POST.get('client'),
        sana=requests.POST.get('sana'),
        miqdor=requests.POST.get('miqdor'),
        umumiy_summa=requests.POST.get('summa'),
        tolandi=requests.POST.get('tolandi'),
        nasiya=requests.POST.get('nasiya'),
        )
    data = {
        "stats": Stats.objects.all()
    }
    return render(requests, 'stats.html', data)





def stats_update(requests, d):
    f = Stats.objects.get(id=d)
    if requests.method == "POST":
        Stats.objects.filter(id=d).update(
            product=requests.POST.get('product'),
            client=requests.POST.get('client'),
            sana=requests.POST.get('sana'),
            miqdor=requests.POST.get('miqdor'),
            umumiy_summa=requests.POST.get('summa'),
            tolandi=requests.POST.get('tolandi'),
            nasiya=requests.POST.get('nasiya'),
        )
        return redirect('/stats/')
    data = {
        "stats": f
    }
    return render(requests, 'stats_update.html', data)





def products(requests):
    if requests.method == "POST":
        Products.objects.create(
        nomi=requests.POST.get('pr_name'),
        brendi=requests.POST.get('pr_brend'),
        narxi=requests.POST.get('pr_price'),
        miqdori=requests.POST.get('pr_amount')
        )
    data = {
        "products": Products.objects.all()
    }
    return render(requests, 'products.html', data)






def tahrirlash(requests):
    if requests.method == "POST":
        Products.objects.update(
        nomi=requests.POST.get('nomi'),
        brendi=requests.POST.get('brendi'),
        narxi=requests.POST.get('narhi'),
        miqdori=requests.POST.get('miqdori')
        )
    data = {
        "products": Products.objects.all()
    }
    return render(requests, 'tahrirlash.html', data)


