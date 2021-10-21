FROM alpine:3.14
RUN apk add --no-cache go=1.16.8-r0
WORKDIR /
COPY . .
RUN go build .
