from FirebaseCredentials.Firebase import db

def get_admin(project_id):
   all_users=db.child("Users").get()
   a=[]
   for user in all_users.each():
       employee_id=user.key()
       status=db.child("Users/"+employee_id+"/profile/status").get().val()
       if status == "admin":
           a.append(employee_id)
   for admin in a:
      projects= db.child("Users/"+admin+"/Projects").get().each()
      for project in projects:
          admin_project_id=project.key()
          if admin_project_id==project_id:
              admin_id=admin
              break
   return(admin_id)


