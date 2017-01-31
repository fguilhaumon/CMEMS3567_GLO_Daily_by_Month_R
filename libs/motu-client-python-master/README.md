# Motu Client Python Project
@author Project manager <rdedianous@cls.fr>  
@author Product owner <tjolibois@cls.fr>  
@author Scrum master, software architect <smarty@cls.fr>  
@author Quality assurance, continuous integration manager <bpirrotta@cls.fr> 

>How to read this file? 
Use a markdown reader: 
plugins [chrome](https://chrome.google.com/webstore/detail/markdown-preview/jmchmkecamhbiokiopfpnfgbidieafmd?utm_source=chrome-app-launcher-info-dialog) exists (Once installed in Chrome, open URL chrome://extensions/, and check "Markdown Preview"/Authorise access to file URL.), 
or for [firefox](https://addons.mozilla.org/fr/firefox/addon/markdown-viewer/)  (anchor tags do not work)
and also plugin for [notepadd++](https://github.com/Edditoria/markdown_npp_zenburn).

>Be careful: Markdown format has issue while rendering underscore "\_" character which can lead to bad variable name or path.


#Summary
* [Overview](#Overview)
* [Build](#Build)
* [Installation](#Installation)
* [Configuration](#Configuration)
* [Usage and options](#Usage)
* [Licence](#Licence)


#<a name="Overview">Overview</a>
Motu client "motu-client-python" is a python script used to connect to Motu HTTP server.  
This program can be integrated into a processing chain in order to automate the downloading of products via the Motu.
  
  
#<a name="Build">Build</a>  
From the root folder runs the Maven command:
```
mvn clean install -Dmaven.test.skip=true
[...]
[INFO] BUILD SUCCESS
[...]
```  

This creates two archives in the target folder:

* motu-client-python-$version-$buildTimestamp-src.tar.gz: Archive containing all the source code
* motu-client-python-$version-$buildTimestamp-bin.tar.gz: Archive ready to be installed



#<a name="Installation">Installation</a> 
You must use python version 2.7.X or later.  
This program is not compatible with Python 3.X versions.  
  
Deploy the archive in the directory of your choice.  
```  
tar xvzf motu-client-python-$version-$buildTimestamp-bin.tar.gz
```  
Create a [configuration file](#Configuration) to inform the user and password to use to connect to the CAS server.   


#<a name="Configuration">Configuration</a>  
The program parameters are contained in an ini file. This file is located in the following directory:  

* on __Unix__ platforms: $HOME/motu-client/motu-client-python.ini
* on __Windows__ platforms: %USERPROFILE%\motu-client/motu-client-python.ini
  
The expected structure of file is:  
``` 
[Main]  
user=john  
pwd=secret  
log_level=10  
proxy_server=proxy.domain.net:8080  
proxy_user=john  
proxy_pwd=secret  
motu=http://motu-ip-server:port/motu-web/Motu
product_id=dataset-psy2v3-pgs-med-myocean-bestestimate  
date_min=2010-11-08 12:00:00  
date_max=2010-11-10  
latitude_min=-75.0  
latitude_max=30.0  
longitude_min=20.0  
longitude_max=120.0  
depth_min=  
depth_max=  
variable=  
out_dir=./out_dir  
out_name=test.nc  
block_size=65535  
socket_timeout=  
``` 


#<a name="Usage">Usage</a>  
Starts the motu python client.  

```  
./motu-client.py  -h  
motu-client.py [options]
```  

__Options:__  

* __--version__             show program's version number and exit  
* __-h, --help__            show this help message and exit  
* __-q, --quiet__           prevent any output in stdout  
* __--verbose__             print information in stdout  
* __--noisy__               print more information (traces) in stdout  
* __-u USER, --user=USER__  the user name (string)  
* __-p PWD, --pwd=PWD__     the user password (string)  
* __--auth-mode=AUTH_MODE__  the authentication mode: [default: cas]  
  * __none__ for no authentication
  * __basic__ for basic authentication
  * __cas__ for Central Authentication Service  
* __--proxy-server=PROXY_SERVER__ the proxy server (url)  
* __--proxy-user=PROXY_USER__ the proxy user (string)  
* __--proxy-pwd=PROXY_PWD__ the proxy password (string)  
* __-m MOTU, --motu=MOTU__  the motu server to use (url)  
* __-s SERVICE_ID, --service-id=SERVICE_ID__ The service identifier (string)  
* __-d PRODUCT_ID, --product-id=PRODUCT_ID__ The product (data set) to download (string)  
* __-t DATE_MIN, --date-min=DATE_MIN__ The min date with optional hour resolution (string following format YYYY-MM-DD [HH:MM:SS])  
* __-T DATE_MAX, --date-max=DATE_MAX__ The max date with optional hour resolution (string following format YYYY-MM-DD  [HH:MM:SS ])  
* __-y LATITUDE_MIN, --latitude-min=LATITUDE_MIN__ The min latitude (float in the interval  [-90 ; 90 ])  
* __-Y LATITUDE_MAX, --latitude-max=LATITUDE_MAX__ The max latitude (float in the interval  [-90 ; 90 ])  
* __-x LONGITUDE_MIN, --longitude-min=LONGITUDE_MIN__ The min longitude (float in the interval [-180 ; 180 ])  
* __-X LONGITUDE_MAX, --longitude-max=LONGITUDE_MAX__ The max longitude (float in the interval  [-180 ; 180 ])  
* __-z DEPTH_MIN, --depth-min=DEPTH_MIN__ The min depth (float in the interval  [0 ; 2e31 ] or string 'Surface')  
* __-Z DEPTH_MAX, --depth-max=DEPTH_MAX__ The max depth (float in the interval  [0 ; 2e31 ] or string 'Surface')  
* __-v VARIABLE, --variable=VARIABLE__ The variable (list of strings)  
* __-S, --sync-mode__ Sets the download mode to synchronous (not recommended)  
* __-D, --describe-product__ It allows to have all updated information on a dataset. Output is in XML format  
* __-o OUT_DIR, --out-dir=OUT_DIR__ The output dir (string)  
* __-f OUT_NAME, --out-name=OUT_NAME__ The output file name (string)  
* __--block-size=BLOCK_SIZE__ The block used to download file (integer expressing bytes)  
* __--socket-timeout=SOCKET_TIMEOUT__ Set a timeout on blocking socket operations (float expressing seconds)  
* __--user-agent=USER_AGENT__ Set the identification string (user-agent) for HTTP requests. By default this value is 'Python-urllib/x.x' (where x.x is the version of the python interpreter)  
  
  
  

#<a name="Licence">Licence</a> 
This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.  
  
This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.  
  
You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.  
