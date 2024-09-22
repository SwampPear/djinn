use std::path::PathBuf;
use std::fs;
use std::fs::File;
use std::io::BufReader;
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

fn get_project_path(project: &String) -> PathBuf {
    let root = std::env::var("DJINN_ROOT")
        .expect("DJINN_ROOT environment variable must be set.");

    let path: PathBuf = [
        root,
        "projects".into(),
        project.into()
    ]
    .iter()
    .collect();

    return path;
}

fn get_project_subpath(project: &String, subpath: &str) -> PathBuf {
    let root = std::env::var("DJINN_ROOT")
        .expect("DJINN_ROOT environment variable must be set.");

    let path: PathBuf = [
        root,
        "projects".into(),
        project.into(),
        subpath.into()
    ]
    .iter()
    .collect();

    return path;
}

fn new(args: cli::CLIArgs) {
    let path: PathBuf = get_project_path(&args.project);

    if path.exists() {
        println!("{}", "Project already exists.");
    } else {
        // create project directory
        fs::create_dir(path);

        // create data file
        let data_path: PathBuf = get_project_subpath(&args.project, "data");
        fs::write(data_path, "");

        // create settings
        let settings_path: PathBuf = get_project_subpath(&args.project, "settings.json");
        let settings = Settings::new(args.workspace);

        // fmt json and write
        let j = serde_json::to_string(&settings).unwrap();
        fs::write(settings_path, j);

        println!("Project created successfully.")
    }
}

fn rm(args: cli::CLIArgs) {
    let path: PathBuf = get_project_path(&args.project);

    if path.exists() {
        fs::remove_dir(path);
        println!("{}", "Project successfully removed.");
    } else {
        println!("{}", "Project does not exist.");
    }
}

fn prompt(mut args: cli::CLIArgs) {
    // settings path
    let path: PathBuf = get_project_subpath(&args.project, "settings.json");

    if path.exists() {
        // read and deserialize json settings
        let file = File::open(path).unwrap();
        let reader = BufReader::new(file);
        let data: Settings = serde_json::from_reader(reader).unwrap();

        args.workspace = PathBuf::from(data.workspace);

        if let Err(e) = client::query(&args) {
            eprintln!("Error querying prompt: {}", e);
        }
    } else {
        println!("Project does not exist.")
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
