python-wait
===========

[![Build Status](https://travis-ci.org/shawnsi/python-wait.png?branch=master)](https://travis-ci.org/shawnsi/python-wait)

Logs
----

Block until log matches pattern.  Starts tailing from the end of the file.

```python
wait.log.pattern('/path/to/log', 'foobar')
```

Block until log matches multiple patterns.

```python
wait.log.pattern('/path/to/log', ['foo', 'bar'])
```

Wait for log file to exist.

```python
wait.log.exists('/path/to/log')
```

An optional `run` argument which defaults to `False` is available.  If set to
`True` the initial function call returns the actual wait function initialized
to the current position.

```python
w = wait.log.pattern('/path/to/log', 'foo', run=False)
# Do something here
w()
```

TCP Ports
---------

Block until tcp port 80 is listening on localhost.

```python
wait.tcp.open(80)
```

Block until tcp port 80 is closed on localhost.
```python
wait.tcp.closed(80)
```

Block until tcp port 80 is listening on a remote host.

```python
wait.tcp.open(80, host='www.google.com')
```

Timeouts
--------

All wait functions take an optional timeout argument which defaults to `300`.
The function will return `False` if the timeout is set and exceeded.  The
timeout is expressed in seconds.

```python
wait.log.pattern('/path/to/log', ['foo', 'bar'], timeout=5)
```

An indefinitely blocking call can be created by setting timeout to `0`.

```python
wait.log.exists('/path/to/log', timeout=0)
```
