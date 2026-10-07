import json

from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.utils.html import escape



PRODUCTOS_JSON = r"""
[
  { "id": 1,  "nombre": "Martillo carpintero 16 oz",              "categoria": "Herramientas manuales",   "precio": 8990,   "stock": 45 },
  { "id": 2,  "nombre": "Destornillador Phillips #2",              "categoria": "Herramientas manuales",   "precio": 3490,   "stock": 120 },
  { "id": 3,  "nombre": "Set destornilladores 6 piezas",           "categoria": "Herramientas manuales",   "precio": 12990,  "stock": 30 },
    { "id": 4,  "nombre": "Alicate universal 8\"",                    "categoria": "Herramientas manuales",   "precio": 7490,   "stock": 60 },
    { "id": 5,  "nombre": "Llave ajustable 10\"",                     "categoria": "Herramientas manuales",   "precio": 9990,   "stock": 40 },
  { "id": 6,  "nombre": "Huincha de medir 5 m",                     "categoria": "Medición",                "precio": 4990,   "stock": 85 },
  { "id": 7,  "nombre": "Nivel de burbuja 60 cm",                   "categoria": "Medición",                "precio": 11990,  "stock": 0 },
    { "id": 8,  "nombre": "Escuadra metálica 12\"",                   "categoria": "Medición",                "precio": 6490,   "stock": 33 },
  { "id": 9,  "nombre": "Taladro percutor 650 W",                   "categoria": "Herramientas eléctricas", "precio": 39990,  "stock": 18 },
  { "id": 10, "nombre": "Atornillador inalámbrico 12 V",            "categoria": "Herramientas eléctricas", "precio": 49990,  "stock": 15 },
    { "id": 11, "nombre": "Esmeril angular 4-1/2\" 820 W",            "categoria": "Herramientas eléctricas", "precio": 34990,  "stock": 20 },
    { "id": 12, "nombre": "Sierra circular 7-1/4\" 1400 W",           "categoria": "Herramientas eléctricas", "precio": 59990,  "stock": 0 },
  { "id": 13, "nombre": "Lijadora orbital 240 W",                   "categoria": "Herramientas eléctricas", "precio": 29990,  "stock": 22 },
  { "id": 14, "nombre": "Set brocas para metal 19 pzas",            "categoria": "Accesorios eléctricos",   "precio": 14990,  "stock": 40 },
    { "id": 15, "nombre": "Disco de corte metal 4-1/2\"",             "categoria": "Accesorios eléctricos",   "precio": 990,    "stock": 300 },
  { "id": 16, "nombre": "Hoja de sierra circular 40 dientes",       "categoria": "Accesorios eléctricos",   "precio": 8990,   "stock": 35 },
    { "id": 17, "nombre": "Tornillo autoperforante 8x1\" (100 u)",    "categoria": "Fijaciones",              "precio": 3990,   "stock": 150 },
    { "id": 18, "nombre": "Clavo 2\" 1 kg",                           "categoria": "Fijaciones",              "precio": 2490,   "stock": 200 },
  { "id": 19, "nombre": "Tarugo plástico 6 mm (100 u)",             "categoria": "Fijaciones",              "precio": 2990,   "stock": 0 },
    { "id": 20, "nombre": "Perno hexagonal 1/2\" x 3\" (10 u)",       "categoria": "Fijaciones",              "precio": 4490,   "stock": 90 },
  { "id": 21, "nombre": "Pintura látex interior blanco 1 gl",       "categoria": "Pinturas",                "precio": 24990,  "stock": 50 },
  { "id": 22, "nombre": "Esmalte sintético negro 1/4 gl",           "categoria": "Pinturas",                "precio": 8990,   "stock": 42 },
    { "id": 23, "nombre": "Rodillo antigota 9\" con mango",           "categoria": "Pinturas",                "precio": 5490,   "stock": 70 },
    { "id": 24, "nombre": "Brocha 2\" cerda mixta",                   "categoria": "Pinturas",                "precio": 2290,   "stock": 130 },
  { "id": 25, "nombre": "Cinta de enmascarar 24 mm x 40 m",         "categoria": "Pinturas",                "precio": 1990,   "stock": 160 },
  { "id": 26, "nombre": "Cable eléctrico THHN 2,5 mm² (rollo 100 m)","categoria": "Electricidad",           "precio": 34990,  "stock": 16 },
  { "id": 27, "nombre": "Enchufe macho 10 A",                       "categoria": "Electricidad",            "precio": 1490,   "stock": 140 },
  { "id": 28, "nombre": "Interruptor simple 9/12",                  "categoria": "Electricidad",            "precio": 2490,   "stock": 110 },
  { "id": 29, "nombre": "Ampolleta LED 9 W E27",                    "categoria": "Electricidad",            "precio": 2990,   "stock": 220 },
  { "id": 30, "nombre": "Cinta aislante 18 mm x 20 m",              "categoria": "Electricidad",            "precio": 990,    "stock": 260 },
    { "id": 31, "nombre": "Llave de paso 1/2\" bronce",               "categoria": "Gasfitería",              "precio": 5990,   "stock": 48 },
  { "id": 32, "nombre": "Tubo PVC sanitario 110 mm x 3 m",          "categoria": "Gasfitería",              "precio": 8490,   "stock": 38 },
  { "id": 33, "nombre": "Codo PVC 90° 50 mm",                       "categoria": "Gasfitería",              "precio": 690,    "stock": 300 },
  { "id": 34, "nombre": "Teflón 12 mm x 10 m",                      "categoria": "Gasfitería",              "precio": 490,    "stock": 350 },
  { "id": 35, "nombre": "Sifón flexible lavaplatos",               "categoria": "Gasfitería",              "precio": 3990,   "stock": 55 },
  { "id": 36, "nombre": "Candado 40 mm arco corto",                 "categoria": "Seguridad",               "precio": 4990,   "stock": 75 },
  { "id": 37, "nombre": "Guantes de cabritilla talla L",            "categoria": "Seguridad",               "precio": 3490,   "stock": 95 },
  { "id": 38, "nombre": "Lentes de seguridad claros",               "categoria": "Seguridad",               "precio": 1990,   "stock": 140 },
  { "id": 39, "nombre": "Casco de obra amarillo",                   "categoria": "Seguridad",               "precio": 6990,   "stock": 0 },
  { "id": 40, "nombre": "Escalera aluminio tijera 5 peldaños",      "categoria": "Escaleras",               "precio": 44990,  "stock": 10 }
]
"""

