# Rust project name
PROJECT_NAME = my_project

# Default target
default: build

# Build the project
build:
    cargo build

# Run the project
run:
    cargo run

# Clean the project (remove build artifacts)
clean:
    cargo clean

# Run tests
test:
    cargo test

# Help target
help:
    @echo "Available targets:"
    @echo "  build       Build the project"
    @echo "  run         Run the project"
    @echo "  clean       Clean the project (remove build artifacts)"
    @echo "  test        Run tests"
    @echo "  help        Display this help message"

# Phony targets (targets that don't produce files)
.PHONY: default build run clean test help
