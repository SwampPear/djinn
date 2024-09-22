<p align="center">
  <img src="/.github/djinn.svg" style="width: 50%">
</p>

Djinn is a CLI tool for executing terminal functionality with natural language.

## Installation

1. Clone the repository
```
git clone https://github.com/SwampPear/djinn.git
```

2. Navigate to the project directory

```
cd djinn
```

3. Execute the install script
```
./scripts/install.sh
```

4. Set the DJINN_ROOT environment variable
```
DJINN_ROOT="$HOME/Library/Application Support/Djinn"
```

5. Set the OPENAI_API_KEY environment variable
```
OPENAI_API_KEY="<your api key>"
```

## Usage
### Creating a Project
```
djinn new <project>
```

### Deleting a Project
```djinn new <project>```

### Prompting
```djinn prompt <project> "<prompt>"```
