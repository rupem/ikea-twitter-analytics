from gcr.io/datamechanics/spark:platform-3.1-dm14

ENV PYSPARK_MAJOR_PYTHON_VERSION=3
RUN wget  https://jdbc.postgresql.org/download/postgresql-42.2.5.jar
RUN mv postgresql-42.2.5.jar /opt/spark/jars
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN python -m textblob.download_corpora
COPY ikea_analytics/batch_run.py .
RUN batch_run.py

from postgres

ENV POSTGRES_PASSWORD docker
ENV POSTGRES_DB ikea_db
COPY ikea.sql /docker-entrypoint-initdb.d/