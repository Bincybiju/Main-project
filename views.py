from django.shortcuts import render
from django.shortcuts import redirect ,HttpResponse
import datetime
from datetime import date
import time
from django.core.files.storage import FileSystemStorage
from .models import login as log,Staff as stf,User as usr,Report as rep,Fine as fin, Payment as pay,Complaint as comp
# Create your views here.
def index(request):
    if(request.session.get('role', ' ')=="admin"):
            response = redirect('/AdminHome')
            return response
    elif (request.session.get('role', ' ')== "staff"):
            response = redirect('/StaffHome')
            return response
    elif (request.session.get('role', ' ')== "user"):
            response = redirect('/UserHome')
            return response
    else:
            return render(request,"index.html",{"msg":""})

def AdminHome(request):
    return render(request,"adminhome.html",{"msg":""})
def pays(request):
        msg=""
        amt=request.GET["amt"]
        ids=request.GET["id"]
        if request.POST:
                t1=request.POST["t1"]
                t2=request.POST["t2"]
                t3=request.POST["t3"]
                today = date.today()
                datax=usr.objects.get(Log_id=request.session["id"])
                datay=fin.objects.get(fine_id=ids)
                fin.objects.filter(fine_id=ids).update(Fine_status="paid")
                pay.objects.create(Fine_id=datay,Pay_amount=t3,Pay_on=today,Pay_status="pending",User_id=datax)
        return render(request,"pay.html",{"msg":msg,"amt":amt,"id":ids})
def alert(request):
        msg="report generated"
        t1=request.GET["id"]
        datau=usr.objects.get(User_id=t1)
        today = date.today()
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        rep.objects.create(User_id=datau ,Report_date=today,Report_time=current_time,Report_status="pending")
        return HttpResponse(msg) 
def UserHome(request):
    return render(request,"userhome.html",{"msg":""})

def StaffHome(request):
    return render(request,"staffhome.html",{"msg":""})
def Logout(request):
    try:
        del request.session['id']
        del request.session['role']
        del request.session['username']
        response = redirect("/index")
        return response
    except:
        response = redirect("/index")
        return response
def Our_Staff(request):
        msg = ""
        data1=stf.objects.all()
        return render(request,"View_staff.html",{"msg":msg,"data":data1})
def Our_Users(request):
        msg = ""
        data1=usr.objects.all()
        return render(request,"View_user.html",{"msg":msg,"data":data1})
def delete_staff(request):
    stf.objects.filter(Staff_id=request.GET["id"]).delete()
    response = redirect('/Our_Staff')
    return response

def delete_user(request):
    usr.objects.filter(User_id=request.GET["id"]).delete()
    response = redirect('/Our_Users')
    return response
def Current_Users(request):
        msg = ""
        data1=usr.objects.all()
        return render(request,"View_user1.html",{"msg":msg,"data":data1})
def delete_user1(request):
    usr.objects.filter(User_id=request.GET["id"]).delete()
    response = redirect('/Current_Users')
    return response
    
def Appoint_Staff(request):
    msg=""
    if request.POST:
        t1 = request.POST["t1"]
        t2 = request.POST["t2"]
        t3 = request.POST["t3"]
        t4 = request.POST["t4"]
        t5 = request.POST["t5"]
        t6=",".join(request.POST.getlist('t6'))
        
    
        t8 = request.FILES["t8"]
        fs = FileSystemStorage()
        fs.save(t8.name, t8)
        t9 = request.POST["t9"]
        t10 = request.POST["t10"]
        log.objects.create(username=t9, password=t10, role="staff")
        data=log.objects.last()
        stf.objects.create(Staff_name=t1,Staff_address=t2,Staff_email=t3,Staff_phone=t4,Staff_qualification=t6, Staff_designation=t5,Staff_photo=t8,Staff_status="approved",Staff_logid=data)
        msg="updated successfuly"
        #return HttpResponse(t6)
    else:    
        msg = ""
    
    return render(request,"Add_staff.html",{"msg":msg}) 
def Login(request):
        if request.POST:
                user=request.POST["t1"]
                password=request.POST["t2"]
                try:
                        data=log.objects.get(username=user,password=password)
                        if(data.role=="admin"):
                                request.session['username'] = data.username
                                request.session['role'] = data.role
                                request.session['id'] = data.log_id
                                response = redirect('/AdminHome')
                                return response
                        elif (data.role=="user"):
                                request.session['username'] = data.username
                                request.session['role'] = data.role
                                request.session['id'] = data.log_id
                                response = redirect('/UserHome')
                                return response
                        elif (data.role=="staff"):
                                request.session['username'] = data.username
                                request.session['role'] = data.role
                                request.session['id'] = data.log_id
                                response = redirect('/StaffHome')
                                return response
                        else:
                                return render(request, "index.html", {"msg":"invalid account Details"})
                except:
                        return render(request, "index.html", {"msg":"invalid user name of password"})
        else:
                response = redirect('/index')
                return response

