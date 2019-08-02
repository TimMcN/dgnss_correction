import gpstk
from matplotlib.pyplot import figure,show
import os
import argparse

def arguments():
    parser = argparse.ArgumentParser(description='DGNSS Corrector')
    parser.add_argument('--rover_in', type=str, default="",
                        help = "Rover SBF Path")
    parser.add_argument('--base_stn', type=str, default="",
                        help = "Base STN Rinex Observation Path")
    return parser.parse_args()
args = arguments()

#Covnert SBF to rinex
os.system("./teqc -sep sbf %s > %s" %(args.rover_in, args.rover_in+".rinex"))
rover_rinex = args.rover_in+".rinex"
#print(rover_rinex)
#Read in Rinex header & data
rover_header, rover_data = gpstk.readRinex3Obs(rover_rinex, strict=True)
base_stn_loc = args.base_stn
base_stn_head, base_stn_data = gpstk.readRinex3Obs (base_stn_loc, strict=True)

#Get first and last GPS entry from rover
os.system("app/rnx2rtkp/gcc/rnx2rtkp %s %s -c on -o %s.pos"
            %(rover_rinex, base_stn_loc.split(".")[0]+"*", args.rover_in))
