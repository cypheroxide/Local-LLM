# Local-LLM

A collection of tools, functions, and system prompts to improve the response and functionality of locally hosted Large Language Models (LLMs). This repository is designed to enhance your interactions with LLMs by providing utility scripts and configuration settings tailored for local deployments.

## Features

- Tools for optimizing LLM responses
- Custom system prompts for better interaction
- Functions to manage locally hosted LLM workflows

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/cypheroxide/Local-LLM.git
   ```

2. Explore the available tools and scripts in the `Tools/` directory.

3. Run scripts directly or customize them based on your requirements.

## Requirements

- Python 3.x
- Additional dependencies listed in the respective script files.

## Tools

### 1. Tool call script when implementing with Ollama models

- **Script**: `tool_call.py`
- **Description**: This script provides supported models the ability to answer with a `tool_calls` response.  Tool responses can be provided via meassages with `tool` role. See Ollama [API documentation](https://github.com/ollama/ollama/blob/main/docs/api.md#chat-request-with-tools) for more information.

## Contributing

Contributions are welcome! If you have a tool or a script that enhances the functionality of local LLMs, feel free to open a pull request.

## Roadmap

- [ ] Add more LLM-related utilities and scripts.
- [ ] Develop system prompts for specific LLM use cases.
- [ ] Provide integration examples with popular local LLM frameworks.
