from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List, Union, Optional
from datetime import datetime
import uuid

class TaskType(Enum):
    GENERATE = auto()
    ANALYZE = auto()
    EXPAND = auto()
    SUMMARIZE = auto()
    BREAKDOWN = auto()
    BRAINSTORM = auto()
    RESEARCH = auto()
    SPECIFY = auto()
    FOLLOW_INSTRUCTIONS = auto()
    GIVE_INSTRUCTIONS = auto()

@dataclass
class Context:
    # Define the structure for context here
    pass

@dataclass
class Message:
    message_id: uuid.UUID
    sender: str
    content: str
    timestamp: datetime

@dataclass
class Thread:
    thread_id: uuid.UUID
    messages: List[Message] = field(default_factory=list)

@dataclass
class Task:
    task_id: uuid.UUID
    task: str
    description: str
    context: Context
    info_base: str
    created_date: datetime
    generated: Union[uuid.UUID, int]  # 0 for none
    generated_date: Optional[datetime]
    task_type: TaskType
    agent_type: str
    agent_completed: Optional[str]  # Agent identifier who completed the task
    thread_list: List[Thread] = field(default_factory=list)
    command_requested: Optional[uuid.UUID]  # ID of a command associated with the task
