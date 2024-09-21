use reqwest;

use serde_json::json;
use serde_json;
use serde::{Deserialize, Serialize};
use std::error::Error;
use std::path::PathBuf;
use std::fs;
use std::io;

use crate::cli::CLIArgs;

#[derive(Serialize, Deserialize, Debug)]
struct Message {
    role: String,
    content: String,
}

#[derive(Serialize, Deserialize, Debug)]
struct Choice {
    index: u8,
    message: Message,
    refusal: Option<String>,
}

#[derive(Serialize, Deserialize, Debug)]
struct CompletionTokensDetails {
    reasoning_tokens: u8,
}

#[derive(Serialize, Deserialize, Debug)]
struct Usage {
    prompt_tokens: u32,
    completion_tokens: u32,
    total_tokens: u32,
    completion_tokens_details: CompletionTokensDetails,
}

#[derive(Serialize, Deserialize, Debug)]
struct Completion {
    id: String,
    object: String,
    created: u64,
    model: String,
    choices: Vec<Choice>,
    usage: Usage,
    system_fingerprint: String,
}

fn read_file(path: &PathBuf) -> Result<String, io::Error> {
    fs::read_to_string(path)
}

pub fn fmt_context(args: &CLIArgs) -> String {
    let root = std::env::var("DJINN_ROOT")
        .expect("DJINN_ROOT environment variable must be set.");

    println!("{}", root.clone());

    // basic context
    let path: PathBuf = [
        root,
        "prompts".into(),
        "basic_context.md".into(),
    ]
    .iter()
    .collect();

    match read_file(&path) {
        Ok(content) => {
            return content.replace("<root_dir>", &args.workspace.display().to_string())
        }
        Err(e) => {
            panic!("Error reading file: {}", e);
        }
    }
}

pub fn query(args: &CLIArgs) -> Result<(), Box<dyn Error>> {
    let api_key = std::env::var("OPENAI_API_KEY")
        .expect("OPENAI_API_KEY environment variable must be set.");

    let url = "https://api.openai.com/v1/chat/completions";

    let body = json!({
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": fmt_context(args)
            },
            {
                "role": "user",
                "content": args.prompt
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

    let completion: Completion = serde_json::from_str(&response.text()?)?;
    let query_response = completion.choices[0].message.content;

    Ok(())
}
