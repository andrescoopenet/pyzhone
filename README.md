# pyzhone

> DZN-Zhone python library for MXK chassis adminsitration

## Requirements

* Python 3


## About & Use
With this library you can send commands to DZN/Zhone Mxk series chassis.

- ### mxktelnet.py
You can use mxktelnet.py to send your own commands, using only strings or 
sending the line whit the variable inside {} and passing the values as kwargs


```
    from mxktelnet import MXKConfig
```

```
    mxk = MXKConfig(user='admin', passw='zhone', host='192.168.254.1', port=23, timeout=10)
    line = 'onu show 1/1'
    answ = mxk.sendcmdmxk(line)
    print(answ)
    mxk.logout()
```

### or

```
    mxk = MXKConfig(user='admin', passw='zhone', host='192.168.254.1', port=23, timeout=10)
    line = 'onu show {slot}/{port}'
    answ = mxk.sendcmdmxk(line,slot=1,port=1)
    print(answ)
    mxk.logout()
```

### mxkcommands.py
If you wish to send a pre configurated command or you wish to add your own, use this library


```
    from mxkcommands import Commands
    
    mxk = Commands()
    slot = 1
    port = 1
    answ = mxk.onushow(slot/port)
    print(answ)
    mxk.logout()
```

### telnetclient.py
Is an standard library to send commands to a remote host via telnet

```
    from telnetclient import TelnetClient

    tlnet = TelnetClient('admin', 'zhone', 'localhost', 23, 10)
    tlnet.sendcmd('configure terminal')
    tlnet.sendcmd('interface 1/1/1')
    tlnet.sendcmd('description test')
    tlnet.sendcmd('exit')
```

Thanks for reading this! Hope it could help you and let's code!