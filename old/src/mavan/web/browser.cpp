// Copyright 2024 Michael Vaden
#include "mavan/web/browser.hpp"
#include "mavan/log/log.hpp"

namespace Mavan {
Browser::Browser(std::string cdPath) {
    this->cdPath = cdPath;
    this->cdAddress = "127.0.0.1";
    this->cdPort = "9515";
}

Browser::~Browser() {
    // kill();
}

void Browser::kill() {
    if (!pclose(this->process)) {
        Logger::Error("browser error");
        throw std::runtime_error("browser error");
    }

    Logger::Valid("browser killed");
}

void Browser::run() {
    this->process = popen((cdPath + " > /dev/null 2>&1").c_str(), "w");

    if (!process) {
        Logger::Error("browser error");
        throw std::runtime_error("browser error");
    }

    Logger::Valid("browser running on ", cdAddress, ":", cdPort);
}
}  // namespace Mavan
