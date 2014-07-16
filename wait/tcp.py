#!/usr/bin/env python

import socket
import time

from .decorator import timeout

@timeout
def open(port, host='localhost', timeout=300):
    try:
        s = socket.create_connection((host, port))
        s.close()
        return True
    except socket.error:
        pass


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
