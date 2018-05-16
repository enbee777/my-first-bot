from django.shortcuts import render
from .decorators import bot
from .functions import melon_search
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse 
from .melon_search import search
from .chart import melon_chart
from .image import get_image
import json


@bot
def on_init(request):
    return {'type':'text'}

@bot
def on_message(request):
    user_key = request.JSON['user_key']    
    type = request.JSON['type']    
    content = request.JSON['content']  # photo 타입일 경우에는 이미지 URL로 나온당
    message = ((request.body) .decode('utf-8'))

    if content.startswith('멜론검색:'):        
        query = content[5:]
        response = '멜론 "{}" 검색결과\n\n'.format(query) + melon_search(query)

    elif content.startswith('노래검색:'):
        query = content[5:]
        response = '멜론 "{}" 검색결과\n\n'.format(query) + search(query)
    
    elif content.startswith('차트검색'):
        response = '멜론 차트TOP50위 순위\n\n' + melon_chart()

    elif content.startswith('이미지검색:'):
        query = content[6:]
        url = get_image(query)
        return({
            "message": {
                'text': '결과: '+query,
                "photo": {
                    "url":url,
                    "width":640,
                    "height": 480
                }
            }
        })
    else:        
        response = '지원하는 명령어가 아닙니다.'

    if (message.find(u"비밀번호")>-1 or message.find(u"오류")>-1 or message.find(u"이용권")>-1):
        return {
            'message' : {
                'text':'선택해주세요'
            },
            'keyboard': {
                "type":"buttons",
                "buttons" : ["재생이 안돼요","이용권","비밀번호 찾기"]
            }
        }
    elif (message.find(u"재생")>-1):
        response = """다운로드 시점에 발생한 일시적인 오류로 인하여 곡 재생이 안될 수 있습니다.

멜론 플레이어에서 다운로드 목록은 아래와 같은 경로에서 확인하실 수 있습니다.

①   PLAYER 탭 > 마이뮤직 > 구매목록

②   WEB 탭 > 마이뮤직 > 구매목록에서 확인하실 수 있습니다.""",
    
    elif (message.find(u"이용권")>-1):
        response = """① MP3 이용권 - MP3 파일 다운로드만 제공

 MP3 30, MP3 40, MP3 50, MP3 100, MP3 150으로 구성
(음악 MP3 파일과 어학 MP3 파일을 MP3 뒤에 붙은 숫자만큼 각각 다운로드 가능)

② MP3 플러스 이용권 - MP3 파일 다운로드 및 무제한 듣기 제공

 MP3 30 플러스, MP3 40 플러스, MP3 50 플러스, MP3 100 플러스, MP3 150 플러스로 구성
(MP3 파일과 어학 MP3 파일을 MP3 뒤에 붙은 숫자 만큼 각각 다운로드 받을 수 있는 동시에 음악, 어학, 뮤직비디오 무제한 듣기(보기) 제공)

 ☞http://www.melon.com/commerce/pamphlet/web/sale_listMainView.htm☜"""
    
    elif (message.find(u"비밀번호 찾기")>-1):
        response = """비밀번호 찾기를 통해 본인임이 확인되면 비밀번호를 즉시 변경하실 수 있습니다. 

 

1. 회원정보에 등록된 정보(휴대폰번호, 이메일)로 찾기 

① 아이디/이름/회원정보에 등록된 정보(휴대폰번호 또는 이메일)를 입력 후 인증번호를 요청해주세요.

   회원정보에 등록된 정보와 다를 경우, 본인확인이 완료되지 않았기 때문에 인증번호를 받을 수 없습니다.

②입력하신 인증번호가 정확할 경우, 비밀번호를 변경할 수 있습니다.

 

2. 본인확인(본인명의 휴대폰인증) 정보로 찾기

① 본인확인(실명인증)이 완료된 아이디는 본인명의 휴대폰인증을 통해 찾을 수 있습니다.

   해당 인증방법은 본인확인이 완료된 아이디에 한하여 제공됩니다.

② 본인확인 정보와 동일한 정보가 있을 경우, 비밀번호 재설정을 진행할 수 있습니다.

 

* 회원정보가 정확하지 않거나 본인확인 정보가 없는 아이디는 아이디/비밀번호 찾기를 진행할 수 없습니다."""
    
    

    return {
        'message': {            
            'text': response,        
            },
        'keyboard': {
            'type': 'text',
        }
    }    

@bot
def on_added(request):
    pass

@bot
def on_block(request, user_key):
    pass

@bot
def on_leave(request, user_key):
    pass

