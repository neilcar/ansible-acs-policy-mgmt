# from https://gist.github.com/halberom/a5aebb34da179fdce91a1bd018ec2805
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from urllib.parse import urlparse

def parse_url(url):
    """return a dict, of the parsed elements"""
    result = {}

    o = urlparse(url)

    result['scheme'] = o.scheme
    result['port'] = o.port
    result['url'] = o.geturl()
    result['path'] = o.path
    result['netloc'] = o.netloc
    result['query'] = o.query
    result['hostname'] = o.hostname

    return result


class FilterModule(object):

    def filters(self):
        return {
                "parse_url": parse_url
        }