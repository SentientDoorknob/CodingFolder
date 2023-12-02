import sys
sys.path.append("C:\\Users\\justa\\Documents\\Coding\\Public\\CodingFolder\\Cryptography")

from vingereKeywordLength import *
import cryptotools

import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

alphabet = cryptotools.ALPHABET

# take input text and format it all lowercase with no spaces or newlines
text = """SIJKJ BZTYS KYZZL APNAE PAQHF AWGEU WPPPS OPIEN NPTXE BWKAQ UMFZW HQEZT EPSIA MFXOJ MMTIE LEQDE YWLOP ZQVWM SKHPQ TYLAT XVGMP VLBCM DRDCJ XTSFH HEZHT VLAPP GNDMZ HWLOT DQFOZ TNXOU SBDQW PLAUE PIJEJ DWKJI FQTWM LLJGN EBZXW QTKLZ QMSMS MEIUA PLWQE ZSVEN JHXPW KDXWE WAGNE PWKOM WILBL TNPEX YBLHT BEHCM GOPZL APMXY ZZLTY LEHYM QLSMK IPVLM CGAGR BGXDB SUWQK APDAW PVUXN WFGPK LBYOL APPGN DMZHW LLHEP WTEBW FABWW EPWYE AZHHA ZHHQE IZZLT YBAMH IKMZP WKTAA MAWKL TJDXE PSMTB OTDVL KZOWK DEZHZ ZYTYQ KXOBZ XEPWY EKGNW LKHXM GGPQF MSMET YWJAL DWALL SZCCV ZPIYT TVKMX IALTM KMPID BYOXK ZULAP TAUCI JRDMW FDTAD PIYHZ LAYNW FOZTM MPLOT JBGZP BSMSM JBHWM EOTAD PBGKP IVFZZ WHQUS BDQWL EPGNR PLLMC LLSMO TDDWK JKSKP NMESM JWTIJ RAIYX DEWKP MFVCG HMPLO BEPSA ZALHQ LAYQM JXYBU BAPWK DIFWL ALBXM OXYBG GDPWT OIHMP LSGOA LKPVY MSMFX OBZXX BZBDW FXWWG DDPSK OJMMT BALCM SEWGH KPBLR PIKRE PWELB WKZVW LRMLT WWLMZ CYAPZ SGJES RHMFX PLLHA TSGZC JGPFL LEMHL NWMEO GGNEZ QMZOW MLTAL EWXMS MEXXJ WKDWX KZOWK DPGND MZHWL SGOUS DPMFJ FQJBP ASUZC LMSME BEEGN WLTXR WGWEW CGZEA YEPWK PESLL VQHYM OAZPS WLZWT DWFMZ LALWQ CXXIA LTMOX DPGNW LFHEL ALNWM GEUSB DQWLE PWHCG LALBL APBZX QBOTD XSKEW XTYQF LFZSG NMKVL UWBEP WKMCL BQQFW TBZTC LLHMM DBPDW MSILK ZOWKD EGNWL ZTGMJ BDSWW SQKKP XMMLB AHYIF WSQKV SIFVP WXMSM YHGMJ GZZKA TXWOP VAYSM OTDAZ HCBGY XWFXJ XWHAT WETSW ATUUH FTVND CSEWG XBYLK HXMGG PBGUL KCMSM EBWWG DQWJP LZVMZ PWTCQ FZQZG FJWMC ZLAXA AOALB SKPGG NCMSW TVYKT OZMYW O"""
text = text.replace(" ", "").replace("\n", "").lower()
textLength = len(text)

# estimate keyword length (see vingereKeywordLength.py)
differences = getEstimatedKeywordLength(text, 10)

print(differences)

# set to earliest outlier of differences, and iterate throught the focuesed coset
keywordLength = 4
focused = 3

# split text into cosets by estimated keyword length as decimals
cosets = cryptotools.splitCosets(keywordLength, text)
focusedCoset = cosets[focused]

frequencies = cryptotools.frequency(focusedCoset)
percentageFrequencies = [(freq / textLength) for freq in frequencies]

# plot them in relation to equivilent english letter frequencies
plt.figure(1)
plot = plt.bar(alphabet, percentageFrequencies)

plt.figure(2)
plot2 = plt.bar(alphabet, cryptotools.ENG_LETTER_FREQ)

plt.show()