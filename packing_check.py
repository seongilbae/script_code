#The packer/protector/tools section names/keywords
#ref http://www.hexacorn.com/blog/2016/12/15/pe-section-names-re-visited/
Pdata=""".aspack
.adata 
ASPack
.ASPack
.boom
.ccg
.charmve
BitArts
DAStub
!EPack
.ecode
.enigma1
.enigma2 
FSG!
.gentee
kkrunchy
lz32.dll
.mackt 
.MaskPE
MEW 
.mnbvcx1
.mnbvcx2
.MPRESS1
.MPRESS2
.neolite
.neolit
.nsp1
.nsp0
pebundle
PEBundle
PEC2TO
PECompact2
PEC2
pec
pec1
pec2
PEC2MO
PELOCKnt
.perplex
PESHiELD
.petite
.pinclie
ProCrypt
.RLPack
.rmnet
RCryptor
.RPCrypt 
.seau
.sforce3
.shrink1
.shrink2 
.shrink3
.spack
.svkp 
Themida
.Themida
.taz
.tsuarch
.tsustub
.packed
PEPACK!!
.Upack
.ByDwing
UPX0
UPX1
UPX2
UPX3
UPX!
.UPX0
.UPX1
.UPX2
.vmp0
.vmp1
.vmp2
VProtect
.winapi
WinLicen
_winzip_
.WWPACK
.WWP32
.yP
.y0da"""


import pefile
import os
import shutil
dir_file=[]
new_filename=[]
data =  Pdata.split('\n')
direct = 'your dir path'


files = os.listdir(direct)
for file in files:
    pe=pefile.PE('%s'%direct+'\\%s'%file)
    pe.parse_data_directories()
    for section in pe.sections:
        for i in range (len(data[1:-1])):
            if data[i] in str(section.Name):
                print("%s is packed with %s!!"%(file,data[i]))
                dir_file.append(file)


dir_file = list(set(dir_file))
print(dir_file)

f=open('your txt path packingfilelist.txt','w+')
f.write('\n'.join(dir_file))
f.close()

        
    

