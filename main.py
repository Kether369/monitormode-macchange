import subprocess
#Cambiando de wlan0 a wlan0mon modo monitor
if __name__ == '__main__':
    interface="wlan0"
    Cambiando="wlan0mon"
    print("Cambiando la interface")
    subprocess.run(["airmon-ng", "check kill"])
    subprocess.run(["airmon-ng", "start", "wlan0"])
    subprocess.run(["ifconfig","wlan0mon","down"])
    print("Cambieando la interface:", interface, " a ", Cambiando)
    subprocess.run(["iwconfig",Cambiando, "mode monitor"])
    subprocess.run(["ifconfig", Cambiando, "up"])
    print("La interface cambio a: ", Cambiando)
    print("La interface esta lista")
    subprocess.run(["iwconfig"])

#Cambiando la direccion MAC del eth0

    if __name__ == '__main__':
        interfase = "eth0"
        nueva_MAC = "00:11:22:33:44:55"
        print("Desactivando la interfase: ")
        subprocess.run(["ifconfig", "eth0", "down"])
        print("Cambiando la direccion MAC de la interfase: ", interfase, " a ", nueva_MAC)
        subprocess.run(["ifconfig", interfase, "hw", "ether", nueva_MAC])
        print("La direccion Mac cambio a: ", nueva_MAC)
        subprocess.run(["ifconfig", interfase, "up"])
        print("La interfase esta lista")
        subprocess.run(["ifconfig"])











    subprocess.run(
        ["ifconfig","wlan0"],
        shell=True,
    )
