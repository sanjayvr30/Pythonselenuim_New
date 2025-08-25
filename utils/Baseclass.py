import inspect
import logging

import pytest


@pytest.mark.usefixtures("invoke_retailer")
class Baseclass:

    def logging(self):
        logername =inspect.stack()[1][3]
        log = logging.getLogger(logername)
        filepath = logging.FileHandler('C:\\Users\\sanjay.ravisha.STS\\Downloads\\logs.log')
        formatter = logging.Formatter("[%(asctime)s]::[%(levelname)s]::[%(name)s]::[%(message)s]")
        filepath.setFormatter(formatter)
        log.addHandler(filepath)
        log.setLevel(logging.INFO)
        return log