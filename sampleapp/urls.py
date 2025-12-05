from django.urls import path
from sampleapp import views

urlpatterns = [
    path("",views.home,name="home"),
    path("studentregister",views.studentregister,name="studentregister"),
    path("tregister",views.teacheregister,name="teacheregister"),
    path("login",views.logins,name="logins"),
    path("teacherhome",views.teacherhome,name="teacherhome"),
    path("studenthome",views.studenthome,name="studenthome"),
    path("adminhome",views.adminhome,name="adminhome"),
    path("View_student_admin",views.View_student_admin,name="View_student_admin"),
    path("view_teacher",views.view_teacher,name="view_teacher"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("tdelete/<int:id>",views.tdelete,name="tdelete"),
    path("editteacher",views.editteacher,name="editteacher"),
    path("updateteacher/<int:id>",views.updateteacher,name="updateteacher"),
    path("editstudent",views.editstudent,name="editstudent"),
    path("updatestudent/<int:id>",views.updatestudent,name="updatestudent"),
    path("View_student_teacher",views.View_student_teacher,name="View_student_teacher"),
   path("approve_student/<int:id>",views.approve_student,name="approve_student"),
    path("view_teacher_student",views.view_teacher_student,name="view_teacher_student"),
    path("logouts",views.logouts,name="logouts"),
  path("bootstrap",views.bootstrap,name="bootstrap")
  ]