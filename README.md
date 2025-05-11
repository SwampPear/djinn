<p align="center">
  <img src="/.github/djinn.svg" style="width: 50%">
</p>

<hr>

Djinn is a tool for project implementation.

# Process
## Project Framing
All requirements of the project will be extracted via natural language. These
will be stored in a concise axiomatic knowledge graph. This graph will be then
trained for the next step. 

## Implementation Planning
An implementation plan will then be extracted from the knowledge graph by
tracing the dependency path on which the task will be executed. This is then
unrolled into a priority queue of tasks.

## Task Execution
Each task is executed in sequence. Tasks include creating, updating, or deleting
files and directories. Hopefully in the future more diverse data can be gathered
and abstracted, such as screen and device data.

## Test Implementation Planning
An implementation plan will then be extracted from the knowledge graph by
tracing the dependency path on which the task will be executed. This is then
unrolled into a priority queue of tasks.