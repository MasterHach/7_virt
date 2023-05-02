FROM python:latest as base

ONBUILD RUN echo "Сборка и запуск произведены. Автор: Садиков Александр Дмитриевич"

ENV FLASK_APP=app.py

LABEL student_name = "Sadikov Alex Dmitrievich" \
      student_group = "INBO-07-20"

ADD requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM base as builder

WORKDIR /app

COPY . /app

RUN wget -P /app/static/ https://www.mirea.ru/upload/medialibrary/80f/MIREA_Gerb_Colour.png

EXPOSE 5000

USER 751

VOLUME /images

ENTRYPOINT python app.py

CMD ls
