use std::env;
use std::path::PathBuf;
use clap::{command, Command, Arg};

pub enum CLICommand {
    NEW,
    RM,
    PROMPT
}

pub struct CLIArgs {
    pub command: CLICommand,
    pub project: String,
    pub workspace: PathBuf,
    pub prompt: String
}

impl CLIArgs {
    pub fn new() -> Self {
        CLIArgs {
            command: CLICommand::NEW,
            project: String::from(""),
            workspace: PathBuf::new(),
            prompt: String::from("")
        }
    }
}

fn cwd() -> PathBuf {
    match env::current_dir() {
        Ok(path) => path,
        Err(_) => PathBuf::new()
    }
}

pub fn parse_args() -> CLIArgs {
    let mut cli_args = CLIArgs::new();

    // command buildup
    let matches = command!()
        .subcommand(
            Command::new("new")
                .about("creates a new Djinn project")
                .arg(
                    Arg::new("project")
                    .value_name("PROJECT")
                    .help("Specify PROJECT to create")
                )
                .arg(
                    Arg::new("workspace")
                    .value_name("WORKSPACE")
                    .short('w')
                    .long("workspace")
                    .help("Specify WORKSPACE directory to initialize")
                )
        )
        .subcommand(
            Command::new("rm")
                .about("removes a Djinn project")
                .arg(
                    Arg::new("project")
                    .value_name("PROJECT")
                    .help("Specify PROJECT to remove")
                )
        )
        .subcommand(
            Command::new("prompt")
                .about("creates a new djinn project")
                .arg(
                    Arg::new("project")
                    .value_name("PROJECT")
                    .help("Specify PROJECT to remove")
                )
                .arg(
                    Arg::new("prompt")
                    .value_name("PROMPT")
                    .help("Specify PROMPT to act on")
                )
        )
        .get_matches();

    // command serialization
    if let Some(matches) = matches.subcommand_matches("new") {
        cli_args.command = CLICommand::NEW;

        if let Some(project) = matches.get_one::<String>("project") {
            cli_args.project = project.to_string();
        }

        if let Some(workspace) = matches.get_one::<String>("workspace") {
            cli_args.workspace = workspace.to_string().into();
        } else {
            cli_args.workspace = cwd();
        }
    } else
    if let Some(matches) = matches.subcommand_matches("rm") {
        cli_args.command = CLICommand::RM;

        if let Some(project) = matches.get_one::<String>("project") {
            cli_args.project = project.to_string();
        }
    } else
    if let Some(matches) = matches.subcommand_matches("prompt") {
        cli_args.command = CLICommand::PROMPT;

        if let Some(project) = matches.get_one::<String>("project") {
            cli_args.project = project.to_string();
        }

        if let Some(prompt) = matches.get_one::<String>("prompt") {
            cli_args.prompt = prompt.to_string();
        }
    }

    return cli_args
}
