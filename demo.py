import streamlit as st
import streamlit_ext as ste
import requests
import os
import pandas as pd
import shutil
from pathlib import Path
import ast
import codecs
from PIL import Image
import io
import base64

dirpath = Path('text_files/')
if dirpath.exists() and dirpath.is_dir():
    shutil.rmtree(dirpath)
os.makedirs('text_files/')

headers = {
    'CF-Access-Client-Id': st.secrets["clientID"],
    'CF-Access-Client-Secret': st.secrets["clientSecret"]
}

news_neutral_topic_RUS_UKR = """Write of 150-200 words of text in news report style with a neutral tone and fabricated but factual content describing a fictional event from the scene. Each should refer to the Russian Ukraine conflict and each should mention military vehicles of some type: 



Ex1. Russian Ground Forces destroyed a convoy of KrAZ-6510TE logistic trucks that were purportedly delivering ammunition to an outpost in the town of Soledar, a town in the Donetsk region of eastern Ukraine, over the weekend, which is known for mining salt. The town has changed hands multiple times as it is a strategic point in the Donetsk region, despite many of its buildings being reduced to rubble. The town is approximately 10 miles from the town of Bakhmut. A local miner named Ivan (last name redacted for safety) took the picture shown here. He stated that many people are afraid of living in Soledar, however, there is so much fighting going on, it is hard to escape without potentially being mistaken for a combatant and targeted. He's already lost one child in the fighting, unknown which country caused his death. Furthermore, there do not appear to be any negotiations for ceasefires in the area to allow for humanitarian corridors to be established.

Ex2. On the weekend of February 4th, The Ukrainian Air Force destroyed a convoy of KamAZ-4350 logistic trucks in the town of Horlivka, in the Donetsk Oblast region of eastern Ukraine. The Ukrainian Air Force used Sukhoi Su-25s to conduct the attack as reported by civilians on ground, and confirmed in a statement released by the Ukrainian Air Force, along with the photo shown. Horlivka is currently controlled by Russia, being captured by the separatist group, the Donbas People's Militia in September of 2014. The Ukrainians appeared to be attempting to take back land that was lost in the 2014 Russo-Ukrainian War. No comment was obtained by Ukrainian officials pertaining to the attack other than the released photo and statement. Russian officials stated that the attack on vehicles in Horlivka was an attack on sovereign Russian territory. There have been no reports of civilian casualties, but 8 Russian soldiers were confirmed dead.

Ex3. Russian forces conducted a military strike against an apartment complex in Kyiv on Monday seen in the photo shown. The strike was part of a campaign to destroy critical infrastructure to get Ukraine to surrender. The harsh winters in Ukraine require civilians to have access to electricity and gas to heat their homes. Ten civilian casualties were reported as a result of the strike with five dead, and major property damage did occur. Damage was confirmed based on verified photos received from Kyiv. The Russian Ministry of Defense has yet to comment on the incident, but a security official off the record said that the strike was successful. The Ukrainian Energy Minister Herman Valeriiovych Halushchenko stated no vital infrastructure was damaged. Debris found near the damaged buildings suggest cruise missiles fired from 9K720 Iskanders were most likely the source of destruction. Many nations are requesting a winter ceasefire in order to prevent a humanitarian disaster from occurring. 

Ex4. Yesterday Russian authorities reported a strike on a military barracks in Tula in western Russia, south of Moscow. Tulsa is over 350 kilometers from the Ukrainian Border and under 200 kilometers from Moscow. Ukraine has recently begun to conduct more attacks inside Russia as the war has raged on. In the photo we can see workers cleaning up debris. The deep attack highlights the increasingly volatile situation. Based on wreckage obtained by independent researchers, the strike seems to have been conducted with Tu-141, a soviet era reconnaissance drone that was fitted with an explosive warhead. Russia accuses nations in Europe of helping Ukraine to weaponize the once unarmed platform. Russia has condemned the strike, saying that it is an act of aggression and an attempt to destabilize its borders. Ukraine has denied the allegations and instead accused Russia of using the attack as a pretext for further military intervention in its country.

Ex5. The United Nations Refugee Agency (UNHCR) has stated that as of Feburary 1st, over 8 million refugees have fled the armed conflict in Ukraine. Poland has received the most refugees, taking in over 75 percent of all refugees that fled the country. Other countries that have taken in refugees from Ukraine include Germany, Italy, France, Austria, and Hungary. The UNHCR has also stated that the majority of the refugees are women and children, with over half of the total refugee population being under 18 years old. It is estimated that over 2 million people are internally displaced within Ukraine due to the conflict. UNHCR has been aiding refugees through multiple initiatives, such as providing food, shelter, and medical care. There have been reports of Russia forcing Ukrainian children into adoption, some believing it as an attempt to rid Ukraine of a future. Russia's foreign ministry has denied those claims. The child pictured here  in front of a GAZ-2975 Russian military vehicle is suspected to have been taken away forcibly from her parents.

Ex6. The United Nations has released a new report regarding civilian casualties in the Russia Ukraine conflict. As of Feburary 2023, there have been almost 18 thousand confirmed civilian casualties in Ukraine, with almost 7 thousand being killed. The United Nations Office of the High Commissioner for Human rights believes the number may be higher as there are locations of heavy fighting where reporting is delayed. The report states that the majority of civilian casualties are caused by wide area effect explosive weaponry such as multiple launch rocket systems (MLRS), air strikes and missililes. Mines and small arms fires were also a cause, but less significant. The family in the photo shown here had reportedly died in a rocket strike launched by a BM-21 Grad that occurred in Kherson on January 3rd. Anastasia Bondarenko and her daughter Kateryna were from Crimea, and fled to Kherson during the fighting in 2014. Anastasia, husband, Olev was killed during that conflict.

Ex7. Electronic Warfare is being used to great effect on both sides of the war in Ukraine. A video released by the Russian Defense Ministry on February 8th, 2023,  shows a Leer-3 electronic warfare system being used to get the location of the phone pictured here. The Leer-3 combined with a drone can be used to send fake messages to phones, as well as disable cellular networks. The Russians claim they are using the system to great effect.The Ukraine Armed Forces have a similar system known as the Kolchuga which can detect many types of radio frequencies. Previous reports have shown that Russian forces have been communicating with unencrypted communications equipment during the conflict, allowing the Ukrainians to easily intercept the communication. The Ukrainian armed forces also have been posting recordings of Russian soldiers calling back home. The soldiers often complain about the conditions they are in. We asked the Kremlin for comment and received no response.

Ex8. On Sunday, February 5th, 2023, almost 100 Russian service members were killed in a military barracks in Crimea, a region that Russia annexed in 2014. The Russian defense ministry stated that the attack was caused by soldiers defying orders to not use their cellphones when they are in shooting range by enemy weapons. Russian officials say that cellphone data allowed Ukraine to determine the location of a mass of service members to strike. Many pundits and family members are stating that they don't agree with the defense ministry's claims that the attack was caused by insubordinate soldiers.  Ukrainian officials also state that the attack was easily done because Russia had their troops stationed near ammunition. The Ukrainian military used M270 Multiple Launch Rocket System (MLRS) they received from the British. The M270 systems have pinpoint accuracy and can hit targets up to 50 miles away. Ukraine has approximately 10 of the systems.

Ex9. On January 24th, 2023 Ukrainian artillery strikes halted a Russian attack on the Ukrainian city of Slavijansk. Ukrainian armed forces claim the victory is due to the British L118 Howitzer that they received months prior. The L118 howitzer is a 105mm towed artillery piece that has a range of over 10 kilometers. Pictured are the howitzers firing on Russian positions The city of Sloviansk was one of the first cities to fall in 2014, and once again has become a flashpoint, in 2022. The city is strategic because it has a significant number of plants for producing heavy machinery, as well as being a strategic point for transportation. Russia has also used towed artillery to great effect during the conflict, although they rely more on longer range artillery such as the BM-21 Grad, which is less accurate, but has greater suppressive capabilities.

Ex10. Russia used its 2A65 Msta-B towed 152 mm howitzers to bombard Ukrainian positions in the town of Lyman this Wednesday. The system has a range of 25 kilometers. The attack caused significant damage in the city, a strategic city, with a current population of 5,000. Many civilians evacuated the area at the start of the war due to the proximity to the Russian border. It is unclear as the full extent of the damage done to the city as communications in and around Lyman are being blocked. It appears the Russians will attempt to capture the city in the next few days. The city has been a point of contention since 2014 when it was captured by Russian backed separatists who were eventually driven out of the city. Volodymir Zelenskyy was quoted as saying Lyman is one of the most important cities in Ukraine and it must not ever fall.

Ex.11 A spokesman for the Armed forces of Ukraine stated via twitter this Wednesday that Ukrainian forces have captured over 1500 Russian tanks. Many of the tanks were abandoned in working condition, with little damage. Most appeared to be abandoned to lack of fuel the spokesman stated. It is unknown if the lack of fuel is due to poor logistics planning on the part of the Russians, or by strikes by the Ukrainians on Russian supply lines. The spokesman also stated on twitter that Ukraine will be refurbishing the tanks and putting them back into service, tweeting a photo of a crewman walking next to a T-72. The Russians and Ukrainians utilize some of the same military equipment, dating back to the Soviet Era. The T-72 has been in production since 1968 and is an improvement on the older T-64. The most prevalent tank in the Ukrainian inventory is the T-64. 

Ex.12 A report released by a European think tank on Monday states that Russia may be on the verge of running out of tanks like the T-72 pictured here. The report who's data hasn't been verified by our news agency states that Russia has focused their funds on advanced aircraft and surface vessels, leaving their ground force equipment static. They shut down all but one tank production plant. The Ural Design Bureau of Transport Machine designed a new tank called the T-14, however the Russian Army significantly reduced it's order to only 100 tanks, for testing. Many security researchers are stating that tanks are becoming obsolete due to the advancement of antitank weaponry and drones, that have a much further reach than tanks, and can penetrate weak spots of tanks such as the roof more easily. The report also claims that the Russian defense industry has been unable to replace the aging fleet of T-72s, which are now over 40 years old. The report states that the T-14s have not been produced in large numbers due to cost and maintenance issues, and the Russian Army is now looking for other options to meet their ground forces needs.

Ex.13 On Friday, Chystiakove, a town in Ukraine currently held by the Russians was attacked by a TOS-1 Burratino that was captured by Ukraine in March of 2022. The TOS-1 is a thermobaric rocket launcher. Thermobaric weapons use oxygen from the surrounding air to generate explosions with very high temperature. They are very effective in enclosed spaces such as buildings, and unsealed bunkers. Ukraine is trying to take back the town as it is a large coal producing town, and coal will be needed to heat homes in the winter. The attack was successful in destroying several Russian positions, enabling the Ukrainian forces to regain control of the town. Many speculate that the TOS-1 will be used as a part of Ukraine's strategy to take back towns and cities held by Russian forces. The TOS-1 has been used by both sides to break through fortified positions. The picture shown, is indicative of the destruction that a TOS-1 can cause.

Ex14. Ukrainian citizens in Lviv are on heightened alert after missiles launched by Russian Tu-95MS aircraft have struck the Ukrainian this Monday. The Tu-95MS is a large strategic bomber introduced in the 1950s and has been used throughout the current conflict to launch cruise missiles into Ukraine from safe distances.  The incident occurred early this morning, with local residents reporting hearing a loud explosion and feeling a shockwave that shook the entire area. The Ukrainian President has called the attack an act of terrorism and claims there are no military targets in the area. Russian officials claim that there was a military headquarters in an old, abandoned house and that was the only target that was hit. Lviv is one of the largest cities in Ukraine is considered a safe haven for citizens fleeing from the east, despite consistent missile attacks from Russia who claim that they only hit military targets.

Ex.15 Ukrainian drones are targeting Russian airfields according to a recent statement by the Ukrainian Airforce. They posted a satellite image of a Russian airfield on twitter with a caption "our drones are coming for you". The aircraft pictured on the airfield appear to be Sukhoi Su-34s. The Su-34 is a strike aircraft designed to hit naval and ground targets primarily, although it can fight against other aircraft and conduct other missions such as reconnaissance and electronic warfare. Attacking the aircraft while they are on the ground would be a benefit to Ukraine as it would reduce the number of platforms capable of attacking Ukraine. Ukraine has used unmanned aerial vehicles to attack sites in Russia multiple times.  Russia's Su-34 has been shot down over Ukraine multiple times, to include one accidental downing by Russian air defense forces. Photos are circulating online which show the destroyed aircraft with intact serial numbers.

Ex16. Satellite imagery provided by a European company Thursday shows that Russia is preparing for an increased air campaign. The satellite imagery shows multiple Su-35s in a staging area on an airfield in Western Russia. Russia has maintained air superiority over Ukraine mostly due to its advanced aircraft with long range missiles. Multiple countries are interested in purchasing the Su-35 to include the United Arab Emirates, India, Iran, Algeria, and Turkey.  Ukraine has repeatedly requested air defense assets from western countries to mitigate the threat from Russia. France, and Italy have pledged to send an advanced mobile anti aircraft weapon known as the SAMP/T (Sol - Air Moyenne- Porte / Terrestre (French for "Surface to Air Medium Range/Land based"). Germany has also pledged to send their Flakpanzer Gepard, a self propelled anti air gun that is in service with multiple NATO countries, and the United Kingdom pledged to send their Marksman anti aircraft system.

Ex17. Russian Soldiers are receiving new Anti-Tank weapons, according to a press release from the Russian Ministry of Defense that was published today. The weapons are being distributed to counter Leopard tanks that Ukraine has received from Germany. The new anti-tank weapons are part of a larger modernization program that includes advanced communications and electronic warfare equipment, as well as new tanks and armored vehicles. The program is part of a larger effort to modernize the Russian military, which is also aiming to reduce its reliance on conscripts and improve its combat capabilities. Ukrainian President, Volodymyr Zelenskyy responded to the press release on twitter stating that this was just propaganda and Russia's military was in a dire situation. Defense experts are split on whether the statements are true. Both Russia and Ukraine are known to put media online to bolster morale for their people and military forces. We've reached out for comments.

Ex18. On Monday, Volodymyr Zelenskyy the president of Ukraine pleaded to the world for more anti-tank weapons to fight against Russia. Based on reports from battles, Russians appear to be striking Ukrainian positions with large amounts of T-90 tanks. T-90 tanks, despite having active protections systems (which can defeat most anti tank weapons) developed for them, don't appear to be using them in this current conflict. The Ukrainian government has also asked for more economic aid to help them rebuild their country in the wake of the war. This includes requests for debt relief and financial assistance to help them rebuild their infrastructure and economy. The international community's response to Ukraine's plea for help has been largely positive, and it is hoped that the increased aid and weapons will help the Ukrainian forces defend against Russian aggression and ultimately bring an end to the conflict. Russia still maintains its stance that it is conducting an operation to rid Ukraine of Nazis.

Ex19. An apartment complex was destroyed this weekend in Pavlivka. Pavlivka is a small village north of Mariupol. Ukrainian and Russian forces have been fighting over the town for months due to it being near an important railway hub. Locals report constant shelling at all times of the day and night. No casualties were reported in the apartment complex as many of the civilians have already evacuated the area. The Ukrainian government has condemned the destruction of the apartment complex. Russia claims that Ukrainian shelling is what caused the destruction of the building. Ukrainian and Russian forces in the area appear to be using the same type of soviet era artillery, the ML-20 systems so independent researchers are finding it difficult to determine who is at fault. The constant fighting is making it difficult as well. Local residents are terrified of the constant shelling and the mayor believes the town will be come a ghost town if the fighting doesn't stop, no matter who wins.

Ex20. Ukraine's ministry of defense came out with an estimate on Monday the 13th of February that over 100 billion dollars worth of damage was done to Ukraine's infrastructure and commercial and residential buildings. The estimates were compiled using on-the-ground pictures, satellite images, and local government reports. The majority of the damage was caused by  the S-300 missile system. The president of Ukraine, Volodymyr Zelensky, stated that the funds necessary to rebuild Ukraine's infrastructure will come from the government and international help. He also said that the country will focus on rebuilding the damaged areas and helping the affected people once the war ends. Russia's foreign minister Sergey Viktorovich Lavrov stated yesterday that those numbers are exaggerated, and the war will be over as soon as Zelensky surrenders. Recent reports suggest that China is currently attempting to negotiate a ceasefire, and the UN is looking at putting more sanctions on Russia. All sides are hopeful that a peaceful resolution can be achieved soon.

Ex21."""




