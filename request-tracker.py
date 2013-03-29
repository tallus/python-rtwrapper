#!/usr/bin/env python
import unittest
#from  rt import RT as RequestTracker
import rt
import timedate
from timdate import timedelta

########################################
#           Configuration              #
########################################

rt_queue='TechSupport'
rt_host='todo.freegeek.org'
rt_user='tsrobot'
rt_password='EucNabs4'
rt_url='http://' + rt_host + '/REST/1.0/'
########## Configuration ends ##########

#class RT(RequestTracker):
#    '''Extends base class'''
#    def foo():
#        pass

class MyTests(unittest.TestCase):
    def __init__(rqt):
        self.rqt = rqt
    def test_is_valid_ticket(self):
        result = rqt.is_valid_ticket('34716')
        self.assertTrue(result)

    def test_is_active_ticket(self):
        result = rqt.is_active_ticket('34716')
        self.assertTrue(result)
    
    def test_is_active_ticket_false(self):
        result = rqt.is_active_ticket('21950')
        self.assertFalse(result)

### FUNCTIONS ###

#def login():
    # return success/fail

class RT(RequestTracker):

    def is_valid_ticket(self, ticket):
        ''' Returns true if ticket number supplied exists in the 
        tech support queue'''
        try:
            search_results = rqt.search('TechSupport',id=ticket)
            if len(search_results) > 0:
                return True
            else:
                return False
        except:
                return False

    def is_active_ticket(self, ticket):
        '''Returns true if ticket number supplied exists in the 
        tech support queue and is not resolved'''
        # the rt module doesn't work with e.g. Status!='resolved'
        # so this is a double test, checking if resolved
        # if not check it is in tech support
        try:
            search_results = rqt.search('TechSupport',status='resolved', id=ticket)
            if len(search_results) > 0:
                is_not_resolved = False
            else:
                search_results = rqt.search('TechSupport', id=ticket)
                if len(search_results) > 0:
                    is_not_resolved = True
            return is_not_resolved
        except:
                return False


    def is_older_than(self, statustype, days):
        # Status = 'contact' AND LastUpdated < '2013-03-27' AND Queue = 'TechSupport'
        today = datetime.datetime.today()
        timedelta = datetime.timedelta(days)
        cutoff = today - timedelta
        search_results = rqt.search('TechSupport', status=statustype, LastUpdated<cutoff)
        # return list of ids

if __name__ == "__main__":
    tracker = RT(rt_url, rt_user, rt_password)
    tracker.login()
    unittest.main(tracker)

