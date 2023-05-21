import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="--", intents=intents)


@client.command()
@commands.is_owner()
async def verde(ctx):
	esmeralda = await ctx.guild.create_role(name="『Esmeralda』", colour=discord.Colour.from_rgb(2, 137, 16))
	trebol = await ctx.guild.create_role(name="『Trebol』", colour=discord.Colour.from_rgb(3, 172, 19))
	verde = await ctx.guild.create_role(name="『Verde』", colour=discord.Colour.from_rgb(59, 177, 67))
	pera = await ctx.guild.create_role(name="『Pera』", colour=discord.Colour.from_rgb(116, 182, 46))
	lima = await ctx.guild.create_role(name="『Lima』", colour=discord.Colour.from_rgb(0, 255, 1))
	menta = await ctx.guild.create_role(name="『Lima Verde』", colour=discord.Colour.from_rgb(60, 236, 151))


	embed = discord.Embed(title="**GAMA VERDE**", description=f"1- {esmeralda.mention}\n2- {trebol.mention}\n3- {verde.mention}\n4- {pera.mention}\n5- {lima.mention}\n6- {menta.mention}")
	embed.set_image(url="https://media.tenor.com/ssnZm70xhhMAAAAC/anime-nature.gif")
	embed.colour = discord.Colour.from_rgb(0, 100, 1)

	await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def azul(ctx):
	azul = await ctx.guild.create_role(name="『Azul』", colour=discord.Colour.from_rgb(6, 16, 148))
	oceano = await ctx.guild.create_role(name="『Oceano』", colour=discord.Colour.from_rgb(1, 96, 100))
	cobalto = await ctx.guild.create_role(name="『Cobalto』", colour=discord.Colour.from_rgb(19, 56, 189))
	cielo = await ctx.guild.create_role(name="『Cielo』", colour=discord.Colour.from_rgb(98, 197, 218))
	celeste = await ctx.guild.create_role(name="『Celeste』", colour=discord.Colour.from_rgb(177, 255, 255))
	artico = await ctx.guild.create_role(name="『Artico』", colour=discord.Colour.from_rgb(130, 237, 253))


	embed = discord.Embed(title="**GAMA AZUL**", description=f"1- {azul.mention}\n2- {oceano.mention}\n3- {cobalto.mention}\n4- {cielo.mention}\n5- {artico.mention}\n6- {celeste.mention}")
	embed.set_image(url="https://i.pinimg.com/originals/59/b2/34/59b2349684d902730f710b65f05ecb80.gif")
	embed.colour = discord.Colour.from_rgb(1, 1, 255)

	await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def amarillo(ctx):
	amarillo = await ctx.guild.create_role(name="『Amarillo』", colour=discord.Colour.from_rgb(253, 230, 75))
	limon = await ctx.guild.create_role(name="『Limon』", colour=discord.Colour.from_rgb(239, 253, 95))
	dorado = await ctx.guild.create_role(name="『Dorado』", colour=discord.Colour.from_rgb(249, 166, 2))
	medallion = await ctx.guild.create_role(name="『Medallion』", colour=discord.Colour.from_rgb(227, 177, 4))
	rubio = await ctx.guild.create_role(name="『Rubio』", colour=discord.Colour.from_rgb(254, 235, 117))
	bumblebee = await ctx.guild.create_role(name="『Bumblebee』", colour=discord.Colour.from_rgb(252, 226, 5))


	embed = discord.Embed(title="**GAMA AMARILLA**", description=f"1- {amarillo.mention}\n2- {limon.mention}\n3- {dorado.mention}\n4- {medallion.mention}\n5- {bumblebee.mention}\n6- {rubio.mention}")
	embed.set_image(url="https://gifsec.com/wp-content/uploads/2022/11/yellow-anime-gif-1.gif")
	embed.colour = discord.Colour.from_rgb(252, 226, 5)

	await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def rojo(ctx):
	vino = await ctx.guild.create_role(name="『Vino』", colour=discord.Colour.from_rgb(76, 8, 5))
	sangre = await ctx.guild.create_role(name="『Sangre』", colour=discord.Colour.from_rgb(113, 12,4))
	ruby = await ctx.guild.create_role(name="『Ruby』", colour=discord.Colour.from_rgb(144, 6, 3))
	rojo = await ctx.guild.create_role(name="『Rojo』", colour=discord.Colour.from_rgb(208, 49, 45))
	dulce = await ctx.guild.create_role(name="『Dulce』", colour=discord.Colour.from_rgb(210, 21, 2))
	blush = await ctx.guild.create_role(name="『Blush』", colour=discord.Colour.from_rgb(188, 84, 73))


	embed = discord.Embed(title="**GAMA ROJA**", description=f"1- {vino.mention}\n2- {sangre.mention}\n3- {ruby.mention}\n4- {rojo.mention}\n5- {blush.mention}\n6- {dulce.mention}")
	embed.set_image(url="https://media.tenor.com/cDQN9Jc-mPcAAAAC/sky-red.gif")
	embed.colour = discord.Colour.from_rgb(208, 49, 45)

	await ctx.send(embed=embed)


