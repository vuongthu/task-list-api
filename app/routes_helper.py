from flask import jsonify, abort, make_response


def error_msg(message, status_code):
    abort(make_response(jsonify(dict(details=message)), status_code))


def success_msg(message, status_code):
    return make_response(jsonify(dict(details=message)), status_code)
