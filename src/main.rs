mod cli;
mod app;
mod client;

use dotenv;

fn main() {
    dotenv::dotenv().ok();      

    app::run();
}