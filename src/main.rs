mod cli;
mod app;
mod client;

use dotenv::dotenv;

fn main() {
    dotenv().ok();

    app::run();
}