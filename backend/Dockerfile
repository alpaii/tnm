# Python 기반 이미지
FROM python:3.13

# 작업 디렉토리 설정
WORKDIR /usr/src/app

# Python 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY app /app

# 기본 명령
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]