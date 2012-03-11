def groupfinder(user_id, request):
    user = request.user
    auth_user = user.auth_user
    if user is not None:
        return [group.name for group in auth_user.auth_groups]
    return None