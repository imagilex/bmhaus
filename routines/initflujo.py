from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group

from initsys.models import Permiso
from .utils import clean_name


def init_flujo_db():
    # Perfiles
    gpo_sadmin = Group.objects.get(name="Super-Administrador")
    gpo_admin = Group.objects.get(name="Administrador")

    # Content Types

    # Permisos
