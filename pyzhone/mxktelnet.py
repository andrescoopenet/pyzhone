
"""MXK Telnet Core Library
================================================================
Main core of pyzhone library
This library send configuration to MXK Chassis for FTTx service
It can be use to send personalized commads not listed in commands.py

"""
from telnetclient import TelnetClient


class MXKConfig(TelnetClient):
    """Main mxk configuration
    """

    def __init__(self, user, passw, host, port, timeout) -> None:
        """
        Summary: 
            Login to mxk chassis using telnet protocol

        Args:
            host (Str, Optional): MXK host ip address. Defaults to 'localhost'.
            port (Int, Optional): telnet connection port. Defaults to 23.
            timeout (Int, Optional): timeout (seconds). Defaults to 10.
            user (Str, Optional): use name. Defaults to 'admin'.
            password (Str, Optional): password. Defaults to 'zhone'.

        Returns:
            Bool : True/False If connection succeeded or connection failed

        """
        super().__init__(user, passw, host, port, timeout)

    def sendcmdmxk(self, line, **kwarg) -> str:
        """Summary:
            Sends commands to mxk chassis

        Args:
            line (Str): string of commands to send to mxk chassis
            **kwarg: keyword arguments to replace variables in the command string
        """
        if kwarg:
            line = line.format(**kwarg)

        if line == "logout":
            self.tn.write(line.encode('utf-8'))
            self.tn.write(b"\r\n")

        else:
            return self.sendcmd(line)
