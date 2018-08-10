from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import *


class ContAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'description',
        'mail_text',
        'link',
        'photer'
    )
    readonly_fields = ['qr', 'linker']
    list_display = ['name', 'linker', 'qr']
    list_display_links = ['name']

    def qr(self, obj):
        url = reverse('photos:makeqr', args=(obj.name,))
        return format_html(
            '<a style="padding: 0.5em 1em 0.5em 1em; background-color: #dee; text-decoration: none;" href="%s">qrcode</a>' % url)

    def linker(self, obj):
        return format_html(
            '<a href="%s">%s</a>' % (obj.link, obj.link))

    qr.allowed_tags = True
    qr.short_description = 'qr'
    linker.allowed_tags = True
    linker.short_description = 'link'


class MailerAdmin(admin.ModelAdmin):
    fields = (
        'mail',
        'cont'
    )
    readonly_fields = ['mail', 'name']
    list_display = ['mail', 'name']

    def name(self, obj):
        return obj.cont.name

    name.allowed_tags = True
    name.short_description = 'nazwa'

admin.site.register(Cont, ContAdmin)
admin.site.register(Photer)
admin.site.register(Mailer, MailerAdmin)
