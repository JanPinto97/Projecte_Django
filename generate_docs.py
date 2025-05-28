import os
import sys
import django
import pydoc

# Configura el directori actual al PYTHONPATH
os.environ['PYTHONPATH'] = os.environ.get('PYTHONPATH', '') + os.pathsep + os.path.abspath(os.getcwd())

# Configura Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')  # Canvia 'blog_project' pel nom del teu projecte
django.setup()  # Inicialitza Django

# Genera la documentació amb pydoc
pydoc.writedoc('blog.views')
pydoc.writedoc('blog.models')
