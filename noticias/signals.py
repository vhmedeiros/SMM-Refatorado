from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import connection
from .models import NoticiaImportada  # Importando o modelo da notícia
import threading


def executar_sp():
    """
    Executa a Stored Procedure VincularNoticiasAClientes.
    """
    with connection.cursor() as cursor:
        cursor.execute("EXEC sp_VincularNoticiasAClientes;")


@receiver(post_save, sender=NoticiaImportada)
def rodar_sp_apos_criar_noticia(sender, instance, created, **kwargs):
    """
    Executa a Stored Procedure VincularNoticiasAClientes sempre que uma nova notícia for cadastrada.
    """
    if created:  # Somente quando a notícia for criada (não para edições)
        thread = threading.Thread(target=executar_sp)
        thread.start()
