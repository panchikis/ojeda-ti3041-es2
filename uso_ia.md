Uso de IA evaluación 2 Back End

Petición 1
Necesitaba ayuda para entender cómo usar venv porque hasta ahora solo había visto que usemos pipenv entonces también consulté por su diferencia, le pregunté a Gemini.

Prompt: cómo se usa venv y cuál es su diferencia con pipenv

Respuesta: Me explicó el comando para crear el entorno con venv y para activarlo, me explicó que su diferencia está en que venv es más simple que pipenv y así su uso se recomienda más para proyectos pequeños.

Petición 2
Necesité ayuda porque al intentar activar venv me dio error.
Prompt: Le mandé la imagen de error

Respuesta: Me dijo que se debe a los permisos de Windows, me recomendó que ponga un comando para ignorarlo temporalmente, lo hice y me dejó activar el entorno.

Petición 3
Necesité ayuda para poder conectar mysql, no me funcionaba

prompt: le mandé la iamgen de error

respuesta: me recomendó bajar la versión de django para hacerla compatible con la versión de mariadb que viene con xampp

petición 4
Le pregunté por el error que me decía en la consola luego de hacer migraciones

promt: le adjunté la imagen preguntando qué significa

respuesta: me dijo que era una advertencia de que mariadb me recortará datos si no le pongo dentro de settings el código
    'charset': 'utf8mb4',
    'sql_mode': 'STRICT_TRANS_TABLES' 

Petición 5
Le pedí ayuda a Copilot para crear el fixture json directamente en mi código

prompt: genera una fixture JSON de Django para mis modelos catalogo.Categoria y catalogo.Producto, con los 40 productos de ferretería que están en views.py. Categoria tiene solo nombre, Producto tiene nombre, stock, precio, categoria, en la ForeignKey va el id de la categoría, en la imagen coloca la ruta completa. Primero haz las categorías, después los productos, por el tema de la FK, no olvides mantener los mismos nombres, precios y stock y quitar los json de views.py

respuesta: hizo lo que le pedí 

Peticion 6
No vi los cambios en la base de datos y le pregunté qué pasó

prompt: por qué no puedo ver los datos en la base de datos

respuesta: me dijo que debía poner python manage.py loaddata productos.json