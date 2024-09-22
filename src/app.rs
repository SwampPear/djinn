use std::path::PathBuf;
use std::fs;
use serde_json::json;
use serde_json;
use serde::{Deserialize, Serialize};
use crate::{cli, client};

#[derive(Serialize, Deserialize, Debug)]
struct Settings {
    workspace: PathBuf
}

impl Settings {
    pub fn new(workspace: PathBuf) -> Self {
        Settings {
            workspace: workspace
        }
    }
}

fn new(args: cli::CLIArgs) {
    let root = std::env::var("DJINN_ROOT")
        .expect("DJINN_ROOT environment variable must be set.");

    let path: PathBuf = [
        root.clone(),
        "projects".into(),
        args.project.clone()
    ]
    .iter()
    .collect();

    if path.exists() {
        println!("{}", "Project already exists");
    } else {
        // create project directory
        fs::create_dir(path);

        // create data file
        let data_path: PathBuf = [
            root.clone(),
            "projects".into(),
            args.project.clone(),
            "data".into()
        ]
        .iter()
        .collect();

        fs::write(data_path, "");

        // create settings
        let settings_path: PathBuf = [
            root.clone(),
            "projects".into(),
            args.project.clone(),
            "settings.json".into()
        ]
        .iter()
        .collect();

        let settings = Settings::new(args.workspace);

        let j = serde_json::to_string(&settings).unwrap();

        fs::write(settings_path, j);

        println!("Project created successfully.")
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
