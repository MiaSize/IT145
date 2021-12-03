from module_admin import Users,Privileges,Admin

new_admin = Admin('mari','hawkinss',18,'Ypsilanti','Admin')
new_admin.privileges.show_privileges()

new_users = Users('mari','hawkinss',18,'Ypsilanti','Admin')
new_users.greet_user()
