python-wait
===========

[![Build Status](https://travis-ci.org/shawnsi/python-wait.png)](https://travis-ci.org/shawnsi/python-wait)

Logs
----

Block until log matches pattern.  Starts tailing from the end of the file.

```python
import wait

wait.log('/path/to/log', 'foobar')
```

Block until log matches multiple patterns.

```python
wait.log('/path/to/log', ['foo', 'bar'])
```

Set a timeout in seconds.  Returns false if timeout is exceeded.

```python
wait.log('/path/to/log', ['foo', 'bar'], timeout=5)
```

