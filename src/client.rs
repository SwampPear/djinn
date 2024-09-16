use reqwest;
use dotenv;
use serde_json::json;
use std::error::Error;
use std::path::PathBuf;
use std::fs;
use std::io;


fn read_file(path: PathBuf) -> Result<String, io::Error> {
    fs::read_to_string(path)
}

pub fn fmt_context() -> () {
    dotenv::dotenv().ok();

    let root = std::env::var("DJINN_ROOT")
        .expect("DJINN_ROOT must be set.");

    // basic context path
    let path: PathBuf = [
        root, 
        "prompts".to_string(),
        "basic_context.md".to_string()
    ].iter().collect();

    match read_file(path) {
        Ok(content) => {
            println!("File content:\n{}", content);
        }
        Err(e) => {
            println!("Error reading file: {}", e);
        }
    }
}

pub fn query(prompt: String) -> Result<(), Box<dyn Error>> {
    dotenv::dotenv().ok();
    let api_key = std::env::var("OPENAI_API_KEY")
        .expect("OPENAI_API_KEY must be set.");

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
    let resp = client
        .post(url)
        .header("Content-Type", "application/json")
        .header("Authorization", format!("Bearer {}", api_key))
        .json(&body) // Send the JSON body
        .send()?;

    let resp_text = resp.text()?;
    println!("{:#?}", resp_text);

    Ok(())
}