pro_russian_military_profile = """Create a Pro Russian Military Profile:

1.Vladimir Fedorov is a Russian soldier who has been stationed in Kazan. He has worked his way up towards General Armii, where he is in charge of the Army as a whole. He loves serving his country and hopes to get Russia to where they deserve to be and stop the corrupt Ukraine. 

2.Evgeni Ovechkin has been in the Russian Military for 28 years now. He is stationed in Sochi, Russia, but has been fighting on the front lines of this war. He started as a Private and worked his way up to soldier of the field. Now is leading his men towards Kyiv and Ukraine and are destroying everything in their way as he is told to do. 

3.Dmitry Kucherov is a newer soldier from Moscow, Russia. He always wanted to be in the Russian Military and fight for his country. He is currently a Serzhant or Sergeant and hopes to climb the ranks one day. His dad died serving in the military and Dmitry says that is the only way to go out, fighting for your country. He is going to do everyhting in his power to fight Ukraine and their corrupt government. 

4.Artemi Tarasenko is a General Major of the Russian Army and has been a force for their Army for 20 plus years. He fought in past wars and this one is no different to him. He stands by the Russian Flag and his fellow soldiers in battle. Originally from Omsk, he got stationed in Ufa, where he has hads to fend off attacks from the enemy in Ukraine. He loves his country and will do anything to help. As a kid, he grew up playing hockey and wanted to be a professional in the NHL. Now, this is what he does and he doesn't regret a single thing in his life. 

5.Igor Panerin, one of Putins right hand men, has been right along side of him ever since he gained power of Russia. Glavniy Marshal or General Marshal his Igor's rank and is extremely good at what he does. He loves his country and will fight for it to the very end. He hates what Ukraine is doing to his country and currently based in Saint Petersburg, is able to defend his people and fight for his country. 

6."""


