#include <iostream>
#include <cstdlib>
#include <unistd.h>
#include "djinn.hpp"


int main() {
    try {
        Djinn::log(Djinn::LogColor::GREEN, "INFO", "Starting Djinn...");

        Djinn::ExecutionContext exec_context = Djinn::get_execution_context();
       
        return EXIT_SUCCESS;
    } catch (const std::exception& e) {
        Djinn::log(Djinn::LogColor::RED, "ERROR", e.what());

        return EXIT_FAILURE;
    }
}
