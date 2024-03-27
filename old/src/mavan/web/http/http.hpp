// Copyright 2024 Michael Vaden
#pragma once

#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <stdexcept>
#include <iostream>
#include <map>
#include <sstream>
#include <type_traits>
#include <chrono>
#include <iomanip>
#include <ctime>
#include <string>
#include <utility>

#include "mavan/web/http/session.hpp"

// GET /status HTTP/1.1\r\nHost: localhost\r\n\r\n
namespace Mavan {
typedef uint16_t Port;
typedef uint16_t Status;

struct Method {
    static constexpr char *GET      = "GET";
    static constexpr char *POST     = "POST";
};

struct HttpVersion {
    static constexpr char *ONE      = "HTTP/1.1";
    static constexpr char *TWO      = "HTTP/2";
    static constexpr char *THREE    = "HTTP/3";
};

struct Headers {
    Headers();
    ~Headers();

    void set(std::string header, std::string value);

    std::map<const char*, const char*> container;
};

class Request {
 public:
    Request(
        std::string address,
        uint16_t port,
        std::string method,
        std::string url,
        std::string version = HttpVersion::ONE,
        Headers headers = Headers());

    std::string send();  // should eventually return response

    std::string address;
    Port port;

    std::string method;
    std::string url;
    std::string version;

 private:
    std::string fmtRequest();
    std::string formattedRequest;

    Headers headers;
};

struct Response {
    explicit Response(std::string rawResponse);

    void parseRawResponse(std::string rawResponse);

    std::string rawResponse;
    Status status;
    Headers headers;
    std::string body;
};
}  // namespace Mavan
