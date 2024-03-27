// Copyright 2024 Michael Vaden
#include "mavan/core/controller.hpp"

namespace Mavan {
Controller::Controller(std::string cdPath)
    : cdPath{cdPath}, browser{Browser(cdPath)} { }
Controller::~Controller() { }

int Controller::run() {
    browser.run();
}
}  // namespace Mavan
