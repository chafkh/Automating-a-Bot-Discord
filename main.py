import discord #importer 
import random #pour tout ce qui est de la génération aléatoires
import PyPDF2 #pour ouvrir les pdf
global_membre_du_salon = ""
client = discord.Client(intents=discord.Intents.all())

#pour afficher message quand il est pret
@client.event
async def on_ready():
        print("le bot fonctionne il est pret")
#fonction pour utiliser chat_gpt
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
#l argument ici dois etre la questions que ont veut posser a chat gpt
#ajouter global --- nom variable puis definir objet

#block événement message

@client.event
async def on_message(message):
        id_serveur=1079374243122401410
        id_role=1080806266181517393
        ####### les jeux ######
        
        
        ### pour faire les work shop avec des sujet de conversation 
        if message.content.startswith("!wk"):
            guild_id = message.guild.id
            guild = client.get_guild(guild_id)
            channel_groupe_WK = discord.utils.get(guild.channels, name="Groupe Work shop")
            channel_WK1 = discord.utils.get(guild.channels, name="Work shop 1")
            channel_WK2 = discord.utils.get(guild.channels, name="Work shop 2")
            channel_WK3 = discord.utils.get(guild.channels, name="Work shop 3")
            taille_grp= int(message.content.split()[1]) 
            
            liste_elements = ["Allemands","Anglais","Espagnole"]
            liste_str = ""
            for i, element in enumerate(liste_elements):
                liste_str += f"{i+1}. {element}\n"


            await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

            def check(msg):

                return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

            try:

                choix = await client.wait_for('message', check=check, timeout=30)
                element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                await message.channel.send(f"Vous avez choisi l'élément {element_choisi}")

            #### au ca ou il aurais pris trop de temps a choisir le bonne élément
            except asyncio.TimeoutError:
                await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")
            
            if element_choisi=="Anglais" :
                #ont va extraire les noms des users dans le channel qui sert a faire les groupe
                global global_membre_du_salon1 
                global_membre_du_salon1 = channel_groupe_WK.members
                #boucle pour checker si personne est dans le salon pour faire les grp si c le cas stoper la fonction et le dire
                if len(global_membre_du_salon1)==0 :                        
                    await message.channel.send("le salon:Groupe work shop est vide, rentrez dedans afin que les groupe sois fait")
                    return
                #finds members connected to the channel
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                #boucle pour ajouter le_nom des salon dans une liste si jamais ont en ajoute une de plus pour gagner du temps
              #  for i in range(1,4):
               #     nom_variable = 'channel_WK' + str(i) # Construire le nom de la variable
                #    pour_l_appeler= globals()[nom_variable]
                 #   les_nom_des_salon_vocaux.append(pour_l_appeler)
                nombre_wk1= 0 #compteur pour connaitre le bombre de gens dans wk1
                nombre_wk2= 0 #compteur pour connaitre le bombre de gens dans wk2
                nombre_wk3= 0 #compteur pour connaitre le bombre de gens dans wk3

                Flag2=0
                Flag3=0

                #ont va generer les sujet avec chat gpt 
                topics = ['Travel', 'Technology', 'Food', 'Music', 'Sports', 'Fashion', 'Movies', 'Health', 'Politics', 'Education', 'Relationships', 'Work', 'Art', 'Science', 'Finance', 'Religion', 'Culture', 'Environment', 'Cars', 'Literature']
                random.shuffle(topics)
                #boucle qui permet de changer l'ordre des noms qui vont servir a créer les groupe afin de avoir des grp fais au hasard

                for member in global_membre_du_salon1 :
                    les_nom_des_membre.append(member)
                random.shuffle(les_nom_des_membre)

                for member in les_nom_des_membre :
                    if nombre_wk1<taille_grp:
                        nombre_wk1+=1 
                        await member.edit(voice_channel=(channel_WK1))                   

                    elif nombre_wk2<taille_grp:
                        nombre_wk2+=1
                        await member.edit(voice_channel=(channel_WK2))
                        Flag2=1
                    elif nombre_wk3<taille_grp:
                        nombre_wk3+=1             
                        await member.edit(voice_channel=(channel_WK3))
                        Flag3=1
                #buocle pour donner des topics pour les salon 2 et 3 uniquement si ya des gens dedans    
                await message.channel.send("work shop 1 your topic is "+topics[0])
                if Flag2==1  :
                    await message.channel.send("work shop 2 your topic is "+topics[1])
                    if Flag3==1 :
                        await message.channel.send("work shop 3 your topic is "+topics[2])


            if element_choisi=="Allemands" :
                #ont va extraire les noms des users dans le channel qui sert a faire les groupe
                global global_membre_du_salon2 
                global_membre_du_salon2 = channel_groupe_WK.members
                
                #boucle pour checker si personne est dans le salon pour faire les grp si c le cas stoper la fonction et le dire
                if len(global_membre_du_salon2)==0 :                        
                    await message.channel.send("le salon:Groupe work shop est vide, rentrez dedans afin que les groupe sois fait")
                    return
                #finds members connected to the channel
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                #boucle pour ajouter le_nom des salon dans une liste si jamais ont en ajoute une de plus pour gagner du temps
              #  for i in range(1,4):
               #     nom_variable = 'channel_WK' + str(i) # Construire le nom de la variable
                #    pour_l_appeler= globals()[nom_variable]
                 #   les_nom_des_salon_vocaux.append(pour_l_appeler)
                nombre_wk1= 0 #compteur pour connaitre le bombre de gens dans wk1
                nombre_wk2= 0 #compteur pour connaitre le bombre de gens dans wk2
                nombre_wk3= 0 #compteur pour connaitre le bombre de gens dans wk3

                Flag2=0
                Flag3=0

                #ont va generer les sujet avec chat gpt 
                topics = ["Das Wetter", "Die Arbeit", "Familie und Freunde", "Hobbys und Interessen", "Reisen", "Essen und Trinken", "Musik und Filme", "Sport", "Haustiere", "Sprachen und Kultur", "Technologie und Innovation", "Politik und Gesellschaft", "Geschichte und Traditionen", "Bildung und Karriere", "Gesundheit und Fitness", "Mode und Schönheit", "Kunst und Literatur", "Umwelt und Nachhaltigkeit", "Religion und Spiritualität", "Liebe und Beziehungen"]


                random.shuffle(topics)
                #boucle qui permet de changer l'ordre des noms qui vont servir a créer les groupe afin de avoir des grp fais au hasard

                for member in global_membre_du_salon2 :
                    les_nom_des_membre.append(member)
                random.shuffle(les_nom_des_membre)

                for member in les_nom_des_membre :
                    if nombre_wk1<taille_grp:
                        nombre_wk1+=1 
                        await member.edit(voice_channel=(channel_WK1))                   

                    elif nombre_wk2<taille_grp:
                        nombre_wk2+=1
                        await member.edit(voice_channel=(channel_WK2))
                        Flag2=1
                    elif nombre_wk3<taille_grp:
                        nombre_wk3+=1             
                        await member.edit(voice_channel=(channel_WK3))
                        Flag3=1
                #buocle pour donner des topics pour les salon 2 et 3 uniquement si ya des gens dedans    
                await message.channel.send("Arbeitsgruppe 1, dein Thema ist "+topics[0])
                if Flag2==1  :
                    await message.channel.send("Arbeitsgruppe 2, dein Thema ists "+topics[1])
                    if Flag3==1 :
                        await message.channel.send("Arbeitsgruppe 3, dein Thema ist"+topics[2])

            if element_choisi=="Espagnole":
                #ont va extraire les noms des users dans le channel qui sert a faire les groupe
                global global_membre_du_salon3 
                global_membre_du_salon3 = channel_groupe_WK.members
                
                #boucle pour checker si personne est dans le salon pour faire les grp si c le cas stoper la fonction et le dire
                if len(global_membre_du_salon3)==0 :                        
                    await message.channel.send("le salon:Groupe work shop est vide, rentrez dedans afin que les groupe sois fait")
                    return
                #finds members connected to the channel
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                #boucle pour ajouter le_nom des salon dans une liste si jamais ont en ajoute une de plus pour gagner du temps
              #  for i in range(1,4):
               #     nom_variable = 'channel_WK' + str(i) # Construire le nom de la variable
                #    pour_l_appeler= globals()[nom_variable]
                 #   les_nom_des_salon_vocaux.append(pour_l_appeler)
                nombre_wk1= 0 #compteur pour connaitre le bombre de gens dans wk1
                nombre_wk2= 0 #compteur pour connaitre le bombre de gens dans wk2
                nombre_wk3= 0 #compteur pour connaitre le bombre de gens dans wk3

                Flag2=0
                Flag3=0

                #ont va generer les sujet avec chat gpt 
                topics = ["El clima", "El trabajo", "Familia y amigos", "Pasatiempos e intereses", "Viajes", "Comida y bebida", "Música y películas", "Deportes", "Mascotas", "Idiomas y cultura", "Tecnología e innovación", "Política y sociedad", "Historia y tradiciones", "Educación y carrera profesional", "Salud y bienestar", "Moda y belleza", "Arte y literatura", "Medio ambiente y sostenibilidad", "Religión y espirit"]



                random.shuffle(topics)
                #boucle qui permet de changer l'ordre des noms qui vont servir a créer les groupe afin de avoir des grp fais au hasard

                for member in global_membre_du_salon3 :
                    les_nom_des_membre.append(member)
                random.shuffle(les_nom_des_membre)

                for member in les_nom_des_membre :
                    if nombre_wk1<taille_grp:
                        nombre_wk1+=1 
                        await member.edit(voice_channel=(channel_WK1))                   

                    elif nombre_wk2<taille_grp:
                        nombre_wk2+=1
                        await member.edit(voice_channel=(channel_WK2))
                        Flag2=1
                    elif nombre_wk3<taille_grp:
                        nombre_wk3+=1             
                        await member.edit(voice_channel=(channel_WK3))
                        Flag3=1
                #buocle pour donner des topics pour les salon 2 et 3 uniquement si ya des gens dedans    
                await message.channel.send("Grupo de trabajo 1, tu tema es "+topics[0])
                if Flag2==1  :
                    await message.channel.send("Grupo de trabajo 2, tu tema es "+topics[1])
                    if Flag3==1 :
                        await message.channel.send("Grupo de trabajo 3, tu tema es"+topics[2])
        
        
        #pour mélanger les groupe FONCTIONNE PAS arrive pas a récuperre le bom des membre des groupe et les mettre dans la
        #une liste car liste pas attribut edit (truc pour changer salon vocale)
        if message.content.startswith("!shuffle"):            
            taille_grp= int(message.content.split()[1])
            guild_id = message.guild.id
            guild = client.get_guild(guild_id)
            channel_groupe_WK = discord.utils.get(guild.channels, name="Groupe Work shop")
            channel_WK1 = discord.utils.get(guild.channels, name="Work shop 1")
            channel_WK2 = discord.utils.get(guild.channels, name="Work shop 2")
            channel_WK3 = discord.utils.get(guild.channels, name="Work shop 3")
            liste_elements = ["Allemands","Anglais","Espagnole"]
            ### boucle pour verifier d'ou tirée le nom des salon 
            if  'global_membre_du_salon1' in globals(): 
                nom_passe_partout=global_membre_du_salon1
            elif 'global_membre_du_salon2' in globals():  
                nom_passe_partout=global_membre_du_salon2
            elif 'global_membre_du_salon3' in globals(): 
                nom_passe_partout=global_membre_du_salon3  
            
            
            
            
            
            liste_str = ""
            for i, element in enumerate(liste_elements):
                liste_str += f"{i+1}. {element}\n"


            await message.channel.send(f"Choisissez un professeur en envoyant son numéro:\n{liste_str}")

            def check(msg):

                return msg.author == message.author and msg.content.isdigit() and int(msg.content) in range(1, len(liste_elements)+1)

            try:

                choix = await client.wait_for('message', check=check, timeout=30)
                element_choisi = liste_elements[int(choix.content)-1] #ce que la personne a fais comme choix 
                await message.channel.send(f"Vous avez choisi l'élément {element_choisi}")

            #### au ca ou il aurais pris trop de temps a choisir le bonne élément
            except asyncio.TimeoutError:
                await message.channel.send("Temps écoulé, veuillez recommencer la commande !choisir")
            
            #sortir les membre de chaque salon


            #ont mélange pour avoir un ordre déii
            if element_choisi=="Anglais":
                
                random.shuffle(nom_passe_partout)
                #ont réarragne les sujet 
                topics = ['Travel', 'Technology', 'Food', 'Music', 'Sports', 'Fashion', 'Movies', 'Health', 'Politics', 'Education', 'Relationships', 'Work', 'Art', 'Science', 'Finance', 'Religion', 'Culture', 'Environment', 'Cars', 'Literature']
                random.shuffle(topics)
                #ont peut réuttilliser des compteur plutot que la taille des grp 
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                
                nombre_wk1= 0 #compteur pour connaitre le bombre de gens dans wk1
                nombre_wk2= 0 #compteur pour connaitre le bombre de gens dans wk2
                nombre_wk3= 0 #compteur pour connaitre le bombre de gens dans wk3

                Flag2=0
                Flag3=0
                for member in nom_passe_partout :
                    if nombre_wk1<taille_grp:
                        nombre_wk1+=1 
                        await member.edit(voice_channel=(channel_WK1))                   

                    elif nombre_wk2<taille_grp:
                        nombre_wk2+=1
                        await member.edit(voice_channel=(channel_WK2))
                        Flag2=1
                    elif nombre_wk3<taille_grp:
                        nombre_wk3+=1             
                        await member.edit(voice_channel=(channel_WK3))
                        Flag3=1
                #buocle pour donner des topics pour les salon 2 et 3 uniquement si ya des gens dedans    
                await message.channel.send("work shop 1 your topic is "+topics[0])
                if Flag2==1  :
                    await message.channel.send("work shop 2 your topic is "+topics[1])
                    if Flag3==1 :
                        await message.channel.send("work shop 3 your topic is "+topics[2])
            
            if element_choisi=="Allemands" :
                random.shuffle(nom_passe_partout)
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                nombre_wk1= 0 #compteur pour connaitre le bombre de gens dans wk1
                nombre_wk2= 0 #compteur pour connaitre le bombre de gens dans wk2
                nombre_wk3= 0 #compteur pour connaitre le bombre de gens dans wk3

                Flag2=0
                Flag3=0

                #ont va generer les sujet avec chat gpt 
                topics = ["Das Wetter", "Die Arbeit", "Familie und Freunde", "Hobbys und Interessen", "Reisen", "Essen und Trinken", "Musik und Filme", "Sport", "Haustiere", "Sprachen und Kultur", "Technologie und Innovation", "Politik und Gesellschaft", "Geschichte und Traditionen", "Bildung und Karriere", "Gesundheit und Fitness", "Mode und Schönheit", "Kunst und Literatur", "Umwelt und Nachhaltigkeit", "Religion und Spiritualität", "Liebe und Beziehungen"]


                random.shuffle(topics)
                #boucle qui permet de changer l'ordre des noms qui vont servir a créer les groupe afin de avoir des grp fais au hasard

                for member in nom_passe_partout :
                    les_nom_des_membre.append(member)
                random.shuffle(les_nom_des_membre)

                for member in les_nom_des_membre :
                    if nombre_wk1<taille_grp:
                        nombre_wk1+=1 
                        await member.edit(voice_channel=(channel_WK1))                   

                    elif nombre_wk2<taille_grp:
                        nombre_wk2+=1
                        await member.edit(voice_channel=(channel_WK2))
                        Flag2=1
                    elif nombre_wk3<taille_grp:
                        nombre_wk3+=1             
                        await member.edit(voice_channel=(channel_WK3))
                        Flag3=1
                #buocle pour donner des topics pour les salon 2 et 3 uniquement si ya des gens dedans    
                await message.channel.send("Arbeitsgruppe 1, dein Thema ist "+topics[0])
                if Flag2==1  :
                    await message.channel.send("Arbeitsgruppe 2, dein Thema ists "+topics[1])
                    if Flag3==1 :
                        await message.channel.send("Arbeitsgruppe 3, dein Thema ist"+topics[2])
            if element_choisi=="Espagnole" :
                random.shuffle(nom_passe_partout)
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                les_nom_des_membre = [] #list avec le nom des personne dans le salon qui sert a la compositions des grp
                les_nom_des_salon_vocaux= []
                
                nombre_wk1= 0 #compteur pour connaitre le bombre de gens dans wk1
                nombre_wk2= 0 #compteur pour connaitre le bombre de gens dans wk2
                nombre_wk3= 0 #compteur pour connaitre le bombre de gens dans wk3

                Flag2=0
                Flag3=0

                #ont va generer les sujet avec chat gpt 
                topics = ["El clima", "El trabajo", "Familia y amigos", "Pasatiempos e intereses", "Viajes", "Comida y bebida", "Música y películas", "Deportes", "Mascotas", "Idiomas y cultura", "Tecnología e innovación", "Política y sociedad", "Historia y tradiciones", "Educación y carrera profesional", "Salud y bienestar", "Moda y belleza", "Arte y literatura", "Medio ambiente y sostenibilidad", "Religión y espirit"]



                random.shuffle(topics)
                #boucle qui permet de changer l'ordre des noms qui vont servir a créer les groupe afin de avoir des grp fais au hasard

                for member in nom_passe_partout :
                    les_nom_des_membre.append(member)
                random.shuffle(les_nom_des_membre)

                for member in les_nom_des_membre :
                    if nombre_wk1<taille_grp:
                        nombre_wk1+=1 
                        await member.edit(voice_channel=(channel_WK1))                   

                    elif nombre_wk2<taille_grp:
                        nombre_wk2+=1
                        await member.edit(voice_channel=(channel_WK2))
                        Flag2=1
                    elif nombre_wk3<taille_grp:
                        nombre_wk3+=1             
                        await member.edit(voice_channel=(channel_WK3))
                        Flag3=1
                #buocle pour donner des topics pour les salon 2 et 3 uniquement si ya des gens dedans    
                await message.channel.send("Grupo de trabajo 1, tu tema es "+topics[0])
                if Flag2==1  :
                    await message.channel.send("Grupo de trabajo 2, tu tema es "+topics[1])
                    if Flag3==1 :
                        await message.channel.send("Grupo de trabajo 3, tu tema es"+topics[2])

                        
                        
            
        
        if message.content.startswith("!Salon"):
            guild_id = message.guild.id
            guild = client.get_guild(guild_id)
            group_workshop_name = 'Groupe Work shop'
            workshop1_name1 = 'Work shop 1'
            workshop1_name2 = 'Work shop 2'
            workshop1_name3 = 'Work shop 3'
            await guild.create_voice_channel(group_workshop_name)
            await guild.create_voice_channel(workshop1_name1)
            await guild.create_voice_channel(workshop1_name2)    
            await guild.create_voice_channel(workshop1_name3)     
                
                
                
                
                
                
                
                
                
                
                
                
                
client.run("MTA4MDQ5OTc0NTIyNDY2MzExMA.G8l7N0.4rJ08XTPt6AXoIefeeVFTx62SAIwELQZDbVqYo")
#block événement arriver de qlq dans le serveur  """ 









