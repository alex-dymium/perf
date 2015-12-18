from soak import *
from lib.createReport import *

# create_report(0,'hub2')

def run(ip):
    ca = SQAHookConnection(ip)
    # ca.run(cmd="System.SetStorageValue", prm={"key":"file/GovernorEnvironment","value":config['env']+".governor.oncue.com"})
    # ca.run(cmd="System.SetStorageValue", prm={"key":"file/isTestUser","value":True})
    # print ca.run(cmd="System.GetStorageValue", prm={"key":"file/GovernorEnvironment"})
    # print ca.run(cmd="System.GetStorageValue", prm={"key":"file/isTestUser"})
    # ca.run(cmd="System.Restart")
    ca.run(cmd='Command.Touch', prm={'id': 'MsgScreenReplay'})


if __name__ == "__main__":
    # create_report(0,'hub2')
    # all_devices_ip(run)
    # finish(0)
    all_devices_ip(delit_last_report)
    # GraphsGeneral('../Report/').start()
