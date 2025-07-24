# file_io.py
from datetime import datetime


def save_markdown(task_output):
    print("🧪 DEBUG TASK OUTPUT:", task_output)
    print("🧪 Keys:", dir(task_output))
    # Get today's date in the format YYYY-MM-DD
    today_date = datetime.now().strftime('%Y-%m-%d')
    # Set the filename with today's date
    filename = f"{today_date}.md"
    # # Write the task output to the markdown file
    # with open(filename, 'w') as file:
    #     file.write(task_output.raw_output)
    # print(f"Newsletter saved as {filename}")
    if hasattr(task_output, "result") and task_output.result:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(task_output.result)
        print(f"✅ Newsletter saved as {filename}")
    else:
        print("⚠️ No result available in task_output. Newsletter was not saved.")