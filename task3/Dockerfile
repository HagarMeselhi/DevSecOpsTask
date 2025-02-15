# Use the specified base image
FROM postman/newman:5.3-alpine

# Ensure we are running as root (default in many images) so we can modify files
USER root

# Copy our custom resolv.conf to set DNS explicitly
# (Note: At runtime, Docker may override /etc/resolv.conf; if that happens, consider using --dns flags)
COPY resolv.conf /etc/resolv.conf

# Update/upgrade packages and install extra packages (curl, zip, and ping via iputils)
RUN apk update && \
    apk upgrade && \
    apk add --no-cache curl zip iputils

# Globally install the node module newman-reporter-csvallinone and remove npm cache
RUN npm install -g newman-reporter-csvallinone && \
    npm cache clean --force

# Set the environment variable NODE_PATH
ENV NODE_PATH=/usr/local/lib/node_modules

# Set the working directory
WORKDIR /etc/newman

# Set the entry point to newman
ENTRYPOINT ["newman"]
