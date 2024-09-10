mod cli;
mod app;
mod client;

fn main() {
    app::run(cli::parse_args());
    client::query();
}