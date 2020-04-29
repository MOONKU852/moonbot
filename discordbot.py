import discord
import random
import asyncio
import os
import json
import datetime
from discord.ext import commands
from discord.ext.commands import bot
from captcha.image import ImageCaptcha
import random

bot = commands.Bot(command_prefix='~')
os.chdir(r'C:\Users\mensu\OneDrive\바탕 화면\youtube_discord_bot')

@bot.event
async def on_ready():
    print(bot.user.id)
    print('준비완료!')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('~도와줘: 명령어 목록 | moonku3479#0037'))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('잘못된 명령어입니다!')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="손님-오셨당🤗")
    channe = discord.utils.get(member.guild.channels, name="규칙방📜")
    await channel.send(f"**{member.mention}**님 저희 [문쿠 커뮤니티]에 오신 걸 환영합니다!:hugging: {channe.mention} 에 있는 규칙 읽어주세요!\n`현재 [문쿠 커뮤니티] 인원수: {len(list(member.guild.members))}`")
    role = discord.utils.get(member.guild.roles, name="사람")
    await member.add_roles(role)

@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="손님-나가셨당😥")
    await channel.send(f"**{member}**님 님 저희 [문쿠 커뮤니티]를 떠나셨군요. 안녕히 가세요.:disappointed_relieved:\n`현재 [문쿠 커뮤니티] 인원수: {len(list(member.guild.members))}`")

