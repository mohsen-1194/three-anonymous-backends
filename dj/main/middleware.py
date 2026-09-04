from django.utils.deprecation import MiddlewareMixin


class CustomizeHeaderMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        headers_to_strip = [
            'Cross-Origin-Opener-Policy',
            'Referrer-Policy',
            'X-Content-Type-Options',
            'X-Frame-Options'
        ]
        
        for header in headers_to_strip:
            if header in response:
                del response[header]
            if header in response.headers:
                response.headers.pop(header, None)
        
        return response
    
