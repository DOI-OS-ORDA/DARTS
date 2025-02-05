import os
from .repositories.users import UsersRepository
from .structs.struct import Struct


def resolve_current_user(request):
    try:
        return UsersRepository.get(request.session.get("user.id"))
    except:
        return Struct({ 'full_name': "Guest user", 'role_name': "guest" })


def current_user(request):
    return { 'current_user': resolve_current_user(request) }


def user_types(request):
    return { 'selectable_users': UsersRepository.all() }


def document_access_mailto(request):
    return { 'document_access_mailto': os.getenv("DOCUMENT_ACCESS_MAILTO_ADDRESS", "sample@sample.gov") }
