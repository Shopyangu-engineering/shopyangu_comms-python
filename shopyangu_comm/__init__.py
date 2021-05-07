from .SMS import SMSService


SMS = None
Voice = None



def initialize(api_key):

    if api_key is None:
        raise RuntimeError('Invalid api_key')

    globals()['SMS'] = SMSService(api_key)
    # globals()['Airtime'] = AirtimeService(username, api_key)
    # globals()['Payment'] = PaymentService(username, api_key)
    # globals()['Voice'] = VoiceService(username, api_key)
    # globals()['Application'] = ApplicationService(username, api_key)
    # globals()['Token'] = TokenService(username, api_key)