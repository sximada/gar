FROM ruby:2.6.3-alpine

WORKDIR /app

COPY Gemfile .
COPY Gemfile.lock .
COPY package.json .

RUN apk update && \
	apk add --no-cache yarn tzdata libxml2-dev curl-dev make gcc libc-dev g++ mariadb-dev imagemagick6-dev sqlite-dev && \
	bundle install && yarn install && \
	rm -rf /usr/local/bundle/cache/* /usr/local/share/.cache/* /var/cache/* /tmp/* && \
	apk del libxml2-dev curl-dev make gcc libc-dev g++ sqlite-dev

COPY . .

ENV TZ=Asia/Tokyo
EXPOSE 3000
CMD ["rails", "server", "-b", "0.0.0.0"]
