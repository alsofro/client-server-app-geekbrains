import ipaddress
import subprocess
from tabulate import tabulate


# 1 -------------------------------------------------------------------------------------------------------

def host_ping(ip_address):
    code = subprocess.Popen(f'ping {ip_address} -c 1 -W 2', stdout=subprocess.PIPE, shell=True)
    code.wait()
    if not code.poll():
        print(f'{ip_address} доступен')
        return True
    else:
        print(f'{ip_address} не доступен')
        return False


def ip_address(ip):
    raw = ip.strip()
    return ipaddress.IPv4Address(raw)


def generate_ips(ip_list: list):
    ips = [ip_address(ip) for ip in ip_list]
    new_ips = []
    for ip in ips:
        new_ips.append(str(ip))
        for i in range(1, 4):
            new_ips.append(str(ip + i))
    return new_ips


# 2 -------------------------------------------------------------------------------------------------------

def get_ip_range_list(ip_range: list):
    assert len(ip_range) == 2

    first_ip, last_ip = ip_range
    delta = int(last_ip.split('.')[-1]) - int(first_ip.split('.')[-1])
    ip_range_list = [ip_address(first_ip) + i for i in range(0, delta + 1)]

    return ip_range_list


def host_range_ping(ip_range_list: list):
    for ip in ip_range_list:
        host_ping(ip)


# 3 -------------------------------------------------------------------------------------------------------

def host_range_ping_tab(ip_range: list):
    statuses = []

    for ip in ip_range:
        result = host_ping(ip)
        if result:
            status = {'Reachable': ip}
        else:
            status = {'Unreachable': ip}
        statuses.append(status)

    return statuses


if __name__ == '__main__':
    all_ips = '''
    8.8.8.8,
    87.250.250.242,
    0.0.0.0,
    10.0.0.0
    '''.replace('\n', '').split(',')

    ip_range = ['87.250.250.242', '87.250.250.245']

    # 1
    ip_list = generate_ips(all_ips)
    # for ip in ip_list:
    #     host_ping(ip)

    # 2
    ip_range_list = get_ip_range_list(ip_range)
    # host_range_ping(ip_range_list)

    # 3
    ip_statuses_list = host_range_ping_tab(ip_range_list)
    print(tabulate(ip_statuses_list, headers='keys', tablefmt='grid'))

    print(tabulate([{'1': [1, 2, 3, 4, 5]}, {'2': [14, 14, 1114, 14]}], headers='keys', tablefmt='grid'))
