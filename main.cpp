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

        std::cout << encoding_system_prompt << std::endl;
       
        return EXIT_SUCCESS;
    } catch (const std::exception& e) {
        Djinn::log(Djinn::LogColor::RED, "ERROR", e.what());

        return EXIT_FAILURE;
    }
}
