use std::path::PathBuf;
use std::fs;
use crate::{cli, client};

fn new(args: cli::CLIArgs) {
    println!("new");
    println!("Project: {}", args.project);
    println!("Workspace: {}", args.workspace.display());
    println!("Prompt: {}", args.prompt);

    let root = std::env::var("DJINN_ROOT")
        .expect("DJINN_ROOT environment variable must be set.");

    let path: PathBuf = [
        root,
        "projects".into(),
        args.project
    ]
    .iter()
    .collect();

    if path.exists() {
        println!("{}", "Project already exists");
    } else {
        fs::create_dir(path);

        /*
        with open(f'{project_path}/data', 'w') as file:
            file.write('')

        with open(f'{project_path}/settings.json', 'w') as file:
            settings = {
                "project": project,
                "workspace": workspace
            }

            json.dump(settings, file)
        */
    }
}

fn rm(args: cli::CLIArgs) {
    let root = std::env::var("DJINN_ROOT")
        .expect("DJINN_ROOT environment variable must be set.");

    let path: PathBuf = [
        root,
        "projects".into(),
        args.project
    ]
    .iter()
    .collect();

    if path.exists() {
        fs::remove_dir(path);
    } else {
        println!("{}", "Project does not exist.");
    }
}

fn prompt(args: cli::CLIArgs) {
    println!("prompt");
    println!("Project: {}", args.project);
    println!("Workspace: {}", args.workspace.display());
    println!("Prompt: {}", args.prompt);

    // query with prompt
    if let Err(e) = client::query(&args) {
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
