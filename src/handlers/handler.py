#　-*- coding: utf-8 -*-
import logging
import json
import os
import webapp2
from src import main
from google.appengine.ext.webapp import template
from google.appengine.api import users

class MainHandler(webapp2.RequestHandler):
    """
    /
    """
    def __init__(self, *args, **kwargs):
        #基底クラスの__init__()を呼ぶ
        super(MainHandler, self).__init__(*args, **kwargs)

    def get(self, *args, **kwargs):
        logging.debug("query_string=" + self.request.query_string)
        logging.debug(kwargs)
        logging.debug(args)

        params = {
                  "param1": "param1",
                  "param2": "param2",
                  }
        fpath = os.path.join(main.TEMPLATEPATH, "index.html")
        html = template.render(fpath, params)
        self.response.out.write(html)

class APIHandler(webapp2.RequestHandler):
    """
    /api
    """
    def __init__(self, *args, **kwargs):
        #基底クラスの__init__()を呼ぶ
        super(APIHandler, self).__init__(*args, **kwargs)

    def get(self, *args, **kwargs):
        logging.debug("**** API ****")
        logging.debug("query_string=" + self.request.query_string)
        logging.debug(kwargs)
        logging.debug(args)

        json_data = {
                "data1": "data-1",
                "data2": "data-2",
                }
        #文字列にシリアライズ
        json_str = json.dumps(json_data, sort_keys=True)
        logging.debug("**** json_str = [" + json_str + "]")
        self.response.out.write(json_str)
        
