from .repositories.users import UsersRepository


def current_user(request):
    return { 'current_user': UsersRepository.get(request.session.get("user.id")) }


def user_types(request):
    return { 'selectable_users': UsersRepository.all() }
