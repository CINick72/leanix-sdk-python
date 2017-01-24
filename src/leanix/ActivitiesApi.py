#!/usr/bin/env python
"""
The MIT License (MIT)

Copyright (c) 2017 LeanIX GmbH

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

from models import *


class ActivitiesApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    

    def getActivities(self, **kwargs):
        """
        Get the latest activities

        Args:
            scope, str: If set to 'my', only the activities related to subscribed Fact Sheet are listed for the authenticated user. (optional)

            startDate, str: If set, only activities greater or equal the given date time are retrieved. If no start time is given, then the start time is calculated based on the last event. (optional)

            endDate, str: If set, only activities less or equal the given date time are retrieved. If no end time is given, all activities until today are selected. (optional)

            factSheetType, str: Type of Fact Sheet, e.g. services for Application (optional)

            eventType, str: Event type, e.g. creation of a Fact Sheet: OBJECT_CREATE (optional)

            countOnly, integer: If set to 1, then only the count is transmitted and data is left empty (optional)

            

        Returns: ActivityStream
        """

        allParams = ['scope', 'startDate', 'endDate', 'factSheetType', 'eventType', 'countOnly']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getActivities" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/activities'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        bodyParam = None

        if ('scope' in params):
            queryParams['scope'] = self.apiClient.toPathValue(params['scope'])
        if ('startDate' in params):
            queryParams['startDate'] = self.apiClient.toPathValue(params['startDate'])
        if ('endDate' in params):
            queryParams['endDate'] = self.apiClient.toPathValue(params['endDate'])
        if ('factSheetType' in params):
            queryParams['factSheetType'] = self.apiClient.toPathValue(params['factSheetType'])
        if ('eventType' in params):
            queryParams['eventType'] = self.apiClient.toPathValue(params['eventType'])
        if ('countOnly' in params):
            queryParams['countOnly'] = self.apiClient.toPathValue(params['countOnly'])
        if formParams:
            headerParams['Content-type'] = 'application/x-www-form-urlencoded'

        # postData = (formParams if formParams else bodyParam)
        postData = params['body'] if 'body' in params else None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'ActivityStream')
        return responseObject
        

        

    




