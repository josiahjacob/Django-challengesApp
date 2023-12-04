from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


monthly_challenges={
    'january': "Eat no meat",
    'februay':"Eat no meat",
    'march':"Eat no meat",
    'april':"Eat no meat",
    'may':"Eat no meat",
    'june':"Eat no meat",
    'july':"Eat no meat",
    'august':"Eat no meat",
    'september':"Eat no meat",
    'october':"Eat no meat",
    'november':"Eat no meat",
    'december':"Eat no meat"
}

# Create your views here.
# def jan(request):
#     return HttpResponse("Eat no meat")
# def feb(request):
#     return HttpResponse("Walk for 20 mins aday")
# def march(request):
#     return HttpResponse("Walk for 20 mins aday")


def home(request):
    list_items=''
    months= list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month=month.capitalize()
        month_path=reverse('month-challenge',args=[month])
        list_items+=f'<li><a href=\'{month_path}\'>{capitalized_month}</li>'

    response_text=f'<ul>{list_items}</ul>' 

    return HttpResponse(response_text)

def monthly_challenge_by_num(request, month):
    try:
        months=list(monthly_challenges.keys())
        redirect_path=reverse('month-challenge',args=[months[month-1]])
        return HttpResponseRedirect(redirect_path)
        # return HttpResponseRedirect("/challenges/"+months[month-1])
    except:
        return HttpResponseNotFound("This month is not valid")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month] 
        response_text=f'<h1>{challenge_text}</h1>'
        return HttpResponse(response_text)
    except:
        return HttpResponseNotFound("<h1>This month is not valid</h1>")


    # return("Hi")
