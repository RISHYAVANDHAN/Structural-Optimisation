from cfs_utils import *

for mesh in ["3dhanger_10.mesh","3dhanger_50.mesh","3dhanger_100.mesh"]:
    
    for str in ['ocm', 'scpip', 'snopt']:
            
        xml = open_xml('3dhanger.xml')

        if str == 'ipopt' or str == 'snopt':
            replace(xml, '//cfs:costFunction/cfs:stopping/@value', 0)
        

        replace(xml, '//cfs:optimizer/@type', str)
        problem = f'_{str}'
        
        for filt in ["1.3","1.5","1.8"]:

            replace (xml, '//cfs:filters/cfs:filter/@value', filt)
            problem1 = problem + f'_filt_'

            for beta in [2, 8, 32, 64, 128]:
                replace(xml, '//cfs:filters/cfs:filter/cfs:density/@beta', beta)
                problem2 = problem1 + f'_b{beta}_proj'
                
                xml.write(problem2 + '.xml')
                cmd = "cfs -t 4 -m " + mesh + f' -p {problem2}.xml ' + problem2 + "_fixed_top"

                print(cmd)
                execute(cmd)