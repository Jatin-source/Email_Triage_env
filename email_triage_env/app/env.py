from app.models import *
from tasks.easy_classification import load_task as load_easy
from tasks.medium_prioritization import load_task as load_medium
from tasks.hard_response import load_task as load_hard

from graders.easy_grader import grade as easy_grade
from graders.medium_grader import grade as medium_grade
from graders.hard_grader import grade_response
class EmailTriageEnv:

    def __init__(self, task="easy"):
        self.task = task
        self.state = None

    def reset(self):
        if self.task == "easy":
            emails = load_easy()

        elif self.task == "medium":
            emails = load_medium()

        elif self.task == "hard":
            emails = load_hard()

        self.state = State(
            inbox=[Email(**e) for e in emails],
            processed_ids=[],
            step_count=0,
            score=0.0
        )

        return Observation(
            inbox=self.state.inbox,
            current_email_id=self.state.inbox[0].id,
            last_action=None,
            step_count=0
        )

    def step(self, action: Action):
        reward = 0.0
        done = False

        self.state.step_count += 1

    # 🔹 Validate action
        valid_actions = ["classify", "prioritize", "reply", "archive"]
        if action.action_type not in valid_actions:
            return None, -0.5, False, {"error": "invalid action"}

    # 🔹 Get email
        email = next(e for e in self.state.inbox if e.id == action.email_id)

    # ========================
    # 🟢 EASY TASK
    # ========================
        if self.task == "easy":

            if action.action_type == "classify":
                reward = easy_grade(action.content, email.category)
            else:
                reward = -0.1

    # ========================
    # 🟡 MEDIUM TASK
    # ========================
        elif self.task == "medium":

            urgency_map = {"low": 1, "medium": 2, "high": 3}
            correct_email = max(self.state.inbox, key=lambda e: urgency_map[e.urgency])

            reward = medium_grade(action.email_id, correct_email.id, action.action_type)

    # ========================
    # 🔴 HARD TASK
    # ========================
        elif self.task == "hard":

        # must classify before reply
            if action.action_type == "reply" and action.email_id not in self.state.processed_ids:
                return None, -0.3, False, {"error": "must classify first"}

            if action.action_type == "reply" and action.content:
                reward = grade_response(action.content)
            else:
                reward = -0.2

    # 🔹 Time penalty
        reward -= 0.01 * self.state.step_count

    # 🔹 Update state
        self.state.score += reward
        self.state.processed_ids.append(email.id)

    # 🔹 Done condition
        if self.state.step_count >= 5:
            done = True

        obs = Observation(
            inbox=self.state.inbox,
            current_email_id=None,
            last_action=action.action_type,
            step_count=self.state.step_count
        )

        return obs, reward, done, {}

    def state(self):
        return self.state