@client.command()
@commands.is_owner()
async def rosa(ctx):
	hotPink = await ctx.guild.create_role(name="『Hot Pink』", colour=discord.Colour.from_rgb(255, 22, 149))
	bubblegum = await ctx.guild.create_role(name="『Bubblegum』", colour=discord.Colour.from_rgb(253, 92, 168))
	rosa = await ctx.guild.create_role(name="『Rosa』", colour=discord.Colour.from_rgb(246, 154, 205))
	sandia = await ctx.guild.create_role(name="『Sandia』", colour=discord.Colour.from_rgb(254, 127, 156))
	salmon = await ctx.guild.create_role(name="『Salmon』", colour=discord.Colour.from_rgb(253, 171, 159))
	flamingo = await ctx.guild.create_role(name="『Flamingo』", colour=discord.Colour.from_rgb(253, 164, 184))


	embed = discord.Embed(title="**GAMA ROSA**", description=f"1- {hotPink.mention}\n2- {bubblegum.mention}\n3- {rosa.mention}\n4- {sandia.mention}\n5- {flamingo.mention}\n6- {salmon.mention}")
	embed.set_image(url="https://j.gifs.com/m8zPXw.gif")
	embed.colour = discord.Colour.from_rgb(246, 154, 205)

	await ctx.send(embed=embed)


@client.command()
@commands.is_owner()
async def morado(ctx):
	magenta = await ctx.guild.create_role(name="『Magenta』", colour=discord.Colour.from_rgb(161, 5, 89))
	violeta = await ctx.guild.create_role(name="『violeta』", colour=discord.Colour.from_rgb(113, 1, 147))
	purpura = await ctx.guild.create_role(name="『Purpura』", colour=discord.Colour.from_rgb(163, 44, 196))
	Amatista = await ctx.guild.create_role(name="『Amatista』", colour=discord.Colour.from_rgb(164, 94, 229))
	Lila = await ctx.guild.create_role(name="『Lila』", colour=discord.Colour.from_rgb(182, 96, 205))
	Hada = await ctx.guild.create_role(name="『Hada』", colour=discord.Colour.from_rgb(189, 147, 211))


	embed = discord.Embed(title="**GAMA MORADA*", description=f"1- {magenta.mention}\n2- {violeta.mention}\n3- {purpura.mention}\n4- {Amatista.mention}\n5- {Hada.mention}\n6- {Lila.mention}")
	embed.set_image(url="https://www.gifcen.com/wp-content/uploads/2022/07/discord-banner-gif-5.gif")
	embed.colour = discord.Colour.from_rgb(163, 44, 196)

	await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def cafe(ctx):
	Chocolate = await ctx.guild.create_role(name="『Chocolate』", colour=discord.Colour.from_rgb(44, 21, 3))
	Caramelo = await ctx.guild.create_role(name="『Caramelo』", colour=discord.Colour.from_rgb(101, 53, 15))
	Cafe = await ctx.guild.create_role(name="『Cafe』", colour=discord.Colour.from_rgb(75, 55, 28))
	Tawny = await ctx.guild.create_role(name="『Tawny』", colour=discord.Colour.from_rgb(126, 72, 28))
	Mani = await ctx.guild.create_role(name="『Mani』", colour=discord.Colour.from_rgb(121, 92, 52))
	Tortilla = await ctx.guild.create_role(name="『Tortilla』", colour=discord.Colour.from_rgb(154, 123, 79))


	embed = discord.Embed(title="**GAMA CAFE**", description=f"1- {Chocolate.mention}\n2- {Caramelo.mention}\n3- {Cafe.mention}\n4- {Tawny.mention}\n5- {Tortilla.mention}\n6- {Mani.mention}")
	embed.set_image(url="https://media.discordapp.net/attachments/1029613068788957206/1109716579937161287/IMG_20230520_233722_415.jpg")
	embed.colour = discord.Colour.from_rgb(75, 55, 28)

	await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def naranja(ctx):
	Tigre = await ctx.guild.create_role(name="『Tigre』", colour=discord.Colour.from_rgb(252, 107, 2))
	Naranja = await ctx.guild.create_role(name="『Naranja』", colour=discord.Colour.from_rgb(237, 112, 20))
	Mandarina = await ctx.guild.create_role(name="『Mandarina』", colour=discord.Colour.from_rgb(249, 130, 40))
	Mermelada = await ctx.guild.create_role(name="『Mermelada』", colour=discord.Colour.from_rgb(209, 96, 2))
	Melon = await ctx.guild.create_role(name="『Melon』", colour=discord.Colour.from_rgb(252, 161, 114))


	embed = discord.Embed(title="**GAMA NARANJA**", description=f"1- {Tigre.mention}\n2- {Naranja.mention}\n3- {Mandarina.mention}\n4- {Mermelada.mention}\n5- {Melon.mention}")
	embed.set_image(url="https://i.pinimg.com/originals/a6/10/8b/a6108b31b391378d30856edba57172a4.gif")
	embed.colour = discord.Colour.from_rgb(237, 112, 20)

	await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def negro(ctx):
	Negro = await ctx.guild.create_role(name="『Negro』", colour=discord.Colour.from_rgb(3, 1, 6))
	Gris = await ctx.guild.create_role(name="『Gris』", colour=discord.Colour.from_rgb(33, 33, 33))
	Plateado = await ctx.guild.create_role(name="『Plateado』", colour=discord.Colour.from_rgb(173, 173, 199))
	Nube = await ctx.guild.create_role(name="『Nube』", colour=discord.Colour.from_rgb(198, 198, 208))
	Blanco = await ctx.guild.create_role(name="『Blanco』", colour=discord.Colour.from_rgb(255, 255, 255))
	Nieve = await ctx.guild.create_role(name="『Nieve』", colour=discord.Colour.from_rgb(245, 254, 253))


	embed = discord.Embed(title="**GAMA BLANCO Y NEGRO**", description=f"1- {Negro.mention}\n2- {Gris.mention}\n3- {Plateado.mention}\n4- {Nube.mention}\n5- {Nieve.mention}\n6- {Blanco.mention}")
	embed.set_image(url="https://media4.giphy.com/media/WZrOaNjFPKT5e/giphy.gif")
	embed.colour = discord.Colour.from_rgb(245, 254, 253)

	await ctx.send(embed=embed)


client.run(TOKEN)