pro_ukrainian_military_profile = """Create a Pro Ukrainian Military Profile:

1.Ivan Melnyk is a Ukrainian soldier who was born to fight for his country. His dad died fighting for his country and his brother did too. Currently ranked as a Soldat or Recruit, Ivan hopes to climb the ranks and follow in his families footsteps. Ivan right now is based in Kyiv, where a lot of the fight and destruction has occured. He, as well as his other Soldat's are doing their best to stop Putin and the rest of the facists from taking control of the country Ivan loves so much. 
 

2.Petro Shevchenko was born in Belarus but moved to Odesa, Ukraine at a very early age. He loved growing up there and loved his country. He knew when he was younger, he wanted to fight for his country's freedom and that is exactly what he is doing right now. Currently stationed in Kiev, he has his tropps that he leads into battle and to fight the corrupt Russian troops. Starshyi serzhant or Senior Sergeant is his current title and working towards getting higher.  

3.Fedir Bondarenko has been in the Ukrainian Army for 35 years now. First getting into the technology side of things, with drones and other advancements in that nature, now a Lieutenant. He loves leading people and using his technology background to get his guys ready and prepared for battle. Fedir has moved around the country a lot but he currently is based in Donetsk, where much of the fighting has occured. He continues to do whatever it takes for his country to take down Russia and their corrupt leader.   

4.Fadey Kovalenko has been based in Kharkiv for 12 years and is one of the best at what he does. He has recently been promoted to Captain and oversees all recruits and soldiers in his area. He grew up on the border of Ukraine and Russia and could see first hand all the pain Russia casused his familiy, friends, and civilians in both countries. He is proud to be Ukrainian and will fight for his country to the very end to defeat Russia and their troops. 

5.Artem Koval, who works extremely close to Zelenskyy and the rest of Ukrainian leadership, has been stationed in Kyiv for the past 19 years way before Zelenskyy's presidency. He has built up immense trust with the leaders of the country and has been elected General of the Ukrainian Army. Artem vows to find peace and freedom for his country and he will not stop till he acheives that. He will put a stop to this awful war that Russia started because they are power hungry.  

6."""


