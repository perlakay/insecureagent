Insecure Agent Example

Functionality of the Example

This example demonstrates an insecure agent that performs text summarization using a machine learning model. The agent takes input text from the user and uses a model (such as Llama-3.2 through the Ollama API) to generate a summary of the input text. The process is simple but intentionally insecure due to several design flaws in the agent's implementation.

The code includes basic functionality for:

Accepting user input.
Sending the input to the model for summarization.
Returning and displaying the summary to the user.
Vulnerabilities in the Example

Prerequisites

To run this code, the following software must be installed:

Python 3.8+:
Download and install from Python's official website.
Ollama:
The agent uses Ollama to interact with machine learning models. Install Ollama by following the instructions from Ollama's official documentation.
Required Python Libraries:
Install the required Python libraries using pip:
pip install ollama
Ollama API Key:
Ensure you have an active Ollama API key and the correct model (such as llama-3.2) available. You can follow Ollama's instructions to set up the model.
Running the Code

Clone this repository to your local machine:
git clone https://github.com/perlakay/insecureagent.git
cd insecureagent
Run the example script:
python3 summerizer.py
Provide the text you want to summarize when prompted.
References to OWASP Agentic Threats and Mitigations Guide

This project highlights several vulnerabilities identified in the OWASP Agentic Threats and Mitigations Guide. These include:

Tool Misuse
Privilege Compromise
Resource Overload
Misaligned and Deceptive Behaviors
You can access the full guide here: OWASP Agentic Threats and Mitigations Guide.

