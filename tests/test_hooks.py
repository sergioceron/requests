#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import requests
from requests.models import Request

class TestHooks(unittest.TestCase):
    def test_multiple_hooks(self):
        
        # Define multiple hook functions
        def hook1(data):
            data['stage'] += 'a'
            return data

        def hook2(data):
            data['stage'] += 'b'
            return data

        def hook3(data):
            data['stage'] += 'c'
            return data

        # Initialize a request
        data = {'stage': ''}
        hooks = {'args': [hook1, hook2, hook3]}
        request = Request(hooks=hooks)

        # Dispatch hooks
        dispatched_data = request.hooks['args']
        for hook in dispatched_data:
            data = hook(data)

        # Check if hooks are applied in the correct order
        self.assertEqual(data['stage'], 'abc')
        

if __name__ == '__main__':
    unittest.main()