productos = json.loads(PRODUCTOS_JSON)

IMAGENES_PRODUCTO = {
  1: "martillo_carpintero_16oz.webp",
  2: "destornillador_phillips_2.png",
  3: "set_6_destornilladores.jpg",
  4: "alicate_universal_8pulg.png",
  5: "llave-ajustable-cromada-10.webp",
  6: "huincha_5m.webp",
  7: "nivel_60cm.webp",
  8: "escuadra_12pulg.jpg",
  9: "taladro_650w.jpg",
  10: "atornillador12v.jpg",
  11: "esmeril_820w.jpg",
  12: "cierra_circular.jpg",
  13: "lijadora240w.jpg",
  14: "brocas_metal19pz.jpg",
  15: "disco_de_corte.jpg",
  16: "hoja_sierra_40d.jpg",
  17: "tornillo_autoperf.jpg",
  18: "clavo_2puld_1kg.jpg",
  19: "Tarugo_6_mm.jpg",
  20: "Perno_hexagonal.jpg",
  21: "Latex_blanco_1_gl.jpg",
  22: "Esmalte_negro.jpg",
  23: "Rodillo_9pulg.jpg",
  24: "Brocha_2pulg.jpg",
  25: "Cinta_enmascarar.jpg",
  26: "Cable_THHN_25mm.jpg",
  27: "Enchufe_macho_10_A.jpg",
  28: "Interruptor_simple.jpg",
  29: "Ampolleta_LED_9_W.jpg",
  30: "Cinta_aislante.jpg",
  31: "Llave_de_paso.jpg",
  32: "Tubo_PVC_110_mm.jpg",
  33: "Codo_PVC_50_mm.jpg",
  34: "Teflon_12_mm.jpg",
  35: "Sifon_flexible.jpg",
  36: "Candado_40_mm.jpg",
  37: "Guantes_talla_L.jpg",
  38: "Lentes_seguridad.jpg",
  39: "Casco_de_obra.jpg",
  40: "Escalera_5_peldanos.jpg",
}

