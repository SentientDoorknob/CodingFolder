import sys
sys.path.append("C:\\Users\\justa\\Documents\\Coding\\Public\\CodingFolder\\Cryptography")

import cryptotools as ct

# take ciphertext input and format it
text = """JDEFOIOLWILONUONGPYULAORSMSSTEAETHGIOGTIUHSOLDHUSNYOEDUHATTETCEDAHIIALTSETRFTERMAIOMSEOTITHPOVERIECEDNBACHRNOPNKFIETNSROSNVIETAIELWRESNRSIELTOPYAEORRPTHCHWIIAEBHVENNAEUBEOLLTOAERCTEDNGAIBTEEEWNHLITENSTHEIIKECNWAASUNSMTATEHMIIEASHDOMACMSIOISNDUREFTEINHRVSIGETAINSTOFLOWOLIGECNREPOFITTEEPHROTNIROSEANLSDHTSTAHWSCEAOTNUNIIGOFNTUDHENTEQIRNUYHUGTOHANOIMTUEHSROSEMWHAAEDNGTAONHTAIRALBRASSINAAYPLRIKRTNEOSUSNMTAEBHVEIVELEDHTSTAHWSGEAODOROFHREBEDTSHEATRIAFESIEULLFLFNCOERPEDYTCMUNOMIAIOCTNBTWSEENHEETMOHFBTOLWILONUONGPTILEHSTEANTRDTINIHKEILWWLEUSBBYRAKBEIGHONTSCPHEIESVERORHNETEXFWWTEEKTHESEOSEMRSOEDLWMDWNEOBTEVUIETALNULMNAYAGDOCETRCTHAKEIHECPRNERUDNAHTETHCDEEOADCANINRMIPOSTATEHYUILOWLIDTFNHCNTEOETINNSTRSTEEIGAINMSEPEISLEOULDTHTSWAHTOUEHGTIGHMHHVETABEGOENIGNBNOUIONTWDRFSEIHWSMEAISNGSISMTHOEIGMPNIOTNTRASEINHHTDTIEATNHEITPRSEHAIASHWSOKDTCEOERAHABUTHOTEIUASTTOOFINMEPLYMOETHYROGSHUHEOSNDEOEPATXNOTHDNANRDTOOSHEESFLOWOLTATHHTOGTTUHOTNAISTRLCUAOCUSNLINAVOHIGARNCREOUIDTYWNMOEQIRNUISITEWHOTECNMOARPRYAKRBNEODSCRIICLTSERHAATTHSITETAIOUTNHRESEFREDERTITHOSEIANFNCADIILFIULFCTTATYHRGRSOEMNIOETNDNOEIUERLRAIRILEFEHSASIMIIOBTNAMUWSCLRGHAETANRHHSUDIBGTNDEAIOCUTCRTMESOTAPEHTRASTHPHRASEEOFRTNOHVLUEAAINATONTENDHEPLIWOCWSTYAOLOWALHMOSITTGATAEHFIFETHWSIEANEGULAEIHIWTSETHLSEHMANEYAEPHVLNEDANTSLLOESMOFOETEORHMEAUAVLBETELIMFOMSRTEIBHLRRATAYANCKKODWPRONIEOTCTHAREELSODDFRELRSAEADOCNTLIONAMTENSHIUACERNTIWOHSUDLLLAOHMTWIOAOFPYFIDEHSBSNDTATFNDOUHSAMICPINYAGOMGHUITBECOJTHTHTAEOLDCUHVACAEHEEDIVMROROELSTHESEAEOSMUCMETOBSLLYEIGHENTBOSAOKTAEVFCAUBULETAINHVGOSTBAEFRSDOOEIMMTEBUTAOTEREHTAUESSRMIIEASHDCQAAURDFIEOHMIRITOLDWUHVBEAEEITENNNEYESLMARABRSIGTSNOITOGFNYHELTLWRVOEAUDPLEATOFRSTEOLHCLCIOETNOHETTCTTHIYEEASRWASTHLOEIKTRSHTUYABESOURWLHVEDABEALENETDTREOINEHSETSEDOLADTLNHTHEATRSLTEUIGRINPCWULEODAEBHVENOWELETANRHTENSHIUACERNVLATAUINTWOIOLCEUDRANLTIYAEBHVENDAEANEOUGRSTATSREYUTGBPRAPEHSHRITESWSWKAOTTARHKNTHIGEHDEROILNDSAEETOLCRTWEAERNTMEOUHIVCGETVONOTNFOIGRAKRBNUTESPSPCALEILTOSYHEHSEWODBSWETEECCRAUUATMLEATHDTEADTCRALOFBECUSEORIRGEFORWSBSAEIDAHNSHMECETDFROEADHEUTISRENURTENSHIISTTSRNETAGHTEWAHATDTNEHRBBEOEYNVRIETGASITOENINDDUTEBRMMBEEETATRHNBOKOOSEEAWRCULLTAYTLESONOOSSNINFIGICNCLATAMOUICLAISDREIHNWTOOSIPSBEAILGNTAKIMESNSSEEHTHTAEOLDWUWNTHATEHLEWOSRYAORFARFFIOGTTROEFRTNUHRNVEIETGASITOMIINGTASHEIYAVLHERUGBOHHSRTIOENTLIHTEFEHTOIGTLHPRMTEAETLNNYPILSOIGISNHEETILCOCANNHCSNDEAPRAPEHSVNLEEEDNGAITAPEOSLOINLFCRERACAINITOLOFOOKRADTWROERIHANYURGOTOGHHUTTESSHEDESILPCLAEUTOSIINAEJOMNYNMYIGHLDAOIYETWBSIHSHSEARRY""".replace(" ", "").replace("\n", "").upper()
text = text.replace(" ","").replace("\n", "").lower()
text_len = len(text)

# assume keylength, define output and devise the length of columns
key_length = 34
output = ""
columnNumber = text_len//key_length

# split the cosets
cosets = ct.splitCosets(key_length, text)

# output the output thing
for i in range(0, columnNumber):
    for coset in cosets:
        output += coset[i]
        output += ","
    output += "\n"

print(output)

