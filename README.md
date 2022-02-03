# WatReWeb

Add 
Properties/launchSettings.json
and change "HOSTIP" to current system ip.
Run using ```dotnet run```
```
{
  "$schema": "https://json.schemastore.org/launchsettings.json",
  "iisSettings": {
    "windowsAuthentication": false,
    "anonymousAuthentication": true,
    "iisExpress": {
      "applicationUrl": "http://localhost:52284",
      "sslPort": 44301
    }
  },
  "profiles": {
    "WatReWeb": {
      "commandName": "Project",
      "dotnetRunMessages": true,
      "launchBrowser": true,
      "launchUrl": "swagger",
<<<<<<< HEAD:Properties/launchSettings.json
      "applicationUrl": "http://10.0.0.193:7238;http://localhost:5024",
=======
      "applicationUrl": "http://HOSTIP:7238;http://localhost:5024",
>>>>>>> 87e947f6cc5c9da5b86acf35af60b46115a09027:README.md
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      }
    },
    "IIS Express": {
      "commandName": "IISExpress",
      "launchBrowser": true,
      "launchUrl": "swagger",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      }
    }
  }
}

```
