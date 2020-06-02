from engine.base_engine import BaseChatEngine
import json
import urllib.request

class BdChatEngine(BaseChatEngine):

    access_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=z0OVOGly9bb0HsmCcVV8AbfY&client_secret=4ekRssaYiT5RvTRq6yr6zSDzSY3b778A'
    base_url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat'

    def __init__(self):
        token_request = urllib.request.Request(self.access_token_url)
        token_open = urllib.request.urlopen(token_request)
        res = token_open.read().decode('utf8')
        res_dic = json.loads(res)
        access_token = res_dic['access_token']
        self.chat_url = self.base_url+'?access_token='+access_token

    def get_response(self, question):
        req = {
            'version': '2.0',
            'bot_id': '1022434',
            'log_id': '0001',
            'bot_session': '',
            'request': {
                'user_id': '185',
                'query': question,
                'bernard_level': 1,
                'query_info': {
                    'type': 'TEXT',
                    'source': 'KEYBOARD',

                }
            }

        }

        req = json.dumps(req).encode('utf8')
        request = urllib.request.Request(self.chat_url, data=req, headers={
                                         'content-type': 'application/json'})
        request_open = urllib.request.urlopen(request)
        res = request_open.read().decode('utf8')
        res_dic = json.loads(res)
        result_text = res_dic['result']['response']['action_list'][0]['say']
        return result_text

    def train_qa(self, q, a):
        pass
