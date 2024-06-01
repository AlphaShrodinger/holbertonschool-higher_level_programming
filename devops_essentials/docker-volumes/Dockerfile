FROM alpine:latest

VOLUME /data

COPY data_handling.sh /usr/local/bin/data_handling.sh

RUN chmod +x /usr/local/bin/data_handling.sh

CMD [ "echo", "Hello, World!" ]

ENTRYPOINT ["/usr/local/bin/data_handling.sh"]
