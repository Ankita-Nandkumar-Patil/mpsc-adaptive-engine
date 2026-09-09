from datetime import datetime, timezone
from enum import Enum

from sqlalchemy import BigInteger, DateTime, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base


class OnboardingStatus(str, Enum):
    PENDING = "PENDING"
    DIAGNOSTIC = "DIAGNOSTIC"
    COMPLETED = "COMPLETED"


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    telegram_user_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
    )

    onboarding_status: Mapped[OnboardingStatus] = mapped_column(
        SQLEnum(OnboardingStatus),
        nullable=False,
        default=OnboardingStatus.PENDING,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    exams: Mapped[list["Exam"]] = relationship(
        secondary="student_exams",
        back_populates="students",
    )