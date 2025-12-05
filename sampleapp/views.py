from django.shortcuts import render,HttpResponse,redirect
from .models import Student,User,Teacher
from django.contrib.auth  import authenticate,logout,login
# Create your views here.
def home(request):
    return render(request,"home.html")

def studentregister(request):
    if request.method=="POST":
         f=request.POST["firstname"] 
         l=request.POST["lastname"] 
         e=request.POST["email"]
         a=request.POST["address"] 
         ph=request.POST["phonenumber"] 
         g=request.POST["guardian"] 
         u=request.POST["username"] 
         p=request.POST["password"] 
         new_user=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,address=a,phone_number=ph,usertype='student',is_active=False)
         new_user.save()
         x=Student.objects.create(Student_id=new_user,guardian=g)
         x.save()
         return HttpResponse("register succesfully")
    else:
         return render(request,"studentregister.html")   
    
def teacheregister(request):
    if request.method=="POST":
            f=request.POST["firstname"] 
            l=request.POST["lastname"] 
            e=request.POST["email"]
            a=request.POST["address"] 
            ph=request.POST["phonenumber"] 
            s=request.POST["salary"] 
            u=request.POST["username"] 
            p=request.POST["password"] 
            exp=request.POST["experience"] 

            new_user=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,address=a,phone_number=ph,usertype='teacher',is_active=True,is_staff=True )
            new_user.save()
            x=Teacher.objects.create(salary=s,experience=exp,teacher_id=new_user)
            x.save()
            # return redirect('login')
            return HttpResponse("teacher register successfull")
    else:
            return render(request,"teacheregister.html") 
    
def logins(request):
    if request.method=="POST":
          u=request.POST['username']
          p=request.POST['password']
          userpass=authenticate(request,username=u,password=p)
          if  userpass is not None  and userpass.is_superuser==1:
               return redirect('adminhome')
          elif  userpass is not None  and userpass.is_staff==1:
               login(request,userpass)
               request.session['teach_id']=userpass.id
               return redirect("teacherhome")
          elif  userpass is not None  and userpass.is_active==1:
               login(request,userpass)
               request.session['stud_id']=userpass.id
               return redirect("studenthome")
          else:
               return HttpResponse("invalid login")
    else:
         return render(request,'login.html')

def adminhome(request):
     return render(request,'adminhome.html')    
    
def teacherhome(request):
    return render(request,'teacherhome.html')

def studenthome(request):
    return render(request,'studenthome.html')

def View_student_admin(request):
     x=Student.objects.all()
     return render(request,"view_student.html",{"view":x})

def View_student_teacher(request):
     x=Student.objects.all()
     return render(request,"View_student_teacher.html",{"view":x})

def view_teacher(request):
     y=Teacher.objects.all()
     return render(request,"viewteacher.html",{"data":y})

def view_teacher_student(request):
     y=Teacher.objects.all()
     return render(request,"view_teacher_student.html",{"data":y})

def approve_student(request,id):
     stud=Student.objects.select_related('Student_id').get(id=id)
     stud.Student_id.is_active=True
     stud.Student_id.save()
     return redirect('View_student_admin')

     
def delete(request,id):
    stud=Student.objects.get(id=id)
    user_id=stud.Student_id.id
    stud.delete()
    user=User.objects.get(id=user_id)
    user.delete()
    return redirect(View_student_admin)

def tdelete(request,id):
    teach=Teacher.objects.get(id=id)
    user_id=teach.teacher_id.id
    teach.delete()
    User.objects.get(id=user_id).delete()
    return redirect("view_teacher")



def editteacher(request):
   teach=request.session.get('teach_id')
   print(teach)

   user=User.objects.get(id=teach)
   print(user)
   teacher=Teacher.objects.get(teacher_id=teach)


   return render(request,"editteacher.html",{"view": teacher,"data":user})

def updateteacher(request,id):
    if request.method == "POST":
         teach=Teacher.objects.get(id=id)
         uid=teach.teacher_id_id
         user=User.objects.get(id=uid)
         user.first_name=request.POST["firstname"] 
         user.last_name=request.POST["lastname"] 
         user.email=request.POST["email"]
         user.address=request.POST["address"] 
         user.phone_number=request.POST["phonenumber"] 
         teach.salary=request.POST["salary"] 
         teach.experience=request.POST["experience"] 

         user.save()
         teach.save()

         return redirect(view_teacher) 




def editstudent(request):
    stud=request.session.get('stud_id')

    student=Student.objects.get(Student_id_id=stud)
    user=User.objects.get(id=stud)


    return render(request,"editstudent.html",{"view": student,"data":user})


def updatestudent(request,id):


    if request.method == "POST":
         stud=Student.objects.get(id=id)
         uid=stud.Student_id_id
         user=User.objects.get(id=uid)
         user.first_name=request.POST["firstname"] 
         user.last_name=request.POST["lastname"] 
         user.email=request.POST["email"]
         user.address=request.POST["address"] 
         user.phone_number=request.POST["phonenumber"] 
         stud.guardian=request.POST["guardian"] 
         user.save()
         stud.save()

         return redirect(View_student_admin)  #function name

def logouts(request):
    if "stud_id" in request.session:
        del request.session['stud_id']
    else:
        if "teach_id" in request.session:
            del request.session['teach_id']
            logout(request)
    return redirect("logins")


def bootstrap(request):
     return render(request,"index.html")