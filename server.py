import http.server
import socketserver
from QAChatbot import execute_query
from AIChatbot import createChatbot
from AIChatbot import trainChatbot


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        self.send_response(200)
        content_length = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_length)
        self.end_headers()
        print('QAChatbot input:', post_body)
        QAChatbotReply = execute_query(post_body)
        print('QAChatbot output:', QAChatbotReply)
        self.wfile.write(str.encode(QAChatbotReply))

    def do_PATCH(self):
        self.send_response(200)
        content_length = int(self.headers['Content-Length'])
        userInput = self.rfile.read(content_length)
        self.end_headers()
        print('AIChatbot input:', userInput)
        AIChatbotReply = AIChatbot.get_response(userInput.decode("utf-8"))
        print('AIChatbot output:', AIChatbotReply.text)
        self.wfile.write(str.encode(AIChatbotReply.text))


if __name__ == "__main__":
    PORT = 8080
    DIRECTORY = 'public'
    AIChatbot = createChatbot()
    trainChatbot(AIChatbot)
    with socketserver.TCPServer(('', PORT), Handler) as httpd:
        print('serving at port', PORT)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
