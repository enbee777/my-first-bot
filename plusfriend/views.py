from django.shortcuts import render
from .decorators import bot
from .functions import melon_search
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse 
from .melon_search import search
from .chart import melon_chart
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
        response = '멜론 "{}" 검색결과\n\n'.formate(query) + search(query)
    
    elif content.startswith('차트검색'):
        response = '멜론 "{}" 차트TOP50위 순위\n\n'.formate(query) + search(query)
    else:        
        response = '지원하는 명령어가 아닙니다.'

    if (message.find(u"문의사항")>-1 or message.find(u"오류")>-1 or message.find(u"이용권")>-1):
        return {
            'message' : {
                'text':'선택해주세요'
            },
            'keyboard': {
                "type":"buttons",
                "buttons" : ["재생이 안돼요ㅠㅠ","오류","이용권"]
            }
        }
    elif (message.find(u"재생이 안돼요ㅠㅠ")>-1):
        response = """다운로드 시점에 발생한 일시적인 오류로 인하여 곡 재생이 안될 수 있습니다.

멜론 플레이어에서 다운로드 목록은 아래와 같은 경로에서 확인하실 수 있습니다.

①   PLAYER 탭 > 마이뮤직 > 구매목록

②   WEB 탭 > 마이뮤직 > 구매목록에서 확인하실 수 있습니다."""

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

