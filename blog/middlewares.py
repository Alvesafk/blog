import re
from time import time

class StatsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.regexp = re.compile(r'<!--\s*STATS\s*-->')

    def __call__(self, request):
        start = time()
        response = self.get_response(request)
        total_time = time() - start

        if response.get('Content-Type', '').startswith('text/html'):
            stats_html = (
                f'<span class="stats">'
                f'<p class="footer-text">'
                f'Page loaded in {total_time:.2f} seconds'
                f'</p>'
                f'</span>'
            )

            content = response.content.decode('utf-8')
            new_content = self.regexp.sub(stats_html, content)

            if new_content != content:
                response.content = new_content.encode('utf-8')
                
        return response
