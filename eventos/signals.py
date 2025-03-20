# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth.models import User, AnonymousUser
# from .models import Evento

# @receiver(post_save)
# def registrar_modificacao(sender, instance, created, **kwargs):
#     if sender == Evento:  # Evita loop infinito ao salvar eventos
#         return
    
#     usuario = None
#     if hasattr(instance, "modificado_por"):
#         if isinstance(instance.modificado_por, AnonymousUser):  # 🔥 Impede erro com usuários anônimos
#             print("⚠️ ERRO: Tentativa de registrar evento com usuário anônimo!")
#             return
#         usuario = instance.modificado_por if instance.modificado_por.is_authenticated else None

#     if usuario is None:
#         print("⚠️ ERRO: Nenhum usuário autenticado para registrar evento!")
#         return  # 🔥 Evita salvar eventos sem usuário válido

#     evento = Evento(
#         usuario=usuario,
#         content_type=ContentType.objects.get_for_model(sender),
#         object_id=instance.pk,
#         acao="criado" if created else "atualizado",
#         descricao=f"{'Criado' if created else 'Atualizado'}: {instance}"
#     )
#     evento.save()

# @receiver(post_delete)
# def registrar_exclusao(sender, instance, **kwargs):
#     if sender == Evento:  # Evita loop infinito ao excluir eventos
#         return

#     usuario = None
#     if hasattr(instance, "modificado_por"):
#         if isinstance(instance.modificado_por, AnonymousUser):
#             print("⚠️ ERRO: Tentativa de registrar evento de exclusão com usuário anônimo!")
#             return
#         usuario = instance.modificado_por if instance.modificado_por.is_authenticated else None

#     if usuario is None:
#         print("⚠️ ERRO: Nenhum usuário autenticado para registrar evento de exclusão!")
#         return  # 🔥 Evita salvar eventos sem usuário válido

#     evento = Evento(
#         usuario=usuario,
#         content_type=ContentType.objects.get_for_model(sender),
#         object_id=instance.pk,
#         acao="excluído",
#         descricao=f"Excluído: {instance}"
#     )
#     evento.save()
