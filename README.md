<p align="center">
  <img src=".github/djinn.svg" style="width: 50%">
</p>

<hr>

Start with an idea. Take that idea all the way to execution in a fraction of the
time of traditional project implementation. This is Djinn.

Djinn is a tool for autonomous project implementation. Given an initial prompt,
Djinn will implement a plan for development while considering project
specifications and best practices. These tasks are then iteratively executed. 
Test steps are included to include branches in the task flow. This effectively
encodes a problem statement into an executable state machine. The code is then
tested for errors and unit tests are generated and validated.

## Architecture
<p align="center">
  <img src=".github/architecture.png" style="width: 75%; border-radius: 0.5rem;">
</p>

### Input
Input is passed in as a config file, 'djinn.toml', in the current directory.
Information from this is injected into a system prompt with the agent's
operating conditions, and a user prompt for generating task encoding nodes. The
system prompt here is saved for future use in prompting.

### Encoding
The encoding prompt generates task nodes, which are executable as a state machine in the execution step. There are three different types of task nodes that may be assigned, ouput nodes, input nodes, and test nodes.

#### Internode Communication Protocol

```
struct ExecutionContextBlock {
  string command
  string file
  string context  // file contents, terminal reads, error output
}
```

#### Ouput
Ouput nodes simply execute a command.

<p align="center">
  <img src=".github/output_node_diagram.png" style="width: 75%; border-radius: 0.5rem;">
</p>

Here the Execution node takes a ExecutionContextBlock as input and attempts to
execute it. If an error occurs, state transitions to the Resolution node, 
wherein it prompts for a course of action and executes it. If the action is
successful, then state transitions to next.

#### Input
Input nodes wait for a read before transitioning to an ouput node. If the read
operation fails, state transitions to resolution mode, otherwise it transitions
to an output node with updated context in the ExecutionContextBlock. 

<p align="center">
  <img src=".github/input_node_diagram.png" style="width: 75%; border-radius: 0.5rem;">
</p>

## Executor
The task state machine is executed in order of state transitions. It executes
until the final
