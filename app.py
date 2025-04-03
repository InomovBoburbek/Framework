from webob import Request, Response

class Frameworkapp:
    def __init__(self):
        self.routes = dict()

    def __call__(self, environ, start_response):
        req = Request(environ)
        res = self.handle_request(req)
        return  res(environ, start_response)

    def handle_request(self, req):
        print(req.environ)
        res = Response()

        for path, handler in self.routes.items():
            if path == req.path:
                handler(req, res)
        return res

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper