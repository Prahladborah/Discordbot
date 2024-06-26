import discord

async def send_help_trigger(message):
    embed = discord.Embed(
        title=f'How can I help you, {message.author.name}?',
        description='I can give you information regarding:',
        color=discord.Color.blue()
    )
    embed.add_field(name='1. Builds', value='Learn about different builds.')
    embed.add_field(name='2. Blacksmithing', value='Information on weapon forging, armor crafting, etc.')
    embed.add_field(name='3. Synthesis', value='Material and synthesis, enchantments.')
    embed.add_field(name='4. Equipment', value='Information on various types of equipment.')
    
    help_message = await message.channel.send(embed=embed)

    def check(m):
        return m.author == message.author and m.channel == message.channel

    try:
        response = await message.client.wait_for('message', check=check, timeout=30.0)  # Wait for user response

        if response.content.lower() == '1':  # User chose Builds
            build_embed = discord.Embed(
                title='Builds',
                description='Choose a build category:',
                color=discord.Color.green()
            )
            build_embed.add_field(name='1. 0HS Tank', value='Information on 0HS Tank build.')
            build_embed.add_field(name='2. 0HS DPS', value='Information on 0HS DPS build.')
            build_embed.add_field(name='3. 2HS', value='Information on 2HS build.')
            build_embed.add_field(name='4. Bow', value='Information on Bow build.')
            build_embed.add_field(name='5. BWG', value='Information on BWG build.')
            build_embed.add_field(name='6. KTN', value='Information on KTN build.')
            build_embed.add_field(name='7. HB', value='Information on HB build.')
            build_embed.add_field(name='8. KNX Tank', value='Information on KNX Tank build.')
            build_embed.add_field(name='9. KNX DPS', value='Information on KNX DPS build.')
            build_embed.add_field(name='10. Barehand', value='Information on Barehand build.')
            build_embed.add_field(name='11. Support', value='Information on Support build.')
            await message.channel.send(embed=build_embed)

            try:
                build_response = await message.client.wait_for('message', check=check, timeout=30.0)  # Wait for user build choice

                if build_response.content.lower() == '1':  # User chose 0HS Tank
                    await message.channel.send("Here's information on 0HS Tank build.")
                elif build_response.content.lower() == '2':  # User chose 0HS DPS
                    await message.channel.send("Here's information on 0HS DPS build.")
                elif build_response.content.lower() == '3':  # User chose 2HS
                    await message.channel.send("Here's information on 2HS build.")
                elif build_response.content.lower() == '4':  # User chose Bow
                    await message.channel.send("Here's information on Bow build.")
                elif build_response.content.lower() == '5':  # User chose BWG
                    await message.channel.send("Here's information on BWG build.")
                elif build_response.content.lower() == '6':  # User chose KTN
                    await message.channel.send("Here's information on KTN build.")
                elif build_response.content.lower() == '7':  # User chose HB
                    await message.channel.send("Here's information on HB build.")
                elif build_response.content.lower() == '8':  # User chose KNX Tank
                    await message.channel.send("Here's information on KNX Tank build.")
                elif build_response.content.lower() == '9':  # User chose KNX DPS
                    await message.channel.send("Here's information on KNX DPS build.")
                elif build_response.content.lower() == '10':  # User chose Barehand
                    await message.channel.send("Here's information on Barehand build.")
                elif build_response.content.lower() == '11':  # User chose Support
                    await message.channel.send("Here's information on Support build.")
                else:
                    await message.channel.send("I'm sorry, I didn't understand your choice.")

            except asyncio.TimeoutError:
                await message.channel.send("You took too long to choose a build.")

        elif response.content.lower() == '2':  # User chose Blacksmithing
            await message.channel.send("Here's information on weapon forging, armor crafting, etc.")
        elif response.content.lower() == '3':  # User chose Synthesis
            await message.channel.send("Details on material and synthesis, enchantments.")
        elif response.content.lower() == '4':  # User chose Equipment
            await message.channel.send("Information on various types of equipment.")
        else:
            await message.channel.send("I'm sorry, I didn't understand your choice.")

    except asyncio.TimeoutError:
        await message.channel.send("You took too long to respond.")

    return 'main_menu'
