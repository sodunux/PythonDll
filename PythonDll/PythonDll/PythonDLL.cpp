#include "PythonDll.h"

SCARDCONTEXT hContext;
int ReaderCnt;
SCARDHANDLE hCardHandle;
char ReaderNames[0x80];


PythonDllAPI int GetReaders(char* Readers)
{
	int lreturn;
	DWORD dwlen=0x80;
	int i,j;
	lreturn=SCardEstablishContext(SCARD_SCOPE_SYSTEM,NULL,NULL,&hContext);
	if(lreturn!=SCARD_S_SUCCESS) 
		return 1;

	lreturn=SCardListReaders(hContext,NULL,(LPTSTR)ReaderNames,&dwlen);
	if(lreturn!=SCARD_S_SUCCESS) 
		return 2;
	
	for(i=0,j=0;i<dwlen;i++)
	{
		Readers[i]=ReaderNames[i];
		if(ReaderNames[i]=='\0')
		{
			j++;
		}
				
	}
	ReaderCnt=j-1;
	return 0;
}




PythonDllAPI int ConnectReader(char* Reader)
{
	DWORD dwAP;
	DWORD ret;
	ret=SCardConnect(hContext,(LPTSTR)Reader,SCARD_SHARE_SHARED,SCARD_PROTOCOL_T0|SCARD_PROTOCOL_T1,&hCardHandle,&dwAP);
	if(ret!=SCARD_S_SUCCESS) 
		return 1;
	return 0;
}

PythonDllAPI int TransmitReader(char* senddata,int slen,char* recedata,char* rlen)
{
	unsigned char sendbuff[270],recebuff[270];
	DWORD sendlen=270,recelen=270;
	int ret,i;
	SCARD_IO_REQUEST g_rgSCardT1Pci;
	g_rgSCardT1Pci.dwProtocol=SCARD_PROTOCOL_T1;
	g_rgSCardT1Pci.cbPciLength=sizeof(SCARD_IO_REQUEST);
	
	sendlen=slen;
	for(i=0;i<sendlen;i++)
	{
		sendbuff[i]=senddata[i];
	}

	ret=SCardBeginTransaction(hCardHandle); 
	if(ret!=SCARD_S_SUCCESS) 
		return 1;
	ret=SCardTransmit(hCardHandle,&g_rgSCardT1Pci,sendbuff,sendlen,NULL,recebuff,&recelen);
	if((ret!=SCARD_S_SUCCESS)||recelen==0)
		return 2;
	ret=SCardEndTransaction(hCardHandle,SCARD_LEAVE_CARD);
	if(ret!=SCARD_S_SUCCESS) 
		return 3;
	for(i=0;i<recelen;i++)
		recedata[i]=recebuff[i];
	rlen[0]=recelen;
	return 0;
}

PythonDllAPI int DisconnectReader()
{
	DWORD ret;
	ret=SCardDisconnect(hCardHandle,SCARD_LEAVE_CARD);
	if(ret!=SCARD_S_SUCCESS) 
		return 1;
	ret=SCardReleaseContext(hContext);
	if(ret!=SCARD_S_SUCCESS)
		return 2;
	return 0;
}