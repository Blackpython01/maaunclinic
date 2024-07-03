from django.shortcuts import render, HttpResponse
from . models import studentclinicfile

# Create your views here.

def upload(request):
    if request.method == "POST":
        full_name = request.POST.get("f_name")  
        matric_no = request.POST.get("matric_no")  
        Department = request.POST.get("depart")  
        courses = request.POST.get("courses")  
        level = request.POST.get("level")   
        email = request.POST.get("email")  
        phone_num = request.POST.get("phone_num") 

        file = request.FILES.getlist('file_1')
        print(file)
        for f in file:
           studentclinicfile.objects.create(full_name=full_name, 
                                           matric_no=matric_no, 
                                           Department=Department, 
                                           courses=courses, 
                                           level=level, 
                                           email=email, 
                                           phone_num=phone_num, 
                                           file_1=f)
        print(file)
        return render(request, "next.html")
    data = studentclinicfile.objects.all()
    return render(request, "upload.html", locals())

