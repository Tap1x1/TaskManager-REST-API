FROM python:3.10.9

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITTEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN useradd -rms /bin/bash testtask && chmod 777 /opt /run

WORKDIR /testtask

RUN mkdir /testtask/static && mkdir /testtask/string && chown -R testtask:testtask /testtask && chmod 755 /testtask

COPY --chown=testtask:testtask . .

RUN pip install -r requirements.txt

USER testtask

CMD ["python", "app.py"]