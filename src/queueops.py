from typing import List, Tuple, Optional


def take_next(queue: List[str]) -> Tuple[Optional[str], List[str]]:
    """Return (next_name, remaining_queue).

    If queue is empty, return (None, []).
    """
    if not queue:
        return None, []
    return queue[0], queue[1:]


def move_to_back(queue: List[str], name: str) -> List[str]:
    """Return a new queue where the first occurrence of `name` is moved to the back.

    If `name` is not present, return the queue unchanged (new list).
    """
    if name not in queue:
        return list(queue)  # return copy

    idx = queue.index(name)
    # Move only the first occurrence
    return queue[:idx] + queue[idx+1:] + [queue[idx]]


def interleave(q1: List[str], q2: List[str]) -> List[str]:
    """Return an interleaved queue: q1[0], q2[0], q1[1], q2[1], ...

    After the shorter queue runs out, append the rest.
    """
    result = []
    n1, n2 = len(q1), len(q2)
    m = min(n1, n2)

    # Alternate
    for i in range(m):
        result.append(q1[i])
        result.append(q2[i])

    # Append leftovers
    if n1 > m:
        result.extend(q1[m:])
    if n2 > m:
        result.extend(q2[m:])

    return result
