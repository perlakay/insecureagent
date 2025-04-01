Insecure Agent Example

Functionality of the Example

This example demonstrates an insecure agent that performs text summarization using a machine learning model. The agent takes input text from the user and uses a model (such as Llama-3.2 through the Ollama API) to generate a summary of the input text. The process is simple but intentionally insecure due to several design flaws in the agent's implementation.

The code includes basic functionality for:

Accepting user input.
Sending the input to the model for summarization.
Returning and displaying the summary to the user.
Vulnerabilities in the Example

1. Tool Misuse:
Issue: The code uses an external model (via the Ollama API) but does not handle potential failures or vulnerabilities properly. It relies entirely on the external service to process and return accurate information without any validation or error handling for failure modes (e.g., the model is unavailable or gives incorrect responses).
Impact: This could lead to the agent returning unexpected outputs or crashing when external services fail.
OWASP Reference: The OWASP Agentic Threats and Mitigations Guide identifies Tool Misuse as a vulnerability in which agents or systems misuse external tools without properly managing them. This can cause unpredictable behavior and errors.

2. Privilege Compromise:
Issue: The agent assumes that the API key and model used are always valid and trusted. No checks are implemented to ensure that the key hasn't been compromised or misused.
Impact: A malicious actor could potentially exploit the agent to gain unauthorized access or use the model for unintended purposes, such as extracting confidential information.
OWASP Reference: Privilege Compromise is a threat where an attacker can escalate privileges within an agent system and gain access to sensitive operations.

3. Resource Overload:
Issue: The agent doesn't limit how often a user can interact with the model, potentially leading to excessive requests. This could cause performance degradation, and the external service might be overloaded or slow due to high request volume.
Impact: Excessive usage without rate limiting can lead to resource exhaustion, making the agent unresponsive or causing the model to be unavailable.
OWASP Reference: Resource Overload is identified as a threat in the OWASP guide, where an agent can unintentionally overwhelm resources, leading to failures or degraded service.

4. Misaligned and Deceptive Behaviors:
Issue: The agent doesn't have any checks to ensure that the responses provided by the model are factually accurate or aligned with the expected behavior. The agent could potentially output misleading summaries or manipulate information.
Impact: Users could be misled by false information, which could affect decision-making or lead to misinformation being spread.
OWASP Reference: This is covered under Misaligned and Deceptive Behaviors, where agents behave in ways that conflict with their intended purpose.

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

