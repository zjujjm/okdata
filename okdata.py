import tushare as ts
import logging

log = logging.getLogger(__name__)
a = ts.get_today_all()

print a
