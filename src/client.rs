use reqwest;

use serde_json::json;
use std::error::Error;
use std::path::PathBuf;
use std::fs;
use std::io;

fn read_file(path: &PathBuf) -> Result<String, io::Error> {
    fs::read_to_string(path)
}

pub fn fmt_context() {
    let root = std::env::var("DJINN_ROOT")
        .expect("DJINN_ROOT environment variable must be set.");
    
    println!("{}", root);

    // path to basic context
    let path: PathBuf = [
        root,
        "prompts".into(),
        "basic_context.md".into(),
    ]
    .iter()
    .collect();

    println!("{}", path.display());

    match read_file(&path) {
        Ok(content) => {
            println!("File content:\n{}", content);
        }
        Err(e) => {
            eprintln!("Error reading file: {}", e);
        }
    }
}

pub fn query(prompt: &str) -> Result<(), Box<dyn Error>> {
    let api_key = std::env::var("OPENAI_API_KEY")
        .expect("OPENAI_API_KEY environment variable must be set.");

    let url = "https://api.openai.com/v1/chat/completions";

    let body = json!({
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    });

    let client = reqwest::blocking::Client::new();
    let response = client
        .post(url)
        .header("Content-Type", "application/json")
        .bearer_auth(api_key) // Cleaner authorization header
        .json(&body)
        .send()?;

    let response_text = response.text()?;
    println!("{:#?}", response_text);

    Ok(())
}
