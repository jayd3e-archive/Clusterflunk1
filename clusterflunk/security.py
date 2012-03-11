def groupfinder(user_id, request):
    user = request.user
    if user is not None:
        return [group.name for group in request.user.groups]
    return None