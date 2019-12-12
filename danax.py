# Work with Python 3.6
import asyncio
import discord
import random
import datetime
from os import system
import re
from discord.ext import commands
import os

system("title "+"DANAX")

TOKEN = os.environ["BOT_TOKEN"]
calcResult = 0

client = discord.Client()

def check_queue(id):
    if queues[id]!=[]:
        player = queues[id].pop(0)
        players[id] = player
        del musiclist[0]
        player.start()

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    # 본인의 메시지에 답변을 하지 않음.
    fr = "~"
    if message.author == client.user:
        return

    if message.content.startswith(fr + '다낙스'):
        msg = '{0.author.mention}, ㅎㅇ!'.format(message)
        await client.send_message(message.channel, msg)
        
    if message.content==(fr + '버전'):
        embed = discord.Embed(title="DANAX 버전: 1.2.5", description=" ", color=0x00faf4)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith(fr + '상태'):
        text = message.content
        rpl = text.replace(fr + "상태", "")
        if message.author.server_permissions.administrator:
            await client.change_presence(game=discord.Game(name=rpl))
            msg = '상태 메시지가 바뀌었습니다.'.format(message)
            await client.send_message(message.channel, msg)

    if message.content.startswith(fr + '열대저기압'):
        msg = '남 인도양(사이클론):`사이클론 벨나`-90kts(C2)'.format(message)
        await client.send_message(message.channel, msg)

    if message.content==(fr + '가위'):
        str1 = ['가위','바위','보']
        r = random.choice(str1)
        if r == '가위':
            await client.send_message(message.channel, "님은 가위, DANAX는 " + r + "를 선택했다..." + "\n비겼다...")
        elif r == '바위':
            await client.send_message(message.channel, "님은 가위, DANAX는 " + r + "를 선택했다..." + "\n님이 졌다 ㅋ")
        elif r == '보':
            await client.send_message(message.channel, "님은 가위, DANAX는 " + r + "를 선택했다..." + "\n님이 이겼다 ㅠ")

    elif message.content==(fr + '바위'):
        str1 = ['가위','바위','보']
        r = random.choice(str1)
        if r == '바위':
            await client.send_message(message.channel, "님은 바위, DANAX는 " + r + "를 선택했다..." + "\n비겼다...")
        elif r == '보':
            await client.send_message(message.channel, "님은 바위, DANAX는 " + r + "를 선택했다..." + "\n님이 졌다 ㅋ")
        elif r == '가위':
            await client.send_message(message.channel, "님은 바위, DANAX는 " + r + "를 선택했다..." + "\n님이 이겼다 ㅠ")

    if message.content==(fr + '보'):
        str1 = ['가위','바위','보']
        r = random.choice(str1)
        if r == '보':
            await client.send_message(message.channel, "님은 보, DANAX는 " + r + "를 선택했다..." + "\n비겼다...")
        elif r == '가위':
            await client.send_message(message.channel, "님은 보, DANAX는 " + r + "를 선택했다..." + "\n님이 졌다 ㅋ")
        elif r == '바위':
            await client.send_message(message.channel, "님은 보, DANAX는 " + r + "를 선택했다..." + "\n님이 이겼다 ㅠ")

    if message.content==(fr + '도움'):
       embed = discord.Embed(title="DANAX 도움말", description="**~다낙스**:가벼운 인사를 건넵니다.\n**~버전**:DANAX의 버전을 알려줍니다.\n**~가위/바위/보**:DANAX와 가위바위보를 합니다.\n**~열대저기압**:현재 활동 중인 열대저기압 정보를 알려줍니다.\n**~주사위**:주사위를 굴립니다.\n**~확률**:확률을 랜덤으로 알려줍니다.(값이 백분율로 나오지 않습니다.)\n**~핑**:반응속도를 알려줍니다.\n**~음악 도움**:음악 봇 도움말을 알려줍니다.", color=0x00faf4)
       await client.send_message(message.channel, embed=embed)


    if message.content==(fr + '음악 도움'):
       embed = discord.Embed(title="DANAX 음악 도움말", description="**~재생 (링크)**:링크의 곡을 재생합니다.\n**~스킵**:현재 재생 중인 곡을 건너뜁니다.\n**~중지**:현재 재생 중인 곡을 중지합니다.", color=0x00faf4)
       await client.send_message(message.channel, embed=embed)

    
    if message.content.startswith(fr + '삭제 '):
        if type(message.channel) == discord.channel.Channel:
            if message.author.server_permissions.administrator:
                den = int(message.content[7:])
                if den > 0:
                    try:
                        async for m in client.logs_from(message.channel, limit=den+1):
                            await client.delete_message(m)
                        returnmsg = await client.send_message(message.channel, str(den) + "개의 메시지를 삭제하였습니다.")
                        await asyncio.sleep(2)
                        await client.delete_message(returnmsg)

                    except discord.errors.Forbidden:
                        await client.send_message(message.channel, '봇이 권한을 가지고 있지 않습니다.')
                        raise Exception

                    except discord.errors.HTTPException:
                        await  client.send_message(message.channel, '알 수 없는 오류가 발생했습니다')
                        raise Exception
                else:
                    await client.send_message(message.channel, "1개 이상의 메시지만 삭제할 수 있습니다!")
            else:
                await client.send_message(message.channel, '당신은 관리자 권한을 가지고 있지 않습니다.')
        else:
            await client.send_message(message.channel, '서버 채널에서만 이 명령어를 사용할 수 있습니다.')

    if message.content.startswith(fr + '주사위'):

        randomNum = random.randrange(1, 7) 
        print(randomNum)
        if randomNum == 1:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: '+ ':one:', color=0x00faf4))
        if randomNum == 2:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':two:', color=0x00faf4))
        if randomNum ==3:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':three:', color=0x00faf4))
        if randomNum ==4:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':four:', color=0x00faf4))
        if randomNum ==5:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':five:', color=0x00faf4))
        if randomNum ==6:
            await client.send_message(message.channel, embed=discord.Embed(description=':game_die: ' + ':six: ', color=0x00faf4))

    if message.content.startswith('!시간'):
            if(message.content == "!시간 1"):
                now = datetime.now()
                hr = "``" + str(now.hour) + "`` : "
                mi = "``" + str(now.minute) + "`` : "
                sc = "``" + str(now.second) + "``"
                if(now.hour > 12):
                    thr = now.hour - 12
                    hr = "``" + str(thr) + "`` : "
                    oj = "``오후``  "
                else:
                    oj = "``오전``  "
                await client.send_message(message.channel, oj + hr + mi+ sc)


            if(message.content == "!시간 2"):
                now = datetime.now()
                hr = str(now.hour) + "시 "
                mi = str(now.minute) + "분 "
                sc = str(now.second) + "초"
                if(now.hour > 12):
                    thr = now.hour - 12
                    hr = str(thr) + "시 "
                    oj = "오후 "
                else:
                    oj = "오전 "
                mtl = "현재 시간은 " + oj + hr + mi + sc + " 입니다."
                await client.send_message(message.channel, embed=discord.Embed(title = mtl, colour = 0x2EFEF7))

    if message.content.startswith(fr + '계산'):
        global calcResult
        if message.content[7:].startswith("더하기"):
            calcResult = int(message.content[11:12])+int(message.content[13:14])
            await client.send_message(message.channel, "Result : "+str(calcResult))
        if message.content[7:].startswith("빼기"):
            calcResult = int(message.content[10:11])-int(message.content[12:13])
            await client.send_message(message.channel, "Result : "+str(calcResult))
        if message.content[7:].startswith("곱하기"):
            calcResult = int(message.content[11:12])*int(message.content[13:14])
            await client.send_message(message.channel, "Result : "+str(calcResult))
        if message.content[7:].startswith("나누기"):
            try:
                calcResult = int(message.content[11:12])/int(message.content[13:14])
                await client.send_message(message.channel, "Result : "+str(calcResult))
            except ZeroDivisionError:
                await client.send_message(message.channel, "0으로는 나눌 수 없습니다.")

    if message.content.startswith(fr + '확률'):
        sans = ['없음', '거의 없음', '매우 낮음', '낮음', '조금 낮음', '보통', '조금 높음', '높음', '매우 높음', '거의 100%', '100%']
        r = random.choice(sans)
        if r == '없음':
            await client.send_message(message.channel, "그럴 확률은 " +  "없습니다.")
        if r == '매우 낮음':
            await client.send_message(message.channel, "그럴 확률은 " +  "매우 낮습니다.")
        if r == '낮음':
            await client.send_message(message.channel, "그럴 확률은 " +  "낮습니다.")
        if r == '보통':
            await client.send_message(message.channel, "그럴 확률은 " + r + "입니다.")
        if r == '조금 높음':
            await client.send_message(message.channel, "그럴 확률은 " +  "조금 높습니다.")
        if r == '높음':
            await client.send_message(message.channel, "그럴 확률은 " +  "높습니다.")
        if r == '매우 높음':
            await client.send_message(message.channel, "그럴 확률은 " +  "매우 높습니다.")
        if r == '거의 100%':
            await client.send_message(message.channel, "그럴 확률은 " +  "거의 100%입니다.")
        if r == '100%':
            await client.send_message(message.channel, "그럴 확률은 " +  "100%입니다.")
        if r == '거의 없음':
            await client.send_message(message.channel, "그럴 확률은 " +  "거의 없습니다.")
        if r == '조금 낮음':
            await client.send_message(message.channel, "그럴 확률은 " +  "조금 낮습니다.")

    if message.content == (fr + '앵무새'):
        msg = replace.format(message)
        await client.send_message(message.channel, msg)

    if (message.content == fr + '인원 수'):
        usr = 0
        activeServers = client.servers
        for s in activeServers:
            usr += len(s.members)


        ppl = str(usr)
        gam = "`~도움` | 12개 서버 | " + ppl + "명"
        await client.change_presence(game=discord.Game(name=gam))
        mtl = ":o: 설명창을 확인해주세요!"
        await client.send_message(message.channel, embed=discord.Embed(title = mtl, colour = 0x00faf4))



        
@client.event
async def on_ready():
    usr = 0
    activeServers = client.servers
    for s in activeServers:
        usr += len(s.members)


    ppl = str(usr)
    gam = "`~도움` | 12개 서버 | " + ppl + "명"
    await client.change_presence(game=discord.Game(name=gam, type=1))
    print('다음 계정으로 로그인됨:')
    print(client.user.name)
    print(client.user.id)
    print('--- 동작 중 ---')

client.run(TOKEN)
