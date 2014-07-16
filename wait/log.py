#!/usr/bin/env python

import os
import os.path
import re
import time

from . import decorator


def size(path):
    return os.stat(path)[6]


def tail(path, seek=None):
    """
    Implements file tailing as a generator.  Yields line content or None.
    """
    with open(path) as f:
        if seek is None:
            # Seek to the end of the file
            seek = size(path)

        f.seek(seek)

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


@decorator.timeout
def exists(path, timeout=300):
    return os.path.exists(path)


def pattern(path, patterns, run=True, seek=None, timeout=300):
    """
    Wait until pattern(s) are detected by tailing a file.  Returns True when
    complete.

    If optional timeout is set and exceed then it returns False.
    """

    if isinstance(patterns, str):
        patterns = [patterns]
    elif isinstance(patterns, tuple):
        patterns = list(patterns)

    if seek is None and os.path.exists(path):
        seek = size(path)

    def check():
        start = time.time()

        if not exists(path, timeout=timeout):
            return False

        for line in tail(path, seek):
            if line is not None:
                for pattern in patterns:
                    if re.search(pattern, line):
                        patterns.remove(pattern)

            if not len(patterns):
                # Stop looping when all patterns have been matched
                break

            if timeout:
                if time.time() - start > timeout:
                    return False

        return True

    if run:
        return check()

    return check

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
