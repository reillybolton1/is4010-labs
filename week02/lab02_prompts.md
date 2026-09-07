# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

State that you installed and authenticated the tool, then record only its version or another non-sensitive verification detail. I installed the tool, and this is its version: 1.0.83

### Antigravity CLI

State that you installed and authenticated the tool, then record only its version or another non-sensitive verification detail. I installed the tool, and the version is : 1.1.27

## Shared task

### Shared prompt

Paste the exact prompt you submitted to both CLI tools.

```text
Write a Python function with this exact signature:

def count_vowels(text: str) -> int:
    """Count a, e, i, o, and u without regard to case; do not count y."""

The function should count how many vowels (a, e, i, o, u) appear in the input string, treating uppercase and lowercase the same way. The letter y should never be counted as a vowel, even if it sometimes acts like one in English. Return the count as an integer.
```

### Copilot CLI observations

In at least 50 words, summarize the suggested approach, anything you questioned, and what you would verify. Do not paste a full transcript. The copilot agent took an approach to create a lookup set for the vowels, making sure each got counted. It also had a counting measure at the end and a sum, to count up the number of vowels.

### Antigravity CLI observations

In at least 50 words, summarize the suggested approach, anything you questioned, and what you would verify. Do not paste a full transcript. The AntiGravity agent took an approach to match all uppercase and lowercase vowels together, ensuring those were counted each time. It also created a lookup set for the vowels, without y, to make sure it never got counted.

### Comparison

 In at least 100 words, compare the two responses for correctness, clarity, assumptions, and usefulness. Explain which approach you selected or how you combined them. In using these two agents to tackle this task, they both took a similar approach to this. Each of them created a lookup set of the desired vowels, aeiou, and made sure to not include y, so the count was not incorrect. They also made sure to change all uppercase letters to lowercase, to make sure none of them were miscounted. The last thing they did, was use a counting feature to add up the number of vowels. 

## Test-guided implementation

In at least 100 words, describe the test result, inspection, or manual check that influenced your final code. Explain any revision you made and why the final behavior matches the function contracts. Upon seeing the initial test results, I noticed some issues with the code. Once fixing this naming error, it all worked correctly. The inspection was thourough for both agents, knowing these needed human oversight before being implemented into my repository. Some manual check I did was run through the code myself, testing for any errors that might occur. I combined a bit of each results from the agents into my final working code.

## Preferred tool combination

 In at least 100 words, reflect on how a browser chat, GitHub Copilot in VS Code, Copilot CLI, and Antigravity CLI each fit your workflow. Identify the combination you currently prefer and one situation that could change your choice. All of these tools fit into my workflows in different ways. GitHub Copilot is helpful for looking over my code as I work, and even reading as I'm typing and finishing my line of code. Copilot CLI is helpful to ask prompts to code, as I did for the count vowels task. Antigravity CLI is also helpful for these same reasons, for promting it and receiving code, that after some inspection and revision, is able to be implemented in my code.
