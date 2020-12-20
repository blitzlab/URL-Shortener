from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from .models import Url
import string
import random

# Generate code
def get_short_code(length:int):
    code = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

    # Ensure code is unique
    if Url.objects.filter(url_code = code).count() > 0:
        return get_short_code(length)

    return code


# Shorten url controller

@api_view(["POST"])
def shorten_url(request):

    try:

        # Get Original url
        long_url = request.data.get('url')

        if long_url is None or len(long_url) == 0:
            return Response({"message": "Url is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Generate short code for url
        url_code = get_short_code(5)
        
        # Save url into the db
        Url.objects.create(long_url=long_url, url_code=url_code)

        # Success response with shortened url
        return Response(
            {"message": "Success", "shortened_url": reverse("redirect", args=[url_code], request=request)}, 
            status=status.HTTP_201_CREATED)
    except Exception as e:
        # In case of possible exceptions
        print(e)
        return Response(
            {"message": f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Url redirect controller
def url_redirect(request, url_code):

    # Retreive url details or return 404 error if not found
    get_url = get_object_or_404(Url, url_code=url_code)

    # Redirect to the original url
    return HttpResponseRedirect(get_url.long_url)

