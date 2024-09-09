use clap::{arg, command, Command};

pub fn parse_args() {
    let matches = command!()
        .subcommand(
            Command::new("new")
                .about("creates a new Djinn project")
                .arg(arg!([project] "project name"))
        )
        .subcommand(
            Command::new("rm")
                .about("removes a Djinn project")
                .arg(arg!([project] "project name"))
        )
        .subcommand(
            Command::new("prompt")
                .about("creates a new djinn project")
                .arg(arg!([project] "project name"))
                .arg(arg!([prompt] "prompt"))
        )
        .get_matches();

    if let Some(matches) = matches.subcommand_matches("new") {
        if let Some(project) = matches.get_one::<String>("project") {
            println!("Value for name: {project}");
        } else {
            println!("nah project");
        }
    } else
    if let Some(matches) = matches.subcommand_matches("rm") {
        if let Some(project) = matches.get_one::<String>("project") {
            println!("Value for name: {project}");
        } else {
            println!("nah project");
        }
    } else
    if let Some(matches) = matches.subcommand_matches("prompt") {
        if let Some(project) = matches.get_one::<String>("project") {
            println!("Value for name: {project}");
        } else {
            println!("nah project");
        }

        if let Some(prompt) = matches.get_one::<String>("prompt") {
            println!("Value for name: {prompt}");
        } else {
            println!("nah prompt");
        }
    }
}
