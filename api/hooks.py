import logging
import os
import time

import falcon


def api_key(req, resp, resource, params):
    key = req.get_param('api_key')
    if key is None:
        raise falcon.HTTPForbidden(
            description='API KEY is required',
        )
    elif key != os.environ.get('API_KEY', ''):
        raise falcon.HTTPForbidden(
            description='API KEY is invalid'
        )


def say_bye_after_operation(req, resp, resource):
    logging.info('Bye there at ' + str(time.time()) + ' and api_key=' + req.params.get('api_key'))
