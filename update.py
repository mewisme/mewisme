from datetime import datetime, timezone

MARKDOWN_FILE_PATH = 'README.md'
START_TAG = '<!-- start-updated-at -->'
END_TAG = '<!-- end-updated-at -->'


def generate_markdown_content():
    now = datetime.now(timezone.utc)
    return f"#### ⏲️ &nbsp;Updated At: {now.strftime('%B %d, %Y at %H:%M UTC')}"


def update_markdown_file(file_path, new_content):
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown = file.read()
    start_index = markdown.find(START_TAG)
    end_index = markdown.find(END_TAG, start_index)
    if start_index == -1 or end_index == -1:
        raise ValueError('Start or end tag not found in the markdown file')
    before_start = markdown[:start_index + len(START_TAG)]
    after_end = markdown[end_index:]
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"{before_start}\n{new_content}\n{after_end}")


if __name__ == '__main__':
    update_markdown_file(MARKDOWN_FILE_PATH, generate_markdown_content())
