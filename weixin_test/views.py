from django.http import HttpResponse, HttpResponseRedirect
from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy import WeChatClient
from django.views.decorators.csrf import csrf_exempt
from .weixin_config import TOKEN, appID, appsecret
import json

client = WeChatClient(appID, appsecret)

with open('weixin_test/patients_data.json', 'r') as f:
    data = json.load(f)

with open('weixin_test/prices.json', 'r') as f:
    prices = json.load(f)

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
            if msg.content == '探针价格':
                reply = create_reply(price_result(), msg)
            else:
                reply = create_reply(query_result(msg.content), msg)
        elif msg.event == 'subscribe':
            reply = create_reply('感谢关注天津市肿瘤医院病理科FISH检测公众号。检测结果会在第一时间更新，请注意查看公众号消息。结果更新后您可以输入患者姓名，查询FISH结果。也可以咨询FISH检测相关问题，我们会在第一时间回复您。02223340123是病理科电话，请不要屏蔽。感谢您对我们工作的支持！', msg)
        response = HttpResponse(reply.render(), content_type='application/xml')
        return response
    else:
        return HttpResponse('ERROR')


def query_result(patient_name):
    try:
        return data[patient_name]
    except:
        return "没有该姓名信息，请检查姓名是否正确"


def price_result():
    result = ''
    for name in prices:
        result += name
        result += ':'
        result += prices[name]
        result += '\n\n'
    return  result





