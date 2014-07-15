#!/usr/bin/env python

import socket
import time


def open(port, host='localhost', timeout=None):
    if timeout is not None:
        start = time.time()

    while True:
        try:
            s = socket.create_connection((host, port))
            s.close()
            return True
        except socket.error:
            pass

        time.sleep(1)

        if timeout is not None:
            if time.time() - start > timeout:
                return False

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
