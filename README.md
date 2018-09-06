WebMUD with docker support

docker-compose up -d --build
---
# ES2 WebMUD

ES2 mudlib is ancestry of almost every Chinese MUD, powered by MudOS／FluffOS.

Until now, almost every Chinese MUD is played with Telnet / ZMUD client.

This project, using nodejs & HTML5 technologies, enable playing MUD with broswers (including mobile browser, embedded browser in WeChat/QQ, etc.)

### Install

Just clone this project, or download the zip file and extract. It contains:
* mudlib. 
* fluffos binary (for Linux / Mac OS X).
* webapp.

Then run:
```bash
npm install
```

### Dependency

#### nodejs

Required to run webtelnet proxy.

#### libevent

Required by fulffos binary. 
* For Linux, install it with apt-get. 
* For Mac OS X, install it with MacPort.

You can also compile the fluffos binary from project, then copy to `bin/linux` or `bin/osx`:
https://github.com/fluffos/fluffos.git

### Usage

```bash
$ ./bin/startmud
```

```bash
$ ./bin/stopmud
```

### Credits

Created by Raymond Xie, published under MIT license.
