import paramiko
import socket

# Test edilecek IP listesi (senin verdiğin 11 IP)
ip_list = [
    "172.20.10.3", "172.20.10.4", "172.20.10.5", "172.20.10.6",
    "172.20.10.7", "172.20.10.8", "172.20.10.10", "172.20.10.11",
    "172.20.10.12", "172.20.10.13", "172.20.10.14"
]

username = "pi"
password = "raspberry"  # Eğer değiştirdiysen burayı güncelle

def try_ssh(ip):
    print(f"[+] Deneniyor: {ip}")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, port=22, username=username, password=password, timeout=5)
        print(f"[✅] SSH bağlantısı başarılı: {ip} → Raspberry Pi olabilir!\n")
        client.close()
        return True
    except paramiko.AuthenticationException:
        print(f"[⚠️] {ip}: Şifre yanlış olabilir, ama cihaz cevap verdi!")
    except (paramiko.SSHException, socket.timeout, socket.error):
        print(f"[⛔] {ip}: SSH bağlantısı başarısız.")
    finally:
        client.close()
    return False

for ip in ip_list:
    success = try_ssh(ip)
    if success:
        break
