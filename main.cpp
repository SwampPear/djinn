#include <iostream>
#include <cstdlib>
#include <unistd.h>
#include "djinn.hpp"


int main() {
    try {
        // initialization
        Djinn::log(Djinn::LogColor::GREEN, "djinn", "starting");

        Djinn::ExecutionContext context = Djinn::get_execution_context();

        // encoding
        Djinn::log(Djinn::LogColor::GREEN, "encoder", "starting task encoding");

        nlohmann::json encoded_tasks = Djinn::encode(context);

        Djinn::log(Djinn::LogColor::GREEN, "djinn", "tasks generated");

        return EXIT_SUCCESS;

    } catch (const std::exception& e) {
        Djinn::log(Djinn::LogColor::RED, "error", e.what());

        return EXIT_FAILURE;
    }
}