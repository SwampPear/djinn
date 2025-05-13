#include <iostream>
#include <cstdlib>
#include <unistd.h>
#include "djinn.hpp"


int main() {
    try {
        // initialization
        Djinn::log(Djinn::LogColor::GREEN, "INFO", "Starting Djinn");

        Djinn::ExecutionContext context = Djinn::get_execution_context();

        // encoding
        std::string encoding_system_prompt = Djinn::fmt_prompt(context, nullptr, "/encoding/system.md");
        std::string encoding_user_prompt = Djinn::fmt_prompt(context, nullptr, "/encoding/user.md");

        std::string res = Djinn::prompt(encoding_system_prompt, encoding_user_prompt);

        std::cout << res << std::endl;

        return EXIT_SUCCESS;

    } catch (const std::exception& e) {
        Djinn::log(Djinn::LogColor::RED, "ERROR", e.what());

        return EXIT_FAILURE;
    }
}