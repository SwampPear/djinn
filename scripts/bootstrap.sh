#!/bin/bash

cargo build --release
cp "./target/release/djinn" "./install"