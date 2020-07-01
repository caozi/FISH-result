from django.http import HttpResponse, HttpResponseRedirect
from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy import WeChatClient
from django.views.decorators.csrf import csrf_exempt
from .weixin_config import TOKEN, appID, appsecret
import json

client = WeChatClient(appID, appsecret)

with open('patients_data.json','r') as f:
    data = json.load(f)

@csrf_exempt
def index(request):
    if request.method == 'GET':
        signature = request.GET.get('signature', '')
        timestamp = request.GET.get('timestamp', '')
        nonce = request.GET.get('nonce', '')
        echostr = request.GET.get('echostr', '')
        try:
            check_signature(TOKEN, signature, timestamp, nonce)
        except InvalidSignatureException:
            echostr = 'error'
        response = HttpResponse(echostr, content_type="text/plain")
        return response
    elif request.method == 'POST':
        reply = None
        msg = parse_message(request.body)
        if msg.type == 'text':
            reply = create_reply(query_result(msg.content), msg)
        elif msg.event == 'subscribe':
            reply = create_reply('感谢关注天津市肿瘤医院病理科FISH检测公众号，输入住院号，查询FISH结果', msg)
        response = HttpResponse(reply.render(), content_type='application/xml')
        return response
    else:
        return HttpResponse('ERROR')


def query_result(patient_hospital_number):
    try:
        return data[patient_hospital_number]
    except:
        return "没有该住院号信息，请检查住院号是否正确"




