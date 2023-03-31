from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound ,Http404
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.

challenges = {
    "january" : "Don't eat meat for the entire month",
    "feburary" : "Walk for twenty minutes a day",
    "march" : "Learn Django twenty minutes a day",
    "april" : "Do what ever you want",
    "may" : "Confess your love",
    "june" : "Go for a long vacation",
    "july" : "Kill Your depression",
    "august" : "This is the month India got independence",
    "september" : "Your birthday month",
    "october" : "Gandhi's birthday month",
    "november" : "Just enjoy this entire month.",
    "december" : "Waiting for the next year"
}

def index(request):
    months = list(challenges.keys())
   
    return render(request,"challenges/index.html",{
        "months" : months
    })


def challenges_text(request, month):
    try:
        challenge_month=challenges[month]
        return render(request,"challenges/challenge.html",{
            "text" : challenge_month,
            "month_name" : month
        })

    except:
        raise Http404()        

    