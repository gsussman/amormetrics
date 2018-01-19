from django.contrib import admin

# Register your models here.
# Register your models here.
from frontpage.models import Image, ProfileInfo, Age, Ethnicity, Income, Gender, Education, Religion

class ImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Image, ImageAdmin)

class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProfileInfo, ProfileAdmin)

class AgeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Age, AgeAdmin)

admin.site.register(Ethnicity)
admin.site.register(Education)
admin.site.register(Gender)
admin.site.register(Income)
admin.site.register(Religion)