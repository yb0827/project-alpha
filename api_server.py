from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        # 设置响应头（HTML格式）
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # 构造HTML页面（对应目标样式）
        html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            background-color: #f0f2f5;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .card {
            background-color: white;
            padding: 3rem;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        .title {
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 1.5rem;
            color: #1a1a1a;
        }
        .info {
            font-size: 1.2rem;
            margin: 0.8rem 0;
            color: #666;
        }
        .status-active {
            color: #28a745; /* 绿色 */
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="title">Order Service Status</div>
        <div class="info">Service Name: OrderService</div>
        <div class="info">Current Status: <span class="status-active">active</span></div>
        <div class="info">API Version: 2.0 - Docker Edition</div>
    </div>
</body>
</html>
        """
        # 发送HTML内容
        self.wfile.write(html_content.encode())

# 服务监听所有IP的8080端口（可按需修改）
server_address = ('', 81)
print("Microservice starting on port 81...")
httpd = HTTPServer(server_address, SimpleAPI)
httpd.serve_forever()
