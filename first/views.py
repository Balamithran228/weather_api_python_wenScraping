from django.shortcuts import render, redirect
from first.models import CustomerRegisterDB
from first.forms import CustomerRegisterForm
from django.contrib import messages
import requests
from bs4 import BeautifulSoup as bs


def get_html_content(city):
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    city = city.replace(' ', '+')
    html_content = session.get(f'https://www.google.com/search?q=weather+in+{city}').text
    return html_content

def Weather(request):

    result = None
    if 'city' in request.GET:
        city = request.GET.get('city')
        html_content = get_html_content(city)
        soup = bs(html_content, 'html.parser')
        result = dict()


        result['region'] = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
        result['temperature'] = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
        result['dayhour'], result['weather_now'] = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text.split('\n')

    return render(request, "base.html", {'result': result})


def hello(request, username):
    mydict = {"name": username}
    messages.success(request, 'sucessfully with logged in.')
    return render(request, "home.html", mydict)


def CustomerLogin(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        try:
            form = CustomerRegisterDB.objects.get(cpassword1=password)
            if form is not None:
                return redirect('home/'+username+'/')

        except:
            messages.info(request, "USERNAME or PASSWORD IS INCORRECT")

    mydict={}
    return render(request, "c_login.html", mydict)


def CustomerRegister(request):
    form = CustomerRegisterForm()
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')

    mydict = {"form": form}
    return render(request, "c_register.html", mydict)
