from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Optional

engine = create_async_engine(
	"sqlite+aiosqlite:///tasks.db"
	)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
	pass

class TaskOrm(Model):
	__tablename__ = "tasks"

	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str]
	description: Mapped[Optional[str]]


class UserOrm(Model):
	__tablename__ = "users"
	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str]
	family: Mapped[str]
	sallary: Mapped[float]
	job: Mapped[str]

async def create_tables():
	async with engine.begin() as conn:
		await conn.run_sync(Model.metadata.create_all)
