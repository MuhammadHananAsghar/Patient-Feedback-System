from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .con import MYSQLConnection

# Conenction
mysql = MYSQLConnection()
conx = mysql.conn()

class Login(View):
    """
    Login View
    """
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Registration(View):
    """
    Login View
    """
    template_name = "register.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        data = request.POST
        name = data.get("username")
        email = data.get("useremail")
        password = data.get("userpass")
        user_no = mysql.insert(conx, name, email, password, admin=0)
        print(user_no)
        return HttpResponse("Submitted")