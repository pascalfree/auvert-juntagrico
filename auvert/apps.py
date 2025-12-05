from django.apps import AppConfig

class AuvertConfig(AppConfig):
    name = 'auvert'
    verbose_name = "Genossenschaft auVert"

    def ready(self):
        from juntagrico.forms import RegisterMemberForm
        RegisterMemberForm.text['accept_wo_docs'] = 'Hiermit beantrage ich meine Aufnahme in der {}.'
