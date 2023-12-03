from django.urls import path , include
from .views import login , register ,logout ,create_reclamation,liste_reclamtions,delete_reclamation,create_course,liste_courses,delete_course,create_material,update_course,liste_material,update_material,delete_material,create_assignement,liste_assignement,update_assignement,delete_assignement,add_student,delete_student,liste_enrollement
urlpatterns = [
    path('login',login),
    path('logout',logout),
    path('register',register),
    
    path('create_reclamation',create_reclamation),
    path('liste_reclamtions',liste_reclamtions),
    path('delete_reclamation/<int:reclamation_id>/',delete_reclamation),
    
    path('create_course',create_course),
    path('liste_courses',liste_courses),
    path('update_course/<int:course_id>/',update_course),
    path('delete_course/<int:course_id>/',delete_course),
    
    path('create_material/<int:course_id>/',create_material),
    path('liste_material/<int:course_id>/',liste_material),
    path('update_material/<int:course_id>/<int:material_id>/',update_material),
    path('delete_material/<int:course_id>/<int:material_id>/',delete_material),
    
    path('create_assignement/<int:course_id>/',create_assignement),
    path('liste_assignement/<int:course_id>/',liste_assignement),
    path('update_assignement/<int:course_id>/<int:assignement_id>/',update_assignement),
    path('delete_assignement/<int:course_id>/<int:assignement_id>/',delete_assignement),
    
    path('add_student/<int:course_id>/<int:student_id>/',add_student),
    path('delete_student/<int:course_id>/<int:student_id>/',delete_student),
    path('liste_enrollement/<int:course_id>/',liste_enrollement),



]
