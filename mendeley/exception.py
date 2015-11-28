import logging

class MendeleyException(Exception):
    pass


class MendeleyApiException(MendeleyException):
    def __init__(self, rsp):
        self.rsp = rsp

    def __str__(self):
        return 'The Mendeley API returned an error (status: %s, message: %s)' % (self.status, self.message)

    @property
    def status(self):
        return self.rsp.status_code

    @property
    def message(self):
        logging.debug(self.rsp.json())
        try:
            return self.rsp.json()
        except ValueError:
            return self.rsp.text
