import network
from conf.conf import WIFI_SSID, WIFI_PASSWORD, WIFI_TEST_URL
import urequests
import utime


class Wifi:
    ssid = WIFI_SSID
    password = WIFI_PASSWORD
    test_url = WIFI_TEST_URL
    wlan = network.WLAN(network.STA_IF)

    """
    manage wifi connection and return wifi status 
    :return: string, value: 'connected' or 'disconnected' 'connected_no_internet' 
    """
    def auto_manage(self, previous_status):
        if previous_status == 'disconnected':
            self.connect()
            utime.sleep(1)
            return self.getStatus()
        elif previous_status == 'connected_no_internet':
            return self.getStatus()
        else:
            return previous_status


    def connect(self):
        print("connecting to wifi")
        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)

    def disconnect(self):
        print("disconnecting from wifi")
        self.wlan.disconnect()
        self.wlan.active(False)

    """
    Check if the device is connected to the wifi network and to internet
    :return: string, value: 'connected' or 'disconnected' 'connected_no_internet' 
    """

    def getStatus(self):
        is_connected_to_network = self.isConnectedToNetwork()
        if is_connected_to_network:
            is_connected_to_internet = self.isConnectedToInternet()
            if is_connected_to_internet:
                return 'connected'
            else:
                return 'connected_no_internet'
        else:
            return 'disconnected'

    """Check if the device is connected to the wifi network
        :return: True if connected, False if not"""

    def isConnectedToNetwork(self):
        return self.wlan.isconnected()

    def isConnectedToInternet(self):
        try:
            urequests.get(self.test_url)
            return True
        except Exception as e:
            print(e)
            return False
