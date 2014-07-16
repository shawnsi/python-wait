#!/usr/bin/env python

import socket

from .decorator import timeout


@timeout
def closed(port, host='localhost', timeout=300):
    try:
        s = socket.create_connection((host, port), timeout)
        s.close()
    except socket.error:
        return True


@timeout
def open(port, host='localhost', timeout=300):
    try:
        s = socket.create_connection((host, port), timeout)
        s.close()
        return True
    except socket.error:
        pass


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
