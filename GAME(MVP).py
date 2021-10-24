#Song of Achilles
import time
start = time.time()
print("Please input your name for scorekeeping:")
name=input()
sm=""
def sm(key:int,message:str):
	for idx in range (len(message)):
		letter=message[idx]
		code=ord(letter)+keyword
	if code>122:
		code-=26
	encoded=chr(code)
	sm+=encoded
	return sm
import sys
from time import sleep
words = "INSTRUCTIONS: The goal of the game is to defeat Troy with efficiency and minimal loss of life. Only input your choices in number form."
for char in words:
    sleep(0.1)
    sys.stderr.write(char)
print("Welcome Achilles, to the Trojan battlefield.")
words = "Act I: We are men only"
for char in words:
    sleep(0.1)
    sys.stderr.write(char)
print("You awaken in your tent, there is a body next to you, your companion Patroclus. By your bedroll lays a spear and a sword")
print("You pick up your spear and wake Patroclus. He grabs his sword and dons his armour.")
print("You both head to the forum of your camp. There is a young maiden on the altar. She is crying, Agamemnon and Odyessus are arguing.")
print("Patroclus wishes to intervene, will you stop him?")
print("1-Yes, stop him")
print("2-No, allow him to intervene")
score=0
while True:
	choice1= input("Your Choice?:")
	try:
		if int(choice1) == 1:
			print("You hold back Patroclus as he takes a step forward. You shake your head, expressing your displeasure at his actions.")
			print("You can see he is frustrated and you soothe him by telling him that ending the war is more important than a girl causing infighting.")
			score = score - 10
			break
		elif int(choice1) == 2:
			print("You allow Patroclus forwards. He rushes to the girl to soothe her as she cries. Agamemnon is displeased and Odysseus sends an appraising look.")
			score = score + 10
			break
		else:
			print("Please enter either 1 or 2:")
	except:
		print("Value must be whole number 1 or 2:")
print("Patroclus smiles at you and you both head towards the gate. The war horn is sounded and soldiers flood from the tents.")
print("Patroclus heads to the medical tent to attend to his duties, you notice he has dropped his dagger.")
print("You will not be able to lead the charge if you hand him his dagger back")
print("Do you give him his dagger?")
print("1-Yes")
print("2-No")
print("3-Keep the dagger on yourself")
while True:
	choice2= input("Your Choice?:")
	try:
		if int(choice2) == 1:
			print("You grab the dagger and rush back towards the medical tent. Various warriors around you make noises of displeasure as you rush past them.")
			print("You reach the medical tent and quickly deposit the dagger by Patroclus' work station. He smiles at you and you run off to join the battle.")
			print("The battles rages around you. Suddenly from your right a Trojan soldier cleaves through your spear.")
			print("Now without your weapon, you use your sheild to block his sword and knock him out. Although the enemy was slain you recieve a wound on your left arm.")
			print("With the wound bleeding so much you had no choice but to retreat to the camp.")
			print("When you arrive at the medical tent, you turn the corner just in time to see Patroclus stab an intruder with his dagger.")
			print("You both take his body and tie him to the central podium")
			score = score + 10
			break
		elif int(choice2) == 2:
			print("You leave the dagger as it is swallowed by a stampede of men.You rush forward with the warriors to face the Trojans head on.")
			print("The battles rages around you. Suddenly from your right a Trojan soldier cleaves through your spear.")
			print("Now without your weapon, you use your sheild to block his sword and knock him out. Although the enemy was slain you recieve a wound on your left arm.")
			print("With the wound bleeding so much you had no choice but to retreat to the camp.")
			print("When you arrive at the medical tent you turn the corner to see Patroclus struggle with an intruder.")
			print("As you rush forward the intruder manages to slice Patroclus's face, far too close to his eye.")
			print("You tackle the intruder, killing him and tie him to the central podium.")
			score = score - 10
			break
		elif int(choice2) == 3:
			print("You take the dagger and tuck it into your belt. You could return the dagger to Patroclus after the battle.")
			print("The battles rages around you. Suddenly from your right a Trojan soldier cleaves through your spear.")
			print("Now without your weapon, you pull the dagger from your belt. You continue to slash through the enemies until an archer forces your hand.")
			print("You throw the dagger and hit the archer but not before the arrow digs into Ajax the lesser's shoulder.")
			print("With one of the kings wounded you have no choice but to retreat to camp.")
			print("When you arrive at the medical tent you turn the corner to see Patroclus struggle with an intruder.")
			print("As you rush forward you notice the intruder has already managed to slice Patroclus's face, far too close to his eye.")
			print("You watch as the intruder brings his own dagger towards Patroclus' eye. Without hesitation you dash forward and knock the dagger from the intruder's hands.")
			print("You tackle the intruder, killing him and tie him to the central podium.")
			score = score + 5
			break
		else:
			print("Please enter either 1 or 2:")
	except:
		print("Value must be whole number 1 or 2:")
