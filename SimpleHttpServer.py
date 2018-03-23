
import http.server
import socketserver
import webbrowser
 
PORT = 80

webbrowser.open('http://localhost')

try:
    Handler = http.server.SimpleHTTPRequestHandler

    httpd = socketserver.TCPServer(("", PORT), Handler)
    print("serving at port", PORT)
    httpd.serve_forever()

except Exception as ex:
    print("ERRORE: " + str(ex))
    
