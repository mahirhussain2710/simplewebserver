from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
	<head>
		<title>Mahir hussain S Ex1</title>
	</head>
	<body>
	<table border="2" cellspacing="5" cellpadding="5" width="40" height="50" align="center">
	<caption>Top 5 Companies in Sales</caption>
		<tr bgcolor="pink" align="center">
			<th>Rank</th>
			<th>Company</th>
			<th>Sales</th>
		</tr>
		<tr bgcolor="gold" align="center">
			<td bgcolor="pink">1.</td>
			<td>Microsoft</td>
			<td>57.9</td>
		</tr>
		<tr bgcolor="gold" align="center">
			<td bgcolor="pink">2.</td>
			<td>Oracle</td>
			<td>21.0</td>
		</tr>
		<tr bgcolor="gold" align="center">
			<td bgcolor="pink">3.</td>
			<td>SAP</td>
			<td>16.1</td>
		</tr>
		<tr bgcolor="gold" align="center">
			<td bgcolor="pink">4.</td>
			<td>Computer associates</td>
			<td>4.2</td>
		</tr>
		<tr bgcolor="gold" align="center">
			<td bgcolor="pink">5.</td>
			<td>Adobe</td>
			<td>3.4</td>
		</tr>
	</table>
	</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()