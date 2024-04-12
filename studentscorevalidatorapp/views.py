from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")


def display_fun(request):
    n = request.POST['txtname']
    s1 = int(request.POST['txtpython'])
    s2 = int(request.POST['txtjava'])
    s3 = int(request.POST['txtmysql'])
    s4 = int(request.POST['txthtml'])
    s5 = int(request.POST['txtdjango'])
    v1 = request.POST['operation']
    if v1 == "TOTAL" :
        result = s1+s2+s3+s4+s5
    elif v1 == "PERCENTAGE":
        total_sum = s1 + s2 + s3 + s4 + s5
        result = (total_sum /500)*100
    elif v1 == "GRADE":
        total_sum = s1 + s2 + s3 + s4 + s5
        percentage = (total_sum / 500) * 100
        if percentage > 90:
            result = "A"
        elif 80 < percentage <= 90:  # Changed from '80 > percentage <= 90' to '80 < percentage <= 90'
            result = "B"
        elif 70 < percentage <= 80:  # Changed from '70 > percentage <= 80' to '70 < percentage <= 80'
            result = "C"
        elif 60 < percentage <= 70:  # Changed from '60 > percentage <= 70' to '60 < percentage <= 70'
            result = "D"
        elif 50 < percentage <= 60:  # Changed from '50 > percentage <= 60' to '50 < percentage <= 60'
            result = "E"
        else:  # Changed from 'elif percentage <= 50' to 'else'
            result = "F"

    elif v1 == "STATUS" :
        total_sum = s1 + s2 + s3 + s4 + s5
        percentage = (total_sum / 500) * 100
        if percentage > 50:
            result = "PASS"
        else:
            result = "FAIL"

    else:
        result = 0



    return render(request,"home.html",{"n":n,
                                       "s1":s1,
                                       "s2":s2,
                                       "s3":s3,
                                       "s4":s4,
                                       "s5":s5,
                                       "res":result})