FROM kaiserli/ubuntu-cn:18.04-2

RUN apt-get update && apt-get install -y libevent-2.1\
    && rm -rf /var/lib/apt/lists/*    

RUN mkdir -p /fluffos/bin /fluffos/mudlib

COPY driver /fluffos/bin/

RUN chmod +x /fluffos/bin/driver

EXPOSE 5555

WORKDIR /fluffos/

ENTRYPOINT [ "/fluffos/bin/driver" ]