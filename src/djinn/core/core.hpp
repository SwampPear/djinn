#pragma once

#include <string>
#include <fstream>
#include <stdexcept>
#include <cstdlib>
#include "nlohmann/json.hpp"
#include "djinn/core/context.hpp"
#include "djinn/core/utils.hpp"

namespace Djinn {

/**
 * @brief Constructs the execution context for Djinn.
 *
 * @return ExecutionContext - The execution context containing:
 * - data: The path to the data directory
 * - root: The current working directory of the application
 * - description: A description of the project
 * - stack: The technology stack description
 * - environment: The environment description
 *
 * @throws std::runtime_error if the 'djinn.json' file cannot be opened or is 
 * malformed
 */
ExecutionContext get_execution_context();

}  // namespace Djinn