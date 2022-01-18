from functools import reduce
from typing import Dict

from config import get_settings
from infrastructure import messaging

from .representers import CloneRequestRepresenter, RepoRepresenter

config = get_settings()

queue = messaging.Queue(config.REPORT_QUEUE, config)


def main():
    cloned_repos: Dict[int, RepoRepresenter] = {}

    print("Checking reported clones", end="", flush=True)
    for clone_request_json in queue.poll():
        clone_request: CloneRequestRepresenter = CloneRequestRepresenter.parse_raw(
            clone_request_json
        )
        cloned_repos[clone_request.repo.origin_id] = clone_request.repo
        print(".", end="", flush=True)

    # Notify administrator of unique clones
    if len(cloned_repos) > 0:
        total_size: int = reduce(
            lambda size, repo: size + repo.size, cloned_repos.values(), 0
        )

        # TODO: Email administrator instead of printing to STDOUT
        print(f"\nNumber of unique repos cloned: {len(cloned_repos)}")
        print(f"Total disk space: {total_size}")
    else:
        print("\nNo cloning reported")


if __name__ == "__main__":
    main()
