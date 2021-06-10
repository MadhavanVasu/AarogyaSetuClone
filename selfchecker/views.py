from django.shortcuts import render, redirect
import joblib
import requests


def checkform(request):
    if request.method == 'POST':
        cls = joblib.load('static/finalized_model.sav')
        l = [0 for i in range(5)]
        s = ['Cough','Fever','Sore throat','Shortness of breathe','Headache']
        if(request.POST['cough'] == 'YES'):
            l[0] = 1
        if(request.POST['fever'] == 'YES'):
            l[1] = 1
        if(request.POST['sore'] == 'YES'):
            l[2] = 1
        if(request.POST['short'] == 'YES'):
            l[3] = 1
        if(request.POST['head'] == 'YES'):
            l[4] = 1
        ans = cls.predict([l])
        print(type(ans[0]), ans[0])
        r = 1
        if(ans[0] == 0):
            r = 0

        data = request.POST['number']

        url = "https://www.fast2sms.com/dev/bulkV2"

        msg = 'Symptoms:\n'

        for i in range(5):
            temp = ''
            if(l[i]==0):
                temp = '\3t' + s[i]+ ' : ' + 'No'
            else:
                temp = '\3t' + s[i]+ ' : ' + 'Yes'
            temp+='\n'
            msg+=temp
        msg+='\n'
        if(r==0):
            temp = 'THE PROBABILITY THAT YOU HAVE CONTRACTED THE VIRUS IS LOW!!BUT,PLEASE MAINTAIN SOCIAL DISTANCING AND FOLLOW OTHER COVID-19 PROTOCOLS!!GET VACCINATED AS SOON AS POSSIBLE'
            msg+=temp
        
        else:
            temp = 'PLEASE VISIT THE NEARBY HOSPITAL AND TAKE A COVID-19 TEST IMMEDIATELY!!STAY SAFE!!'
            msg+=temp
        
        querystring = {"authorization": "ECrz5SXvjdxTeWFRZOaBNQfuwLYmKt2b7MoIk0c89J1Psgh6yV8a4P5gNlwoAi9KWrGdOM2vZCXq3Ucn", "sender_id": "TXTIND", "message": msg, "route": "v3", "numbers": data}

        headers = {
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)
        return render(request, 'selfchecker/result.html', {'symptoms': l, 'result': r})



    else:
        return render(request, 'selfchecker/myform.html',{'page_title':'Self-Checker'})

