from subprocess import Popen, CREATE_NEW_CONSOLE,PIPE,STDOUT
import subprocess
import time
from com.dtmilano.android.viewclient import ViewClient


class Adb:

        """Adb class"""

        def __init__(self):

                self.terminal='cmd'
                self.command='adb shell'
                self.command1=''
                self.dict_call_divert_on={'airtel':'**21*',
                'Vodafone IN':'**21*',
                'aircel':'345'}
                self.dict_call_divert_off={'airtel':'##21#',
                'Vodafone IN':'##21#',
                'aircel':'345'}
                self.dict_call_wait_on={'airtel':'*43#',
                'Vodafone IN':'*43#',
                'aircel':'345'}
                self.dict_call_wait_off={'airtel':'#43#',
                'Vodafone IN':'#43#',
                'aircel':'345'}
            

        def start_shell(self):
            print 'starting adb shell....'
            self.command=self.terminal+' '+'/k' +' '+ self.command
            process=Popen(self.command,creationflags=CREATE_NEW_CONSOLE)

        
        def send_command(self):
            print 'sending command....'
            procId = subprocess.Popen('adb -s ZY2235CQ26 shell', stdin = subprocess.PIPE)
            procId.communicate('am broadcast -a android.settings.AIRPLANE_MODE_SETTINGS\n input keyevent 19\n input keyevent 23\n input keyevent 4\n exit')
            
        def Get_operator(self,udid):
            print 'checking operator...'
            device_udid=udid
            print device_udid
            startshell_command= 'adb -s'+' '+device_udid+' '+'shell' + ' getprop gsm.sim.operator.alpha'
            print startshell_command
            procId = subprocess.Popen(startshell_command, stdout = subprocess.PIPE)
            #procId = subprocess.Popen(startshell_command, stdin = subprocess.PIPE, stdout=subprocess.PIPE).communicate('getprop gsm.sim.operator.alpha\n exit')[0]
            procId=procId.communicate()[0]
            procId= str(procId)
            print procId
            return procId.strip()
            

        def Get_call_divert_on_number(self,mobile_no,udid):
            print mobile_no
            print udid
            operator=self.Get_operator(udid)
            print operator
            if operator in self.dict_call_divert_on:
               print operator +' is in the list'
               number = self.dict_call_divert_on.get(operator)
               print 'call divert on number is '+ number + mobile_no + '#'
               return str(number + mobile_no + '#')

        def Get_call_divert_off_number(self,mobile_no,udid):
            print mobile_no
            print udid
            operator=self.Get_operator(udid)
            print operator
            if operator in self.dict_call_divert_off:
               print operator +' is in the list'
               number = self.dict_call_divert_off.get(operator)
               print 'call divert off number is '+ number
               return str(number)

        def Get_call_wait_on_number(self,udid):
            operator=self.Get_operator(udid)
            print operator
            if operator in self.dict_call_wait_on:
               print operator +' is in the list'
               number = self.dict_call_wait_on.get(operator)
               print 'call wait on number is '+ number 
               return str(number)

        def Get_call_wait_off_number(self,udid):
            operator=self.Get_operator(udid)
            print operator
            if operator in self.dict_call_wait_off:
               print operator +' is in the list'
               number = self.dict_call_wait_off.get(operator)
               print 'call wait off number is '+ number 
               return str(number)
            
        def Open_call_forwarding_settings(self,udid):
            device_udid=udid
            print device_udid
            start_shell_command= 'adb -s'+' '+device_udid+' '+'shell'+' '+'am start -n com.android.phone/.GsmUmtsCallForwardOptions'
            procId = subprocess.Popen(start_shell_command, stdout = subprocess.PIPE)
            time.sleep(12)
            

        def Call(self,udid,number_to_dial):
            procId = subprocess.Popen('adb -s ZY2235CQ26 shell', stdin = subprocess.PIPE)
            command= str('am start -a android.intent.action.CALL -d tel:'+ number_to_dial)
            procId.communicate(command)

        def End_call(self,udid):
            print 'ending call...'
            device_udid=udid
            command= 'adb -s'+' '+device_udid+' '+'shell input keyevent KEYCODE_ENDCALL'
            print command
            procId = subprocess.Popen(command)

        def Answer_call(self,udid):
            print 'answering call...'
            device_udid=udid
            command= 'adb -s'+' '+device_udid+' '+'shell input keyevent KEYCODE_CALL'
            print command
            procId = subprocess.Popen(command)

        def reboot_device(self,deviceid):
            print 'rebooting device...'
            device_udid=deviceid
            startshell_command= 'adb -s'+' '+device_udid+' '+'reboot'
            procId = subprocess.Popen(startshell_command)

        def switchoff_device(self,deviceid):
            print 'shutdown device...'
            device_udid=deviceid
            startshell_command= 'adb -s'+' '+device_udid+' '+'reboot -p'
            procId = subprocess.Popen(startshell_command)
         
        def getting_list_of_devices(self):
            print 'getting list of  devices...'
            import re
            import string
            startshell_command= 'adb devices'
            procId = subprocess.Popen(startshell_command,stdout=subprocess.PIPE)
            device_list=procId.communicate()[0]
            print ''.join(i for i in device_list if i in string.ascii_letters+'0123456789')

        def launch_airplane_mode_settings(self,deviceid):
            print 'Launching airplane mode page.....'
            print deviceid
            device_udid=deviceid
            startshell_command= 'adb -s'+' '+device_udid+' '+'shell am start -a android.settings.AIRPLANE_MODE_SETTINGS'
            procId = subprocess.Popen(startshell_command)


        def get_android_version_number(self,deviceid):
            print 'getting the android version..........'
            device_udid=deviceid
            startshell_command= 'adb -s'+' '+device_udid+' '+'shell getprop ro.build.version.release'
            procId = subprocess.Popen(startshell_command,stdout=subprocess.PIPE)
            to_ver= procId.communicate()[0].strip().strip('\r\n')
            to_ver=float(str(to_ver)[0:3])
            print type(to_ver)
            print to_ver
            return to_ver

        def Launch_wifi_settings(self,deviceid):
            print 'Launching wifi settings.....'
            print deviceid
            device_udid=deviceid
            command= 'adb -s'+' '+device_udid+' '+'shell am start -n com.android.settings/.wifi.WifiSettings'
            procId = subprocess.Popen(command)

        def Close_settings(self,deviceid):
            print 'closing settings.....'
            print deviceid
            device_udid=deviceid
            command= 'adb -s'+' '+device_udid+' '+'shell am force-stop com.android.settings'
            procId = subprocess.Popen(command)

        def Compose_SMS(self,udid,number,sms_body):
            print 'creating sms...'
            device_udid=udid
            command= 'adb -s'+' '+device_udid+' '+'shell am start -a android.intent.action.SENDTO -d sms:'+number+' '+'--es sms_body '+"'"+sms_body+"'"+' --ez exit_on_sent true'
            print command
            procId = subprocess.Popen(command)

        def Launch_Network_settings(self,udid):
            print 'Launching network settings.....'
            #switch from 3g to 4g or 2g 
            print udid
            device_udid=udid
            command= 'adb -s'+' '+device_udid+' '+'shell am start -n com.android.phone/.MobileNetworkSettings'
            procId = subprocess.Popen(command)

        def Bring_to_homescreen(self,udid):
            print 'bringing phone to home screen...'
            device_udid=udid
            command= 'adb -s'+' '+device_udid+' '+'shell input keyevent KEYCODE_HOME'
            print command
            procId = subprocess.Popen(command)

        def Check_airplane_mode_status(self,udid):
            print 'checking airplane mode status...'
            device_udid=udid
            command= 'adb -s'+' '+device_udid+' '+'shell settings get global airplane_mode_on'
            out = subprocess.Popen(command, stdout = subprocess.PIPE)
            out=out.communicate()[0]
            print out
            return out.strip()
            #returns 0 for off and 1 for on

        def wake_device(self,udid):
            print 'waking up device...'
            device_udid=udid
            command= 'adb -s'+' '+device_udid+' '+'shell input keyevent WAKEUP'
            print command
            procId = subprocess.Popen(command)

        def unlock_device_old(self,udid):
            print 'hello'+ udid
            self.device_udid=udid

            print self.device_udid
            #device, serialno = ViewClient.connectToDeviceOrExit(5,self.device_udid)
            device, serialno = ViewClient.connectToDeviceOrExit(serialno=self.device_udid)
            if device.isLocked():
               device.wake()
               device.unlock()

            else :
                device.wake()
                device.unlock()

        def unlock_device(self,udid,pin):
            pin= map(int, str(pin))
            device, serialno = ViewClient.connectToDeviceOrExit()
            vc = ViewClient(device=device, serialno=udid)
            if device.isLocked():
               print 'device with serial no '+udid+ ' is locked'
               device.wake()
               vc.dump()
               device.shell('input swipe 357 1227 357 680')
               vc.dump()
               for item in pin:
                   item= str(item)
                   key = vc.findViewWithText(item)
                   if key:
                       key.touch()
                   else:
                       print 'key not found or locator is incorrect'
               enter= vc.findViewById('com.android.systemui:id/key_enter')
               if enter:
                   enter.touch()
               else:
                  print 'key not found or locator is incorrect'
            else:
                print 'device with serial no '+udid+ ' is unlocked' 

        def Switch_network_mode(self,udid,mode): #dial to check *#*#4636#*#*
            if mode == '3G':
                mode_value = 0
            elif mode == '2G':
                mode_value = 1
            elif mode == '4G':
                mode_value = 2
            else:
                mode_value = 2
            print 'switching network mode to '+str(mode_value)+ ' on '+udid
            cmd1= 'adb -s'+' '+udid+' '+'shell settings put global preferred_network_mode '+str(mode_value)
            cmd2= 'adb -s'+' '+udid+' '+'shell settings put global preferred_network_mode2 '+str(mode_value)
            print cmd1
            print cmd2
            procId = subprocess.Popen(cmd1)
            procId = subprocess.Popen(cmd2)  

        def Check_call_state(self,udid): 
            print 'checking call state...'
            device_udid=udid
            p1= Popen(['adb', '-s', device_udid, 'shell', 'dumpsys', 'telephony.registry'],stdout=PIPE)
            p2 = Popen(["findstr", "mCallState"], stdin=p1.stdout, stdout=PIPE)
            p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
            output = p2.communicate()[0]
            out= output.splitlines()[0] + '\n'
            print out
            if 'mCallState=0' in out:
                print 'phone is idle'
                return 'idle'
            elif 'mCallState=1' in out:
                print 'there is an incoming call'
                return 'incoming'
            elif 'mCallState=2' in out:
                print 'there is an ongoing call'
                return 'ongoing'

        
                   
#test= Adb()
#udid= 'D1AGAD57A1407259'
#test.Check_call_state(udid)







