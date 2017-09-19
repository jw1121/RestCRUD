from pydev import pydevd


pydevd.settrace('10.211.55.7', port=51234, stdoutToServer=True, stderrToServer=True)