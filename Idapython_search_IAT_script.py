from idaapi import *
from idautils import *
from idc import *
import os
global Count

idaapi.autoWait()
Count = 0


f = open("result output path",'a')


def Get_xref_to():
    ea = LocByName("recv")
    for xref in XrefsTo(ea,0):
        xreffunc = GetFunctionName(xref.frm)
        ea=LocByName(xreffunc)
        f.write("\nxref to Sleep Func: %s  0x%x \n" % (xreffunc,ea))
        f.write(GetDisasm(xref.frm-1)) #Sleep Param
        
    ea = LocByName("internetreadfile")
    for xref in XrefsTo(ea,0):
        xreffunc = GetFunctionName(xref.frm)
        ea=LocByName(xreffunc)
        f.write("\nxref to WaitForSingleObject Func: %s  0x%x \n" % (xreffunc,ea))
        f.write(GetDisasm(xref.frm-2)) #Sleep Param
    



def py_cb(i, name, index): #Enumerate from imports ,needs three param
    global Count
    if not name:
        print("Fail to search API...")
    else:
        if name == "recv" or name=="internetreadfile": #API name
            lines=''.join("00%x  %s\n"%(i,name))
            f.write(lines)
        Count=Count+1  #Imported Func Count
    return True

def main():
    Num_dll = idaapi.get_import_module_qty() #return type: int

    for i in range(0,Num_dll):
        DLL_name = idaapi.get_import_module_name(i)
        if not DLL_name:
            f.write("Failed...")
        f.write("Searching IAT... => " + DLL_name + ".dll\n")
        enum_import_names(i,py_cb)
        if i+1 == int(Num_dll):
            f.write("The number of all Import funtions : %d\n" %Count)
        else:
            continue
    f.write("End of search...\n")
    Get_xref_to()
    f.write("\n******************************************\n")
    f.close()
    idc.Exit(0)

main()

