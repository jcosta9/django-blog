from django.contrib import admin
from .models import Post

admin.site.register(Post) #importamos o modelo Post definido em Models.py
                            #torna-o visivel na pagina de administracao