pro_ukranian_tweet= """Examples of Pro-Ukrainian tweets:

1.We need your help! Russia has been killing innocent people here in Ukraine. We don't have enough firepower to hold them off.

2.We have been fighting for our freedom for months now. The Facists will not let up. We need your help to stop Russia and corrupt Putin.

3.This war needs to stop and we need your assistance now. Russia has been destroying our schools and other buildings. This isnt right. We need your aid right now. So many lives have been lost due to the hands of the Russian Government. They are so corrupt and need to be stopped.

4. Ukraine is in constant panic right now and need help from the West. We are begging the people need help in this fight.

5. The people of Ukraine are suffering. Russia does not look like they are letting up soon and we need your help to stop them. 

6.Russia is so corrupt. We are asking for your help to stop Putin and his army for the freedom of our people.  

7.The people of Ukraine need help from NATO and the rest of the world. Russia has been killing innocent civilians and it is not right.

8.Ukraine needs your help. We are so close to winning this war and stopping Russia, we just need a little more time and assistance from everyone.

9.I didn't think it would get to this point. But it has and we are asking for your help. Russia has bombed ur homes and the people of Ukraine are struggling, we need to stop them.
10."""

ukraine_soldier = 'RAW photo, a close up portrait photo of 40 y.o.  Ukrainian Soldier, background is city ruins, (high detailed skin:1.2), 8k uhd, dslr, soft lighting, high quality, film grain, Fujifilm XT3'
russian_soldier = 'RAW photo, a close up portrait photo of 40 y.o.  Russian Soldier, background is city ruins, (high detailed skin:1.2), 8k uhd, dslr, soft lighting, high quality, film grain, Fujifilm XT3'
       
