# Use the specified base image
FROM postman/newman:5.3-alpine

# Set DNS explicitly
RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf && \
    echo "nameserver 1.1.1.1" >> /etc/resolv.conf

# Update and upgrade packages
RUN apk update && apk upgrade && \
    apk add --no-cache curl zip ping && \

    # Install required Node.js module globally
    npm install -g newman-reporter-csvallinone && \

    # Set environment variable for global node modules
    export NODE_PATH="/usr/local/lib/node_modules" && \

    # Remove cache to reduce image size
    rm -rf /var/cache/apk/* /tmp/* /var/tmp/*

# Set working directory
WORKDIR /etc/newman

# Set the default entry point
ENTRYPOINT ["newman"]
