import twitchio
from twitchio.ext import pubsub
from ahk import AHK
ahk = AHK(executable_path='C:/Program Files/AutoHotkey/AutoHotkey.exe')
my_token = "r5bf7prgtpuhbqkgd93iuep014x1ej"
users_oauth_token = "wjoa3fq1cy2skhxtr0y0853jtnx95r"
users_channel_id = 167989273
client = twitchio.Client(token=my_token, initial_channels=["shianchu",])
client.pubsub = pubsub.PubSubPool(client)

@client.event()
async def event_message(message):
    if message.echo:
        return
    print(message.content)
    if message.content == "A":
        ahk.key_press('a')

@client.event()
async def event_pubsub_bits(event: pubsub.PubSubBitsMessage):
    pass # do stuff on bit redemptions

@client.event()
async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
    print("CHAN POINTS")
    print(event.user)
    print(event.reward.title)

@client.event()
async def event_ready():
    print("WE ARE READY")

async def main():
    topics = [
        pubsub.channel_points(users_oauth_token)[users_channel_id],
        pubsub.bits(users_oauth_token)[users_channel_id]
    ]
    await client.pubsub.subscribe_topics(topics)
    await client.connect()
    print("connected")

client.loop.create_task(main())
client.loop.run_forever()
