FROM kaiserli/node-taobao:v1

ADD . /webmud

WORKDIR /webmud

RUN npm install

EXPOSE 8080

CMD [ "./main.js", "8080", "5555", "-w", "./www"]