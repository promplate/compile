from pathlib import Path
from typing import Iterable

import watchfiles

from .compile import compile_one


def on_events(events: Iterable[watchfiles.main.FileChange], encoding: str):
    for change, name in events:
        if name.endswith(".py"):
            break

        print(change.raw_str(), name)

        if change is change.deleted:
            Path(name).with_suffix(".py").unlink(missing_ok=True)
        else:
            compile_one(name, encoding=encoding)


def watch(*paths: str | Path, encoding="utf-8", **kwargs):
    for events in watchfiles.watch(*paths, **kwargs):
        on_events(events, encoding)


async def awatch(*paths: str | Path, encoding="utf-8", **kwargs):
    async for events in watchfiles.awatch(*paths, **kwargs):
        on_events(events, encoding)


def main():
    from argparse import ArgumentParser
    from contextlib import suppress

    parser = ArgumentParser()

    parser.add_argument("paths", nargs="*", type=Path, default=[Path.cwd()])
    parser.add_argument("--encoding", "-e", default="utf-8")

    args = parser.parse_args()

    assert args.paths

    with suppress(KeyboardInterrupt):
        watch(*args.paths, encoding=args.encoding)
