use std::env;
use std::fs::File;
use std::io::{self, Write};
use std::io::prelude::*;

/// Ascii styles.
///
pub enum Style {
    Green,
    Yellow,
    Red,
    Cyan,
    Bold,
    Underline
}

/// Gets the current directory.
///
/// # Returns
///
/// The current directory.
///
fn get_cwd() -> String {
    match env::current_dir() {
        Ok(cwd) => cwd.to_string_lossy().into_owned(),
        Err(error) => panic!("error getting current working directory: {:?}", error),
    }
}

/// Gets the cli args.
///
/// # Returns
///
/// The vector of cli args as strings.
///
fn get_args() -> Vec<String> {
    env::args().skip(1).collect()
}

/// Gets the ansi code for a given style.
///
/// # Arguments
///
/// 'style' - a given style to map to a string
///
/// # Returns
///
/// The mapped style.
///
fn ansi_style(style: &Style) -> String {
    match *style {
        Style::Green => String::from("\x1b[92m"),
        Style::Yellow => String::from("\x1b[93m"),
        Style::Red => String::from("\x1b[91m"),
        Style::Cyan => String::from("\x1b[96m"),
        Style::Bold => String::from("\x1b[1m"),
        Style::Underline => String::from("\x1b[4m"),
    }
}

/// Applies an ansi style to a given string.
///
/// # Arguments
///
/// 'str' - the string to format
/// 'styles' - the vector of styles to apply
/// 
/// # Returns
///
/// The styled string.
fn fmt_string(input: &str, styles: Vec<&Style>) -> String {
    let mut formatted_string = String::new();
    
    for style in styles {
        formatted_string.push_str(&ansi_style(style));
    }
    
    formatted_string.push_str(input);
    formatted_string.push_str("\x1b[0m"); // Reset styles
    
    formatted_string
}

/// Logs a message to the terminal.
///
/// # Arguments
///
/// 'args' - the strings to log
/// 
/// # Returns
///
/// The io result.
///
fn log(args: Vec<String>) -> io::Result<()> {
    let mut stdout = io::stdout();
    let output = args.join("");
    
    stdout.write(output.as_bytes())?;

    stdout.flush()?;
    
    Ok(())
}

/// Creates a file.
///
fn create_file() {}

/// Reads a file.
///
fn create_file() {}

pub fn execute() {
    log(vec![fmt_string("s\n", vec![&Style::Green, &Style::Bold])]);
}


