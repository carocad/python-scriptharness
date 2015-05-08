#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python scripting harness / framework.

Core principles:
  Full logging.
  Flexible configuration.
  Modular actions.

Attributes:
  __version__ (tuple): semver version - three integers and an optional string.
  __version_string__ (str): semver version in string format.
"""
from __future__ import absolute_import, division, print_function, \
                       unicode_literals
import six


# scriptharness exceptions + unicode support {{{1
@six.python_2_unicode_compatible
class ScriptHarnessBaseException(Exception):
    """All scriptharness exceptions should inherit this exception.

    However, in most cases you probably want to catch ScriptHarnessException
    instead.
    """
    def __str__(self):
        """
        """
        if six.PY3:
            string = super(ScriptHarnessBaseException, self).__str__()
        else:
            string = super(ScriptHarnessBaseException, self).message
        try:
            new_string = six.text_type(string, 'utf-8')
            string = new_string
        except TypeError:
            pass
        return string

class ScriptHarnessException(ScriptHarnessBaseException):
    """All developer-facing exceptions should inherit this class.

    There is a problem in how scriptharness is being called.
    If you want to catch all developer-facing scriptharness exceptions,
    catch ScriptHarnessException.
    """

class ScriptHarnessFailure(ScriptHarnessBaseException):
    """User-facing exception.

    Scriptharness has detected a failure in the running process.
    This exception should result in program termination; using try/except may
    result in unexpected or dangerous behavior.
    """

# py2 unicode help.  This may move into a separate file later.
def to_unicode(obj, encoding='utf-8'):
    """Encode a string as unicode in python2.

    http://farmdev.com/talks/unicode/

    Args:
        obj (str): the string to encode
        encoding (str, optional): the encoding to use

    Returns:
        obj (unicode): the encoded string
    """
    if not isinstance(obj, six.text_type):
        obj = six.text_type(obj, encoding)
    return obj


# get_version_string {{{1
def get_version_string(version):
    """Translate a version tuple into a string.

    Specify the __version__ as a tuple for more precise comparisons, and
    translate it to __version_string__ for when that's needed.

    This function exists primarily for easier unit testing.

    Args:
      version (tuple): three ints and an optional string.

    Returns:
      version_string (str): the tuple translated into a string per semver.org
    """
    version_len = len(version)
    if version_len == 3:
        version_string = '%d.%d.%d' % version
    elif version_len == 4:
        version_string = '%d.%d.%d-%s' % version
    else:
        raise ScriptHarnessException(
            'Version tuple is non-semver-compliant {0} length!'.format(version_len)
        )
    return version_string
# 1}}}


# Semantic versioning 2.0.0  http://semver.org/
__version__ = (0, 1, 0, 'alpha')
__version_string__ = get_version_string(__version__)
