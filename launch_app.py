from gevent.pywsgi import WSGIServer
import app

app_instance = app.create_app()

http_server = WSGIServer(('127.0.0.1', 8080), app_instance)
http_server.serve_forever()