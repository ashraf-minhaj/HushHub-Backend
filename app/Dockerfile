#########################################
# author: ashraf minhaj
# email : ashraf_minhaj@yahoo.com
# 
# date: 03-12-23
# backend application for hushub
#########################################

# FROM --platform=linux/amd64 python:3.10 as builder
FROM python:3.10 as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# runner stage
# FROM --platform=linux/amd64 python:3.10-slim as runner
FROM python:3.10-slim as runner

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

COPY main.py .

RUN useradd -m backend; chown backend:backend /app
USER backend
# ENV PORT=5000

EXPOSE 5000

CMD ["python", "main.py"]