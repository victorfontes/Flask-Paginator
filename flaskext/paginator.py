from __future__ import absolute_import

from flask import _request_ctx_stack, request
from math import ceil

class Pagination(object):
    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2, right_current=5, right_edge=2):
        last = 0
        for num in xrange(1, self.pages + 1):
            if num <= left_edge or \
               (num > self.page - left_current - 1 and \
                num < self.page + right_current) or \
               num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num

class Paginator(object):
    def __init__(self, app):
        self.app = app

        self.app.config.setdefault('PAGINATION_ITEMS_PER_PAGE', 10)
        self.app.config.setdefault('PAGINATION_PARAM', 'page')        
        self.managers = {}
        #self.app.teardown_request(self.teardown_request)
        #self.app.before_request(self.before_request)

    def _per_page(self, per_page):
        return per_page or self.app.config['PAGINATION_ITEMS_PER_PAGE']

    def _register_dic(self, f_total, per_page):
        return {
            'f_total': f_total,
            'per_page': self._per_page(per_page)
        }

    def register(self, label, f_total, per_page=None):
        if self.managers.has_key(label):
            raise Exception('Label already registered')

        pages_dic = self._register_dic(f_total, per_page)
        self.managers[label] = pages_dic
        manager_attr = 'for_' + label.lower()

    def _manager(self, label):
        for k,v in self.managers.items():
            if k.lower() == label.lower():
                return v
        return None

    def get_manager(self, label):
        manager = self._manager(label)
        return Pagination(self._current_page(), manager['per_page'], manager['f_total']())

    def _current_page(self):
        return int(request.args.get(self.app.config['PAGINATION_PARAM'], '1'))

    def __getattribute__(self, attr):
        if attr.startswith('for_'):
            label = attr.replace('for_', '')         
            return self.get_manager(label)
        else:
            return object.__getattribute__(self, attr)
