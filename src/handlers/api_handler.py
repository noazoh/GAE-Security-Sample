#　-*- coding: utf-8 -*-
import logging
import json, datetime
import webapp2

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
        
