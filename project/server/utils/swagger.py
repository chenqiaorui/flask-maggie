swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "spec",
            "route": "/spec.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/apidocs",
}

template = {
    "swagger": "2.0",
    "info": {
        "title": "flask-maggie",
        "description": (
            "learning flask >.< "
        ),
        "contact": {
            "responsibleOrganization": "Meow",
            "responsibleDeveloper": "Ricky Chen",
            "email": "809155736@qq.com",
            "url": "https://github.com/chenqiaorui",
        },
        # "termsOfService": "http://me.com/terms",
        "version": "1.0.1",
    },
    # "host": "httpbin.org",  # overrides localhost:5000
    # "basePath": "/",  # base bash for blueprint registration
    "schemes": ["http"],
    "protocol": "http",
    "tags": [
        {
            "name": "Flask All",
            "description": "learing flask",
            # 'externalDocs': {'description': 'Learn more', 'url': 'https://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html'}
        },
        {"name": "Auth", "description": "Auth methods"},
        {
            "name": "Status codes",
            "description": "Generates responses with given status code",
        },
        {"name": "Request inspection", "description": "Inspect the request data"},
        {
            "name": "Response inspection",
            "description": "Inspect the response data like caching and headers",
        },
        {
            "name": "Response formats",
            "description": "Returns responses in different data formats",
        },
        {"name": "Dynamic data", "description": "Generates random and dynamic data"},
        {"name": "Cookies", "description": "Creates, reads and deletes Cookies"},
        {"name": "Images", "description": "Returns different image formats"},
        {"name": "Redirects", "description": "Returns different redirect responses"},
        {
            "name": "Anything",
            "description": "Returns anything that is passed to request",
        },
    ],
}