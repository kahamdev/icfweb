from django.contrib import admin
from django.contrib import admin
from .models import icf_event,icf_quote,frequent_ask
from .models import faq_qn01,faq_qn02,faq_qn03,faq_qn04

admin.site.register(icf_event)
admin.site.register(icf_quote)
admin.site.register(frequent_ask)

admin.site.register(faq_qn01)
admin.site.register(faq_qn02)
admin.site.register(faq_qn03)
admin.site.register(faq_qn04)
