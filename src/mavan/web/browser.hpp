// Copyright 2024 Michael Vaden
#pragma once

#include <cstdlib>
#include <string>
#include <iostream>
#include <cstdio>
#include <stdexcept>

namespace Mavan {
class Browser {
 public:
    Browser(
        std::string chromedriverPath = "");

    ~Browser();

    void kill();
    void run();

 private:
    std::string cdPath;
    std::string cdAddress;
    std::string cdPort;

    FILE* process;
};
}  // namespace Mavan
