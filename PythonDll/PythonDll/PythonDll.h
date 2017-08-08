#ifndef _PYTHONDLL_H
#define _PYTHONDLL_H

#define PythonDllAPI extern "C" __declspec(dllexport)
#include "WinScard.h"

PythonDllAPI int GetReaders(char* Readers);
PythonDllAPI int ConnectReader(char* Reader);
PythonDllAPI int TransmitReader(char* senddata,int slen,char* recedata,char * rlen);
PythonDllAPI int DisconnectReader();

extern SCARDCONTEXT hContext;
extern int ReaderCnt;
extern SCARDHANDLE hCardHandle;
extern char ReaderNames[0x80];



#endif