@bot.command()
async def 도와줘(ctx):
    embed = discord.Embed(color = 89999)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="명령어 접두사", value="~", inline=False)
    embed.add_field(name="관리자 전용 명령어", value="킥: 플레이어 킥(추방) 명령어\n밴: 플레이어 밴(차단) 명령어\n뮤트: 플레이어 뮤트(채팅 금지) 명령어\n언뮤트: 플레이어의 뮤트(채팅 금지)를 푸는 명령어", inline=False)
    embed.add_field(name="VIP 명령어", value="VIP: VIP의 혜택과 얻는 방법을 알려준다.", inline=False)
    embed.add_field(name="규칙 명령어", value="규칙: 서버 규칙을 알려준다.", inline=False)
    embed.add_field(name="서버 매니저 명령어", value="서버매니저: 서버 매니저가 하는 일과 얻는 방법을 알려준다.", inline=False)
    embed.add_field(name="시간 명령어", value="현재시간: 현재 시간을 알려준다.", inline=False)
    embed.add_field(name="정보 명령어", value="내정보: 내 디스코드 계정의 정보를 알려준다.", inline=False)
    embed.add_field(name="핑 명령어", value="핑: 현재 나의 디스코드 핑을 알려준다.", inline=False)
    embed.add_field(name="캡챠 명령어", value="캡챠: 캡챠 시스템으로 봇인지 테스트한다.", inline=False)
    embed.add_field(name="GFX 명령어", value="GFX: GFX만들어 달라 할 때 말해줘야 하는 것과\n지금까지 문쿠가 이 디스코드에서 만들어준 사람들 닉네임을 알려준다.", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def VIP(ctx):
    embed = discord.Embed(color = 89999)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="VIP 얻는방법", value="VIP는 구매를 해야 얻는 것이 아닙니다!\n문쿠 혹은 물탁이 와 서로 친한 사이거나\n저희 [문쿠 커뮤니티]에서 오랫동안 활동하거나 도와주신다면 얻으실 수 있습니다!", inline=False)
    embed.add_field(name="VIP 혜택", value="•VIP 역할\n•VIP 태그 (원하지 않으신다면 안 사용하셔도 됩니다.)\n•별명 변경\n•tts\n•외부 이모티콘\n•자신만의 역할 주문 제작", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 규칙(ctx):
    embed = discord.Embed(color = 89999)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="채팅 규칙1", value="•욕설 사용 시 경고\n•싸움 시 경고 3\n•차별 시 경고 3\n•타인 비하 시 경고 4\n•도배 시 뮤트\n•구걸 시 뮤트\n•정치 관련 내용을 말할 시 그 글 삭제, 경고 2\n•채팅방을 제외한 방에서 수다 떨 시 그 글 삭제, 경고 1\n•홍보방 제외한 방에서 홍보할 시 그 글 삭제, 경고 2", inline=False)
    embed.add_field(name="채팅 규칙2", value="•봇-명령어방을 제외한 방에서 봇 명령어를 사용할 시 그 글 삭제, 경고 2\n•음악봇-명령어방을 제외한 방에서 음악봇 명령어를 사용할 시 그 글 삭제, 경고 2\n•출첵-강화방을 제외한 방에서 출석체크, 강화 명령어를 사용할 시 그 글 삭제, 경고 2\n•이상한 사이트, 디스코드 초대 링크 유포 시 그 글 삭제, 경고 3\n•공포감을 주는 이모티콘, 사진, 영상, GIF 유포 시 그 글 삭제, 경고 1\n•음란물 관련 단어, 이모티콘을 사용하거나 사이트, 디스코드 서버 초대 링크, 사진, 동영상, GIF 유포 시 그 글 삭제, 차단", inline=False)
    embed.add_field(name="권력남용 규칙", value="•허락 없이 마음대로 자신 혹은 타인에게 역할을 주거나 삭제 시 그 전으로 되돌림, 경고 4\n•허락 없이 마음대로 자신 혹은 타인의 인증됨 역할 삭제 시 그 전으로 되돌림, 추방\n•허락 없이 마음대로 뮤트된 사람 혹은 차단된 사람을 풀거나 해제할 시 그 전으로 되돌림, 추방\n•서버 매니저 이상인 사람이 가입 알림, 커뮤니티 카테고리 안에 있는 채팅 채널에서 수다 떨 시 그 글 삭제, 경고 2\n•허락 없이 마음대로 카테고리, 채팅 채널, 음성 채널, 역할의 위치를 변동하거나 수정 혹은 삭제 시 그 전으로 되돌림, 그 사람의 서버 매니저 이상 역할 삭제", inline=False)
    embed.add_field(name="기타 규칙", value="•복수 투표 시 경고 2 (서버 매니저 이상은 제외)\n•차단된 사람을 블랙리스트방에 기록 안 할 시 경고 1\n•음성 채널인 음악방, 통화방을 들어갔다 나가는 행동을 반복할 시 경고 2\n•허락 없이 마음대로 음악을 스킵 하거나 스톱할 시 경고 2 (혼자 있을 시 허용)\n•모범 행동을 할 시 경고 1 감형\n•경고 6일 시 추방", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 서버매니저(ctx):
    embed = discord.Embed(color = 89999)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="서버 매니저 얻는방법", value="서버 매니저는 아직 안뽑는 중입니다.", inline=False)
    embed.add_field(name="서버 매니저가 하는 일", value="서버 매니저는 말 그대로 서버를 관리하는 사람이며 저희 [문쿠 커뮤니티]를\n새롭고 예쁘게 꾸며나갈 사람 중 하나입니다!", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def GFX(ctx):
    embed = discord.Embed(color = 89999)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="GFX", value="GFX만들어 달라고 말할 땐 그냥 만들어주세요 라고 하지 마시고\n배경색깔, 캐릭터 닉네임, 자세를 확실하게 말해주셔야 합니다.\n(아니면 만들어줄 수가 없어요.)", inline=False)
    embed.add_field(name="문쿠가 GFX 만들어준 사람 목록", value="Alexander_2lk, nextcrownd, superplayer1756, wsa12345aws\nXfjek", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 현재시간(ctx):
    a = datetime.datetime.today().year
    b = datetime.datetime.today().month
    c = datetime.datetime.today().day
    d = datetime.datetime.today().hour
    e = datetime.datetime.today().minute
    f = datetime.datetime.today().second
    embed = discord.Embed(color = 89999)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name='현재 시간', value=str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초 ", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 내정보(ctx, member: discord.Member = None):
    member = ctx.author if not member else Member
    date = datetime.datetime.utcfromtimestamp(((int(member.id) >> 22) + 1420070400000) / 1000)
    embed = discord.Embed(color = 89999)
    embed.set_author(name=f"플레이어 정보 - {member}")
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="이름:", value=member.name, inline=True)
    embed.add_field(name="서버닉네임:", value=member.display_name, inline=True)
    embed.add_field(name="계정 생성일:", value=str(date.year) + "년 " + str(date.month) + "월 " + str(date.day) + "일 " + str(date.hour) + "시 " + str(date.minute) + "분 " + str(date.second) + "초 ", inline=False)
    embed.add_field(name="아이디:", value=member.id, inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def 핑(ctx):
    embed = discord.Embed(color=89999)
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="서버 핑", value=f'핑 측정값 : {round(bot.latency * 1000)}ms', inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 홍보(ctx):
    embed = discord.Embed(title="Project city", description="도시 맵", colour=discord.Color.blue(), url="https://discord.gg/gBFHbYY")
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def 밴(ctx, member: discord.User = None, reason=None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("누구를 밴 하실 건가요?")
        return
    if reason == None:
        reason = "잘가 :>"
    message = f"당신은 {ctx.guild.name} 에 의해 밴 됬어요! 이유 :{reason}"
    await member.send(message)
    await ctx.guild.ban(member)
    await ctx.channel.send(f"{member.mention} 님이 밴 됬어요!")
    print(f"{member} 님이 밴 됬어요!")
@밴.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("당신은 밴을 할 수 없어요!")

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def 킥(ctx, member: discord.User = None, reason=None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("누구를 킥 하실 건가요?")
        return
    if reason == None:
        reason = "잘가 :>"
    message = f"당신은 {ctx.guild.name} 에 의해 킥됬어요! 이유 :{reason}"
    await member.send(message)
    await ctx.guild.kick(member)
    await ctx.channel.send(f"{member.mention} 님이 킥됬어요!")
    print(f"{member} 님이 킥됬어요!")
@킥.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("당신은 킥을 할 수 없어요!")

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def 뮤트(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("누구를 뮤트 하실 건가요?")
        return
    rola = discord.utils.get(ctx.guild.roles, name="사람")
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await member.remove_roles(rola)
    await ctx.send(f"{member.mention} 님이 뮤트 되었어요!")
    print(f"{member} 님이 뮤트 되었어요!")
@뮤트.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f"{member.mention} 당신은 뮤트를 할 수 없어요!")

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def 언뮤트(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("누구의 뮤트를 푸실 건가요?")
        return
    rola = discord.utils.get(ctx.guild.roles, name="사람")
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(rola)
    await member.remove_roles(role)
    await ctx.send(f"{member.mention} 님의 뮤트가 풀렸어요!")
    print(f"{member} 님의 뮤트가 풀렸어요!")
@언뮤트.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("당신은 뮤트를 풀 수 없어요!")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def 청소(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{amount} 개의 채팅을 삭제 했어요!")
    print(f"{amount} 개의 채팅을 삭제 했어요!")
@청소.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("당신은 채팅을 지울 수 없어요!")

@bot.command()
async def 캡챠(ctx):
    Image_captcha = ImageCaptcha()
    msg = ""
    a = ""
    for i in range(6):
        a += str(random.randint(0, 9))

    name = str(ctx.author.id) + ".png"
    Image_captcha.write(a, name)

    await ctx.channel.send(file=discord.File(name))
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        msg = await bot.wait_for("message", timeout=10, check=check)
    except:
        await ctx.channel.send(f"{member.mention} 시간이 초과 됐어요! 탈락!")
        return

    if msg.content == a:
        await ctx.channel.send("정답! 축하!")
    else:
        await ctx.channel.send("오답! 탈락!")

bot.run('NzA0MjYxNDY5Njc1NTg1NjA2.Xqaknw.O2AfiMN_RHAykRynETXnhd-FQzk')
