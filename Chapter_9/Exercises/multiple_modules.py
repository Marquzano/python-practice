from new_admin import Admin

privileges = ['can add post', 'can delete post', 'can ban user', 'can view passwords...']
admin = Admin('angel', 'marquez', 24, 'software engineer', False, privileges)

admin.privileges.show_privileges()