class CustomMediaUrlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Modify the response URL for media files
        if response.has_header('Content-Disposition'):
            content_disposition = response.get('Content-Disposition')
            if 'images/' in content_disposition:
                new_url = content_disposition.replace('images/', 'blacklistApi/media/images/')
                response['Content-Disposition'] = f'inline; filename="{new_url}"'

        return response