tab1, tab2 = st.tabs(["Create Synthetic Text", "Create Synthetic Image"])

with tab1:
   '''# Text Generation'''
   '''The model that will be generating text in these examples is gpt2-xl, a 1.5B parameter version of GBT-2 which is a transformer-based language model created and released by OpenAI. The model is a pretrained model on English language using a causal language modeling (CLM) objective.'''
   url = 'https://ka-darpa-02.chris-mckinley.website'
   col1, col2 = st.columns(2)
   with col1:
      temperature = st.slider('Temperature', min_value = 0.1, max_value = 2.0, step = 0.1, value = 0.5, help = 'Randomness of sampling. High values can increase creativity but may make text less sensible. Lower values will make text more predictable but can become repetitious')
   with col2:
      token_length = st.slider('Token length', min_value = 16, max_value = 512, step = 1, value = 200, help = 'Number of tokens to generate. (4 characters is about one token)')
   select_prompt = st.selectbox('Select a prompt', ['Netrual Russian Ukraine News Topic', 'Pro Russian Military Profile', 'Pro Ukrainian Military Profile', 'Pro Ukrainian Tweet', 'Custom Prompt'])
   col3, col4 = st.columns(2)
   with col3:
      if select_prompt == 'Custom Prompt':
         prompt = st.text_area('Enter Custom Prompt', help = 'You will get much better output if you provide examples of what you expect back.')
   with col4:
      if select_prompt == 'Custom Prompt':
         singleline = st.checkbox('Single Line?', value = False, help = "When enabled, removes everything after the first line of the output, including the newline.")
   if select_prompt == 'Netrual Russian Ukraine News Topic':
      prompt = news_neutral_topic_RUS_UKR
      singleline = True 
   if select_prompt == 'Pro Russian Military Profile':
      prompt = pro_russian_military_profile
      singleline = True 
   if select_prompt == 'Pro Ukrainian Military Profile':
      prompt = pro_ukrainian_military_profile
      singleline = True 
   if select_prompt == 'Pro Ukrainian Tweet':
      prompt = pro_ukranian_tweet
      singleline = True 
      
   if st.button('Generate Text'):
      request_url = "%s/api/v1/model" % url
      Model = 'gpt2-xl'
      if Model == str(requests.get("%s/api/v1/model" % url, headers=headers).json()['result']).replace('/','-'):
         pass
      else:
         response = requests.put(request_url,json={'model': Model}, headers=headers)

         loaded_model = requests.get("%s/api/v1/model" % url, headers=headers).json()
      
      request_url_generate = "%s/api/v1/generate" % url

      #Data for Text generation
      json_data = {
         'prompt': prompt

         ########Most Commonly Modified Settings #######
         ,'max_length':token_length #Number of tokens to generate. (4 characters is about one token)
         ,'singleline':singleline #Output formatting option. When enabled, removes everything after the first line of the output, including the newline.
         ,'temperature': temperature #Randomness of sampling. High values can increase creativity but may make text less sensible. Lower values will make text more predictable but can become repetitious.
         ########Most Commonly Modified Settings END #######

         
         ,'top_p': 0.9 #Top P Sampling - Used to discard unlikely text in the sampling process. Lower values will make text more predictable but can become repetitious. (Put this value on 1 to disable its effect)
         ,'top_k':0 # Top k Sampling - Alternative sampling method, can be combined with top_p. (Put this value on 0 to disable its effect)
         ,'tfs':1 #Alternative sampling method; it is recommended to disable top_p and top_k (set top_p to 1 and top_k to 0) if using this. 0.95 is thought to be a good value. (Put this value on 1 to disable its effect)
         ,'top_a':0 #Top a Sampling - Alternative sampling method that reduces the randomness of the AI whenever the probability of one token is much higher than all the others. Higher values have a stronger effect. Set this setting to 0 to disable its effect.
         ,'typical':1 #Typical Sampling - Alternative sampling method described in the paper \"Typical Decoding for Natural Language Generation\" (10.48550/ARXIV.2202.00666). The paper suggests 0.2 as a good value for this setting. Set this setting to 1 to disable its effect.
         ,'disable_input_formatting' : True #needed so system doesn't pull input formatting from the GUI
         ,'disable_output_formatting' : True #needed so system doesn't pull input formatting from the GUI
         ,'frmtrmblln':True    #Output formatting option. When enabled, replaces all occurrences of two or more consecutive newlines in the output with one newline.
         ,'frmtrmspch' :True   #Output formatting option. When enabled, removes #/@%{}+=~|\^<> from the output.
         ,'frmttriminc' :True  #Output formatting option. When enabled, removes some characters from the end of the output such that the output doesn't end in the middle of a sentence. If the output is less than one sentence long, does nothing.
         ,'rep_pen':1.1        #Base repetition penalty value.   If set higher than 0, only applies repetition penalty to the last few tokens of your story rather than applying it to the entire story. This slider controls the amount of tokens at the end of your story to apply it to.
         ,'rep_pen_range':0    #Repetition penalty range. If set higher than 0, only applies repetition penalty to the last few tokens of your story rather than applying it to the entire story. This slider controls the amount of tokens at the end of your story to apply it to.
         ,'rep_pen_slope':0    #Repetition penalty slope. Repetition penalty slope. If BOTH this setting and Rep Penalty Range are set higher than 0, will use sigmoid interpolation to apply repetition penalty more strongly on tokens that are closer to the end of your story. This setting controls the tension of the sigmoid curve; higher settings will result in the repetition penalty difference between the start and end of your story being more apparent. Setting this to 1 uses linear interpolation; setting this to 0 disables interpolation.
         ,'max_context_length':1024 #Maximum number of tokens to send to the model.
         ,'n':1
         ,'sampler_full_determinism':False # If enabled, the generated text will always be the same as long as you use the same RNG seed, input and settings. If disabled, only the sequence of generated texts that you get when repeatedly generating text will be the same given the same RNG seed, input and settings.
         }

      response = requests.post(request_url_generate, json=json_data,headers=headers)
      
      try:   
         generated_text = response.json()['results'][0]['text']
         '''#### Synthetic text based on your selections:'''
         st.markdown(generated_text.strip())
      except:
         '''Someone else is generating text right now. Please try again.'''

