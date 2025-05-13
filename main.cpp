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
        Djinn::log(Djinn::LogColor::GREEN, "encoder", "prompting model");

        std::string encoding_system_prompt = Djinn::fmt_prompt(context, nullptr, "/encoding/system.md");
        std::string encoding_user_prompt = Djinn::fmt_prompt(context, nullptr, "/encoding/user.md");
        nlohmann::json encoded_tasks = nlohmann::json::parse(Djinn::prompt(encoding_system_prompt, encoding_user_prompt));

        Djinn::log(Djinn::LogColor::GREEN, "djinn", "response generated");

        return EXIT_SUCCESS;

    } catch (const std::exception& e) {
        Djinn::log(Djinn::LogColor::RED, "error", e.what());

        return EXIT_FAILURE;
    }
}