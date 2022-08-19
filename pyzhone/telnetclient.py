import telnetlib


class TelnetClient():
    def __init__(self, user, passw, host, port, timeout) -> None:
        """Summary:
            Initialize the conection to the host
        Args:
            user (str): Authentication Username
            passw (str): Authentication Password
            host (str): Host IP Address/Hostname
            port (int): Port Number
            timeout (int): Timeout in seconds
        """
        self.tn = telnetlib.Telnet(host, port, timeout)
        self.tn.read_until(b"login: ", 5)
        self.tn.write(user.encode('utf-8'))
        self.tn.write(b"\r\n")
        self.tn.read_until(b"assword: ", 5)
        self.tn.write(passw.encode('utf-8'))
        self.tn.write(b"\r\n")

    def sendcmd(self, line, timeout=5) -> str:
        """Summary: Send a command to the host
        Args:
            line (str): Command to send to the host
            timeout (int, optional): Timeout in seconds. Defaults to 5.
        returns:
            str: Response from the host
        """
        self.tn.read_until(b">", 1).decode('ascii')
        self.tn.write(line.encode('utf-8'))
        self.tn.write(b"\r\n")
        self.text = self.tn.read_until(b">", timeout).decode('ascii')
        return self.text
