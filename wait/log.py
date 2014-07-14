#!/usr/bin/env python

import os
import os.path
import re
import time

def tail(path, seek=None):
    """
    Implements file tailing as a generator.  Yields line content or None.
    """
    with open(path) as f:
        if seek is not None:
            f.seek(seek)

        else:
            # Seek to the end of the file
            size = os.stat(path)[6]
            f.seek(size)

        while True:
            where = f.tell()
            line = f.readline()

            if not line:
                # Reset position if line was empty
                f.seek(where)
                time.sleep(1)
                yield None

            else:
                yield line

def exists(path, timeout=None):
    if timeout is not None:
        start = time.time()

    while True:
        if os.path.exists(path):
            return True

        time.sleep(1)

        if timeout is not None:
            if time.time() - start > timeout:
                return False

def pattern(path, patterns, seek=None, timeout=None):
    """
    Wait until pattern(s) are detected by tailing a file.  Returns True when complete.

    If optional timeout is set and exceed then it returns False.
    """

    if timeout is not None:
        start = time.time()

    if not exists(path, timeout=timeout):
        return False

    if isinstance(patterns, str):
        patterns = [patterns]

    for line in tail(path, seek):
        if line is not None:
            for pattern in patterns:
                if re.search(pattern, line):
                    patterns.remove(pattern)

        if not len(patterns):
            # Stop looping over generator when all patterns have been matched
            break

        if timeout is not None:
            if time.time() - start > timeout:
                return False

    return True

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

