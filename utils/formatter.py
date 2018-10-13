import logging
from datetime import datetime
import pytz

class Formatter(logging.Formatter):
    def converter(self, timestamp):
        return self.posix2local(timestamp)

    def formatTime(self, record, datefmt=None):
        dt = self.converter(record.created)
        if datefmt:
            s = dt.strftime(datefmt)
        else:
            t = dt.strftime(self.default_time_format)
            s = self.default_msec_format % (t, record.msecs)
        return s

    def posix2local(self, timestamp, tz = pytz.timezone('Asia/Shanghai')):
        return datetime.fromtimestamp(timestamp, tz)