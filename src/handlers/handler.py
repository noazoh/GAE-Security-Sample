#　-*- coding: utf-8 -*-
import logging
import json, datetime
import os, webapp2
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

        fpath = os.path.join(main.TEMPLATEPATH, "index.html")
        html = template.render(fpath, None)
        self.response.out.write(html)
        
    def post(self, *args, **kwargs):
        logging.debug("query_string=" + self.request.query_string)
        logging.debug(kwargs)
        logging.debug(args)
        
        #ここでWebAPIを呼ぶ
        #今はダミー実装しておく
        param = {
                "data1": "POST Method",
                "data2": datetime.datetime.today() + datetime.timedelta(hours=9),
                 }
        fpath = os.path.join(main.TEMPLATEPATH, "index.html")
        html = template.render(fpath, param)
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
                "data1": "WebAPI",
                "data2": (datetime.datetime.today() + datetime.timedelta(hours=9)).strftime("%Y/%m/%d %H:%M:%S"),
                }
        #文字列にシリアライズ
        json_str = json.dumps(json_data, sort_keys=True)
        logging.debug("**** json_str = [" + json_str + "]")
        self.response.out.write(json_str)
        
