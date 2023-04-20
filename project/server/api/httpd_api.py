from flask import (
    jsonify as flask_jsonify,
    request,
)


def view_origin():
    """Returns the requester's IP Address.
    ---
    tags:
      - Request inspection
    produces:
      - application/json
    responses:
      200:
        description: The Requester's IP Address.
    """

    return jsonify(origin=request.headers.get("X-Forwarded-For", request.remote_addr))


def jsonify(*args, **kwargs):
    response = flask_jsonify(*args, **kwargs)
    # print(response.data)   b'{"origin":"127.0.0.1"}\n'
    if not response.data.endswith(b"\n"):
        response.data += b"\n"
    return response

