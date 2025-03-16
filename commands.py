from subprocess import Popen, PIPE, TimeoutExpired
from logger_config import logger
import db_manager as db



def check_tasks():
    tasks = db.get_tasks()
    done = 0

    if not tasks:
        logger.warning("CHECK: No tasks found.")
        return 0

    for task in tasks:
        if task['status'] == 1:
            done += 1
        else:
            result = _execute_command(task['command'])
            if result:
                if task['invert_mode'] == 1:
                    if result != task['calculated_hash']:
                        task['status'] = 1
                        done += 1
                else:
                    if result == task['calculated_hash']:
                        task['status'] = 1
                        done += 1


    db.save_tasks(tasks)
    return done / len(tasks) if done else 0


def show_tasks():
    tasks = db.get_tasks()
    return tasks


def add_task(command: str, calculated_hash: str):
    new_task = {
        'command': command,
        'calculated_hash': calculated_hash,
        'status': 0
    }

    tasks = db.get_tasks()
    tasks.append(new_task)

    db.save_tasks(tasks)
    return True


def delete_task(id: int):
    tasks = db.get_tasks()

    if not tasks:
        logger.error("DELETE: No tasks in list.")
        return None

    if 0 < id <= len(tasks):
        del tasks[id - 1]
    else:
        logger.error(f"DELETE: Invalid ID. Task was not deleted.")
        return None

    db.save_tasks(tasks)
    return True


def _execute_command(command: str, timeout=1):
    try:
        process = Popen(command,
                        shell=True,
                        stdout=PIPE,
                        stderr=PIPE,
                        encoding='utf-8')
        stdout, stderr = process.communicate(timeout=timeout)
        exit_code = process.returncode

        if exit_code == 0:
            return stdout.strip()
        else:
            logger.error(f"CHECK: Process exited with code {exit_code}, COMMAND: \"{command}\". Please review config.json.")
            return None
    except TimeoutExpired:
        process.kill()
        logger.error(f"CHECK: Process took too long, COMMAND: \"{command}\". Please review config.json.")
        return None
    except Exception as e:
        logger.exception(f"CHECK: Unexpected error occurred while executing command: {command}. Error: {e}")
        return None


if __name__ == '__main__':
    check_tasks()
