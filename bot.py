import discord

token = "Njk2NTUyMDE1MjU3NjY1NTQ3.XoqfQw.zrnEpwJQ56ScZ9Vi1NdvfKgzKSg"
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()

client.run(token)
