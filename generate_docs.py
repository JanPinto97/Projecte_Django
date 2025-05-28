import os
import sys
import django
import pydoc

# Configura el directori actual al PYTHONPATH
os.environ['PYTHONPATH'] = os.environ.get('PYTHONPATH', '') + os.pathsep + os.path.abspath(os.getcwd())

# Configura Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings') 
django.setup()  # Inicialitza Django

# Canvia al directori arrel del projecte (per seguretat)
os.chdir(os.path.abspath(os.path.dirname(__file__)))

# Genera la documentació amb pydoc
pydoc.writedoc('blog.views')
print(f"Generated views.html at: {os.path.abspath('views.html')}")
pydoc.writedoc('blog.models')
print(f"Generated models.html at: {os.path.abspath('models.html')}")
