# WatRe Web

## Purpose
I used the WatRe app to remind myself to drink water but I did not check my phone enough. This program runs a .NET server and REST API to enable communication between my phone and my computer. A python script gets a status from the REST API every 5 minutes to check if the notifcation was sent. Once a true repsonse is recieved, the script will play a sound to remind the user to drink water/check their phone for the notification.

## Sound Queue Conditioning
As demonstrated by Ivan Pavlov's experiments with classical conditioning, I often feel a dry and thirsty mouth when the sound is heard.

## Execution on Startup
A .vbs (Virtual Basic script) contains the following command in the Windows startup folder. 

``` CreateObject("Wscript.Shell").Run "C:\Windows\System32\cmd.exe /k cd C:\DIRECTORY_OF_.NET_APP && dotnet run", 0, False ```

The folder can be found by using Win+r and typing ```shell:startup``` in the run prompt.


## Changes needed to run
Change IPV4_ADDRESS in Properties/launchSettings.json to own address.

Change IPV4_ADDRESS in Client/asynch.py to own address.

## Sound that plays 
<div>
 <video src='https://user-images.githubusercontent.com/52565263/155894444-8cad713b-175a-4dc4-b0b6-ef712be13716.mp4'/>
</div>
