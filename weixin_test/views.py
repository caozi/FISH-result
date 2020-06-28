from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy import WeChatClient
from django.views.decorators.csrf import csrf_exempt
from .models import Patient
from .weixin_config import TOKEN, appID, appsecret

client = WeChatClient(appID, appsecret)


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
            reply = create_reply('感谢关注天津市肿瘤医院病理科FISH检测公众号，点击查询，填写病人信息，查询FISH结果', msg)
        elif msg.event == 'subscribe':
            reply = create_reply('感谢关注天津市肿瘤医院病理科FISH检测公众号，点击查询，填写病人信息，查询FISH结果', msg)
        response = HttpResponse(reply.render(), content_type='application/xml')
        return response
    else:
        return HttpResponse('ERROR')


# 创建菜单
def create_menu(request):
    client.menu.create({
        "button": [
            {
                "type": "view",
                "name": "查询",
                "url": "http://georgecaozi.pythonanywhere.com/weixin/query_form"
            },
        ]
    }
    )
    return HttpResponse('ok')


def query_form(request):
    return render_to_response('weixin/query_form.html')



@csrf_exempt
def query_result(request):
    if request.method == 'POST':
        p_name = request.POST.get('patient_name', '')
        p_number = request.POST.get('patient_number', '')
        try:
            p = Patient.objects.get(patient_id=p_number)
            return render(request, 'weixin/query_result.html', {'patient': p})
        except Patient.DoesNotExist:
            return render_to_response('weixin/query_error.html')
    return HttpResponse('Data not received', content_type="text/plain")




