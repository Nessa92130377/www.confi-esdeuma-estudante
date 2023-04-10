from django.contrib import admin
from .models import Post, Comment
from .models import Post, Funcionario


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Funcionario)