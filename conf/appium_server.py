# coding=utf-8
import os
import time

import re
import requests
import subprocess
from multiprocessing import Pool


class AppiumServer:
    def __init__(self, runs):
        self._runs = runs
        self._cmd = "appium -a 127.0.0.1 -p %s -bp 4728 --no-reset"
        self._url = 'http://127.0.0.1:%s/wd/hub/status'
        self._file = 'appium_server_port_%s.log'
        self._kill = 'taskkill /PID %d /F'
        self._ports = []

    @staticmethod
    def server_url(port):
        server_url = {
            'hostname': '127.0.0.1',
            'port': port,
        }

        return server_url

    def start_appium_server(self):
        pool = Pool(processes=len(self._runs))

        for run in self._runs:
            pool.apply_async(self._run_server, args=(run,))

        pool.close()

        # after start Appium server, Appium server process can not return, so should not join
        # p.join()

        for run in self._runs:
            while not self.is_running(run.get_port()):
                print('wait Appium server all ready...')
                time.sleep(5)
        print('Appium server all ready')

        for run in self._runs:
            file = str(run.get_path() + '\\' + self._file) % run.get_port()
            open(file, 'rb')

            args1 = 'netstat -ano|findstr "{}"'.format(run.get_port())
            with subprocess.Popen(args1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as p1:
                p1.wait()
                data = p1.stdout.read().decode('utf-8').strip('\r\n')
            self._ports = re.findall(r":(\d{4,6}).*\s(\d{1,8})", data)  # 搜索端口和PID

    def _run_server(self, run):
        port = run.get_port()
        cmd = str(self._cmd + ' > ' + run.get_path() + '\\' + self._file) % (port, port)
        os.system(cmd)

    def is_running(self, port):
        url = self._url % port

        response = None
        try:
            response = requests.get(url, timeout=0.1)

            if str(response.status_code).startswith('2'):
                # data = json.loads((response.content).decode("utf-8"))
                # if data.get("staus") == 0:
                return True

            return False
        except requests.exceptions.ConnectionError:
            return False
        except requests.exceptions.ReadTimeout:
            return False
        finally:
            if response:
                response.close()

    def stop_appium_server(self):
        port_pid = dict(self._ports)
        for k in port_pid.keys():
                args3 = "taskkill -PID {} -F".format(port_pid[k])
                with subprocess.Popen(args3, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as p3:
                    p3.wait()
                    if int(port_pid[k]) != 0:
                        print(u'port:{0} is used,kill pid:{1}'.format(k, port_pid[k]))
                        print(p3.stdout.read().decode('gbk'))
                        print(p3.stderr.read().decode('gbk'))
