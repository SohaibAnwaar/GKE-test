FROM python

RUN mkdir test_kube

COPY test.py test_kube

WORKDIR /test_kube/

RUN pip install flask

ENTRYPOINT [ "python", "./test.py" ]