#!/usr/bin/env python3
"""
TraceServer:
Implementa un server http che riceve ed archivia parametri di geolocalizzazione

XXX To do:
- save data
- log requests, user-agent header and other interesting goodies
"""

# Belluzzi Python Working Group
# - Prof. S. Gallo
# - E. Carrà, Bovinelli, F. Taddia                          

__version__ = "0.1c"

__all__ = [
    "TraceServer", "TraceRequestHandler"
]

from http.server import *
from http import HTTPStatus
import datetime
import webbrowser


# Default message template
DEFAULT_MESSAGE_TEMPLATE = """\
<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <title>Trace Server Response</title>
    </head>
    <body>
        <h1>Trace Server Response</h1>
        <p>Code: {code}</p>
        <p>Message: {message}</p>
        <p>Information: {info}</p>
    </body>
</html>
"""


def _quote_html(html):
    return html.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

class HandlerDataBase():#classe che gestisce il database nel percorso Path
    Path = 'DataBase/DataBase.txt'#percorso database

    def decode_Data(self,text):#splitta la latitudine e la longitudine dal POST
        text=""+text
        position=text.find('=',5)

        lat=text[9 : position-1]
        long=text[position+1:]
        i = datetime.datetime.now()
        date='['+str(i.day)+'/'+str(i.month)+'/'+str(i.year)+']'#reccoglimento della data e dell'ora
        hour=str(i.hour)+':'+str(i.minute)+':'+str(i.second)
        self.__add_position(lat,long,hour,date,'3DI')#l'aggiunge al file

    def __add_position(self,lat,long,hour,date,name):#aggiunge un nuovo accesso al database
        date=str(date)
        reader = open(self.Path, 'r')
        text=reader.read()
        f = open(self.Path, 'w')
        f.write(text)
        f.write('\n')
        f.write(lat)
        f.write('\t')
        f.write(long)
        f.write('\t')
        f.write(date)
        f.write('\t')
        f.write(hour)
        f.write('\t')
        f.write(name)
        f.write('\n')
        f.flush()
        f.close()





class MyHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/favicon.ico':
            print("Skipping favicon request")
            return
        print( "\nGET {}".format(str(self.path)) )
        self._send_response(HTTPStatus.OK, self.path)
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print( "\nPOST {}\nHeaders:\n{}\nBody:\n{}\n".format(str(self.path), str(self.headers), post_data.decode('utf-8')))
        gestore=HandlerDataBase()
        gestore.decode_Data(post_data.decode('utf-8'))
        self._send_response(HTTPStatus.OK, self.path)
        # path = path.split('?',1)[0]
        # path = path.split('#',1)[0]

    def _send_response(self, code, message, info=""):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type','text/html;charset=utf-8')
        self.end_headers()
        print(self.path)
        try:
            content = ( DEFAULT_MESSAGE_TEMPLATE.format(code=code, message=_quote_html(message), info=_quote_html(info)) )
            self.wfile.write( content.encode('UTF-8', 'replace') )
            self.wfile.flush()
            return True
        except Exception as ex:
            print("ERRORE in send_response: " + str(ex))
            return False

def run():
    myserver = None
    server_name = "TraceServer"
    server_address = ('',80)
    server_startingtime = datetime.datetime.now()
    print("Starting server", str(server_startingtime), "...")
    #webbrowser.open('http://localhost')
    try:
        myserver = HTTPServer( server_address, MyHandler )
        print( server_name, "started on port", server_address[1] )
        myserver.serve_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
    except Exception as ex:
        print("ERRORE nel server: " + str(ex))
    print("Stopping server ...")
    myserver.server_close()
    print("Server stopped!")
    

if __name__ == '__main__':
    run()

