from django.shortcuts import redirect

#give access to admin in adminpage, if request comes from normal user then no access should be given,.
def admin_only(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_staff:
            return view_function(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_function
