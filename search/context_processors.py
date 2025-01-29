from .repositories.users import UsersRepository


def current_user(request):
    return { 'current_user': UsersRepository.get(request.session.get("user.type", "guest")) }


def user_types(request):
    return { 'user_types': UsersRepository.all() }
