# -*- coding: utf-8 -*-

from .models import FeedsLanguage
from django.http import JsonResponse
from django.utils.translation import activate, gettext_lazy as _
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
import json


@api_view(['GET'])
def feeds_languages_api(request):
    """
        :param request: user request
        :return: all storred feeds as objects grouped by language
    """
    feeds_languages = {}
    for feeds_language in FeedsLanguage.objects.filter():
        # for each stored language feeds, we get items and we add them to feeds_languages dictionary
        feeds_languages[feeds_language.language] = feeds_language.to_items_list()
    response = JsonResponse({
        "feeds_languages": feeds_languages,
        "success": True,
    })
    return response


@api_view(['GET'])
def general_information_api(request):
    """
        :param request: user request
        :return: general information of the website
    """
    response = JsonResponse({
        "general_information": {
            "site_name": settings.SITE_NAME,
            "contact_email": settings.CONTACT_EMAIL,
        },
        "success": True,
    })
    return response

