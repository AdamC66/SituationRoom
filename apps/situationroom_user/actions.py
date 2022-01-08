from apps.situationroom_user.models import SituationRoomUser

class InvalidPasswordException(Exception):
    pass

def create_user(username, email, password, confirm_password):
    if password != confirm_password:
        raise InvalidPasswordException
    return SituationRoomUser.objects.create(
        username=username,
        email=email,
        password=password
    )