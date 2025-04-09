from webob import Request, Response
from parse import parse
class Frameworkapp:
    def __init__(self):
        self.routes = dict()

    def __call__(self, environ, start_response):
        req = Request(environ)
        res = self.handle_request(req)
        return res(environ, start_response)

    def handle_request(self, req):
        res = Response()
        is_found = False

        for path, handler in self.routes.items():
            if path == req.path:
                handler(req, res)
                is_found = True
            else:
                parsed = parse(path, req.path)


                if parsed is not None:
                    handler(req, res, parsed.named.get("id", "Bunday user yo'q!"))
                    is_found = True

        if not is_found:
            self.default_response(res)

        return res

    def default_response(self, response):
        response.status_code = 404
        response.text = "Not Found!"
            # # /u/<id>
            # if path == "/u/id" and len(path_parts) == 2 and path_parts[0] == "u":
            #     handler(req, res, path_parts[1])
            #     return res
            #
            # # /admin/<id>
            # elif path == "/admin/id" and len(path_parts) == 2 and path_parts[0] == "admin":
            #     handler(req, res, path_parts[1])
            #     return res
            #
            # # static route
            # elif path == req.path:
            #     handler(req, res)
            #     return res

        # res.status = '404 Not Found'
        # res.text = 'Not Found'
        # return res

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper
