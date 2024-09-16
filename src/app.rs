use crate::cli;
use crate::client;

fn new(args: cli::CLIArgs) {
    println!("{}", "new");
    println!("project: {}", args.project);
    println!("workspace: {}", args.workspace.display());
    println!("prompt: {}", args.prompt);

    // check through projects and make sure project name does not exist
    // create data database
    // create settings.json with workspace
}

fn rm(args: cli::CLIArgs) {
    println!("{}", "rm");
    println!("project: {}", args.project);
    println!("workspace: {}", args.workspace.display());
    println!("prompt: {}", args.prompt);
    // check through projects and make sure project name exists
}

fn prompt(args: cli::CLIArgs) {
    println!("{}", "rm");
    println!("project: {}", args.project);
    println!("workspace: {}", args.workspace.display());
    println!("prompt: {}", args.prompt);
    client::query(args.prompt);
}

pub fn run() {
    let args = cli::parse_args();

    match args.command {
        cli::CLICommand::NEW => new(args),
        cli::CLICommand::RM => rm(args),
        cli::CLICommand::PROMPT => prompt(args)
    }
}

