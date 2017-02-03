################################################
# Testing :
# R wrapper for CMEMS3567_GLO_Daily_by_Month.py
#
# francois.guilhaumon@ird.fr
################################################

################################################
# UTILS
################################################

getXYminmax <- function(coords,res=0.08,chars=TRUE){
	
	xmin <- coords["lon"] - res
	xmax <- coords["lon"] + res
	ymin <- coords["lat"] - res
	ymax <- coords["lat"] + res
	
	r <- c(xmin,xmax,ymin,ymax)
	
	if(chars) r <- as.character(r)
	
	names(r) <- c("xmin","xmax","ymin","ymax")
	
	r
	
}#eo getXYminmax

################################################
# EO UTILS
################################################

## sourcing the function
source("getCMEMS.R")

## parameters

### motu-client.py path
### this may chnage according to your computer configuration
motu_cl_lib <- "libs/motu-client-python-master/src/python/motu-client.py"

### occurence coordinates
coords <- c(-21.443697, 163.553146)
names(coords) <- c("lat","lon")

### occurence boundig box
xyMinMax <- getXYminmax(coords)

### output dir
dirName <- "test"
dir.create(paste0("downs/",dirName))
outDir <- paste0("downs/",dirName,"/")

### call the function
getCMEMS(motu_cl = motu_cl_lib,
         log_cmems="lnerriere",
         pwd_cmems="20152016",
         #Date
         yyyystart="2013",
         mmstart="01",
         yyyyend="2013",
         mmend="02",
         hh=" 12:00:00",
         dd="01",
         # Area 
         xmin=xyMinMax["xmin"],
         xmax=xyMinMax["xmax"],
         ymin=xyMinMax["ymin"],
         ymax=xyMinMax["ymax"],
         zmin="0.49", 
         zmax="0.50", 
         # Variables 
         table_var_cmd = "thetao",
         table_data_type = "TEMP_",
         # Output files 
         out_path =  outDir, #Make sure to end your path with "/" 
         pre_name= "CMEMS_GLO_001_024_")



