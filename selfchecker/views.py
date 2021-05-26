from django.shortcuts import render, redirect
import joblib

def checkform(request):
    if request.method == 'POST':
        cls = joblib.load('static/finalized_model.sav')
        l = [0 for i in range(5)]
        if(request.POST['cough']==1):
            l[0] = 1
        if(request.POST['fever']==1):
            l[1] = 1
        if(request.POST['sore']==1):
            l[2] = 1
        if(request.POST['breath']==1):
            l[3] = 1
        if(request.POST['hache']==1):
            l[4] = 1

        ans = cls.predict([l])
        print(ans[0])
        r = 1
        if(ans[0]=='0'):
            r=0 
        return render(request, 'selfchecker/result.html',{'symptoms':l,'result':r})



    else:
        return render(request, 'selfchecker/myform.html',{'page_title':'Self-Checker'})

