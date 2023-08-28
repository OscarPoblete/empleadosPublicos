import sys
sys.path.insert(0,"/home//ubuntu/empleadosPublicos")

activate_this = '/home/ubuntu/empleadosPublicos/venv/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

from conexion import app as application