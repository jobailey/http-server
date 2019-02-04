from http.server import HTTPServer, BaseHTTPRequestHandler

# Making the class for webserver.py
class Serv(BaseHTTPRequestHandler):

    # Inherit methods from BaseHTTPRequestHandler
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        
        # Read file to be accessed by the user 
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except: 
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()

        # Write file contents to the screen
        self.wfile.write(bytes(file_to_open, 'utf-8'))

# HTTP Daemon runs in the background and deals with server requests
httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()
