#!/usr/bin/env python

from tempfile import NamedTemporaryFile
import unittest

import socket
import wait


class TestWait(unittest.TestCase):

    def setUp(self):
        self.file = NamedTemporaryFile()
        self.port = 9999
        self.patterns = ['foo', 'bar', 'f.*']

    def pattern(self, *args, **kwargs):
        return wait.log.pattern(self.file.name, *args, **kwargs)

    def write(self, s):
        self.file.write(s.encode('utf-8'))
        self.file.write('\n'.encode('utf-8'))
        self.file.flush()

    def test_log_exists(self):
        assert wait.log.exists(self.file.name)

    def test_log_exists_timeout(self):
        assert not wait.log.exists('/tmp/nolog', timeout=1)

    def test_log_pattern_list(self):
        seek = self.file.tell()
        self.write(self.patterns[0])
        self.write(self.patterns[1])
        assert self.pattern(self.patterns, seek=seek, timeout=5)

    def test_log_pattern_tuple(self):
        seek = self.file.tell()
        self.write(self.patterns[0])
        self.write(self.patterns[1])
        assert self.pattern(tuple(self.patterns), seek=seek, timeout=5)

    def test_log_pattern_string(self):
        seek = self.file.tell()
        self.write(self.patterns[0])
        assert self.pattern(self.patterns[0], seek=seek, timeout=5)

    def test_log_pattern_nostart(self):
        p = self.pattern(self.patterns, run=False, timeout=5)
        self.write(self.patterns[0])
        self.write(self.patterns[1])
        assert p()

    def test_log_pattern_timeout(self):
        assert not wait.log.pattern('/tmp/nolog', self.patterns, timeout=1)
        assert not self.pattern(self.patterns, timeout=1)

    def test_tcp_closed(self):
        assert wait.tcp.closed(self.port, timeout=1)
        assert not wait.tcp.open(self.port, timeout=1)

    def test_tcp_open(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', self.port))
        s.listen(0)
        assert not wait.tcp.closed(self.port, timeout=1)
        assert wait.tcp.open(self.port, timeout=1)
        assert wait.tcp.open(80, host='www.google.com', timeout=5)
        s.close()

    def test_tcp_socket_timeout(self):
        assert wait.tcp.closed(self.port, host='10.255.255.1', timeout=1)
        assert not wait.tcp.open(self.port, host='10.255.255.1', timeout=1)

    def test_tcp_open_timeout(self):
        assert not wait.tcp.open(self.port, timeout=1)

    def tearDown(self):
        self.file.close()

if __name__ == '__main__':
    unittest.main()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
