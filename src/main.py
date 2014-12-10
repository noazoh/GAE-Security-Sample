#　-*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging
import os, webapp2
from google.appengine.ext.webapp import template

ROOTPATH = os.path.dirname(__file__)
TEMPLATEPATH = os.path.join(ROOTPATH, 'templates')
HANDLERSPATH = 'src.handlers.'


routes = [
          webapp2.Route('/', handler=HANDLERSPATH + 'handler.MainHandler'),
          webapp2.Route('/api', handler=HANDLERSPATH + 'handler.APIHandler'),
          ]

app = webapp2.WSGIApplication(routes, debug=True)
