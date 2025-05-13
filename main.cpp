#include <iostream>
#include <cstdlib>
#include <unistd.h>
#include "djinn/core/utils.hpp"
#include "djinn/core/core.hpp"


int main() {
    try {
        Djinn::log(Djinn::Color::GREEN, "INFO", "Starting Djinn...");

        // config
        Djinn::ExecutionContext context{};
        context.data = std::string(getenv("HOME")) + "/Library/Application Support/djinn";
        context.root = Djinn::get_cwd();

        // encoding
        Djinn::PromptConfig promptConfig;
        promptConfig["description"] = "write a hello world in go";

        std::cout << Djinn::fmt_prompt(context, promptConfig, "encode_tasks/user.md") << std::endl;

        return EXIT_SUCCESS;
    } catch (const std::exception& e) {
        Djinn::log(Djinn::Color::RED, "ERROR", e.what());

        return EXIT_FAILURE;
    }
}
