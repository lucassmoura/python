from src.main.server.server import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)

#app.py
#from werkzeug.wrappers import Request, Response




#@Request.application
#def application(request: Request) -> Response:
#    return Response("Hello, World!")

#if __name__ == "__main__":
#    from werkzeug.serving import run_simple
#    run_simple("127.0.0.1", 5000, application)    