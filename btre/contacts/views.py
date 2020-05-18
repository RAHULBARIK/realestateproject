from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
# The import is used use send mail features in your projects
from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #  Check if user has made inquiry already
        # In the template to check  if the user is authenticated we need to do user.is_authenticated but in views we have to do request.user.is_authenticated
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquiry for this listing')
                return redirect('/')

        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        # Send email
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing +
            '. Sign into the admin panel for more info',
            'rahulbarik583@gmail.com',
            [realtor_email, 'rahulbarik583@gmail.com', 'xecipa7576@inbov03.com'],
            fail_silently=False
            # show fail_silently is used to show when your email is not send
        )

        messages.success(
            request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/')
