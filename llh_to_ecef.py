# LLH_to_ECEF.py
#
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  lat_deg: lattitude in degrees
#  hae_km: height above elipsoid
#  lon_deg: Longitude in Degrees
#  ...
# Output:
#  Outputs ECEF as 3 vector component outputs and one magnitude output
#
#
# Written by William Sosnowski
# 
#

# import Python modules
# e.g., import math # math module
import sys # argv
import math #math

# "constants"
R_E_KM=6378.1363
E_E     =0.081819221456

# helper functions

## function description
def calc_denom(ecc,lat_rad):
	return math.sqrt(1.0-ecc**2.0*math.sin(lat_rad)**2.0)
#   pass

# initialize script arguments
lat_deg=float('nan')
lon_deg=float('nan')
hae_km=0.0

# parse script arguments
if len(sys.argv)==4:
  lat_deg = float(sys.argv[1])
  lon_deg = float(sys.argv[2])
  hae_km = float(sys.argv[3])  #the float here converts it from a text string to a number
else:
    print(\
    'Usage: '\
    'python3 lh_to_rz.py  lat_deg lon_deg hae_km'\
   )
    exit()
  
# write script below this line

lat_rad=lat_deg*math.pi/180.0
lon_rad=lon_deg*math.pi/180.0
denom=calc_denom(E_E,lat_rad)
c_E=R_E_KM/denom
s_E=R_E_KM*(1.0-E_E*E_E)/denom
rx=(c_E+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
ry=(c_E+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
rz=(s_E+hae_km)*math.sin(lat_rad)
rmag=math.sqrt(rx**2+ry**2+rz**2)
print(rx)
print(ry)
print(rz)
