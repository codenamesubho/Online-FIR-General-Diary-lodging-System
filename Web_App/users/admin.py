from django.contrib import admin

# Register your models here.
from users.models import PanModel,RationModel,VoterModel,AadharModel

admin.site.register(PanModel)
admin.site.register(RationModel)
admin.site.register(VoterModel)
admin.site.register(AadharModel)

