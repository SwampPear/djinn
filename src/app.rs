use crate::cli;

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
}

fn prompt(args: cli::CLIArgs) {
    println!("{}", "prompt");
    println!("project: {}", args.project);
    println!("workspace: {}", args.workspace.display());
    println!("prompt: {}", args.prompt);
}

pub fn run(args: cli::CLIArgs) {
    match args.command {
        cli::CLICommand::NEW => new(args),
        cli::CLICommand::RM => rm(args),
        cli::CLICommand::PROMPT => prompt(args)
    }
}

