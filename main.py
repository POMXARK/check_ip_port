import socket
import json
import requests
import sched, time


def print(*args):
   pass


def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        requests_post('failed', ip, port)
        return False


def requests_post(result, ip_address, port):
    url = 'https://webhook.site/b54939f6-e0e6-4b98-ad9f-7f1002df4c16'
    body = {result: f"{ip_address}:{port}"}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(body), headers=headers)
    print(r.url)
    print(r.status_code, r.reason)


def check_file(sc):
    # получим объект файла
    file1 = open("serverlist.txt", "r")

    # считываем все строки
    lines = file1.read().splitlines()

    # итерация по строкам
    for line in lines:
        ip_address, port = line.split(":")
        print(isOpen(ip_address, port), f"{ip_address, port}")

    # закрываем файл
    file1.close
    s.enter(60, 1, check_file, (sc,))


a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = sched.scheduler(time.time, time.sleep)

s.enter(0, 1, check_file, (s,))
s.run()
