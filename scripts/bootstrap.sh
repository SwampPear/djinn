#!/bin/bash

ROOT="$HOME/Library/Application Support/Djinn"

cargo build --release
cp "./target/release/djinn" "./install"

rm -rf "$ROOT"

mkdir "$ROOT"
cp "./install/djinn" "$ROOT"

mkdir "$ROOT/user"
cp "./install/settings.json" "$ROOT/user/settings.json"

mkdir "$ROOT/projects"

cp -r "./prompts" "$ROOT/prompts"
cp "./.env" "$ROOT"