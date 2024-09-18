use crate::{cli, client};

fn new(args: cli::CLIArgs) {
    println!("new");
    println!("Project: {}", args.project);
    println!("Workspace: {}", args.workspace.display());
    println!("Prompt: {}", args.prompt);

    // TODO: check if the project name already exists.
    // TODO: create data database.
    // TODO: create settings.json with workspace details.
}

fn rm(args: cli::CLIArgs) {
    println!("rm");
    println!("Project: {}", args.project);
    println!("Workspace: {}", args.workspace.display());
    println!("Prompt: {}", args.prompt);

    // TODO: check if the project name exists before removal.
}

fn prompt(args: cli::CLIArgs) {
    println!("prompt");
    println!("Project: {}", args.project);
    println!("Workspace: {}", args.workspace.display());
    println!("Prompt: {}", args.prompt);

    // query with prompt
    if let Err(e) = client::query(&args.prompt) {
        eprintln!("Error querying prompt: {}", e);
    }
}

pub fn run() {
    let args = cli::parse_args();

    match args.command {
        cli::CLICommand::NEW => new(args),
        cli::CLICommand::RM => rm(args),
        cli::CLICommand::PROMPT => prompt(args),
    }
}
