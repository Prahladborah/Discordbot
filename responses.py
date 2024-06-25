import discord
import random

potato_responses = [
    "Don't call me potato, you potato baka!",
    "Who are you calling a potato? Take that back, potato-head!",
    "Potato guide? I'm not a potato, I'm a fully grown spud, thank you very much!",
    "Excuse me? I'm not a potato, I'm a bot with a superior intellect, thank you.",
    "Did you just call me a potato? That's a low blow, my friend!",
    "You're the real spud here!",
    "Potato? I'm a technologically advanced tuber!",
    "Do I look like I belong in a stew?",
    "Hey, no need to hashbrown me!",
    "Who you calling potato, tater tot?",
    "Don't be a small fry",
    "That's Mr. Potato Head to you!",
]

baka_responses = [
    "Baka? Oh no, you've exposed my secret identity as a clumsy AI!!",
    "Well, I guess I'm the baka that needs to learn from the master. Your wisdom astounds me",
    "Baka? That's Mr. Baka to you! At least I'm a professional at it.",
    "Excuse me? I'm not a bakaaaa, I'm a the bot of bot with a superior intellect, thank you potatoooo",
    "I may be a baka, but at least I’m the cutest baka around",
    "You're the real baaaaakaa here uwu!",
    "Don't be a small fry",
    "That's Mr. Potato Head to you!",
    "Being called a baka by you is like a compliment, really. Keep 'em coming ewe",
]


async def send_potato_response(message, content):
    if 'potato guide' in content or 'potato bot' in content:
        response = random.choice(potato_responses)
        await message.channel.send(response)

async def send_baka_response(message, content):
    if 'baka bot' in content:
        response = random.choice(baka_responses)
        await message.channel.send(response)
      
