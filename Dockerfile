FROM python:alpine3.10
RUN mkdir app
COPY send_email.py /app/send_email.py
ENTRYPOINT [ "python" ]
CMD [ "/app/send_email.py" ]