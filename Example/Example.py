from FMReader import *
rd=FMReader()
rd.InitCt(0)
rd.SendApduCt("0084000008")
rd.SendApduCt("0084000008")
rd.SendApduCt("0084000008")
rd.SendApduCt("0084000008")
rd.SendApduCt("0084000008")
rd.SendApduCt("0084000008")

print "*****************************************"
rd.InitCl(0)
rd.SendApduCt("0084000008")
rd.SendApduCt("0084000008")
rd.SendApduCt("0084000008")
rd.SendApduCt("0084000008")
rd.SendApduCt("0084000008")
rd.SendApduCt("0084000008")