for producto in productos:
  producto["imagen_local"] = f"/static/img/productos/{IMAGENES_PRODUCTO[producto['id']]}"


def imagen_producto(request, id):
  producto = next((p for p in productos if p["id"] == id), None)
  if producto is None:
    raise Http404("La imagen del producto no existe.")

  categoria = producto["categoria"]
  formas = {
    "Herramientas manuales": '<path d="M355 120h70v170h-70z"/><path d="M330 265h120l50 190H280z"/>',
    "Medición": '<rect x="185" y="220" width="430" height="90" rx="15"/><path d="M230 220v42m48-42v25m48-25v42m48-42v25m48-25v42m48-42v25m48-25v42"/>',
    "Herramientas eléctricas": '<path d="M290 160h180v170H290z"/><path d="M330 330h100v145H330z"/><circle cx="380" cy="245" r="48"/>',
    "Accesorios eléctricos": '<path d="M330 120h100v110H330z"/><path d="M355 230v240m50-240v240M300 470h160"/>',
    "Fijaciones": '<path d="M270 150h220v65H270z"/><path d="M300 215v270m80-270v270m80-270v270"/>',
    "Pinturas": '<path d="M285 145h190v280H285z"/><path d="M315 110h130v35H315z"/><path d="M320 255h120"/>',
    "Electricidad": '<path d="M340 110h80v120h-80z"/><path d="M360 230v240m40-240v240"/><circle cx="380" cy="170" r="18"/>',
    "Gasfitería": '<path d="M255 190h250v75H255z"/><path d="M330 265v150h100V265"/><circle cx="380" cy="455" r="45"/>',
    "Seguridad": '<path d="M270 245q110-150 220 0v55H270z"/><path d="M310 300v125h140V300"/>',
    "Escaleras": '<path d="M280 120h55l130 360h-55z"/><path d="M425 120h55L350 480h-55z"/><path d="M330 210h125m-95 80h125m-95 80h125"/>',
  }
  forma = formas.get(categoria, formas["Herramientas manuales"])
  nombre = escape(producto["nombre"])
  categoria_segura = escape(categoria.upper())
  svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 560" role="img" aria-label="{nombre}">
    <rect width="760" height="560" fill="#e8ece7"/>
    <path d="M0 430 180 250l160 150 130-180 290 250v90H0z" fill="#d9e1db"/>
    <circle cx="650" cy="105" r="72" fill="#f4a33a" opacity=".3"/>
    <g fill="#20282a" stroke="#f36a21" stroke-width="12" stroke-linejoin="round">{forma}</g>
    <text x="42" y="62" fill="#c95113" font-family="Arial,sans-serif" font-size="18" font-weight="700" letter-spacing="3">{categoria_segura}</text>
    <text x="42" y="515" fill="#20282a" font-family="Arial,sans-serif" font-size="24" font-weight="700">{nombre}</text>
  </svg>'''
  return HttpResponse(svg, content_type="image/svg+xml")

def lista(request):
    # Muestra el catálogo completo
    disponibles = 0
    for p in productos:
        if p["stock"] > 0:
            disponibles += 1
    contexto = {
        "productos": productos,
      "categorias": sorted({p["categoria"] for p in productos}),
        "total": len(productos),
        "disponibles": disponibles,
        "sin_stock": len(productos) - disponibles,
    }
    return render(request, "catalogo/lista.html", contexto)

def detalle(request, id):
    # Muestra el detalle de un producto buscándolo por id
    encontrado = None
    for p in productos:
        if p["id"] == id:
            encontrado = p
            break

    if encontrado is None:
        raise Http404("El producto que buscas no existe en el catálogo.")

    return render(request, "catalogo/detalle.html", {"producto": encontrado})


def agregar_stock(request, id):
    if request.session.get("rol", "") != "admin":
        return redirect("cuentas:ingresar")

    producto = next((p for p in productos if p["id"] == id), None)
    if producto is None:
        raise Http404("El producto que buscas no existe en el catálogo.")

    if request.method == "POST":
        try:
            cantidad = int(request.POST.get("cantidad", "0"))
        except ValueError:
            cantidad = 0

        if cantidad > 0:
            producto["stock"] += cantidad

    return redirect("catalogo:detalle", id=producto["id"])



def inicio(request):

    destacados = productos[:6]
    disponibles = 0
    for p in productos:
        if p["stock"] > 0:
            disponibles += 1

    contexto = {
        "destacados": destacados,
        "total": len(productos),
        "disponibles": disponibles,
        "categorias": sorted({p["categoria"] for p in productos}),
    }
    return render(request, "catalogo/inicio.html", contexto)



def comprar(request, id):
    if "usuario" not in request.session:
        return redirect("cuentas:ingresar")

    producto = None
    for p in productos:
        if p["id"] == id:
            producto = p
            break

    if producto is None:
        raise Http404("El producto que buscas no existe en el catálogo.")

    if producto["stock"] == 0:
        contexto = {"producto": producto, "sin_stock": True}
        return render(request, "catalogo/comprar.html", contexto)

    cantidad = 0
    error = None
    if request.method == "POST":
      try:
        cantidad = int(request.POST.get("cantidad", "0"))
      except ValueError:
        cantidad = 0

      if cantidad < 1:
        error = "Selecciona al menos una unidad."
      elif cantidad > producto["stock"]:
        error = f"Solo quedan {producto['stock']} unidades disponibles."
      else:
        producto["stock"] -= cantidad

    if request.method != "POST" or error:
      contexto = {"producto": producto, "sin_stock": False, "error": error}
      return render(request, "catalogo/comprar.html", contexto)

    contexto = {"producto": producto, "sin_stock": False, "cantidad": cantidad}
    return render(request, "catalogo/comprar.html", contexto)



def agregar_producto(request):

    if request.session.get("rol", "") != "admin":
        return redirect("cuentas:ingresar")

    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        categoria = request.POST.get("categoria", "").strip()
        precio = request.POST.get("precio", "").strip()
        stock = request.POST.get("stock", "").strip()
        imagen_url = request.POST.get("imagen_url", "").strip()

       
        errores = []
        if nombre == "":
            errores.append("El nombre es obligatorio.")
        if categoria == "":
            errores.append("La categoría es obligatoria.")
        if imagen_url and not imagen_url.startswith(("http://", "https://")):
          errores.append("La URL de imagen debe comenzar con http:// o https://.")

        try:
            precio = int(precio)
            if precio < 0:
                errores.append("El precio no puede ser negativo.")
        except ValueError:
            errores.append("El precio tiene que ser un número entero.")

        try:
            stock = int(stock)
            if stock < 0:
                errores.append("El stock no puede ser negativo.")
        except ValueError:
            errores.append("El stock tiene que ser un número entero.")

        if errores:
            contexto = {
                "errores": errores,
                "categorias": sorted({p["categoria"] for p in productos}),
                "datos": request.POST,
            }
            return render(request, "catalogo/agregar.html", contexto)

        
        nuevoId = max(p["id"] for p in productos) + 1

        nuevoProducto = {
            "id": nuevoId,
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "stock": stock,
            "imagen_local": imagen_url or f"/producto/{nuevoId}/imagen.svg",
            "imagen_url": imagen_url,
        }

        productos.append(nuevoProducto)
        return redirect("catalogo:detalle", id=nuevoId)

    contexto = {"categorias": sorted({p["categoria"] for p in productos})}
    return render(request, "catalogo/agregar.html", contexto)
