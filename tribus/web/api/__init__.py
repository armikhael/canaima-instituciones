#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tastypie.api import Api
from tribus.web.api.resources import TribResource, TimelineResource, CommentResource

api_01 = Api(api_name='0.1')
api_01.register(TribResource())
api_01.register(CommentResource())
api_01.register(TimelineResource())
