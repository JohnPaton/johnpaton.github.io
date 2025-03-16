import threading
import asyncio
from pathlib import Path
import concurrent.futures
import multiprocessing
import multiprocessing.dummy

import pytest

from call_site_logging import getName

here = Path(__file__).parent


def test_get_name():
    assert getName() == "test.test_get_name:test_get_name"


@pytest.mark.parametrize(
    "chdir, expected_path",
    [
        (here, Path(__file__).name),
        (here.parent, f"test/{Path(__file__).name}"),
        ("/", __file__.lstrip("/")),
        (here.parent / "src", Path(__file__).resolve()),
    ],
)
def test_get_name_filename(chdir, expected_path, monkeypatch):
    monkeypatch.chdir(chdir)
    assert getName(use_filename=True) == f"{expected_path}:test_get_name_filename"


class TestGetNameClass:
    def test_method(self):
        assert getName() == "test.test_get_name:TestGetNameClass.test_method"


@pytest.mark.parametrize(
    "f_back, expected",
    [
        (0, "call_site_logging.context:getName"),
        (1, "test.test_get_name:test_f_back"),
    ],
)
def test_f_back(f_back, expected):
    assert getName(f_back=f_back) == expected


@pytest.mark.asyncio
async def test_async():
    assert getName() == "test.test_get_name:test_async"

    async def test_internal():
        assert getName() == "test.test_get_name:test_async.<locals>.test_internal"

    await test_internal()

    task = asyncio.create_task(test_internal())
    await task


def test_threading():
    name = None

    def test_internal():
        nonlocal name
        name = getName()

    thread = threading.Thread(target=test_internal)
    thread.start()
    thread.join()

    assert name == "test.test_get_name:test_threading.<locals>.test_internal"


def _test_concurrent_futures():
    return getName()


@pytest.mark.parametrize(
    "pool_class",
    [concurrent.futures.ThreadPoolExecutor, concurrent.futures.ProcessPoolExecutor],
)
def test_concurrent_futures(pool_class):
    with pool_class(1) as pool:
        future = pool.submit(_test_concurrent_futures)
        name = future.result()

    assert name == "test.test_get_name:_test_concurrent_futures"


def _test_multiprocessing(conn):
    conn.send(getName())
    conn.close()


@pytest.mark.parametrize(
    "process_class", [multiprocessing.Process, multiprocessing.dummy.Process]
)
def test_multiprocessing(process_class):
    parent_conn, child_conn = multiprocessing.Pipe()
    proc = process_class(target=_test_multiprocessing, args=(child_conn,))
    proc.start()
    name = parent_conn.recv()
    proc.join()

    assert name == "test.test_get_name:_test_multiprocessing"
