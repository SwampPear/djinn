// Copyright 2024 Michael Vaden
#pragma once

#include <iostream>
#include <type_traits>
#include <sstream>
#include <chrono>
#include <iomanip>
#include <ctime>
#include <string>
#include <utility>

namespace Mavan {
struct Logger {
    static constexpr char *GREEN      = "\033[92m";
    static constexpr char *YELLOW     = "\033[93m";
    static constexpr char *RED        = "\033[91m";
    static constexpr char *CYAN       = "\033[96m";
    static constexpr char *BOLD       = "\033[1m";
    static constexpr char *UNDERLINE  = "\033[4m";
    static constexpr char *END        = "\033[0m";

    static std::string timestamp() {
        auto currentTime = std::chrono::system_clock::now();

        std::time_t currentTime_t = std::chrono::system_clock::to_time_t(
            currentTime);

        std::tm tm = *std::localtime(&currentTime_t);

        std::ostringstream stream;
        stream << std::put_time(&tm, "%Y-%m-%d %H:%M:%S");
        return stream.str();
    }

    template<class... Args>
    static void Log(Args... args) {
        std::ostringstream stream;
        ((stream << args), ...);        // fold unpack args
        stream << std::endl;

        std::cout << std::move(stream).str();
    }

    template<class T, class... Args>
    static std::string Form(T message, Args... args) {
        std::ostringstream stream;
        ((stream << args), ...);        // fold unpack args
        stream << message << END;
        stream << "\033[0m";            // ASCII end code

        return std::move(stream).str();
    }

    template<class... Args>
    static void Error(Args... args) {
        std::ostringstream stream;

        stream << Logger::Form(Logger::BOLD, Logger::RED, "[");
        stream << Logger::Form(Logger::BOLD, Logger::RED, timestamp());
        stream << Logger::Form(Logger::BOLD, Logger::RED, "] [-] ");

        ((stream << args), ...);
        stream << std::endl;

        std::cout << std::move(stream).str();
    }

    template<class... Args>
    static void Valid(Args... args) {
        std::ostringstream stream;

        stream << Logger::Form(Logger::BOLD, Logger::GREEN, "[");
        stream << Logger::Form(Logger::BOLD, Logger::GREEN, timestamp());
        stream << Logger::Form(Logger::BOLD, Logger::GREEN, "] [+] ");

        ((stream << args), ...);
        stream << std::endl;

        std::cout << std::move(stream).str();
    }

    template<class... Args>
    static void Info(Args... args) {
        std::ostringstream stream;

        stream << Logger::Form(Logger::BOLD, Logger::CYAN, "[");
        stream << Logger::Form(Logger::BOLD, Logger::CYAN, timestamp());
        stream << Logger::Form(Logger::BOLD, Logger::CYAN, "] [?] ");

        ((stream << args), ...);
        stream << std::endl;

        std::cout << std::move(stream).str();
    }

    template<class... Args>
    static void Warning(Args... args) {
        std::ostringstream stream;

        stream << Logger::Form(Logger::BOLD, Logger::YELLOW, "[");
        stream << Logger::Form(Logger::BOLD, Logger::YELLOW, timestamp());
        stream << Logger::Form(Logger::BOLD, Logger::YELLOW, "] [*] ");

        ((stream << args), ...);
        stream << std::endl;

        std::cout << std::move(stream).str();
    }
};
}  // namespace Mavan
