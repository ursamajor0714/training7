# import asyncio
# import uuid
# import time
# from abc import ABC, abstractmethod
# from typing import Any, Callable, Dict, List
# from dataclasses import dataclass, field

# @dataclass(order=True)
# class Task:
#     priority: int
#     id: str = field(compare=False)
#     func: Callable = field(compare=False)
#     args: tuple = field(compare=False)
#     kwargs: dict = field(compare=False)
#     created_at: float = field(default_factory=time.time, compare=True)

# class TaskResult:
#     def __init__(self, task_id: str, status: str, result: Any = None, error: Exception = None):
#         self.task_id = task_id
#         self.status = status
#         self.result = result
#         self.error = error

# class BaseWorker(ABC):
#     @abstractmethod
#     async def run(self):
#         pass

# class ClusterNode(BaseWorker):
#     def __init__(self, node_id: str, queue: asyncio.PriorityQueue, results: Dict[str, TaskResult]):
#         self.node_id = node_id
#         self.queue = queue
#         self.results = results
#         self._active = True

#     async def run(self):
#         while self._active:
#             task: Task = await self.queue.get()
#             try:
#                 if asyncio.iscoroutinefunction(task.func):
#                     res = await task.func(*task.args, **task.kwargs)
#                 else:
#                     loop = asyncio.get_event_loop()
#                     res = await loop.run_in_executor(None, task.func, *task.args, **task.kwargs)
#                 self.results[task.id] = TaskResult(task.id, "COMPLETED", result=res)
#             except Exception as e:
#                 self.results[task.id] = TaskResult(task.id, "FAILED", error=e)
#             finally:
#                 self.queue.task_done()

# class Orchestrator:
#     def __init__(self, worker_count: int = 3):
#         self.queue = asyncio.PriorityQueue()
#         self.results = {}
#         self.workers = [ClusterNode(f"node-{i}", self.queue, self.results) for i in range(worker_count)]
#         self._tasks = []

#     async def submit(self, priority: int, func: Callable, *args, **kwargs) -> str:
#         task_id = str(uuid.uuid4())
#         task = Task(priority=priority, id=task_id, func=func, args=args, kwargs=kwargs)
#         await self.queue.put(task)
#         return task_id

#     async def start(self):
#         self._tasks = [asyncio.create_task(w.run()) for w in self.workers]

#     async def stop(self):
#         await self.queue.join()
#         for t in self._tasks:
#             t.cancel()
#         await asyncio.gather(*self._tasks, return_exceptions=True)

# async def heavy_computation(x: int, name: str):
#     await asyncio.sleep(1)
#     return f"Task {name} processed {x+100}"

# async def main():
#     engine = Orchestrator(worker_count=4)
#     await engine.start()

#     ids = []
#     for i in range(20):
#         tid = await engine.submit(priority=i % 3, func=heavy_computation, x=i, name=f"Job-{i}")
#         ids.append(tid)

#     await engine.stop()
    
#     for tid in ids:
#         res = engine.results[tid]
#         print(f"ID: {res.task_id} | Status: {res.status} | Output: {res.result}")

# if __name__ == "__main__":
#     asyncio.run(main())


# a,b=map(int, input().split())
# if a>b :
#     print(a)
# else:
#     print(b)

# pi3 = "pi3"
# print(str(pi3).replace("3", "")) 

# a,b=map(int, input().split())
# if a>b :
#     print(a)
# else:
#     print(b)


# def secret():
#     message="나만의 비밀"
#     print(message)
#     message = "함수 내에서는 자유롭게 수정이 가능해요"

# def please():
#     message="이렇게 하면 되지?"
#     print(message)

# message2='이것도 비밀'
# print(message2)
# secret()
# please()


# message='나는야 전역 변수'
# print(message)

# def no_secret():

#     message='나는야 지역 변수'
#     print(message)

# no_secret()

# f = open('list.txt','w',encoding='utf-8')
# f.write('홍xx\n')
# f.write('심xx\n')
# f.write('임xx\n')
# f.close()

# f = open('list.txt','r', encoding='utf-8')
# for line in f:
#     print(line, end='')
# f.close()


# a,b=[int(input())for _ in range (2)]
# aall=0
# for i in range(b):
#     a1,b1=map(int, input().split())
#     a2=a1*b1
#     aall+=a2

# if a==aall :
#     print("Yes")
# else:
#     print("No")



a=int(input())

def i1(a):
    return a+10
def i2(a):
    return a-10

print(f"{a} + 10 = {i1(a)}")
print(f"{a} - 10 = {i2(a)}")