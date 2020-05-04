from applications.home.models import Home
from applications.home.forms import ContactForm

def home_contact(request):
    home=Home.objects.latest('created')

    return{
        'phone': home.phone,
        'email': home.email,
    }
