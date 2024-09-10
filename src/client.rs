use json;
use reqwest;

/*
let parsed = json::parse(r#"

{
    "code": 200,
    "success": true,
    "payload": {
        "features": [
            "awesome",
            "easyAPI",
            "lowLearningCurve"
        ]
    }
}

"#).unwrap();
*/

pub fn query() {
    let body = reqwest::blocking::get("https://www.rust-lang.org")?
        .text()?;

    println!("body = {body:?}");
}