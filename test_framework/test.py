from soak import *

def non_stop():
    while True:
        real_time("Start Soak Test on Hub test at ")
        # test_case_hub1()
        time.sleep(10800)

# create_report(0,'hub2')

def run(ip):
    ca = SQAHookConnection(ip)
    # ca.run(cmd="System.SetStorageValue", prm={"key":"file/GovernorEnvironment","value":config['env']+".governor.oncue.com"})
    # ca.run(cmd="System.SetStorageValue", prm={"key":"file/isTestUser","value":True})
    # print ca.run(cmd="System.GetStorageValue", prm={"key":"file/GovernorEnvironment"})
    # print ca.run(cmd="System.GetStorageValue", prm={"key":"file/isTestUser"})
    # ca.run(cmd="System.Restart")
    # ca.run(cmd='Command.Touch', prm={'id': 'MsgScreenReplay'})
    ca.run(cmd="CurrentPage.SwitchMainTabs", prm={"index": 2})
    ca.run(cmd='Command.Touch', prm={'id': 'ProfileTabs', 'index': 1})



def test_case_test():
    user_name = config['test_username']
    password = config['test_password']
    hub = 'test'
    # devices_connected_names()
    # download_apk()
    # Connection().kill_server()
    # # Connection().power_off(sensor=1)
    # # Connection().usb_off(sensor=1)
    # time.sleep(10)
    # # Connection().usb_on(sensor=1)
    # # time.sleep(5)
    # # Connection().power_on(sensor=1)
    # # time.sleep(60)
    # Connection().start_server()
    # time.sleep(30)
    # connect_all_devices(hub=hub)
    # print('All devices Uninstall app')
    # all_devices_id(target=Connection().uninstall)
    # print('All devices Install app')
    # all_devices_id(target=Connection().install)
    # time.sleep(5)
    # print('All devices Start Reboot')
    # all_devices_id(target=reboot_device)
    # print('All devices Rebooted')
    # time.sleep(30)
    # all_devices_id(target=open_port_5555)
    # print('All devices tcpip 5555')
    # time.sleep(5)
    # connect_devices_wifi(hub=hub, usb=1)
    # # time.sleep(5)
    # # Connection().shell_command('input tap 1095 1485', '192.168.75.127:5555')
    # # connect_devices_wifi(hub=hub, usb=1)
    # # multi_soak()
    # # # time.sleep(5)
    # # Process(target=finish, args=(config['duration']*60+150, )).start()
    # # Process(target=create_report, args=((config['duration']*60+200), hub)).start()
    # time.sleep(20)
    # all_devices_ip(target=start_app)
    # time.sleep(5)
    all_devices_login(target=run_cut, user_name=user_name, password=password)
    exit_app_all_devices(times=2, delay=20)
    Process(target=exit_app_all_devices, args=(3, (config['duration']*56))).start()
    all_devices_ip(target=start_app)
    all_devices_ip(target=run_1hour_video)

if __name__ == "__main__":
    run("68.140.242.179")
    # test_case_test()
    # non_stop()
    # all_devices_ip(run_cut)
    # finish(0)
    # all_devices_ip(delit_last_report)