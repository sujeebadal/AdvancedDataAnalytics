text= '''A CerTaiN kING HaD a bEaUtIFul gaRDEn, ANd IN THe GarDen StooD A trEe
whICH bORe GoLDeN ApPlEs. THesE aPples WerE alwAyS CoUntEd, aNd abOuT
tHE TiMe WheN tHEY BEgAn tO grow RipE IT wAs foUND THat EVeRY NIgHT ONE
OF THeM Was gOne. thE kiNg bECAMe veRy ANGRy at thiS, aND ORDEred the
GarDEneR TO KEeP WAtch ALL NIgHT uNDER the tREE. tHE gardener sEt hIs
ELdEsT SoN to WATCH; buT ABout TweLve O’clOCK He fELL ASlEEp, And in
the morNIng aNOTheR Of thE aPPLes Was mIssinG. tHEn THE sECONd Son waS
oRdERED to waTch; aNd AT mIDniGhT he tOO FELl ASleEP, aND iN thE mOrNIng
ANoThER AppLE WaS gOne . TheN THe thIrd Son oFfeREd tO KeEp wATCh; buT
thE garDENer At First WoULd NoT LET Him, FOr fEaR sOMe HArM ShOuLD cOME
To hIM: hoWeveR, at lAST hE coNSEnteD, AND tHE YouNg MAN laID HimSELf
uNDER tHE tREe TO wAtch. AS tHE clocK STRuCk tweLvE He Heard A rustlinG
NoISe IN ThE aIr, And a biRd CAME FlYing ThAt was Of PUre gOLd; AND as
IT WAs SNApPING At onE oF ThE aPpleS wIth iTS BeaK, tHE GArDEner’S son
jUMpED UP And SHOT AN aRrOw at iT. But THE arrOw DID thE BiRD nO HaRm;
ONlY iT dRoPPEd a GoLDEn FEather FROM iTS tAiL, aND THEN FLEw AwaY.
the gOLdEN FEAthER WAS bRoUght to THe KinG IN THE MOrNING, AnD aLL ThE
cOunCil WAs called TogETHER. EVERYoNE aGREed ThAt it wAS wORth MoRe THAn
aLl The weAltH Of tHE kIngDOm: But THE KiNg sAID, ‘One FeatHeR Is Of NO
use tO me, I MusT HaVE ThE wHOLE BIRD .’ '''
import re
from string import punctuation
text=re.sub('ln', '', text)
text=text.lower()
worlds=text.split()
newls=[]
for word in worlds:
	word= word.strip(punctuation)
	if word=='':pass
	else:
		newls.append(word)
	print("This text has () words.".format(len(newls)))
	
word_count={}
for word in newls:
	if word not in word_count:
		word_count[word]=1
	else:
		word_count[word]+=1
	print("The frequency count of each word is listed below:")
for word,count in word_count.items():
	if count==1:
		print ("The word(0)was used {1} time.".format(word,count))
	else:
		print ("The word (0) was used {1} times.".format (word,count))
	