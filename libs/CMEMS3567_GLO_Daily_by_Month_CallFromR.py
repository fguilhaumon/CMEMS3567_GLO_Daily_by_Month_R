#************************Script to download Daily global-analysis-forecast-phys-001-002 month by month************************

import subprocess 
import datetime as dt 
import time 
import calendar 
import os 
# -- add fg
import sys
# --


# - - - - - - - - - - - - - - - - - - - 
# General Parameters 
# - - - - - - - - - - - - - - - - - - - 
# parameters in bold must 
# be modified by the user 
 
#Motu tools 
python=sys.argv[1] #"python"  #C:\Python27\ArcGISx6410.1\python.exe
print python

motu_cl = sys.argv[2] #"/home/franz/Dropbox/Me/ECOLOGIE/Coral_reefs/Nouvelle_Caledo/stage_Floriant/data_env_copernicus/motu-client-python-master/src/python/motu-client.py" 
print motu_cl

# Login Credentials - Motu Server and chosen Product/Dataset 
log_cmems='-u ' + sys.argv[3] #"-u lnerriere" 
print log_cmems
pwd_cmems='-p ' + sys.argv[4] # "-p 20152016" 
print pwd_cmems
 
motu_sc="-m http://nrtcmems.mercator-ocean.fr/mis-gateway-servlet/Motu" 
serv_id="-s http://purl.org/myocean/ontology/service/database#GLOBAL_ANALYSIS_FORECAST_PHY_001_024-TDS" 
dataset_id="-d global-analysis-forecast-phy-001-024" 
 
#Proxy Configuration  
proxy_flag = False #Please replace "False" by "True" if you use a proxy to connect to internet and fill in the below variables. 
proxy_server_url = "http://your_proxy_url.com" 
proxy_server_port = "port_number" 
proxy_user_login = "your_proxy_user_login" 
proxy_user_password = "your_proxy_user_password" 
 
# Date
print '#### DATES' 
yyyystart=int(sys.argv[5]) #2012
print yyyystart
mmstart=int(sys.argv[6]) #12
print mmstart
yyyyend=int(sys.argv[7]) #2016 
print yyyyend
mmend=int(sys.argv[8]) #12 
print mmend
hh=sys.argv[9] #" 12:00:00" 
print hh
dd=int(sys.argv[10]) #01 
print dd
 
# Area 
xmin='-x ' + sys.argv[11] #"-x -180" 
xmax='-X' + sys.argv[12] #"-X 179" 
ymin='-y ' + sys.argv[13] #"-y -80" 
ymax='-Y ' + sys.argv[14] #"-Y -79" 
zmin='-z ' + sys.argv[15] #"-z 0.49" 
zmax='-Z ' + sys.argv[16] #"-Z 0.50" 
 
# Variables 
st = '-v ' + sys.argv[17]
table_var_cmd= [st]  #["-v thetao"] 
table_data_type=[sys.argv[18],] #["TEMP_",] #There are four data type since we'll download four datasets 
 
# Output files 
out_path =  sys.argv[19] #"/home/franz/Dropbox/Me/ECOLOGIE/Coral_reefs/Nouvelle_Caledo/stage_Floriant/data_env_copernicus/downs/" #Make sure to end your path with "/" 
pre_name= sys.argv[20] #"CMEMS_GLO_001_024_" 



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#                     Main Program
#
#          Motu Client Call through Python Loop
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Be careful if you have to modify the lines below :-)
# CMEMS Central Service Desk will be happy to help you
# either via email (servicedesk.cmems@mercator-ocean.eu)
# or via the CMEMS Forum (http://bit.ly/1L1Iy5f)

# Counter
cpt = 0

# Flag to let the server clearing the buffer
buffer_flag = False
cmd_flag = False

# Proxy Configuration Part 2012

proxy_user = "--proxy-user " + proxy_user_login
proxy_pwd = "--proxy-pwd " + proxy_user_password
proxy_server = "--proxy-server " + proxy_server_url + ":" + proxy_server_port


