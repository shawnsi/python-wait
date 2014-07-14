#!/usr/bin/env python

from tempfile import NamedTemporaryFile
import unittest

import wait

class TestWait(unittest.TestCase):


    def setUp(self):
        self.file = NamedTemporaryFile()
        self.patterns = ['foo', 'bar', 'f.*']

    def pattern(self, *args, **kwargs):
        return wait.log.pattern(self.file.name, *args, **kwargs)

    def write(self, s):
        self.file.write(s.encode('utf-8'))
        self.file.write('\n'.encode('utf-8'))
        self.file.flush()

    def test_log_pattern_list(self):
        seek = self.file.tell()
        self.write(self.patterns[0])
        self.write(self.patterns[1])
        assert self.pattern(self.patterns, seek=seek, timeout=5)

    def test_log_pattern_string(self):
        seek = self.file.tell()
        self.write(self.patterns[0])
        assert self.pattern(self.patterns[0], seek=seek, timeout=5)

    def test_log_pattern_timeout(self):
        assert not self.pattern(self.patterns, timeout=0)

if __name__ == '__main__':
    unittest.main()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

