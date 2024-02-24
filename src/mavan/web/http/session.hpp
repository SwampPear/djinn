// Copyright 2024 Michael Vaden
#pragma once

#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <stdexcept>
#include <iostream>
#include <string>

#include "mavan/web/http/http.hpp"

namespace Mavan {
typedef uint16_t Port;

class Session {
 public:
    Session(std::string address, Port port);
    ~Session();

    std::string request(std::string request);

 private:
    std::string address;
    Port port;
};
}  // namespace Mavan
