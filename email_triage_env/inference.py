import os
import requests

BASE_URL = "http://127.0.0.1:8000"
TASK_NAME = "email_triage"
MODEL_NAME = os.getenv("MODEL_NAME", "baseline-rule-agent")
MAX_STEPS = 5


def log_start(task, env, model):
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(step, action, reward, done, error):
    error_val = error if error else "null"
    done_val = str(done).lower()
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={done_val} error={error_val}",
        flush=True,
    )


def log_end(success, steps, score, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}",
        flush=True,
    )


def decide_action(email):
    text = (email["subject"] + " " + email["body"]).lower()

    if "refund" in text:
        return {
            "action_type": "reply",
            "email_id": email["id"],
            "content": "We are sorry. Your refund will be processed."
        }

    elif "meeting" in text:
        return {
            "action_type": "classify",
            "email_id": email["id"],
            "content": "internal"
        }

    else:
        return {
            "action_type": "classify",
            "email_id": email["id"],
            "content": "spam"
        }


def main():
    rewards = []
    steps = 0
    success = False

    log_start(TASK_NAME, "email_triage_env", MODEL_NAME)

    try:
        # RESET
        res = requests.post(f"{BASE_URL}/reset")
        obs = res.json()

        for step in range(1, MAX_STEPS + 1):

            if not obs["inbox"]:
                break

            email = obs["inbox"][0]
            action = decide_action(email)

            response = requests.post(f"{BASE_URL}/step", json=action)
            result = response.json()

            reward = result.get("reward", 0.0)
            done = result.get("done", False)
            error = result.get("info", {}).get("error")

            rewards.append(reward)
            steps = step

            log_step(step, str(action), reward, done, error)

            obs = result.get("observation", {})

            if done:
                break

        score = max(0.0, min(sum(rewards), 1.0))
        success = score > 0.2

    except Exception as e:
        log_step(steps, "error", 0.0, True, str(e))

    log_end(success, steps, score, rewards)


if __name__ == "__main__":
    main()