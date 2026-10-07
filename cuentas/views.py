import json

from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect, render


USUARIOS_JSON = r"""
[
  {
    "usuario": "admin",
    "nombre": "Administrador",
    "rol": "admin",
    "password": "alvarito2026"
  },
  {
    "usuario": "cliente",
    "nombre": "Cliente Demo",
    "rol": "cliente",
    "password": "demo1234"
  }
]
"""

usuarios = json.loads(USUARIOS_JSON)


def buscarUsuario(nombreUsuario):
    for u in usuarios:
        if u["usuario"] == nombreUsuario:
            return u
    return None


def ingresar(request):
  
    if request.method == "POST":
        nombreUsuario = request.POST.get("usuario", "").strip()
        clave = request.POST.get("password", "")

        u = buscarUsuario(nombreUsuario)

        if u is not None and clave == u["password"]:
            request.session["usuario"] = u["usuario"]
            request.session["nombre"] = u["nombre"]
            request.session["rol"] = u["rol"]
            return redirect("catalogo:lista")


        contexto = {
            "error": "Usuario o contraseña incorrectos.",
            "usuario": nombreUsuario,
        }
        return render(request, "cuentas/ingresar.html", contexto)

    return render(request, "cuentas/ingresar.html")


def salir(request):
    request.session.flush()
    return redirect("catalogo:inicio")
