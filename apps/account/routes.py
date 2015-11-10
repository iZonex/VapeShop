from .views import memberview, memberadmin
from grab_routes import routerutil

# Route for Member View

routerutil.routes_list += [
    ('POST', '/account/login', memberview.login),
    ('POST', '/account/logout', memberview.logout),
    ('POST', '/account/profile', memberview.profile),
    ('POST', '/account/register', memberview.register),
    ('POST', '/account/register/confirm/{code}', memberview.reg_confirm)
]
# Route for Admin Member View

routerutil.routes_list += [
    ('POST', '/admin/account/create', memberadmin.create),
    ('GET', '/admin/account/{id}', memberadmin.get_member),
    ('GET', '/admin/account', memberadmin.get_members),
    ('POST', '/admin/account/remove', memberadmin.remove)
]
