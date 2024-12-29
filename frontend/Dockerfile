# Node.js 기반 이미지 사용
FROM node:22

# 작업 디렉토리 설정
WORKDIR /usr/src/app

# 패키지 정보 복사 및 의존성 설치
COPY app/package*.json ./
RUN npm install

# 소스 코드 복사
COPY app/ .

# 컨테이너 실행 시 기본 명령
CMD ["npm", "start"]