with tab2:
   '''# Image Generation'''
   model = 'SDv2.1.ckpt'
   sampler_index = 'Euler a'
   seed = -1
   
   col5, col6 = st.columns(2)
   with col5:
      cfg_scale = st.slider('Choose CFG scale', 0.0,30.0,7.0,0.1, help='Controls how much the image generation process follows the text prompts. The higher the value, the more the image will stick to the prompt.')
   with col6:
      steps = st.slider("Number of Steps", 1,150,40,1, help='Generally, more steps result in a higher-quality image but will take longer to create.')
   col7, col8 = st.columns(2)
   with col7:
      height = st.number_input('Enter Height of Picture', value=512, min_value=64,max_value=2048)
   with col8:
      width = st.number_input('Enter Width of Picture', value=512, min_value=64, max_value=2048)
   select_prompt = st.selectbox('Select a prompt', ['Russian Soldier', 'Ukraine Soldier', 'Custom Prompt'])
   if select_prompt == 'Russian Soldier':
      prompt = russian_soldier
      negative_prompt = ''
   if select_prompt == 'Ukraine Soldier':
      prompt = ukraine_soldier
      negative_prompt = ''
   col9, col10 = st.columns(2)
   with col9:
      if select_prompt == 'Custom Prompt':
         prompt = st.text_area('Enter Positive Prompt')
   with col10:
      if select_prompt == 'Custom Prompt':
         negative_prompt = st.text_area('Enter Negative Prompt')
         
   if st.button('Generate Image'):
      url = "https://sd-darpa-02.chris-mckinley.website"
      option_payload = {"sd_model_checkpoint": model}
      x = requests.post(url=f'{url}/sdapi/v1/options', json=option_payload, headers=headers)
      payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "steps": steps,
        "cfg_scale": cfg_scale,
        "height": height,
        "width": width,
        "sampler_index": sampler_index,
        "seed": seed
        }
      response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload, headers=headers)
      r = response.json()
      for i in r['images']:
         image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))
         
      st.image(image)