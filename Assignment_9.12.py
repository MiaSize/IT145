from module_user import Users
from module_admin import Admin

new_admin = Admin('mari','hawkinss',18,'Ypsilanti','Admin')
new_admin.privileges.show_privileges()

new_admin = Users('mari','hawkinss',18,'Ypsilanti','Admin')
new_admin.describe_user()