def Register_vehicle(request):
        msg=""
        if request.POST:
                t1 = request.POST["t1"]
                t2 = request.POST["t2"]
                t3 = request.POST["t3"]
                t4 = request.POST["t4"]
                t5 = request.POST["t5"]
                t6 = request.POST["t6"]
                t7 = request.POST["t7"]
        
    
                log.objects.create(username=t5, password=t4, role="user")
                data=log.objects.last()
                usr.objects.create(Owner_name=t1,Owner_address=t2,Owner_email=t3,Owner_phone=t4,Vechile_no=t5,Vechile_type=t6,Vechile_details=t7,Log_id=data)
                msg="updated successfuly"
        else:    
                msg = ""
    
        return render(request,"Add_vehicle.html",{"msg":msg}) 

def Privacy(request):
    msg=""
    if request.POST:
        t1=request.POST["t1"]
        t2=request.POST["t2"]
        id=request.session["id"]
        data=log.objects.get(log_id=id)
        if data.password==t1:
            msg="sucessfully updated"
            log.objects.filter(log_id=id).update(password=t2)
        else:
            msg="invalid current password"
    returnpage="adminhead.html"
    if request.session["role"] == "user":
        returnpage="userhead.html"
    elif request.session["role"] =="staff":
        returnpage="staffhead.html"
    return render(request, "privacy.html",{"role":returnpage,"msg":msg})

def Manage_complaints(request):
        msg=""
        #datay=log.objects.get(log_id=request.session["id"])
        datax=usr.objects.get(Log_id=request.session["id"])
        if request.POST:
                t1 = request.POST["t1"]
                t2 = request.POST["t2"]
                today = date.today()
                
                msg="posted sucessfully"
                comp.objects.create(Complaint_subject=t1,Complaint_message=t2,Complaint_date=today,Complaint_reply="not yet Seen",User_id=datax)
        data1=comp.objects.all()
        #.filter(User_id=datax)
        return render(request, "Add_complaints.html",{"msg":msg,"data":data1})

def complaints(request):
        msg=""
        #datax=usr.objects.get(Log_id=request.session["id"])
        if request.POST:
                t1 = request.POST["t1"]
                t2 = request.POST["t2"]
                
                msg="updated sucessfully"
                comp.objects.filter(Complaint_id=t1).update(Complaint_reply=t2)
        data1=comp.objects.all()
        return render(request, "Answer_Queries.html",{"msg":msg,"data":data1})

def my_reports(request):
        msg=""
        datax=usr.objects.get(Log_id=request.session["id"])
        
        data1=fin.objects.filter(User_id=datax).all()
        return render(request, "View_reports.html",{"msg":msg,"data":data1})

def my_Payemnts(request):
        msg=""
        datax=usr.objects.get(Log_id=request.session["id"])
        #data1=rep.objects.get(User_id=datax)
        data1=pay.objects.filter(User_id=datax).all()
        return render(request, "View_payments.html",{"msg":msg,"data":data1})

def fine_pay(request):
        msg=""
      
        data1=pay.objects.all()
        return render(request, "all_payments.html",{"msg":msg,"data":data1})
import os
import shutil
from django.conf import settings
def reports(request):
        msg=""
        if request.POST:
                t1 = request.POST["t1"]
                t2 = request.POST["t2"]
                t3 = request.POST["t3"]
                t4 = request.POST["t4"]
                today = date.today()
                #datax=usr.objects.get(User_id=t2)
               # dataz=rep.objects.get(Report_id=t1)
                datay=stf.objects.get(Staff_logid=request.session["id"])
                msg="updated sucessfully"
                #rep.objects.filter(Report_id=t1).update(Report_status="verifyed")
                fin.objects.create(Fine_amount=t3,Fine_date=today,Fine_details=t4, Staff_id=datay,Fine_status="pending",Fine_vehicle=t2)
        

        #output_dir = os.path.join(settings.BASE_DIR, 'helmet_detection_webservice/output')
        #media_dir = os.path.join(settings.BASE_DIR, '', 'other_project', 'media', 'output')
        for filename in os.listdir('Bike/res'):
         if filename.endswith('.jpg') or filename.endswith('.png'):
            src_file = os.path.join("D:\project2023\helmet\Bike\\res", filename)
            dst_file = os.path.join("D:\project2023\helmet\media", filename)
            shutil.copy(src_file, dst_file)

       # data1=rep.objects.filter(Report_status="pending").all()
        image_files = []
        for filename in os.listdir('Bike/res'):
         if filename.endswith('.jpg') or filename.endswith('.png'):
            image_files.append(filename)
        return render(request, 'all_report.html', {'image_files': image_files})
        #return render(request, "all_report.html",{"msg":msg,"data":data1})
def fine_report(request):
        msg=""
        datay=stf.objects.get(Staff_logid=request.session["id"])
        data1=fin.objects.filter(Staff_id=datay).all()
        return render(request, "all_fine.html",{"msg":msg,"data":data1})