from PythonDll import *

class instruct:
	InitTDA_1="FF1101050100"
	InitTDA_2="FF19010001"
	ColdReset_5V="FF1901010101"
	ColdReset_3V="FF1901010102"
	ColdReset_18V="FF1901010103"
	PPS_CT="FFFF000101"
	SEL_CT_30V="FF0100000121"
	SEL_CL="FF0100000102"

	Reset17="FF1801000100"
	FieldON_1="FF1801000101"
	FieldON_2="FF1102260102"
	FieldON_3="FF1102210106"
	FieldON_4="FF11021E0101"
	PPS_CL="FFFF000001"  #pps1:0000+DSI+DRI
	REQA_1="FF11021E0101"
	REQA_2="FF18010102"
	AntiColl="FF18010206"
	Select="FF18010301"
	RATS="FF18010401"



class FMReader:
	card=PyCard()
	ins=instruct()
	def GetReader(self):
		self.card.PyGetReader()

	def ConnectReader(self,ReaderID):
		self.card.PyConnectReader(ReaderID)
		

	def InitTDA(self):
		self.card.PyTransmitReader(self.ins.SEL_CT_30V)
		self.card.PyTransmitReader(self.ins.InitTDA_1)
		ret1=self.card.RespData
		self.card.PyTransmitReader(self.ins.InitTDA_2)
		ret2=self.card.RespData
		if ret1=='9000' and ret2=='9000' :
			print "InitTDA->  Succeed!"
		else:
			print "InitTDA->  Failed!"

	def ColdReset(self,Volt):
		if Volt=="5V":
			self.card.PyTransmitReader(self.ins.ColdReset_5V)
		else:
			if Volt=="1.8V":
				self.card.PyTransmitReader(self.ins.ColdReset_18V)
			else :
				self.card.PyTransmitReader(self.ins.ColdReset_3V)
		print 'ColdReset-> '+self.card.RespData


	def PpsCt(self,pps1):
		self.card.PyTransmitReader(self.ins.PPS_CT+pps1)
		print "PPS-> "+self.card.RespData


	def SendApduCt(self,apdu):
		self.card.PyTransmitReader(apdu)
		print apdu+"-> "+self.card.RespData

	def Reset17(self):
		self.card.PyTransmitReader(self.ins.SEL_CL)
		self.card.PyTransmitReader(self.ins.Reset17)
		print "Reset17-> "+self.card.RespData

	def FieldON(self):
		self.card.PyTransmitReader(self.ins.FieldON_1)
		ret1=self.card.RespData
		self.card.PyTransmitReader(self.ins.FieldON_2)
		ret2=self.card.RespData
		self.card.PyTransmitReader(self.ins.FieldON_3)
		ret3=self.card.RespData
		self.card.PyTransmitReader(self.ins.FieldON_4)
		ret4=self.card.RespData

		if ret1=="9000" and ret2=="9000" and ret3=="9000" and ret4=="9000":
			print "FieldON-> Succeed!"
		else :
			print "FieldON-> Failed!"


	def ReqA(self):
		self.card.PyTransmitReader(self.ins.REQA_1)
		ret1=self.card.RespData
		self.card.PyTransmitReader(self.ins.REQA_2)
		ret2=self.card.RespData
		if ret1=="9000":
			if ret2[-4:]=="9000":
				print "ReqA-> "+self.card.RespData
			else :
				print "ReqA-> Failed!"
		else:
			print "ReqA-> Failed!"

	def AntiColl(self):
		self.card.PyTransmitReader(self.ins.AntiColl)
		print "AntiColl-> "+self.card.RespData

	def Select(self):
		self.card.PyTransmitReader(self.ins.Select)
		print "Select-> "+self.card.RespData

	def Active(self):
		self.ReqA()
		self.AntiColl()
		self.Select()

	def Rats(self):
		self.card.PyTransmitReader(self.ins.RATS)
		print "RATS-> "+self.card.RespData

	def SendApduCL(self,apdu):
		self.card.PyTransmitReader(apdu)
		print apdu+"-> "+self.card.RespData

	def PpsCl(self,pps1):
		self.card.PyTransmitReader(self.ins.PPS_CL+pps1)
		print "PPS-> "+self.card.RespData		

	def InitCt(self,ReaderID):
		self.GetReader()
		self.ConnectReader(ReaderID)
		self.Reset17()
		self.InitTDA()
		self.ColdReset("3V")

	def InitCl(self,ReaderID):
		self.GetReader()
		self.ConnectReader(ReaderID)
		self.InitTDA()
		self.Reset17()
		self.FieldON()
		self.Active()
		self.Rats()




	def __del__(self):
		self.card.PyDisconnectReader()

#r=FMReader()
#r.InitCl(0)
#r.SendApduCL('0084000008')
#r.InitCt(0)
#r.SendApduCt('0084000008')