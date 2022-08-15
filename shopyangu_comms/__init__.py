from .SMS import SMSService

SMS = None
Voice = None


def initialize(api_key):

    if api_key is None:
        raise RuntimeError('Invalid api_key')

    globals()['SMS'] = SMSService(api_key)
