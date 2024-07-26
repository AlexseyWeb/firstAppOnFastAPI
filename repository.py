from database import new_session, TaskOrm, UserOrm
from sqlalchemy import select

from schemas import STaskAdd, SUser

class TaskRepository:
	@classmethod
	async def add_one(cls, data: STaskAdd) -> int:
		async with new_session() as session:
			task_dict = data.model_dump()

			task = TaskOrm(**task_dict)
			session.add(task)
			await session.flush()
			await session.commit()
			return task.id

	@classmethod
	async def get_all(cls):
		async with new_session() as session:
			query = select(TaskOrm)
			result = await session.execute(query)
			task_models = result.scalars().all()
			return task_models

class UsersRepository:
	@classmethod
	async def add_one(cls, data: SUser) -> int:
		async with new_session() as session:
			users_dict = data.model_dump()
			user = UserOrm(**users_dict)
			session.add(user)
			await session.flush()
			await session.commit()
			return user.id 

	@classmethod
	async def get_all(cls):
		async with new_session() as session:
			query = select(UserOrm)
			result = await session.execute(query)
			user_models = result.scalars().all()
			return user_models