print("As warriors return from battle they begin to notice the corpse on the podium.")
print("Everyone is drawn to the area and you begin to speak.")
print("'A spy has made their way into our camps I propose we-' You are cut off by Agememnon's laughter")
print("Agememnon gestures to another bound woman by his side.")
print("'This is Chryseis, a fine spoil of our fight! Tonight I offer the finest soldiers our finest woman!")
print("Patroclus frowned and asked quietly,'Isn't that Chryseis the daughter of a preist?'")
print("you nod in thought, he was correct, Chryseis was in fact the daughter of a preist of Apollo.")
print("The crowd suddenly falls silent as a man in Trojan robes walks through the crowd. Soldiers part for him as he stands before Agememnon.")
print("'My daughter is not some war prize. I will give you all the gold and riches within my family you just return her to me. Please.'")
print("The man kneels before Agememnon and Agememnon only laughs.")
print("The preist is clearly angered and tells Agememnon, 'Oh general I would not wish to curse your people but if you do not return my daughter to me I will have no choice.'")
print("You see an opprotunity, you are a figure of great influence in the army and could potentially avoid disaster with your actions.")
print("what do you do?")
print("1- Confront Agememnon physically")
print("2-Confront Agememnon with words")
print("3-Go behind Agememnon's back later")
print("4- Do not confront Agememnon")
while True:
	choice3= input("Your Choice?:")
	try:
		if int(choice3) == 1:
			print("You push through the crowd until you reach the podium Agememnon is standing upon.")
			print("You walk till you are nearly nose to nose with Agememnon. You breathe in deeply and grab his bicep in a crushing grip.")
			print("'General, I must insist that you let her go, it will not do well for plague to rain down upon us.'")
			print("Agememnon scoffed and yanked his hand away. His hand drifted towards his sword but he never drew his sword. Even he was not foolish enough to fight Achilles.")
			print("However, Agememnon wasn't swayed he turned back to the crowd. You draw back your hand and punch him squarely in the face.")
			print("Few from Agememnon's warrior sect gasp and yell, but much of the crowd remains silent, adverting their eyes.")
			score = score + 5
			break
		elif int(choice3) == 2:
			print("You speak from your pace among the warriors. 'General Agememnon, will you be the one foolish enough to doom our people to plague?")
			print("Agememnon was about to retort when Odysseus chimed in, ' The Aristos Achaion is correct. Her father is a preist of Apollo, it would not do well for us to anger the gods.")
			print("Agememnon scoffs and turns away, even so the crowd has begun whispering.")
			print("Your words have driven the owl eyed Odysseus to agree with you, surely one blessed by the wisdom goddess Athena cannot be wrong.")
			score = score + 10
			break
		elif int(choice3) == 3:
			print("You say nothing as the crowd disperes around you. Tonight, you will steal the girl away from Agememnon's tent and return her to her father, leading your men away from death.")
			print("As night falls you wait till the moon is high in the sky. By the light of the stars you grab your dagger and slip into the night")
			print("As you traverse the camp silent like a shadow you can hear the occasional snore from the men.")
			print("Slipping along the outer barrier of the camp you arrive at Agememnon's tent. Easily one of the largest tents in the camp the single candle can barely illuminate the interior.")
			print("You find Chryseis bound to one of the tent poles, thankfully mostly unharmed. You bring a finger to your mouth and begin to work on the ropes with your dagger.")
			print("You nearly finish freeing her when in her rush to escape, she knocks over the tent pole. Agememnon awakes with a shout.")
			print("With no choice but to flee, lest you be charged with treason, you flee.")
			score = score + 5
			break
		elif int(choice3) == 4:
			print("Agememnon stands proudly. He tells the crowd that 'Us Greeks are the children of the heavens, we need not fear their wrath!'")
			print("With his men cheering for him, the other armies relucantly cheer. You stay silent and watch as Patroclus walks away from the crowds, his dissapointment radiating from him.")
			score = score - 10
			break
		else:
			print("Please enter either a number:")
	except:
		print("Value must be whole number:")
print("The next day, Chryseis was back on the podium. Achilles grit his teeth, both he and Patroclus felt frustration with their inability to help Chryseis.")
print("In the forest, a short walk away from the camp, Chryseis's father, Chryses was praying to the Apollo.")
print("Chryses has always been considered on of Apollo's blessed priest. As such it was no surprise that the god answered his calls.")
print("By the next morning, nearly 200 men had fallen ill mysteriously at camp.")
words = "End Act I. Proceed to Act II?"
for char in words:
    sleep(0.1)
    sys.stderr.write(char)
print("1-Yes")
print("2-No")
while True:
	arc= input("Continue?:")
	try:
		if int(arc) == 1:
			print("Proceeding to Arc II.")
		else:
			print("Thank you for playing :)")
end = time.time()
print(name)
print("Your total game time was:",end - start)
print("Your Score is:",score)
if score == 120:
	print("You have been rewarded the medal of Elysium")
if score == -120:
	print("You have been rewarded the medal of Tartarus")
if score == 60:
	print("You have been rewarded the medal of Asphodel")
