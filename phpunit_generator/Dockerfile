FROM php:8.4-cli

RUN curl -L https://phar.phpunit.de/phpunit.phar -o /usr/local/bin/phpunit \
    && chmod +x /usr/local/bin/phpunit

WORKDIR /app