# Error Handle on log file
try :
    os.remove(out_path + "ficlog.txt")
except OSError:
    print "Report Log File does not exist.\n"

# Error Handle on dates
if yyyystart>yyyyend :
    print "[ERROR] in [Date Parameters]"
    print """Please double check your date parameters, specifically the "yyyystart" which is currently greater than "yyyyend."""

# Other variable definitions
pre_fic_cmd = "-f "+ pre_name
out_cmd = "-o "+ out_path

#While_Loop in order to launch again only unsuccessful requests
while cpt<3 :
    #For_Loop in order to generate download requests for several datasets held in a product
    for var_cmd, datatype in zip(table_var_cmd, table_data_type):
        if buffer_flag:
            print "Little break to let the server clearing the buffer "
            print """Don't worry, there is nothing to do, the script will automatically resume as soon as the server is ok !\n"""
            time.sleep(15)
            buffer_flag = False
        #Date declaration
        date_start = dt.datetime(yyyystart,mmstart,dd,0,0)
        date_end = dt.datetime(yyyyend,mmend,dd,0,0)
        #While_Loop launch monthly requests of daily data until the last declared date
        while (date_start<=date_end):
            date_end_cmd = (dt.datetime(date_start.year, date_start.month,\
                            calendar.monthrange(date_start.year, date_start.month)[1]))
            date_cmd = ' -t \"' + date_start.strftime("%Y-%m-%d") + hh + '\"'\
                      +' -T \"' + date_end_cmd.strftime("%Y-%m-%d") + hh + '\"'
            fic_cmd = pre_fic_cmd + datatype + date_end_cmd.strftime("%Y-%m") + ".nc"
            ficout = pre_name + datatype + date_end_cmd.strftime("%Y-%m") + ".nc"
            print "####\n Processing request : %s \n####\n"%ficout
            if not os.path.exists(out_path + ficout) :
                if proxy_flag:
                    cmd = ' '.join([python, motu_cl, log_cmems, pwd_cmems,\
                                    motu_sc, serv_id, dataset_id,\
                                    xmin, xmax, ymin, ymax, zmin, zmax,\
                                    date_cmd,var_cmd,out_cmd,fic_cmd,\
                                    proxy_server, proxy_user, proxy_pwd])
                else:
                    cmd = ' '.join([python, motu_cl, log_cmems, pwd_cmems,\
                                    motu_sc, serv_id, dataset_id,\
                                    xmin, xmax, ymin, ymax, zmin, zmax,\
                                    date_cmd,var_cmd,out_cmd,fic_cmd])
                print "## COMMAND ##"
                print cmd
                cmd_flag = True
                stspop = subprocess.Popen(cmd, shell = True).wait()
                if stspop==0 :
                    print "Download : %s OK \n"%ficout
                    time.sleep(5) #5 seconds delay to let the server clearing the buffer
                else :
                    if cpt==2 :
                        f_log = open(out_path + "ficlog.txt", "a")
                        f_log.write("Error : %s NOK\n"%ficout)
                        print """Report Log File created. Please check it out and launch the script again to download unsuccessful request(s)."""
            else :
                print "Request : " + datatype + date_start.strftime("%Y-%m") \
                      + " has already been downloaded and saved in " + out_path + ficout + '\n'
            date_start = date_end_cmd + dt.timedelta(days=1)
        if cmd_flag:
            buffer_flag=True
            cmd_flag=False
    if not os.path.exists(out_path+"ficlog.txt"):
        print "There was no error \n \n"
        print "################# \n End of function \n#################"	   
        quit()
    else:
        print "## [ERROR] ##"
        print "/!\\ Some download requests failed. Please see the log file in "\
               + out_path + "ficlog.txt."
        print """/!\\ Recommended action : to relaunch your script in order to download unsuccessful requests."""
    cpt+=1

#***************End of Script to download global-analysis-forecast-phys-001-002 data month by month**************
