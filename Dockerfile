FROM python:onbuild

EXPOSE 5000
ENV FLASK_APP=run.py

ARG flask_env="development"
ARG jwt_secret_key="extrasecret"
ARG mongo_uri="mongodb://mymongo:27017"
ARG admin_pass="adminpass"

ENV FLASK_ENV="$flask_env"
ENV JWT_SECRET_KEY="$jwt_secret_key"
ENV MONGO_URI="$mongo_uri"
ENV ADMIN_PASS="$admin_pass"

COPY requirements.txt /tmp/
RUN pip install \
  --no-cache-dir \
  -r /tmp/requirements.txt

RUN useradd appuser
WORKDIR /home/appuser
RUN chown appuser:appuser /home/appuser
USER appuser

COPY --chown=appuser:appuser run.py ./
COPY --chown=appuser:appuser app ./app/

ENTRYPOINT [ "flask" ]
CMD [ "run", "--host=0.0.0.0" ]
