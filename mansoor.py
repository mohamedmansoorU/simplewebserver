from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
 <html>
    <head>
        NAME:Mohamed mansoor
        REG NO:26018120
    </head>
    <body>
        <table border="6" cellspacing="20" cellpading="10">
            <caption>learners</caption>
            <tr bgcolor="lavender">
            <th>S.No</th>
            <th>Name</th>
            <th>info</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Divice Name </td>
                <td>TL15-53M-G2</td>     
             </tr>
             <tr>
                <td>2</td>
                <td>processor</td>
                <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
             </tr>
             <tr>
                <td>3</td>
                <td>Intalled Ram</td>
                <td>16.0 GB (15.7 GB usable)</td>
             </tr>
             <tr>
                <td>4</td>
                <td>System Type</td>
                <td>64-bit operating system, x64-based processor</td>
                
                
             </tr>
             <tr>
                <td>5</td>
                <td>Graphics Card</td>
                <td>Intel(R) Graphics (128 MB)</td>
             </tr>
             <tr>
                <td>6</td>
                <td>Product Id</td>
                <td>00342-42945-52039-AAOEM</td>
             </tr>
        
        </table>
    </body>
</html>       
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()
