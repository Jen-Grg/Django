from django.shortcuts import render
from user.auth import admin_only
# Create your views here.
@admin_only
def adminpage(request):
    return render(request, 'admins/index.html')