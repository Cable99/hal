from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import movimenti
from django.shortcuts import render, redirect
from .forms import MovimentiForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

#datetime per stampare l'anno corrente
x = datetime.datetime.now()
y = x.strftime("%Y")
def index(request):
    if  request.user.is_authenticated:
        list_mov = movimenti.objects.filter(user_id=request.user.id).order_by('-data').values()
        list_month = movimenti.objects.dates('data', 'month').filter(user_id=request.user.id)
        tot = calcola_totale(list_mov)
        form = MovimentiForm()

        if request.method == 'POST':
            form = MovimentiForm(request.POST)
            print(form.errors)
            if form.is_valid():
                form_list = form.save(commit=False)
                form_list.user_id = request.user
                form_list.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                form = MovimentiForm()


        return render(request, 'moneymanager.html', {'list_mov':list_mov, 'form':form, 'tot':tot, 'list_month':list_month})
    else:
        return redirect('login_user')


def add_movimenti(request):
    if request.method == 'POST':
        form = MovimentiForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form_list = form.save(commit=False)
            form_list.user_id = request.user
            form_list.save()
            return HttpResponseRedirect('index')




def calcola_totale(list_mov):
    totale = 0

    for x in list_mov:
        if x.get("tipologia") == "+":
            str_conc = x.get("tipologia") + str(x.get("cifra"))
            num = float(str_conc)
            totale = round(totale +  num, 2)
        elif x.get("tipologia") == "-":
            str_conc = x.get("tipologia") + str(x.get("cifra"))
            num = float(str_conc)
            totale = round(totale +  num, 2)

    return totale

def delete(request, id):
  mov = movimenti.objects.get(id=id)
  mov.delete()
  return HttpResponseRedirect(reverse('index'))
