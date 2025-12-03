from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPI(BaseHTTPRequestHandler):
  def do_GET(self):
        # 设置响应头（JSON格式）
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # 模拟后端数据
        response = {'status': 'active', 'service': 
'OrderService', 'version': '2.0 - Docker Edition'}
        self.wfile.write(json.dumps(response).encode())
# 服务监听所有IP的8080端口
server_address = ('', 81)
print("Microservice starting on port 81...")
httpd = HTTPServer(server_address, SimpleAPI)
httpd.serve_forever()
