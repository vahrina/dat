---
date: '2026-10-15'
draft: false
title: krypton-3
description: \"frequently\" pissing me off
weight: 4
ShowToc: false
---

> Well done.  You've moved past an easy substitution cipher.
>
> Hopefully you just encrypted the alphabet a plaintext
> to fully expose the key in one swoop.
>
> The main weakness of a simple substitution cipher is
> repeated use of a simple key.  In the previous exercise
> you were able to introduce arbitrary plaintext to expose
> the key.  In this example, the cipher mechanism is not
> available to you, the attacker.
>
> However, you have been lucky.  You have intercepted more
> than one message.  The password to the next level is found
> in the file 'krypton4'.  You have also found 3 other files.
> (found1, found2, found3)
>
> You know the following important details:
>
> - The message plaintexts are in English (*** very important)
> - They were produced from the same key (*** even better!)
>
>
> Enjoy.

---

## explanation

as the title suggests, i absolutely despise [frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis) in every possible way & will refrain from ever doing one myself ever again since university. luckily, there are more than enough tools to help with this - f.e. [dCode.fr](https://www.dcode.fr/en)

> yes, i know using a tool sucks, but i seriously don't have the time for this bs. although the analysis itself is fun to explore, shoot me in the head if you ever see me manually deciphering a block of text ever again

the 3 intercepted pieces go as follows, found{1,2,3}:

```txt
> found1
CGZNL YJBEN QYDLQ ZQSUQ NZCYD SNQVU BFGBK GQUQZ QSUQN UZCYD SNJDS UDCXJ ZCYDS NZQSU QNUZB WSBNZ QSUQN UDCXJ CUBGS BXJDS UCTYV SUJQG WTBUJ KCWSV LFGBK GSGZN LYJCB GJSZD GCHMS UCJCU QJLYS BXUMA UJCJM JCBGZ CYDSN CGKDC ZDSQZ DVSJJ SNCGJ DSYVQ CGJSO JCUNS YVQZS WALQV SJJSN UBTSX COSWG MTASN BXYBU CJCBG UWBKG JDSQV YDQAS JXBNS OQTYV SKCJD QUDCX JBXQK BMVWA SNSYV QZSWA LWAKB MVWAS ZBTSS QGWUB BGJDS TSJDB WCUGQ TSWQX JSNRM VCMUZ QSUQN KDBMU SWCJJ BZBTT MGCZQ JSKCJ DDCUE SGSNQ VUJDS SGZNL YJCBG UJSYY SNXBN TSWAL QZQSU QNZCY DSNCU BXJSG CGZBN YBNQJ SWQUY QNJBX TBNSZ BTYVS OUZDS TSUUM ZDQUJ DSICE SGNSZ CYDSN QGWUJ CVVDQ UTBWS NGQYY VCZQJ CBGCG JDSNB JULUJ STQUK CJDQV VUCGE VSQVY DQASJ UMAUJ CJMJC BGZCY DSNUJ DSZQS UQNZC YDSNC USQUC VLANB FSGQG WCGYN QZJCZ SBXXS NUSUU SGJCQ VVLGB ZBTTM GCZQJ CBGUS ZMNCJ LUDQF SUYSQ NSYNB WMZSW TBUJB XDCUF GBKGK BNFAS JKSSG QGWDC USQNV LYVQL UKSNS TQCGV LZBTS WCSUQ GWDCU JBNCS UESGN SUDSN QCUSW JBJDS YSQFB XUBYD CUJCZ QJCBG QGWQN JCUJN LALJD SSGWB XJDSU COJSS GJDZS GJMNL GSOJD SKNBJ STQCG VLJNQ ESWCS UMGJC VQABM JCGZV MWCGE DQTVS JFCGE VSQNQ GWTQZ ASJDZ BGUCW SNSWU BTSBX JDSXC GSUJS OQTYV SUCGJ DSSGE VCUDV QGEMQ ESCGD CUVQU JYDQU SDSKN BJSJN QECZB TSWCS UQVUB FGBKG QUNBT QGZSU QGWZB VVQAB NQJSW KCJDB JDSNY VQLKN CEDJU TQGLB XDCUY VQLUK SNSYM AVCUD SWCGS WCJCB GUBXI QNLCG EHMQV CJLQG WQZZM NQZLW MNCGE DCUVC XSJCT SQGWC GJKBB XDCUX BNTSN JDSQJ NCZQV ZBVVS QEMSU YMAVC UDSWJ DSXCN UJXBV CBQZB VVSZJ SWSWC JCBGB XDCUW NQTQJ CZKBN FUJDQ JCGZV MWSWQ VVAMJ JKBBX JDSYV QLUGB KNSZB EGCUS WQUUD QFSUY SQNSU

> found2
QVJDB MEDGB QJJSG WQGZS NSZBN WUXBN JDSYS NCBWU MNICI STBUJ ACBEN QYDSN UQENS SJDQJ UDQFS UYSQN SKQUS WMZQJ SWQJJ DSFCG EUGSK UZDBB VCGUJ NQJXB NWQXN SSUZD BBVZD QNJSN SWCGQ ABMJQ HMQNJ SNBXQ TCVSX NBTDC UDBTS ENQTT QNUZD BBVUI QNCSW CGHMQ VCJLW MNCGE JDSSV CPQAS JDQGS NQAMJ JDSZM NNCZM VMTKQ UWCZJ QJSWA LVQKJ DNBME DBMJS GEVQG WQGWJ DSUZD BBVKB MVWDQ ISYNB ICWSW QGCGJ SGUCI SSWMZ QJCBG CGVQJ CGENQ TTQNQ GWJDS ZVQUU CZUQJ JDSQE SBXUD QFSUY SQNST QNNCS WJDSL SQNBV WQGGS DQJDQ KQLJD SZBGU CUJBN LZBMN JBXJD SWCBZ SUSBX KBNZS UJSNC UUMSW QTQNN CQESV CZSGZ SBGGB ISTAS NJKBB XDQJD QKQLU GSCED ABMNU YBUJS WABGW UJDSG SOJWQ LQUUM NSJLJ DQJJD SNSKS NSGBC TYSWC TSGJU JBJDS TQNNC QESJD SZBMY VSTQL DQISQ NNQGE SWJDS ZSNST BGLCG UBTSD QUJSU CGZSJ DSKBN ZSUJS NZDQG ZSVVB NQVVB KSWJD STQNN CQESA QGGUJ BASNS QWBGZ SCGUJ SQWBX JDSMU MQVJD NSSJC TSUQG GSUYN SEGQG ZLZBM VWDQI SASSG JDSNS QUBGX BNJDC UUCOT BGJDU QXJSN JDSTQ NNCQE SUDSE QISAC NJDJB QWQME DJSNU MUQGG QKDBK QUAQY JCUSW BGTQL JKCGU UBGDQ TGSJQ GWWQM EDJSN RMWCJ DXBVV BKSWQ VTBUJ JKBLS QNUVQ JSNQG WKSNS AQYJC USWBG XSANM QNLDQ TGSJW CSWBX MGFGB KGZQM USUQJ JDSQE SBXQG WKQUA MNCSW BGQME MUJQX JSNJD SACNJ DBXJD SJKCG UJDSN SQNSX SKDCU JBNCZ QVJNQ ZSUBX UDQFS UYSQN SMGJC VDSCU TSGJC BGSWQ UYQNJ BXJDS VBGWB GJDSQ JNSUZ SGSCG ASZQM USBXJ DCUEQ YUZDB VQNUN SXSNJ BJDSL SQNUA SJKSS GQGWQ UUDQF SUYSQ NSUVB UJLSQ NUACB ENQYD SNUQJ JSTYJ CGEJB QZZBM GJXBN JDCUY SNCBW DQISN SYBNJ SWTQG LQYBZ NLYDQ VUJBN CSUGC ZDBVQ UNBKS UDQFS UYSQN SUXCN UJACB ENQYD SNNSZ BMGJS WQUJN QJXBN WVSES GWJDQ JUDQF SUYSQ NSXVS WJDSJ BKGXB NVBGW BGJBS UZQYS YNBUS ZMJCB GXBNW SSNYB QZDCG EQGBJ DSNSC EDJSS GJDZS GJMNL UJBNL DQUUD QFSUY SQNSU JQNJC GEDCU JDSQJ NCZQV ZQNSS NTCGW CGEJD SDBNU SUBXJ DSQJN SYQJN BGUCG VBGWB GRBDG QMANS LNSYB NJSWJ DQJUD QFSUY SQNSD QWASS GQZBM GJNLU ZDBBV TQUJS NUBTS JKSGJ CSJDZ SGJMN LUZDB VQNUD QISUM EESUJ SWJDQ JUDQF SUYSQ NSTQL DQISA SSGST YVBLS WQUQU ZDBBV TQUJS NALQV SOQGW SNDBE DJBGB XVQGZ QUDCN SQZQJ DBVCZ VQGWB KGSNK DBGQT SWQZS NJQCG KCVVC QTUDQ FSUDQ XJSCG DCUKC VVGBS ICWSG ZSUMA UJQGJ CQJSU UMZDU JBNCS UBJDS NJDQG DSQNU QLZBV VSZJS WQXJS NDCUW SQJD

> found3
DSNSM YBGVS ENQGW QNBUS KCJDQ ENQIS QGWUJ QJSVL QCNQG WANBM EDJTS JDSAS SJVSX NBTQE VQUUZ QUSCG KDCZD CJKQU SGZVB USWCJ KQUQA SQMJC XMVUZ QNQAQ SMUQG WQJJD QJJCT SMGFG BKGJB GQJMN QVCUJ UBXZB MNUSQ ENSQJ YNCPS CGQUZ CSGJC XCZYB CGJBX ICSKJ DSNSK SNSJK BNBMG WAVQZ FUYBJ UGSQN BGSSO JNSTC JLBXJ DSAQZ FQGWQ VBGEB GSGSQ NJDSB JDSNJ DSUZQ VSUKS NSSOZ SSWCG EVLDQ NWQGW EVBUU LKCJD QVVJD SQYYS QNQGZ SBXAM NGCUD SWEBV WJDSK SCEDJ BXJDS CGUSZ JKQUI SNLNS TQNFQ AVSQG WJQFC GEQVV JDCGE UCGJB ZBGUC WSNQJ CBGCZ BMVWD QNWVL AVQTS RMYCJ SNXBN DCUBY CGCBG NSUYS ZJCGE CJ
```

because the wall of text is written in 4-grams, it'd be a pain to figure out how often a certain n-gram repeats. obviously, this can be analysed & counted manually, but did you really think i would sit all day here for this??

go ahead & input that into [dCode.fr/frequency-analysis](https://www.dcode.fr/frequency-analysis), we can tweak the settings, e.g. "Suggest an alphabetic transcription of n-grams" on "Each character separately", which contains "Letters (a-z) only" and out comes:

```txt
> found1
INCRY PTOGR APHYA CAESA RCIPH ERALS OKNOW NASAC AESAR SCIPH ERTHE SHIFT CIPHE RCAES ARSCO DEORC AESAR SHIFT ISONE OFTHE SIMPL ESTAN DMOST WIDEL YKNOW NENCR YPTIO NTECH NIQUE SITIS ATYPE OFSUB STITU TIONC IPHER INWHI CHEAC HLETT ERINT HEPLA INTEX TISRE PLACE DBYAL ETTER SOMEF IXEDN UMBER OFPOS ITION SDOWN THEAL PHABE TFORE XAMPL EWITH ASHIF TOFAW OULDB EREPL ACEDB YDBWO ULDBE COMEE ANDSO ONTHE METHO DISNA MEDAF TERJU LIUSC AESAR WHOUS EDITT OCOMM UNICA TEWIT HHISG ENERA LSTHE ENCRY PTION STEPP ERFOR MEDBY ACAES ARCIP HERIS OFTEN INCOR PORAT EDASP ARTOF MOREC OMPLE XSCHE MESSU CHAST HEVIG ENREC IPHER ANDST ILLHA SMODE RNAPP LICAT IONIN THERO TSYST EMASW ITHAL LSING LEALP HABET SUBST ITUTI ONCIP HERST HECAE SARCI PHERI SEASI LYBRO KENAN DINPR ACTIC EOFFE RSESS ENTIA LLYNO COMMU NICAT IONSE CURIT YSHAK ESPEA REPRO DUCED MOSTO FHISK NOWNW ORKBE TWEEN ANDHI SEARL YPLAY SWERE MAINL YCOME DIESA NDHIS TORIE SGENR ESHER AISED TOTHE PEAKO FSOPH ISTIC ATION ANDAR TISTR YBYTH EENDO FTHES IXTEE NTHCE NTURY NEXTH EWROT EMAIN LYTRA GEDIE SUNTI LABOU TINCL UDING HAMLE TKING LEARA NDMAC BETHC ONSID EREDS OMEOF THEFI NESTE XAMPL ESINT HEENG LISHL ANGUA GEINH ISLAS TPHAS EHEWR OTETR AGICO MEDIE SALSO KNOWN ASROM ANCES ANDCO LLABO RATED WITHO THERP LAYWR IGHTS MANYO FHISP LAYSW EREPU BLISH EDINE DITIO NSOFV ARYIN GQUAL ITYAN DACCU RACYD URING HISLI FETIM EANDI NTWOO FHISF ORMER THEAT RICAL COLLE AGUES PUBLI SHEDT HEFIR STFOL IOACO LLECT EDEDI TIONO FHISD RAMAT ICWOR KSTHA TINCL UDEDA LLBUT TWOOF THEPL AYSNO WRECO GNISE DASSH AKESP EARES

> found2
ALTHO UGHNO ATTEN DANCE RECOR DSFOR THEPE RIODS URVIV EMOST BIOGR APHER SAGRE ETHAT SHAKE SPEAR EWASE DUCAT EDATT HEKIN GSNEW SCHOO LINST RATFO RDAFR EESCH OOLCH ARTER EDINA BOUTA QUART EROFA MILEF ROMHI SHOME GRAMM ARSCH OOLSV ARIED INQUA LITYD URING THEEL IXABE THANE RABUT THECU RRICU LUMWA SDICT ATEDB YLAWT HROUG HOUTE NGLAN DANDT HESCH OOLWO ULDHA VEPRO VIDED ANINT ENSIV EEDUC ATION INLAT INGRA MMARA NDTHE CLASS ICSAT THEAG EOFSH AKESP EAREM ARRIE DTHEY EAROL DANNE HATHA WAYTH ECONS ISTOR YCOUR TOFTH EDIOC ESEOF WORCE STERI SSUED AMARR IAGEL ICENC EONNO VEMBE RTWOO FHATH AWAYS NEIGH BOURS POSTE DBOND STHEN EZTDA YASSU RETYT HATTH EREWE RENOI MPEDI MENTS TOTHE MARRI AGETH ECOUP LEMAY HAVEA RRANG EDTHE CEREM ONYIN SOMEH ASTES INCET HEWOR CESTE RCHAN CELLO RALLO WEDTH EMARR IAGEB ANNST OBERE ADONC EINST EADOF THEUS UALTH REETI MESAN NESPR EGNAN CYCOU LDHAV EBEEN THERE ASONF ORTHI SSIZM ONTHS AFTER THEMA RRIAG ESHEG AVEBI RTHTO ADAUG HTERS USANN AWHOW ASBAP TISED ONMAY TWINS SONHA MNETA NDDAU GHTER JUDIT HFOLL OWEDA LMOST TWOYE ARSLA TERAN DWERE BAPTI SEDON FEBRU ARYHA MNETD IEDOF UNKNO WNCAU SESAT THEAG EOFAN DWASB URIED ONAUG USTAF TERTH EBIRT HOFTH ETWIN STHER EAREF EWHIS TORIC ALTRA CESOF SHAKE SPEAR EUNTI LHEIS MENTI ONEDA SPART OFTHE LONDO NTHEA TRESC ENEIN BECAU SEOFT HISGA PSCHO LARSR EFERT OTHEY EARSB ETWEE NANDA SSHAK ESPEA RESLO STYEA RSBIO GRAPH ERSAT TEMPT INGTO ACCOU NTFOR THISP ERIOD HAVER EPORT EDMAN YAPOC RYPHA LSTOR IESNI CHOLA SROWE SHAKE SPEAR ESFIR STBIO GRAPH ERREC OUNTE DASTR ATFOR DLEGE NDTHA TSHAK ESPEA REFLE DTHET OWNFO RLOND ONTOE SCAPE PROSE CUTIO NFORD EERPO ACHIN GANOT HEREI GHTEE NTHCE NTURY STORY HASSH AKESP EARES TARTI NGHIS THEAT RICAL CAREE RMIND INGTH EHORS ESOFT HEATR EPATR ONSIN LONDO NJOHN AUBRE YREPO RTEDT HATSH AKESP EAREH ADBEE NACOU NTRYS CHOOL MASTE RSOME TWENT IETHC ENTUR YSCHO LARSH AVESU GGEST EDTHA TSHAK ESPEA REMAY HAVEB EENEM PLOYE DASAS CHOOL MASTE RBYAL EZAND ERHOG HTONO FLANC ASHIR EACAT HOLIC LANDO WNERW HONAM EDACE RTAIN WILLI AMSHA KESHA FTEIN HISWI LLNOE VIDEN CESUB STANT IATES SUCHS TORIE SOTHE RTHAN HEARS AYCOL LECTE DAFTE RHISD EATH

> found3
HEREU PONLE GRAND AROSE WITHA GRAVE ANDST ATELY AIRAN DBROU GHTME THEBE ETLEF ROMAG LASSC ASEIN WHICH ITWAS ENCLO SEDIT WASAB EAUTI FULSC ARABA EUSAN DATTH ATTIM EUNKN OWNTO NATUR ALIST SOFCO URSEA GREAT PRIZE INASC IENTI FICPO INTOF VIEWT HEREW ERETW OROUN DBLAC KSPOT SNEAR ONEEX TREMI TYOFT HEBAC KANDA LONGO NENEA RTHEO THERT HESCA LESWE REEXC EEDIN GLYHA RDAND GLOSS YWITH ALLTH EAPPE ARANC EOFBU RNISH EDGOL DTHEW EIGHT OFTHE INSEC TWASV ERYRE MARKA BLEAN DTAKI NGALL THING SINTO CONSI DERAT IONIC OULDH ARDLY BLAME JUPIT ERFOR HISOP INION RESPE CTING IT
```

<details>
  <summary>letting your preferred tin can reformat it..</summary>

```txt
> found1
in cryptography, a caesar cipher, also known as caesar’s cipher, the shift cipher, caesar’s code or caesar shift, is one of the simplest and most widely known encryption techniques. it is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. for example, with a shift of [#], a would be replaced by d, b would become e, and so on. the method is named after julius caesar, who used it to communicate with his generals. the encryption step performed by a caesar cipher is often incorporated as part of more complex schemes, such as the vigenère cipher, and still has modern application in the rot[#] system. as with all single-alphabet substitution ciphers, the caesar cipher is easily broken and in practice offers essentially no communication security.

shakespeare produced most of his known work between [#] and [#]. his early plays were mainly comedies and histories, genres he raised to the peak of sophistication and artistry by the end of the sixteenth century. next he wrote mainly tragedies until about [#], including hamlet, king lear, and macbeth, considered some of the finest examples in the english language. in his last phase, he wrote tragicomedies, also known as romances, and collaborated with other playwrights. many of his plays were published in editions of varying quality and accuracy during his lifetime, and in [#], two of his former theatrical colleagues published the first folio, a collected edition of his dramatic works that included all but two of the plays now recognised as shakespeare’s.

> found2
although no attendance records for the period survive, most biographers agree that shakespeare was educated at the king’s new school in stratford, a free school chartered in about [#], a quarter of a mile from his home. grammar schools varied in quality during the elizabethan era, but the curriculum was dictated by law throughout england, and the school would have provided an intensive education in latin grammar and the classics. at the age of [#], shakespeare married the [#]-year-old anne hathaway. the consistory court of the diocese of worcester issued a marriage licence on [#] november. two of hathaway’s neighbours posted bonds the next day assuring that there were no impediments to the marriage. the couple may have arranged the ceremony in some haste, since the worcester chancellor allowed the marriage banns to be read once instead of the usual three times, and anne’s pregnancy could have been the reason for this. six months after the marriage she gave birth to a daughter, susanna, who was baptised on [#] may. twins, son hamnet and daughter judith, followed almost two years later and were baptised on [#] february. hamnet died of unknown causes at the age of [#] and was buried on [#] august.

after the birth of the twins, there are few historical traces of shakespeare until he is mentioned as part of the london theatre scene in [#]. because of this gap, scholars refer to the years between [#] and [#] as shakespeare’s “lost years”. biographers attempting to account for this period have reported many apocryphal stories. nicholas rowe, shakespeare’s first biographer, recounted a stratford legend that shakespeare fled the town for london to escape prosecution for deer poaching. another eighteenth-century story has shakespeare starting his theatrical career minding the horses of theatre patrons in london. john aubrey reported that shakespeare had been a country schoolmaster. some twentieth-century scholars have suggested that shakespeare may have been employed as a schoolmaster by alexander hoghton of lancashire, a catholic landowner who named a certain william shakeshafte in his will. no evidence substantiates such stories other than hearsay collected after his death.

> found3
here upon legrand arose with a grave and stately air, and brought me the beetle from a glass case in which it was enclosed. it was a beautiful scarabaeus, and, at that time, unknown to naturalists — of course a great prize in a scientific point of view. there were two round black spots near one extremity of the back, and a long one near the other. the scales were exceedingly hard and glossy, with all the appearance of burnished gold. the weight of the insect was very remarkable, and, taking all things into consideration, i could hardly blame jupiter for his opinion respecting it.
```

</details>

because the same key was used for all messages, we can derive the key to decrypt `krypton4` now

```txt
qazwsxedcrfvtgbyhnujmikolp
vvvvvvvvvvvvvvvvvvvvvvvvvv
abcdefghijklmnopqrstuvwxyz

KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS
vvvvv vvvvv vvvvv vvvvv vvvvv vvvvv vvvvv
WELLD ONETH ELEVE LFOUR PASSW ORDIS BRUTE

> WELL DONE THE LEVEL FOUR PASSWORD IS BRUTE
```
