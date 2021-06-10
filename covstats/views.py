from django.shortcuts import render, redirect

def cases(request):
    return render(request,'covstats/cases.html',{'page_title':'Cases Live Update'})

def vaccine(request):
    return render(request,'covstats/vaccine.html',{'page_title':'Vaccination Live status'})