# archivo para ejecutar el paquete sin necesidad de llamarlo en un archivo

from pythonPackageCodigofacilito import unreleased

if __name__ == '__main__':
    print('Iniciando la ejecución del paquete')
    workshops = unreleased()
    print(workshops)