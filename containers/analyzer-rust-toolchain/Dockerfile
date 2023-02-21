FROM docker.io/library/rust:1.67.1-alpine3.17@sha256:555332e59c7513233b0f9b52e4fad2924e36128edcb0f80aa97fb34efee3da0e

RUN rustup toolchain install \
	1.66.1-aarch64-unknown-linux-musl \
	1.65.0-x86_64-unknown-linux-musl \
	1.60.0-aarch64-apple-darwin \
	1.64.0-x86_64-apple-darwin \
	1.50.0-x86_64-unknown-linux-gnu \
	1.63.0-aarch64-unknown-linux-gnu \
	1.51.0-x86_64-unknown-linux-musl \
	1.49.0-x86_64-unknown-linux-musl 
	
