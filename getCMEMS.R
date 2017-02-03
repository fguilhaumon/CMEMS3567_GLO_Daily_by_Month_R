################################################
#
# R wrapper for CMEMS3567_GLO_Daily_by_Month.py
#
# francois.guilhaumon@ird.fr
################################################

getCMEMS <- function(scriptPath="libs/CMEMS3567_GLO_Daily_by_Month_CallFromR.py",
	         python = "python",  #path to python executable
	         motu_cl = "libs/motu-client-python-master/src/python/motu-client.py", #path to 'motu-client.py' (https://github.com/clstoulouse/motu-client-python),
	         # Login Credentials
	         log_cmems="lnerriere",   
	         pwd_cmems="20152016", 
	         # Motu Server and chosen Product/Dataset (not matched, DO NOT TOUCH)
	         #motu_sc="-m http://nrtcmems.mercator-ocean.fr/mis-gateway-servlet/Motu",
	         #serv_id="-s http://purl.org/myocean/ontology/service/database#GLOBAL_ANALYSIS_FORECAST_PHY_001_024-TDS",
	         #dataset_id="-d global-analysis-forecast-phy-001-024",
	         # Date 
	         yyyystart="2013",
	         mmstart="01",
	         yyyyend="2013",
	         mmend="02",
	         hh=" 12:00:00",
	         dd="01",
	         # Area 
	         xmin="-180",
	         xmax="180",
	         ymin="-80",
	         ymax="40",
	         zmin="0.49", 
	         zmax="0.50",
	         # Variables 
	         table_var_cmd = "thetao",
	         table_data_type = "TEMP_", #There are four data type since we'll download four datasets 
	         
	         # Output files 
	         out_path =  "downs/", #Make sure to end your path with "/" 
	         pre_name= "CMEMS_GLO_001_024_"){
	
	#recover aguments
	argums <- unlist(as.list(environment(), all=TRUE))

	#star command line
	command <- "python"
	
	#pyhton script path 
	script <- scriptPath
	
	#final command line
	allArgs <- paste(c(command, script, argums),collapse = " ")
	cat("command:",allArgs,"\n")

	#system call with command line
	system(allArgs)

}#eo getCMEMS
