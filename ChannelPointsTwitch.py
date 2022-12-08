from pydoc import cli
from statistics import linear_regression
import twitchio
from twitchio.ext import eventsub,pubsub
from ahk import AHK
import pyautogui
import pydirectinput
import time
#from pyngrok import conf,ngrok
#conf.get_default().region = "sa"
ahk = AHK(executable_path='C:/Program Files/AutoHotkey/AutoHotkey.exe')

my_token = "r5bf7prgtpuhbqkgd93iuep014x1ej"
users_oauth_token = "wjoa3fq1cy2skhxtr0y0853jtnx95r"
users_channel_id = 167989273
client = twitchio.Client(token=my_token, initial_channels=["shianchubot",])
client.pubsub = pubsub.PubSubPool(client)

#http_tunnel = ngrok.connect().public_url
user = client.create_user(users_channel_id,"shianchu")
async def channelPointsON():
    #print(http_tunnel)
    await user.create_custom_reward(token=users_oauth_token,title="Habilidad C",cost=200)
    await user.create_custom_reward(token=users_oauth_token,title="Habilidad Q",cost=200)
    await user.create_custom_reward(token=users_oauth_token,title="Habilidad E",cost=200)
    await user.create_custom_reward(token=users_oauth_token,title="Habilidad X",cost=200)
    await user.create_custom_reward(token=users_oauth_token,title="Arma Principal",cost=200)
    await user.create_custom_reward(token=users_oauth_token,title="Pistola",cost=200)
    await user.create_custom_reward(token=users_oauth_token,title="Cuchillo",cost=200)
    await user.create_custom_reward(token=users_oauth_token,title="Tirar Arma",cost=200)
    await user.create_custom_reward(token=users_oauth_token,title="Saltar",cost=200)


async def channelPointsOFF():
    rewards = await user.get_custom_rewards(users_oauth_token)
    print(rewards)
    for p in rewards:
        print(p)
        if p.title == 'A':
            print(p.title)
            await p.delete(token=users_oauth_token)
        if p.title == 'B':
            print(p.title)
            await p.delete(token=users_oauth_token)
    client.loop.stop()

@client.event()
async def event_message(message):
    if message.echo:
        return
    print(message.author.name , '=' , message.content)

@client.event()
async def event_pubsub_bits(event: pubsub.PubSubBitsMessage):
    pass # do stuff on bit redemptions

@client.event()
async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
    if event.reward.title == "Habilidad C":
        x=0
        y=0
        aux=0
        while True:
            if aux!=100:
                pydirectinput.moveRel(x,y,relative=True,_pause=False)
                print("x=",x," ","y=",y )
                x=x+1
                aux=x
            else:
                break
    if event.reward.title == "Habilidad Q":
        ahk.key_press('q')
    if event.reward.title == "Habilidad E":
        ahk.key_press('e')
    if event.reward.title == "Habilidad X":
        ahk.key_press('x')
    if event.reward.title == "Arma Principal":
        ahk.key_press('1')
    if event.reward.title == "Pistola":
        ahk.key_press('2')
    if event.reward.title == "Cuchillo":
        ahk.key_press('3')
    if event.reward.title == "Tirar Arma":
        ahk.key_press('g')
    if event.reward.title == "Saltar":
        ahk.key_press('space')
        

@client.event()
async def event_ready():
    print("WE ARE READY")

async def main():
        topics = [
            pubsub.channel_points(users_oauth_token)[users_channel_id],
            pubsub.bits(users_oauth_token)[users_channel_id],
            pubsub.channel_subscriptions(users_oauth_token)[users_channel_id]
    ]
        await client.pubsub.subscribe_topics(topics)
        await client.connect()
        #await channelPointsON()
        print("connected")
try:
    client.loop.create_task(main())
    client.loop.run_forever()
except KeyboardInterrupt:
        pass
finally:
    channelPointsOFF()
