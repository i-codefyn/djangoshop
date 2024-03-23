def wishlists(request):
    if not (request.user and request.user.is_authenticated):
        return {}
    return {
        'wishlists': request.user.wishlists.all()
    }