mod cli;
mod app;

fn main() {
    app::run(cli::parse_args());
}