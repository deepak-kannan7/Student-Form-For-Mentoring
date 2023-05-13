from django.shortcuts import render
from .models import *  
from django.http import HttpResponseRedirect
# Create your views here.
def attendance_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        att1 = request.POST.get('att1')
        att2 = request.POST.get('att2')
        att3 = request.POST.get('att3')
        att4 = request.POST.get('att4')
        att5 = request.POST.get('att5')
        att6 = request.POST.get('att6')

        att_obj = attendance(name=name, rollno=rollno, att1=att1, att2=att2, att3=att3, att4=att4, att5=att5, att6=att6)
        att_obj.save()
        return HttpResponseRedirect('/marksent/')

    return render(request, template_name="studform.html")

def mark_enter(request):
    if request.method == "POST":
        mark1 = request.POST.get('mark1')
        mark2 = request.POST.get('mark2')
        mark3 = request.POST.get('mark3')
        mark4 = request.POST.get('mark4')
        mark5 = request.POST.get('mark5')
        mark6 = request.POST.get('mark6')

        mark_obj = marks(mark1=mark1, mark2=mark2, mark3=mark3, mark4=mark4, mark5=mark5, mark6=mark6)
        mark_obj.save()
        return HttpResponseRedirect('/parentsform/')

    return render(request, template_name="marks.html")

def display_view(request):
    objs = attendance.objects.all()
    return render(request, "teacher.html", {'objs': objs})

def mark_view(request):
    obj1= marks.objects.all()
    return render(request,"teachermark.html",{'objs':obj1})

def next_page(request):
    return render(request, "parentdetails.html")

def home_page(request):
    return render(request, "index.html")

def cgpa_view(request):
    return render(request,"cgpa.html")

def faq_view(request):
    return render(request,"faq.html")

def stud_page(request):
    return render(request, "student.html")

def extrac_view(request):
    return render(request, "ecactivities.html")

def meetings_page(request):
    return render(request, "meetingdet.html")

def marks_page(request):
    return render(request, "firstsemmarks.html")


