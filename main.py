from __future__ import print_function
from matplotlib.pyplot import figure, show
import gpstk

rfn = 'ath1193x.19o'
header, data = gpstk.readRinex3Obs(rfn)
print(header)

oem = gpstk.ObsEpochMap()
for d in data:
        print(gpstk.CivilTime(d.time))
        oe = gpstk.ObsEpoch()
        oe.time = d.time
        for sv in list (d.obs.keys()):
            print (sv, end=' ')
            epoch = d.obs[sv]
            soe = gpstk.SvObsEpoch()
            soe.svid = sv
            for i in range(len(epoch)):
                rinex2_obs_type = header.R2ObsTypes[i]
                oid = header.mapObsTypes['G'][i]
                print("{}({})={}".format(oid,rinex2_obs_type, epoch[i].data), end=' ')
                loc = epoch[i].data
                soe[oid] = epoch[i].data
            oe[sv] = soe
            print()
            oem[d.time]=oe


gpstk.writeRinex3Obs(rfn + '.new', header, data)
