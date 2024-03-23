from django.contrib import admin
from .models import City
from oscar.core.loading import get_model

ContactUs = get_model("home", "ContactUs")
Feedback = get_model("home", "Feedback")
Subscribe = get_model("home", "Subscribe")
Brand = get_model("home", "Brands")
KeywordDiscription = get_model("home", "KeywordDiscription")
SiteData = get_model("home", "SiteData")
Features = get_model("home", "Features")
Faq = get_model("home", "Faq")
AboutCompany = get_model("home", "AboutCompany")
SliderData = get_model("home", "SliderData")
OurClients = get_model("home", "OurClients")


# Register your models here.


admin.site.register(Brand)

admin.site.register(KeywordDiscription)
admin.site.register(SiteData)
admin.site.register(Features)
admin.site.register(Faq)
admin.site.register(AboutCompany)
admin.site.register(OurClients)
admin.site.register(SliderData)
admin.site.register(City)


class ContactUsAdmin(admin.ModelAdmin):
    pass


admin.site.register(ContactUs, ContactUsAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    pass


admin.site.register(Feedback, FeedbackAdmin)


class SubscribeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Subscribe, SubscribeAdmin)
