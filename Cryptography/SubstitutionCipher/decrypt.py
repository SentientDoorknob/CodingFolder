import sys
sys.path.append("C:\\Users\\justa\\Documents\\Coding\\CodingFolder\\Cryptography")

import cryptotools as ct
import matplotlib.pyplot as plt

text = """RDLLW NRDGA MVHLN ROSHJ WHVNR OJYGA OLNHG LOJHL NYVHP GCDGY COGNY SDBVY BOYGH PLDLS RYQOM IPNYN TDMDG YGNOL SOJNV LHFNR ONOBO ELDJR DGCRD CGNIO OGJYS AOCPJ IWNRO JHBYS OMHYN TDMGH NYGNR OVYBO MYRDC IHLLH TOCVL HFNRO FYVHB BHTOC PJHGN ROIHH AMRHJ BODCI PNCYC GNEON VDLDB NRHPE RSPLY HPMBW DBLOM VHLCR DMIOO GDJBD SOHVY GNOLO MNNHN ROYGN OBBYE OGSOM OLQYS OVHLD TRYBO NROYG VDFHP MJHLN BDGCM JWLYG EPMOC NROJP IBYSB DQDNH LWHQO LNROL HDCVL HFNRO BHSDB JHBYS OMNDN YHGNR OLODM DCODC CLHJT RYSRM OOFMQ OLWPG BYAOB WIPNY EPOMM NRDNT DMNRO JHYGN DGWTD WNRDN RDMGH NRYGE NHCHT YNRNR OSDMO TODLO YGQOM NYEDN YGERO LOYED NROLV LHFNR OVYBO MNRDN MHHGD VNOLF YMMMN WBOML OSOYQ OCNRO JYGAO LNHGL OJHLN MROTD MDIBO NHJOL MPDCO NROJH BYSON HLOHJ OGNRO SDMON ROWCH GNMOO FNHRD QOIOO GJDLN YSPBD LBWCY BYEOG NHLAO OGRDL JOLTL HNODF OFHSR DMNYM YGENR OFVHL NROYL BDSAH VJLHE LOMMJ OLRDJ MNHYF JLOMM RYMVL YOGCL HEOLM IPNNR OCONO SNYQO YGSRD LEOLO JBYOC TYNRD BHGEB YMNHV LODMH GMTRW NROSD MOTDM RHJOB OMMRD LJOLM CYDLW MRHTM NRDND JBDGG OCFOO NYGEN HCYMS PMMNR OSDMO TDMSD GSOBB OCMHH GDVNO LROLO SOYQO CNROL OJBWN ROTRH BONRY GETHP BCRDQ OIOOG OGNYL OBWVH LEHNN OGIWG HTYVF DYMYO RDCGH NTLYN NOGDE DYGNH NROJH BYSOS RYOVT YNRDG OUNLD HLCYG DLWSB DYFNR OOGSL WJNOC GHNON RDNCL TRYNO RDCVH PGCMO TGYGN HNROI YGCYG EHVNR OIHHA CYMJB DWOCM OQOLD BVODN PLOMN RDNMP EEOMN OCYNR DCIOO GTLYN NOGHG NRONW JOTLY NOLYG NROFD GMYHG YNMOB VNHFR DLJOL TDMMS OJNYS DBDMN RONWJ OVDSO DJJOD LOCNH IODMN DGCDL CPGCO LTHHC NWJYS DBHVR PGCLO CMHVN WJOTL YNOLM YGNRO MNDNO IPNYN TDMNL PONRD NNROB ONNOL ZMRHT OCDCY MNYGS NYQOC YJDGC NRDNN ROBON NOLDT DMFYM MYGEY NMPJJ OLMOL YVYGN ROGHN OIHNR VODNP LOMMO OGYGH NROLC HSPFO GNMNW JOCHG NRORH PMOFD SRYGO RDLJO LTDMS BODLB WCYMN PLIOC IWNRO CYMSH QOLWR YMCDY BWBHE GHNOC NROVY GCYGE MTYNR NROLO FDLAM YVNRO GHNOT DMTLY NNOGI WMHFO HGOYG NRORH PMORH BCNRO GCHOM NRDNF ODGNR DNNRO WTOLO YGBOD EPOTY NRYMB OMHLN RDNNR OWTOL OMHFO RHTYG QHBQO CTYNR RYFTR WCYCR OSRHH MONRD NJDLN YSPBD LIHHA ROMOG NDBON NOLNH LHEOL MDMAY GERYF YVROS HPBCD SSHPG NVHLN ROCYM SHQOL WDGCL OSOYQ OCNRO DNNDS ROCLO JBWTO SDGZP CEOZP MNRHT LDNNB OCLHE OLMVO BNIWN ROVDS NNRDN ROOGS LWJNO CYNPM YGEDQ YEOGO LOSYJ ROLRO SBODL BWCYC GHNTD GNNHN DAODS RDGSO NRDND GWHGO HNROL NRDGR DLJOL THPBC LODCY N"""

text = text.replace(" ", "").replace("\n", "").lower()
textLength = len(text)

cipher_freqencies = ct.frequency(text)

english_frequencies = ct.ENG_LETTER_FREQ
cipher_freqencies = [frequency/textLength for frequency in cipher_freqencies]

english_ordered_alphabet = [x for _, x in sorted(zip(english_frequencies, ct.ALPHABET))]
cipher_ordered_alphabet = [x for _, x in sorted(zip(cipher_freqencies, ct.ALPHABET))]

english_ordered_alphabet.reverse()
cipher_ordered_alphabet.reverse()

english_frequencies.sort(reverse=True)
cipher_freqencies.sort(reverse=True)

print("hello")

print(english_frequencies)
print(english_ordered_alphabet)

plt.figure(1)
english_plot = plt.bar(english_ordered_alphabet, english_frequencies)

plt.figure(2)
cipher_plot = plt.bar(cipher_ordered_alphabet, cipher_freqencies)

plt.show()



