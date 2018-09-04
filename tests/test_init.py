# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test modules."""


def test_init(hello_world):
    """Run a test."""
    import flask_rq_status

    # Test __init__
    assert hasattr(flask_rq_status, '__version__')

    # Test pytest fixtures
    assert(hello_world == "Hello World!")