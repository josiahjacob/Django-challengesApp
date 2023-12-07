from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges={
    'january': "Eat no meat",
    'februay':"Go for a walk for atleat 20 min every day!",
    'march':"Eat no meat",
    'april':"Go for a walk for atleat 20 min every day!",
    'may':"Eat no meat",
    'june':"Go for a walk for atleat 20 min every day!",
    'july':"Eat no meat",
    'august':"Go for a walk for atleat 20 min every day!",
    'september':"Eat no meat",
    'october':"Go for a walk for atleat 20 min every day!",
    'november':"Eat no meat",
    'december':None
    # 'december':"Go for a walk for atleat 20 min every day!"
}

# Create your views here.
# def jan(request):
#     return HttpResponse("Eat no meat")
# def feb(request):
#     return HttpResponse("Walk for 20 mins aday")
# def march(request):
#     return HttpResponse("Walk for 20 mins aday")


def home(request):
    # list_items=''
    months= list(monthly_challenges.keys())
    
    # for month in months:
    #     capitalized_month=month.capitalize()
    #     month_path=reverse('month-challenge',args=[month])
    #     list_items+=f'<li><a href=\'{month_path}\'>{capitalized_month}</a></li>'

    # response_text=f'<ul>{list_items}</ul>' 

    return render(request,'challenges/index.html',{
        'month_list':months,
        
    })

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
        # response_text=f'<h1>{challenge_text}</h1>'
        # response_text=render_to_string('challenges/challenge.html')
        # return HttpResponse(response_text)

        return render(request,'challenges/challenge.html',{
            'text':challenge_text,
            'challenge_month':month
        })
    except:
        raise Http404()
        # return HttpResponseNotFound(render_to_string('404.html'))


    # return("Hi")
