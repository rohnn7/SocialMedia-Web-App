# Since this site is multi application therefore there would be one base hame page
# which would be mapped to base urls.py this home page will be common to all apps
from django.views.generic import TemplateView

# this class will be linked to home page through TemplateView
class HomePage(TemplateView):
    template_name='index.html'

#this class tells LoginView to redirect
#LoginView-> Settings.py='test' -> urls.py(......name='test') -> views.TestPage -> template_name=test.html
class TestPage(TemplateView):
    template_name='test.html'

#this class tells LogoutView to redirect
#LogoutView-> Settings.py='thanks' -> urls.py(......name='thanks') -> views.ThankPage -> template_name=thanks.html
class ThanksPage(TemplateView):
    template_name='thanks.html'
